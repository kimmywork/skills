# Common Traps & Examples

Reference material for the structured-investigation skill. Read this when you need detailed guidance on avoiding mistakes or want to see a worked example.

---

## Common Traps

| # | Trap | Signal | Correction |
|---|------|--------|-----------|
| 1 | **Shallow exploration** | Conclusions drawn from summaries or secondary sources without tracing to primary sources | Chase every claim to its origin. If you haven't verified the primary source, you can't claim you have. |
| 2 | **Doc-driven conclusions** | Claims sourced from docs, comments, or summaries without primary source verification | Treat all secondary sources as hypotheses. Use primary sources (code, data, original documents) to confirm or refute. |
| 3 | **Single-source tunnel vision** | Findings based on one source type or one perspective | Cross-reference across multiple independent sources. Map the full chain end-to-end. |
| 4 | **Ignoring evolution** | Early versions treated as current state | Always verify the latest state. Check for updates, migrations, corrections after the initial version. |
| 5 | **Single-perspective blind spot** | Pure technical or pure domain viewpoint — missing ops, feasibility, security, or business context | After analysis, review from 2-3 additional role perspectives. |
| 6 | **Unvalidated proposals** | Plans that sound reasonable but have unverified preconditions | For every proposal, ask: "what are the exact steps if we execute today? Are all preconditions met?" |
| 7 | **Cross-document inconsistency** | One doc updated, others still show old info | After any revision, sweep all docs that reference the changed information. |
| 8 | **Optimism bias** | Conclusions only account for the happy path | Identify gaps, edge cases, and conflicting evidence explicitly. Distinguish "confirmed" from "inferred." |
| 9 | **Missing edge cases** | Only main-flow data analyzed; configurations, permissions, less common scenarios overlooked | After main analysis, explicitly ask: "what else participates in this system's operation? What edge cases exist?" |

---

## Example: Tracing a Claim to Its Source

Scenario: An internal wiki states "The system processes 10,000 transactions per second."

**Wrong approach:**
> "The system processes 10,000 TPS." (citing the wiki page)

**Correct approach:**

1. Find the primary source of this claim:
   - Is it a benchmark result? → Find the benchmark report, check methodology, date, environment.
   - Is it a design target? → Find the requirements doc, check if it was validated.
   - Is it a marketing claim? → Treat as unverified.
2. Cross-reference against actual data:
   - Check monitoring dashboards, load test results, production metrics.
   - If production data shows 2,000 TPS, the wiki is wrong.
3. Document with confidence:
   > **Asserted** (source: internal wiki, no benchmark report found): The system is claimed to process 10,000 TPS.
   > **Cross-referenced** (source: production monitoring dashboard, last 30 days): Actual throughput is 1,800-2,200 TPS.

---

## Example: Detecting Outdated Information

Scenario: A design document describes the system architecture with a PostgreSQL database.

**Wrong approach:**
> "The system uses PostgreSQL." (citing the design doc)

**Correct approach:**

1. Check the actual running system:
   - Connection strings, database configs, deployment manifests.
   - The system was migrated to DynamoDB 6 months ago; PostgreSQL is only used for reporting.
2. Document:
   > **Confirmed** (source: deployment manifests, `config/production.yaml`):
   > Primary datastore is DynamoDB. PostgreSQL remains for reporting queries only (read-replica).
   > The design doc is outdated on this point.

---

## Quick-Reference: Confidence Labels

Use these when documenting findings:

| Label | Meaning | When to use |
|-------|---------|-------------|
| **Confirmed** | Verified by reading a primary source directly | Default for most findings |
| **Cross-referenced** | Verified from 2+ independent sources that do not merely repeat the same origin | When triangulation is possible |
| **Inferred** | Deduced from partial evidence | When the full picture isn't accessible |
| **Asserted** | Claimed without verifiable source | When source is unavailable or unreliable |
| **From-agent-knowledge** | Only as a temporary label; not final evidence without confirmation | When the agent's knowledge is the only source |