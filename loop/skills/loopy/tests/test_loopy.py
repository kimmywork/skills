import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "loopy.py"


class LoopyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "workflows").mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def write_workflow(self, name="sample", extra="schedule: '* * * * *'\ntimezone: UTC", body=None):
        body = body or "Do the bounded work.\n\n## Success condition\n\nThe expected artifact exists."
        path = self.root / "workflows" / f"{name}.md"
        path.write_text(
            f"---\nname: {name}\n{extra}\npermissions:\n  - read project files\nconcurrency: forbid\n---\n\n{body}\n",
            encoding="utf-8",
        )
        return path

    def run_cli(self, *args, expected=None):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--project-root", str(self.root), *args],
            capture_output=True,
            text=True,
        )
        if expected is not None:
            self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result, json.loads(result.stdout)

    def test_invalid_cron_is_validation_error_before_first_run(self):
        self.write_workflow(extra="schedule: 'not cron'\ntimezone: UTC")
        _, output = self.run_cli("--validate", expected=1)
        self.assertEqual(output["valid"], [])
        self.assertIn("valid five-field cron", output["errors"][0]["reason"])

    def test_dry_run_never_executes_trigger(self):
        marker = self.root / "marker.txt"
        self.write_workflow(extra=f'trigger: "printf changed > {marker}"')
        _, output = self.run_cli("--dry-run", expected=0)
        self.assertFalse(marker.exists())
        self.assertEqual(output["validated"][0]["trigger_status"], "not_evaluated")
        self.assertFalse((self.root / "workflows/.state").exists())

    def test_explicit_trigger_preview_executes_trigger(self):
        marker = self.root / "marker.txt"
        self.write_workflow(extra=f'trigger: "printf changed > {marker}; printf fired"')
        _, output = self.run_cli("--dry-run", "--evaluate-triggers", expected=0)
        self.assertTrue(marker.exists())
        self.assertEqual(output["validated"][0]["trigger_status"], "fired")

    def test_dispatch_uses_one_lock_and_does_not_create_skipped_state(self):
        self.write_workflow()
        _, first = self.run_cli(expected=0)
        self.assertEqual(len(first["due"]), 1)
        state_file = Path(first["due"][0]["state_file"])
        self.assertTrue(state_file.exists())
        self.assertTrue(state_file.parent.joinpath(".lock").exists())

        _, second = self.run_cli("--run", "sample", expected=0)
        self.assertEqual(second["due"], [])
        self.assertIn("already in progress", second["not_due"][0]["reason"])
        self.assertEqual(len(list(state_file.parent.glob("*.json"))), 1)

    def test_complete_finalizes_state_and_releases_lock(self):
        self.write_workflow()
        _, dispatch = self.run_cli(expected=0)
        state_file = dispatch["due"][0]["state_file"]
        _, completed = self.run_cli("complete", state_file, "--items", "2", expected=0)
        self.assertEqual(completed["status"], "success")
        self.assertTrue(completed["lock_released"])
        state = json.loads(Path(state_file).read_text())
        self.assertEqual(state["items_processed"], 2)
        self.assertFalse(Path(state_file).parent.joinpath(".lock").exists())

    def test_complete_enforces_max_items(self):
        self.write_workflow(extra="schedule: '* * * * *'\ntimezone: UTC\nmax_items: 1")
        _, dispatch = self.run_cli(expected=0)
        state_file = dispatch["due"][0]["state_file"]
        _, output = self.run_cli("complete", state_file, "--items", "2", expected=1)
        self.assertIn("max_items", output["error"])
        self.assertTrue(Path(state_file).parent.joinpath(".lock").exists())

    def test_missing_force_run_is_an_error_and_executes_nothing(self):
        marker = self.root / "marker.txt"
        self.write_workflow(extra=f'trigger: "printf changed > {marker}; printf fired"')
        _, output = self.run_cli("--run", "missing", expected=1)
        self.assertFalse(marker.exists())
        self.assertEqual(output["script_errors"][0]["reason"], "workflow not found")

    def test_missing_permissions_is_invalid(self):
        path = self.root / "workflows/sample.md"
        path.write_text(
            "---\nname: sample\nschedule: '* * * * *'\ntimezone: UTC\n---\n\n## Success condition\n\nDone.\n",
            encoding="utf-8",
        )
        _, output = self.run_cli("--validate", expected=1)
        self.assertIn("permissions", output["errors"][0]["reason"])

    def test_non_firing_trigger_releases_lock_without_run_state(self):
        self.write_workflow(extra="trigger: 'exit 1'")
        _, output = self.run_cli(expected=0)
        self.assertEqual(output["due"], [])
        self.assertIn("exit code 1", output["not_due"][0]["reason"])
        workflow_state = self.root / "workflows/.state/sample"
        self.assertFalse(workflow_state.joinpath(".lock").exists())
        self.assertEqual(list(workflow_state.glob("*.json")), [])

    def test_heartbeat_extends_active_lease(self):
        self.write_workflow()
        _, dispatch = self.run_cli(expected=0)
        state_file = dispatch["due"][0]["state_file"]
        _, output = self.run_cli("heartbeat", state_file, "--lease-seconds", "120", expected=0)
        self.assertEqual(output["state_file"], state_file)
        state = json.loads(Path(state_file).read_text())
        lock = json.loads(Path(state_file).parent.joinpath(".lock").read_text())
        self.assertEqual(state["lease_expires_at"], lock["expires_at"])

    def test_malformed_frontmatter_is_reported(self):
        (self.root / "workflows/broken.md").write_text("not frontmatter", encoding="utf-8")
        _, output = self.run_cli("--validate", expected=1)
        self.assertIn("malformed", output["errors"][0]["reason"])

    def test_recover_marks_stale_state_failed_and_releases_lock(self):
        self.write_workflow()
        _, dispatch = self.run_cli(expected=0)
        state_file = Path(dispatch["due"][0]["state_file"])
        lock_file = state_file.parent / ".lock"
        lock = json.loads(lock_file.read_text())
        lock["expires_at"] = (datetime.now(timezone.utc) - timedelta(seconds=1)).isoformat()
        lock_file.write_text(json.dumps(lock), encoding="utf-8")

        _, output = self.run_cli("recover", "sample", expected=0)
        self.assertTrue(output["recovered"])
        self.assertFalse(lock_file.exists())
        self.assertEqual(json.loads(state_file.read_text())["status"], "failed")


if __name__ == "__main__":
    unittest.main()
