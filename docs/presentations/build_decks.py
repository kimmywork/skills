#!/usr/bin/env python3
"""Generate the presentation deck showcase.

Each deck is a self-contained HTML file. The data in this file is the slide
source: title, budget, speaker notes, and body. Edit here, then run:

    python3 docs/presentations/build_decks.py
"""

from __future__ import annotations

import base64
import html
import os

from visuals import GLOBAL_VISUAL_CSS, DECK_EXTRA, VISUALS

OUT = os.path.dirname(os.path.abspath(__file__))

THEMES = {
    "academic": {
        "bg": "#f7f5ef", "card": "#fffdf8", "fg": "#1e2430", "muted": "#5b6270",
        "accent": "#1f4e79", "accent2": "#b45309", "line": "#d9d4c8",
        "font_display": 'Georgia,"Iowan Old Style","Palatino Linotype",serif',
        "font_ui": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
    },
    "pitch": {
        "bg": "#0b0f14", "card": "#111820", "fg": "#f2f5f8", "muted": "#9aa7b5",
        "accent": "#5eead4", "accent2": "#fbbf24", "line": "#24303b",
        "font_display": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
        "font_ui": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
    },
    "postmortem": {
        "bg": "#f6f4f0", "card": "#fffdfa", "fg": "#1c1c1c", "muted": "#5f5a52",
        "accent": "#b3261e", "accent2": "#2f6f4e", "line": "#ddd6ca",
        "font_display": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
        "font_ui": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
    },
    "architecture": {
        "bg": "#0b1220", "card": "#111b2e", "fg": "#e8eef7", "muted": "#9fb0c7",
        "accent": "#60a5fa", "accent2": "#fbbf24", "line": "#22314a",
        "font_display": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
        "font_ui": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
    },
    "keynote": {
        "bg": "#12100d", "card": "#1a1712", "fg": "#f5efe4", "muted": "#b8aa96",
        "accent": "#f59e0b", "accent2": "#ef4444", "line": "#3a3328",
        "font_display": 'Georgia,"Iowan Old Style","Palatino Linotype",serif',
        "font_ui": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
    },
    "workshop": {
        "bg": "#f7f3ea", "card": "#fffdf7", "fg": "#1f2a2a", "muted": "#5f6b68",
        "accent": "#0f766e", "accent2": "#d97706", "line": "#ddd5c5",
        "font_display": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
        "font_ui": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
    },
    "business": {
        "bg": "#f5f7f8", "card": "#ffffff", "fg": "#15202b", "muted": "#5d6b78",
        "accent": "#0b5d4f", "accent2": "#b45309", "line": "#dce3e8",
        "font_display": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
        "font_ui": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
    },
    "launch": {
        "bg": "#fff7f2", "card": "#ffffff", "fg": "#1d2433", "muted": "#626b7a",
        "accent": "#d6336c", "accent2": "#2f6cb8", "line": "#f0d9d1",
        "font_display": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
        "font_ui": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif',
    },
}

DECK_CSS = """
:root{
  --bg:__BG__; --card:__CARD__; --fg:__FG__; --muted:__MUTED__;
  --accent:__ACCENT__; --accent2:__ACCENT2__; --line:__LINE__;
  --font-display:__FONT_DISPLAY__; --font-ui:__FONT_UI__;
  --font-mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --pad:clamp(24px,3.6vw,64px);
}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font-ui);overflow:hidden}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.deck{height:100dvh;display:flex;flex-direction:column}
.topbar{display:flex;align-items:center;gap:14px;padding:10px 18px;border-bottom:1px solid var(--line);font-size:12px;color:var(--muted);flex:none}
.topbar .name{font-weight:700;color:var(--fg);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topbar .type{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topbar .spacer{flex:1}
.topbar button{min-height:44px;padding:0 14px;border:1px solid var(--line);border-radius:999px;background:transparent;color:var(--fg);font:700 11px/1 var(--font-ui);cursor:pointer}
.topbar button:hover{border-color:var(--accent);color:var(--accent)}
.stage{flex:1;display:grid;place-items:center;padding:18px;min-height:0}
.slide{display:none!important;width:min(100%,1600px);max-height:100%;aspect-ratio:16/9;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:var(--pad);overflow:auto;position:relative}
.slide.active{display:flex!important;flex-direction:column}
.slide.title,.slide.statement,.slide.close{justify-content:center}
.slide h1{margin:0 0 14px;font:700 clamp(38px,5.4vw,78px)/1.02 var(--font-display);letter-spacing:-.035em;max-width:18ch}
.slide h2{margin:0 0 14px;font:700 clamp(30px,3.8vw,58px)/1.04 var(--font-display);letter-spacing:-.03em;max-width:22ch}
.slide h3{margin:0 0 8px;font:700 clamp(18px,1.7vw,26px)/1.15 var(--font-ui);letter-spacing:-.01em}
.slide p,.slide li{font-size:clamp(14px,1.25vw,19px);line-height:1.55}
.slide p{margin:0 0 10px}
.kicker{margin:0 0 12px;font:700 10.5px/1.2 var(--font-mono);letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.lede{color:var(--muted);max-width:64ch}
.meta{color:var(--muted);font-size:clamp(12px,1vw,15px);line-height:1.5}
.small{color:var(--muted);font-size:12px}
.accent{color:var(--accent)}
.grid2,.grid3{display:grid;gap:clamp(12px,1.8vw,24px);margin-top:16px}
.grid2{grid-template-columns:1fr 1fr}
.grid3{grid-template-columns:repeat(3,1fr)}
.card{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:clamp(14px,1.6vw,22px)}
.card h3{margin-bottom:6px}
.card p,.card li{font-size:clamp(13px,1.05vw,16px);color:var(--muted)}
.card ul{margin:6px 0 0;padding-left:18px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:18px}
.stat{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:14px}
.stat b{display:block;font:700 clamp(26px,3.2vw,48px)/1 var(--font-display);letter-spacing:-.03em;color:var(--accent);font-variant-numeric:tabular-nums}
.stat span{display:block;margin-top:6px;color:var(--muted);font-size:11.5px;line-height:1.35}
.table{width:100%;border-collapse:collapse;margin-top:14px;font-size:clamp(12px,.95vw,15px);font-variant-numeric:tabular-nums}
.table th,.table td{text-align:left;padding:8px 9px;border-bottom:1px solid var(--line);vertical-align:top;background:var(--card)}
.table th{color:var(--muted);font-size:10px;letter-spacing:.07em;text-transform:uppercase}
.table td b{color:var(--fg)}
.timeline{display:flex;margin-top:20px;border-top:2px solid var(--line);padding-top:14px}
.timeline > div{flex:1;padding-right:12px;border-right:1px solid var(--line);min-width:0}
.timeline > div:last-child{border-right:0}
.timeline b{display:block;font:700 13px/1 var(--font-mono);color:var(--accent)}
.timeline span{display:block;margin-top:6px;color:var(--muted);font-size:11.5px;line-height:1.35}
.bars{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:end;height:220px;margin-top:18px;border-bottom:1px solid var(--line);padding-bottom:8px}
.bars > div{display:flex;flex-direction:column;justify-content:flex-end;height:100%;gap:6px}
.bars i{display:block;height:var(--h);min-height:6px;background:var(--accent);border-radius:6px 6px 0 0}
.bars b{font:700 14px/1 var(--font-mono)}
.bars span{color:var(--muted);font-size:11.5px}
.quote{margin:0;font:600 clamp(24px,3vw,44px)/1.15 var(--font-display);letter-spacing:-.02em;max-width:28ch}
.quote + .meta{margin-top:16px}
.demo-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:24px;align-items:center;margin-top:12px}
.mock{background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:16px;min-height:220px}
.mock .bar{height:8px;border-radius:999px;background:var(--accent);width:62%;margin-bottom:12px}
.mock .row{height:10px;border-radius:999px;background:var(--line);margin-bottom:8px}
.mock .row.short{width:64%}
.exercise{background:var(--bg);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:16px;margin-top:12px}
.exercise .time{font:700 10px/1 var(--font-mono);letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.exercise h3{margin:6px 0 4px}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.pills span{border:1px solid var(--line);border-radius:999px;padding:5px 10px;font-size:11px;color:var(--muted)}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.three-col{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.note-box{margin-top:14px;padding:12px 14px;border:1px solid var(--line);border-radius:10px;color:var(--muted);font-size:13px}
.deck-footer{display:flex;align-items:center;gap:12px;padding:8px 18px;border-top:1px solid var(--line);font-size:11px;color:var(--muted);flex:none}
.deck-footer .spacer{flex:1}
.progress{position:fixed;left:0;right:0;bottom:0;height:3px;background:var(--line);z-index:30}
.progress i{display:block;height:100%;width:0;background:var(--accent);transition:width .18s ease}
.notes{position:fixed;right:16px;bottom:44px;width:min(440px,calc(100% - 32px));max-height:52vh;overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;box-shadow:0 18px 50px rgba(0,0,0,.25);display:none;z-index:40}
body.notes-open .notes{display:block}
.notes h3{margin:0 0 8px;font:700 11px/1 var(--font-mono);letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}
.notes p{margin:0;color:var(--muted);font-size:13px;line-height:1.55;white-space:pre-wrap}
@media (max-width:900px){
  body{overflow:auto}
  .deck{height:auto;min-height:100dvh}
  .stage{display:block;padding:12px}
  .slide{width:100%;max-height:none;aspect-ratio:auto;min-height:70dvh;margin:0 auto 12px;padding:22px}
  .grid2,.grid3,.stats,.two-col,.three-col,.demo-grid{grid-template-columns:1fr}
  .bars{height:180px}
  .timeline{display:block;border-top:0;padding-top:0}
  .timeline > div{border-right:0;border-bottom:1px solid var(--line);padding:10px 0}
  .topbar .type{display:none}
}
@media print{
  :root{--bg:#fff;--card:#fff;--fg:#000;--muted:#444;--line:#ccc;--accent:#000}
  body{overflow:visible;background:#fff;color:#000}
  .topbar,.deck-footer,.progress,.notes{display:none!important}
  .stage{display:block;padding:0}
  .slide{display:flex!important;width:100%;height:100vh;max-height:none;aspect-ratio:auto;border:0;border-radius:0;page-break-after:always;overflow:hidden;background:#fff;color:#000}
  .slide:last-child{page-break-after:auto}
}
"""

DECK_JS = """
(function(){
  "use strict";
  var slides = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  var counter = document.getElementById("counter");
  var titleEl = document.getElementById("slideTitle");
  var notesBody = document.getElementById("notesBody");
  var notesBtn = document.getElementById("notesBtn");
  var progress = document.getElementById("progressBar");
  var i = 0;

  function show(n){
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach(function(s, k){
      var active = k === i;
      s.classList.toggle("active", active);
      s.setAttribute("aria-hidden", active ? "false" : "true");
    });
    counter.textContent = (i + 1) + " / " + slides.length;
    titleEl.textContent = slides[i].getAttribute("data-title") || "";
    notesBody.textContent = slides[i].getAttribute("data-notes") || "No speaker notes.";
    progress.style.width = ((i + 1) / slides.length * 100) + "%";
  }

  function toggleNotes(){
    var open = document.body.classList.toggle("notes-open");
    notesBtn.setAttribute("aria-pressed", String(open));
  }

  document.addEventListener("keydown", function(e){
    var key = e.key;
    if (key === "ArrowRight" || key === "PageDown" || key === " ") { e.preventDefault(); show(i + 1); }
    else if (key === "ArrowLeft" || key === "PageUp") { e.preventDefault(); show(i - 1); }
    else if (key === "Home") { e.preventDefault(); show(0); }
    else if (key === "End") { e.preventDefault(); show(slides.length - 1); }
    else if (key.toLowerCase() === "n") { e.preventDefault(); toggleNotes(); }
  });

  notesBtn.addEventListener("click", toggleNotes);

  var x0 = null;
  document.addEventListener("touchstart", function(e){ x0 = e.touches[0].clientX; }, {passive:true});
  document.addEventListener("touchend", function(e){
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(i + (dx < 0 ? 1 : -1));
    x0 = null;
  }, {passive:true});

  show(0);
})();
"""

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="__TITLE__ — a fictional presentation deck from the presentation skill showcase.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23161616'/%3E%3Ctext x='16' y='22' text-anchor='middle' font-family='Georgia,serif' font-size='18' fill='%23f4f1e9'%3EP%3C/text%3E%3C/svg%3E">
<title>__TITLE__</title>
<style>__CSS__
__EXTRA_CSS__</style>
</head>
<body data-deck="__DECK_ID__">
<div class="deck">
  <header class="topbar">
    <span class="name">__DECK_TITLE__</span>
    <span class="type">__DECK_TYPE__ · fictional case</span>
    <span class="spacer"></span>
    <button id="notesBtn" type="button" aria-pressed="false">Notes</button>
  </header>
  <main class="stage" id="stage" aria-label="Presentation deck">
    __SLIDES__
  </main>
  <footer class="deck-footer">
    <span id="slideTitle"></span>
    <span class="spacer"></span>
    <span id="counter" aria-live="polite">1 / __TOTAL__</span>
    <span id="totalTime">__TOTAL__ min</span>
    <span>← → navigate · N notes · print to PDF</span>
  </footer>
</div>
<aside class="notes" id="notes" aria-live="polite">
  <h3>Speaker notes</h3>
  <p id="notesBody"></p>
</aside>
<div class="progress"><i id="progressBar"></i></div>
<script>__JS__</script>
</body>
</html>
"""


def theme_css(name: str) -> str:
    t = THEMES[name]
    css = DECK_CSS
    for key, value in {
        "__BG__": t["bg"], "__CARD__": t["card"], "__FG__": t["fg"],
        "__MUTED__": t["muted"], "__ACCENT__": t["accent"], "__ACCENT2__": t["accent2"],
        "__LINE__": t["line"], "__FONT_DISPLAY__": t["font_display"], "__FONT_UI__": t["font_ui"],
    }.items():
        css = css.replace(key, value)
    return css


def render_slide(s: dict) -> str:
    layout = s.get("layout", "default")
    title = html.escape(s.get("title", ""), quote=True)
    notes = html.escape(s.get("notes", ""), quote=True)
    budget = s.get("budget", 1)
    body = s.get("body", "")
    return (
        f'<section class="slide {layout}" data-title="{title}" '
        f'data-budget="{budget}" data-notes="{notes}">{body}</section>'
    )


def render_deck(deck: dict) -> str:
    slides = "\n".join(render_slide(s) for s in deck["slides"])
    total = sum(s.get("budget", 1) for s in deck["slides"])
    out = HTML
    out = out.replace("__TITLE__", html.escape(deck["title"]))
    out = out.replace("__DECK_TITLE__", html.escape(deck["title"]))
    out = out.replace("__DECK_TYPE__", html.escape(deck["type"]))
    out = out.replace("__TOTAL__", str(total))
    out = out.replace("__SLIDES__", slides)
    out = out.replace("__CSS__", theme_css(deck["theme"]))
    out = out.replace("__EXTRA_CSS__", GLOBAL_VISUAL_CSS + DECK_EXTRA.get(deck["id"], "") + background_css(deck))
    out = out.replace("__DECK_ID__", deck["id"])
    out = out.replace("__JS__", DECK_JS)
    return out


def background_css(deck):
    """Photographs are cover or story art in VISUALS, never a wash behind evidence.

    A shared wash made every occasion look like the same card on a stock photo,
    and it hid charts. Do not reintroduce it.
    """
    return ""


# --- decks -----------------------------------------------------------------

DECKS = []

DECKS.append({
    "id": "academic-defense",
    "type": "Academic defense",
    "title": "Nine months after the dike breach",
    "short": "A committee defense: one question, one field study, and the limits of a nine-month answer.",
    "audience": "Thesis committee",
    "mode": "Live + Q&A",
    "time": "20 min + 5 Q&A",
    "theme": "academic",
    "slides": [
        {"layout": "title", "title": "Nine months after the dike breach", "budget": 1, "body": """
            <p class="kicker">PhD defense · fictional case</p>
            <h1>Nine months after the dike breach</h1>
            <p class="lede">Sediment, salt, and the return of the reed belt</p>
            <p class="meta">R. Okafor · L. Brandt · M. Chen · T. Aleman<br>North Inlet Field Station · 18 June 2026</p>
        """, "notes": "Open with the question, not the methods. 30 seconds. Thank the committee and say the study is a nine-month window, not a verdict."},
        {"layout": "statement", "title": "The question", "budget": 2, "body": """
            <p class="kicker">The question</p>
            <h2>Does the marsh self-heal — or convert to open water?</h2>
            <p class="lede">Two trajectories, one decision: invest in monitoring, or intervene at the breach throat.</p>
        """, "notes": "State both trajectories. The committee should hear the decision before the method."},
        {"layout": "grid3", "title": "Why it matters", "budget": 2, "body": """
            <p class="kicker">Why it matters</p>
            <h2>One marsh, three public values</h2>
            <div class="grid3">
              <div class="card"><h3>Storm buffer</h3><p>Every hectare of reed belt reduces wave energy before it reaches the dike.</p></div>
              <div class="card"><h3>Carbon</h3><p>Accretion buries carbon; conversion to open water reverses the sink.</p></div>
              <div class="card"><h3>Habitat</h3><p>The reed belt is nursery habitat for the estuary's commercial fishery.</p></div>
            </div>
        """, "notes": "Keep this short. The decision is the point, not the ecology lecture."},
        {"layout": "default", "title": "Method", "budget": 3, "body": """
            <p class="kicker">Method</p>
            <h2>36 fixed transects, sampled monthly</h2>
            <div class="two-col">
              <div class="card"><h3>Field</h3><ul><li>36 transects, three exposure groups</li><li>Monthly sediment pins</li><li>Salinity loggers at 3 depths</li></ul></div>
              <div class="card"><h3>Remote</h3><ul><li>Drone photogrammetry at 4 cm/px</li><li>Reed cover classified per transect</li><li>Storm events dated from tide-gauge records</li></ul></div>
            </div>
            <p class="meta">Nine months · one site · 14 September 2025 – 12 June 2026</p>
        """, "notes": "Name the limitation now: one site, nine months. Do not hide it until the limitations slide."},
        {"layout": "default", "title": "Result 1: accretion", "budget": 3, "body": """
            <p class="kicker">Result 1</p>
            <h2>Sheltered transects crossed the reed threshold; exposed transects did not</h2>
            <div class="bars">
              <div><i style="--h:78%"></i><b>3.1 cm</b><span>Sheltered (n=21)</span></div>
              <div><i style="--h:35%"></i><b>1.4 cm</b><span>Exposed (n=15)</span></div>
              <div><i style="--h:15%"></i><b>0.6 cm</b><span>Throat edge (n=6)</span></div>
            </div>
            <p class="meta">Threshold for reed establishment: 2.4 cm. Seven of nine months above threshold on the sheltered side.</p>
        """, "notes": "One chart, one claim. Point to the threshold line verbally; do not read the table."},
        {"layout": "default", "title": "Result 2: reed cover and salinity", "budget": 3, "body": """
            <p class="kicker">Result 2</p>
            <h2>Reed cover tracks exposure, not salinity</h2>
            <table class="table">
              <thead><tr><th>Group</th><th>Reed cover</th><th>Salinity</th><th>Interpretation</th></tr></thead>
              <tbody>
                <tr><td>Sheltered (n=21)</td><td><b>38%</b></td><td>within tolerance</td><td>establishment underway</td></tr>
                <tr><td>Exposed (n=15)</td><td><b>12%</b></td><td>within tolerance</td><td>wave stress, not salt</td></tr>
                <tr><td>Throat edge (n=6)</td><td><b>4%</b></td><td>within tolerance</td><td>unstable substrate</td></tr>
              </tbody>
            </table>
        """, "notes": "The surprise is that salinity stayed in band. The driver is wave energy. Say that explicitly."},
        {"layout": "statement", "title": "Interpretation", "budget": 2, "body": """
            <p class="kicker">Interpretation</p>
            <h2>Self-healing is plausible — but not yet stable.</h2>
            <p class="lede">The breach throat widened during the two largest storms. A nine-month trend cannot distinguish recovery from a pause before the next widening.</p>
        """, "notes": "This is the thesis. Do not overclaim. The committee will ask about storm sequencing."},
        {"layout": "grid2", "title": "Limitations", "budget": 2, "body": """
            <p class="kicker">Limitations</p>
            <h2>What this study cannot say</h2>
            <div class="grid2">
              <div class="card"><h3>Time</h3><p>Nine months is shorter than a full storm season and cannot separate recovery from interannual variability.</p></div>
              <div class="card"><h3>Space</h3><p>One site; the throat geometry is not replicated. Transfer to other breaches is an inference.</p></div>
              <div class="card"><h3>Mechanism</h3><p>No belowground biomass or wave-energy measurement at the throat. The mechanism is inferred.</p></div>
              <div class="card"><h3>Observation</h3><p>Reed cover is classified from imagery; observer error is bounded but not eliminated.</p></div>
            </div>
        """, "notes": "Own the limits before the committee does. Each limit has a consequence for the claim."},
        {"layout": "default", "title": "Conclusion", "budget": 2, "body": """
            <p class="kicker">Conclusion</p>
            <h2>Recovery is real, conditional, and worth monitoring</h2>
            <ul>
              <li>Accretion on the sheltered side crossed the reed threshold in 7 of 9 months.</li>
              <li>Reed cover is limited by wave exposure, not salinity.</li>
              <li>The throat remains the failure point; the next two storm seasons decide the trajectory.</li>
            </ul>
            <p class="note-box">Recommendation: maintain monthly transects, add wave-energy loggers at the throat, and review after the next storm season.</p>
        """, "notes": "End with the recommendation, not a summary of the method. 90 seconds."},
        {"layout": "close", "title": "Q&A", "budget": 5, "body": """
            <p class="kicker">Q&A</p>
            <h2>Questions</h2>
            <p class="lede">Backup slides: transect map, storm chronology, salinity series, observer-error check.</p>
            <p class="meta">Five minutes · appendix follows</p>
        """, "notes": "Likely questions: storm sequencing, observer error, transferability, why not model wave energy. Answer briefly; point to appendix."},
    ],
})

DECKS.append({
    "id": "series-a-pitch",
    "type": "Series A pitch",
    "title": "Tidewise — flood-risk intelligence",
    "short": "A ten-minute investor pitch: the maps are older than the storms, and utilities need asset-level risk.",
    "audience": "Series A investors",
    "mode": "Live",
    "time": "10 min + 5 Q&A",
    "theme": "pitch",
    "slides": [
        {"layout": "title", "title": "Tidewise — flood-risk intelligence", "budget": 1, "body": """
            <p class="kicker">Series A · fictional case</p>
            <h1>Tidewise</h1>
            <p class="lede">Asset-level flood risk for coastal utilities.</p>
            <p class="meta">Series A · 2026 · 10 minutes</p>
        """, "notes": "Open with the one-line thesis: utilities are flying blind on asset-level flood risk. 30 seconds."},
        {"layout": "default", "title": "The problem", "budget": 1, "body": """
            <p class="kicker">The problem</p>
            <h2>Utilities plan floods with maps older than the storms</h2>
            <div class="stats">
              <div class="stat"><b>4,200</b><span>coastal utilities in the addressable market</span></div>
              <div class="stat"><b>20 yr</b><span>median age of the flood model used for capex planning</span></div>
              <div class="stat"><b>$2.8B</b><span>annual spend exposed to avoidable flood damage</span></div>
              <div class="stat"><b>1 in 3</b><span>outages traced to an asset the utility already knew was exposed</span></div>
            </div>
        """, "notes": "One number per stat. The last one is the wedge: they know, but cannot prioritize."},
        {"layout": "statement", "title": "The insight", "budget": 1, "body": """
            <p class="kicker">The insight</p>
            <h2>The risk is already in the data. It is not in one place.</h2>
            <p class="lede">Satellite subsidence, tide gauges, asset registers, and outage history describe the same asset. Tidewise joins them into one risk score.</p>
        """, "notes": "Contrast the scattered data with the single score. 60 seconds."},
        {"layout": "grid3", "title": "The product", "budget": 2, "body": """
            <p class="kicker">The product</p>
            <h2>Three workflows, one risk model</h2>
            <div class="grid3">
              <div class="card"><h3>Monitor</h3><p>Live risk map by asset, feeder, and substation.</p></div>
              <div class="card"><h3>Prioritize</h3><p>Rank capex by avoided outage cost and criticality.</p></div>
              <div class="card"><h3>Plan</h3><p>Scenario the next storm, budget cycle, and hardening plan.</p></div>
            </div>
            <p class="meta">API-first; sits beside GIS and EAM, not instead of them.</p>
        """, "notes": "Do not demo every screen. Name the three jobs and the integration boundary."},
        {"layout": "default", "title": "Market", "budget": 1, "body": """
            <p class="kicker">Market</p>
            <h2>Bottom-up: 4,200 utilities, $670k average contract</h2>
            <table class="table">
              <thead><tr><th>Segment</th><th>Utilities</th><th>ACV</th><th>Why now</th></tr></thead>
              <tbody>
                <tr><td>Coastal municipal</td><td>2,900</td><td>$310k</td><td>Rate-case pressure, FEMA mapping</td></tr>
                <tr><td>Investor-owned</td><td>900</td><td>$1.2M</td><td>Capex hearings, resilience mandates</td></tr>
                <tr><td>Co-ops / ports</td><td>400</td><td>$220k</td><td>Insurance and grant requirements</td></tr>
              </tbody>
            </table>
            <p class="meta">$2.8B serviceable market · no single incumbent owns the risk layer.</p>
        """, "notes": "The bottom-up number is the point. Do not quote a top-down TAM."},
        {"layout": "default", "title": "Traction", "budget": 1, "body": """
            <p class="kicker">Traction</p>
            <h2>14 utilities, $1.2M ARR, 132% net revenue retention</h2>
            <div class="stats">
              <div class="stat"><b>$1.2M</b><span>ARR, up from $310k</span></div>
              <div class="stat"><b>132%</b><span>NRR after 12 months</span></div>
              <div class="stat"><b>9 mo</b><span>CAC payback</span></div>
              <div class="stat"><b>14</b><span>production utilities</span></div>
            </div>
        """, "notes": "Traction is the proof of the wedge. Pause after the NRR number; let it land."},
        {"layout": "grid2", "title": "Business model", "budget": 1, "body": """
            <p class="kicker">Business model</p>
            <h2>Per-asset subscription, expanded by API</h2>
            <div class="grid2">
              <div class="card"><h3>Land</h3><p>$180k–$420k annual subscription by asset count; implementation in 6 weeks.</p></div>
              <div class="card"><h3>Expand</h3><p>API calls, scenario modules, and storm-response seats. 78% gross margin at scale.</p></div>
            </div>
        """, "notes": "Land is small enough to skip procurement; expand is the NRR story."},
        {"layout": "default", "title": "Competition", "budget": 1, "body": """
            <p class="kicker">Competition</p>
            <h2>Consultants sell reports. Tidewise is the system of record.</h2>
            <table class="table">
              <thead><tr><th>Alternative</th><th>What it does</th><th>Why it loses</th></tr></thead>
              <tbody>
                <tr><td>Engineering consultancies</td><td>One-off flood studies</td><td>Static, expensive, not operational</td></tr>
                <tr><td>GIS point tools</td><td>Maps and layers</td><td>No asset criticality or capex workflow</td></tr>
                <tr><td>Insurance models</td><td>Portfolio loss estimates</td><td>Not asset-level, not utility-specific</td></tr>
              </tbody>
            </table>
        """, "notes": "Do not disparage consultants; position them as a different job."},
        {"layout": "grid3", "title": "Team", "budget": 1, "body": """
            <p class="kicker">Team</p>
            <h2>Domain, models, and utility operations</h2>
            <div class="grid3">
              <div class="card"><h3>Mara Voss · CEO</h3><p>12 years in utility resilience; former head of asset strategy at a coastal IOU.</p></div>
              <div class="card"><h3>Jon Bell · CTO</h3><p>Built geospatial ML at two climate-risk companies; PhD in remote sensing.</p></div>
              <div class="card"><h3>Priya Nair · COO</h3><p>Scaled field operations at a grid-services firm; owns utility delivery.</p></div>
            </div>
        """, "notes": "One line each. The team slide is not a resume; it answers why this team wins."},
        {"layout": "close", "title": "The ask", "budget": 1, "body": """
            <p class="kicker">The ask</p>
            <h2>$12M Series A</h2>
            <p class="lede">18 months to 60 utilities, $6M ARR, and a validated storm-response module.</p>
            <p class="meta">Milestones: 60 production utilities · $6M ARR · 3 referenceable storm deployments</p>
        """, "notes": "End with the ask and the milestones. Do not end on a thank-you slide."},
    ],
})

DECKS.append({
    "id": "incident-postmortem",
    "type": "Incident postmortem",
    "title": "Checkout outage — 47 minutes",
    "short": "A blameless postmortem readout: timeline, root cause, actions, and the systemic lesson.",
    "audience": "Engineering and operations leadership",
    "mode": "Hybrid readout + written report",
    "time": "15 min + 10 Q&A",
    "theme": "postmortem",
    "slides": [
        {"layout": "title", "title": "Checkout outage — 47 minutes", "budget": 1, "body": """
            <p class="kicker">Blameless postmortem · fictional case</p>
            <h1>Checkout outage — 47 minutes</h1>
            <p class="lede">Northstar Supply · 14 March 2026</p>
            <p class="meta">Readout owner: A. Rivera · Incident commander: S. Chen<br>Written report and timeline in the appendix</p>
        """, "notes": "Set the frame: blameless, evidence-first, actions over blame. 30 seconds."},
        {"layout": "default", "title": "Impact", "budget": 1, "body": """
            <p class="kicker">Impact</p>
            <h2>47 minutes, 18,400 failed checkouts, no data loss</h2>
            <div class="stats">
              <div class="stat"><b>47 min</b><span>customer-facing checkout failure</span></div>
              <div class="stat"><b>18,400</b><span>failed checkout attempts</span></div>
              <div class="stat"><b>$412k</b><span>GMV at risk; $286k recovered after retry</span></div>
              <div class="stat"><b>0</b><span>data loss or PII exposure</span></div>
            </div>
        """, "notes": "Lead with impact, not the deploy. The numbers are the shared facts."},
        {"layout": "default", "title": "Timeline", "budget": 2, "body": """
            <p class="kicker">Timeline</p>
            <h2>From deploy to recovery</h2>
            <div class="timeline">
              <div><b>09:12</b><span>Deploy 4.18.0</span></div>
              <div><b>09:18</b><span>Checkout error rate alert</span></div>
              <div><b>09:24</b><span>Rollback begins</span></div>
              <div><b>09:31</b><span>Partial recovery</span></div>
              <div><b>09:59</b><span>Error rate back to baseline</span></div>
            </div>
            <p class="meta">Times UTC. Full second-by-second timeline in the written report.</p>
        """, "notes": "Walk the timeline in 90 seconds. Do not narrate every log line; point to the report."},
        {"layout": "default", "title": "Root cause", "budget": 3, "body": """
            <p class="kicker">Root cause</p>
            <h2>A config flag mismatch, amplified by a retry storm</h2>
            <div class="two-col">
              <div class="card"><h3>Trigger</h3><p>4.18.0 changed the retry budget from 3 to 8 but left the payment gateway flag at the old ceiling.</p></div>
              <div class="card"><h3>Amplifier</h3><p>Failed authorizations retried immediately; the gateway throttled the whole merchant account, not the single route.</p></div>
            </div>
            <p class="note-box">Not a single bug. A deploy-safety gap let an inconsistent configuration reach 100% of traffic.</p>
        """, "notes": "Separate trigger from amplifier. The systemic cause is the deploy safety gap."},
        {"layout": "grid2", "title": "Contributing factors", "budget": 2, "body": """
            <p class="kicker">Contributing factors</p>
            <h2>What made it possible</h2>
            <div class="grid2">
              <div class="card"><h3>Canary too small</h3><p>2% of traffic for 4 minutes could not surface a gateway-wide throttle.</p></div>
              <div class="card"><h3>No synthetic checkout</h3><p>Health checks covered the API, not the checkout path.</p></div>
              <div class="card"><h3>Runbook stale</h3><p>The rollback step referenced the old deployment tool.</p></div>
              <div class="card"><h3>Handoff gap</h3><p>The on-call handoff missed the deploy note by 12 minutes.</p></div>
            </div>
        """, "notes": "Four factors, each with a consequence. This is where the actions come from."},
        {"layout": "grid2", "title": "What went well", "budget": 1, "body": """
            <p class="kicker">What went well</p>
            <h2>Recovery was faster because the basics held</h2>
            <div class="grid2">
              <div class="card"><h3>Rollback</h3><p>One command; no schema change. The last known-good artifact was available.</p></div>
              <div class="card"><h3>Comms</h3><p>Status page updated at 09:26; support had a script by 09:32.</p></div>
            </div>
        """, "notes": "Name the strengths. A postmortem that only lists failures is incomplete."},
        {"layout": "default", "title": "Actions", "budget": 3, "body": """
            <p class="kicker">Actions</p>
            <h2>Six actions, each with an owner and a date</h2>
            <table class="table">
              <thead><tr><th>Action</th><th>Owner</th><th>Due</th><th>Done when</th></tr></thead>
              <tbody>
                <tr><td>Canary by checkout route</td><td>Platform</td><td>28 Mar</td><td>5% route-level canary</td></tr>
                <tr><td>Synthetic checkout probe</td><td>SRE</td><td>4 Apr</td><td>1-min probe, paging</td></tr>
                <tr><td>Retry budget validation</td><td>Payments</td><td>21 Mar</td><td>Config test in CI</td></tr>
                <tr><td>Rollback runbook refresh</td><td>On-call</td><td>21 Mar</td><td>Drill passed</td></tr>
                <tr><td>Gateway throttle isolation</td><td>Payments</td><td>18 Apr</td><td>Per-route quota</td></tr>
                <tr><td>Deploy note in handoff</td><td>Eng mgmt</td><td>28 Mar</td><td>Template adopted</td></tr>
              </tbody>
            </table>
        """, "notes": "Do not read every row. Point to the two actions that change the system, not just the symptom."},
        {"layout": "default", "title": "Detection and response", "budget": 1, "body": """
            <p class="kicker">Metrics</p>
            <h2>Detection was fast; recovery was the constraint</h2>
            <table class="table">
              <thead><tr><th>Metric</th><th>This incident</th><th>Target</th></tr></thead>
              <tbody>
                <tr><td>Time to detect</td><td>6 min</td><td>≤ 5 min</td></tr>
                <tr><td>Time to mitigate</td><td>41 min</td><td>≤ 20 min</td></tr>
                <tr><td>Error-budget burn</td><td>62% of quarter</td><td>≤ 20%</td></tr>
              </tbody>
            </table>
        """, "notes": "The gap is mitigation, not detection. That is why the canary and runbook actions come first."},
        {"layout": "statement", "title": "The lesson", "budget": 1, "body": """
            <p class="kicker">The lesson</p>
            <h2>Deploy safety is a product, not a checklist.</h2>
            <p class="lede">The system allowed an inconsistent configuration to reach all traffic. Fix the system, not the deploy that exposed it.</p>
        """, "notes": "One lesson, one sentence. Let it sit before Q&A."},
        {"layout": "close", "title": "Appendix", "budget": 10, "body": """
            <p class="kicker">Appendix</p>
            <h2>Evidence</h2>
            <ul>
              <li>Second-by-second timeline and log excerpts</li>
              <li>Customer communication and support script</li>
              <li>Config diff and gateway throttle trace</li>
              <li>Action tracker and review dates</li>
            </ul>
        """, "notes": "Q&A. Use the appendix; do not improvise facts. Written report is the source of truth."},
    ],
})

DECKS.append({
    "id": "architecture-review",
    "type": "Architecture review",
    "title": "Streaming event ingestion at Meridian",
    "short": "A decision review: batch is breaking, streaming is expensive, and the trade-off is operational.",
    "audience": "Staff engineers and architecture board",
    "mode": "Live + Q&A",
    "time": "25 min + 10 Q&A",
    "theme": "architecture",
    "slides": [
        {"layout": "title", "title": "Streaming event ingestion at Meridian", "budget": 1, "body": """
            <p class="kicker">Architecture decision review · fictional case</p>
            <h1>Streaming event ingestion at Meridian</h1>
            <p class="lede">From nightly batch to a six-hour freshness target</p>
            <p class="meta">Decision requested: approve phase 1 · 2026</p>
        """, "notes": "State the decision first: this is a review, not a survey. 30 seconds."},
        {"layout": "default", "title": "Context", "budget": 2, "body": """
            <p class="kicker">Context</p>
            <h2>2.4B events/day, six-hour freshness, and a batch window that no longer fits</h2>
            <div class="grid3">
              <div class="card"><h3>Volume</h3><p>2.4B events/day, 3.1× year over year.</p></div>
              <div class="card"><h3>Freshness</h3><p>Product needs six hours; batch gives 24.</p></div>
              <div class="card"><h3>Pressure</h3><p>The nightly window now overlaps peak ingest.</p></div>
            </div>
        """, "notes": "The freshness requirement is a product constraint, not an engineering preference."},
        {"layout": "grid2", "title": "Requirements", "budget": 2, "body": """
            <p class="kicker">Requirements</p>
            <h2>What any option must satisfy</h2>
            <div class="grid2">
              <div class="card"><h3>Correctness</h3><p>Exactly-once semantics at the sink; idempotent replay.</p></div>
              <div class="card"><h3>Replay</h3><p>90-day replay for backfill and incident recovery.</p></div>
              <div class="card"><h3>Cost</h3><p>≤ 1.4× current run rate at 3× volume.</p></div>
              <div class="card"><h3>Migration</h3><p>No customer-visible cutover; rollback in one hour.</p></div>
            </div>
        """, "notes": "Four constraints. Any recommendation that violates one is out."},
        {"layout": "default", "title": "Options", "budget": 3, "body": """
            <p class="kicker">Options</p>
            <h2>Three credible paths</h2>
            <table class="table">
              <thead><tr><th>Option</th><th>Shape</th><th>Strength</th><th>Weakness</th></tr></thead>
              <tbody>
                <tr><td><b>A · Batch + micro-batch</b></td><td>Keep batch, add 15-min micro-batches</td><td>Lowest migration risk</td><td>Cannot reach 6h freshness at peak</td></tr>
                <tr><td><b>B · Kafka + Flink</b></td><td>Streaming ingest, managed Kafka, Flink jobs</td><td>Meets freshness and replay</td><td>Operational load; new on-call surface</td></tr>
                <tr><td><b>C · Managed ingestion</b></td><td>Vendor-managed pipeline</td><td>Lowest ops</td><td>Cost and lock-in at 3× volume</td></tr>
              </tbody>
            </table>
        """, "notes": "Name the options fairly. Do not set up a straw man."},
        {"layout": "default", "title": "Trade-offs", "budget": 3, "body": """
            <p class="kicker">Trade-offs</p>
            <h2>B wins on the requirements; the cost is operational</h2>
            <table class="table">
              <thead><tr><th>Criterion</th><th>A</th><th>B</th><th>C</th></tr></thead>
              <tbody>
                <tr><td>Six-hour freshness</td><td>No</td><td><b>Yes</b></td><td>Yes</td></tr>
                <tr><td>90-day replay</td><td>Partial</td><td><b>Yes</b></td><td>Vendor-dependent</td></tr>
                <tr><td>Cost at 3×</td><td>Low</td><td>Medium</td><td><b>High</b></td></tr>
                <tr><td>Operational load</td><td><b>Low</b></td><td>High</td><td>Low</td></tr>
                <tr><td>Migration risk</td><td><b>Low</b></td><td>Medium</td><td>Medium</td></tr>
              </tbody>
            </table>
        """, "notes": "The trade-off is not freshness versus cost; it is freshness versus on-call maturity."},
        {"layout": "statement", "title": "Recommendation", "budget": 2, "body": """
            <p class="kicker">Recommendation</p>
            <h2>Adopt B, phased, with batch retained for backfill.</h2>
            <p class="lede">Managed Kafka for ingest, Flink for exactly-once aggregation, and a one-hour rollback to the batch path.</p>
        """, "notes": "One recommendation. Do not offer a menu in the decision meeting."},
        {"layout": "default", "title": "Migration", "budget": 3, "body": """
            <p class="kicker">Migration</p>
            <h2>Four phases, one rollback point</h2>
            <div class="timeline">
              <div><b>P1</b><span>Dual-write to Kafka and batch; compare counts.</span></div>
              <div><b>P2</b><span>Shadow-read from streaming; reconcile 30 days.</span></div>
              <div><b>P3</b><span>Cut over product reads; batch becomes backfill.</span></div>
              <div><b>P4</b><span>Decommission batch ingest after two clean weeks.</span></div>
            </div>
        """, "notes": "The rollback point is P3. State what one hour means operationally."},
        {"layout": "grid2", "title": "Risks", "budget": 2, "body": """
            <p class="kicker">Risks</p>
            <h2>What could break, and the mitigation</h2>
            <div class="grid2">
              <div class="card"><h3>Ordering</h3><p>Partition key change can reorder events; freeze the key at P2.</p></div>
              <div class="card"><h3>Schema evolution</h3><p>Registry compatibility mode; reject breaking changes in CI.</p></div>
              <div class="card"><h3>Cost spike</h3><p>Per-tenant quotas; weekly cost review during P1–P3.</p></div>
              <div class="card"><h3>On-call load</h3><p>Two engineers trained before cutover; runbook and game day.</p></div>
            </div>
        """, "notes": "Risks are operational. Do not pretend the technology is the hard part."},
        {"layout": "close", "title": "Decision", "budget": 2, "body": """
            <p class="kicker">Decision</p>
            <h2>Approve phase 1</h2>
            <p class="lede">Success criteria: 6-hour freshness at 3× volume, 99.95% sink availability, one-hour rollback proven in a game day.</p>
            <p class="meta">Next review: end of phase 2 · Q&A follows</p>
        """, "notes": "Ask for phase 1 only. A phased decision is easier to approve and safer to reverse."},
        {"layout": "default", "title": "Appendix", "budget": 10, "body": """
            <p class="kicker">Appendix</p>
            <h2>Backup</h2>
            <ul>
              <li>Current batch topology and failure modes</li>
              <li>Kafka/Flink sizing and cost model</li>
              <li>Exactly-once proof sketch and replay test</li>
              <li>Migration runbook and game-day plan</li>
            </ul>
        """, "notes": "Q&A. Use the appendix; do not guess at numbers."},
    ],
})

DECKS.append({
    "id": "keynote",
    "type": "Keynote",
    "title": "Design for the worst day",
    "short": "A twelve-minute keynote: the best day is a demo; the worst day is the product.",
    "audience": "Product and design conference",
    "mode": "Live",
    "time": "12 min",
    "theme": "keynote",
    "slides": [
        {"layout": "title", "title": "Design for the worst day", "budget": 1, "body": """
            <p class="kicker">Keynote · fictional case</p>
            <h1>Design for the worst day</h1>
            <p class="lede">The best day is a demo. The worst day is the product.</p>
            <p class="meta">12 minutes · one idea</p>
        """, "notes": "Open with the title and a pause. Do not introduce yourself for more than 10 seconds."},
        {"layout": "statement", "title": "The hook", "budget": 2, "body": """
            <p class="kicker">3:04 a.m.</p>
            <h2>A nurse needs the right record in nine seconds.</h2>
            <p class="lede">The system was designed for a training room with good light, fast Wi-Fi, and a full staff. At 3 a.m. it had none of those.</p>
        """, "notes": "Tell the story in first person if possible. Concrete details: the screen, the wait, the workaround."},
        {"layout": "statement", "title": "The idea", "budget": 2, "body": """
            <p class="kicker">The idea</p>
            <h2>The worst day is the real product.</h2>
            <p class="lede">Not the demo. Not the happy path. The day the network drops, the data is late, and the person is tired.</p>
        """, "notes": "One sentence. Let it land. Do not add a second idea."},
        {"layout": "grid3", "title": "Evidence", "budget": 3, "body": """
            <p class="kicker">Evidence</p>
            <h2>Three domains, one pattern</h2>
            <div class="grid3">
              <div class="card"><h3>Storm</h3><p>A utility's risk model was accurate — until the map server went down with the power.</p></div>
              <div class="card"><h3>Outage</h3><p>A checkout recovered in 47 minutes; the support script arrived in 6.</p></div>
              <div class="card"><h3>Onboarding</h3><p>A first-run flow lost 18% of users at the one step that needed a human.</p></div>
            </div>
        """, "notes": "Three short stories, one pattern. Do not over-explain; the audience will connect them."},
        {"layout": "default", "title": "The pattern", "budget": 2, "body": """
            <p class="kicker">The pattern</p>
            <h2>Stress reveals the system you actually shipped.</h2>
            <div class="two-col">
              <div class="card"><h3>Happy path</h3><p>Designed, measured, demoed. It tells you what the team intended.</p></div>
              <div class="card"><h3>Degraded path</h3><p>Discovered, survived, remembered. It tells you what the product is.</p></div>
            </div>
        """, "notes": "This is the argument. The contrast is the slide."},
        {"layout": "statement", "title": "The counterpoint", "budget": 2, "body": """
            <p class="kicker">Counterpoint</p>
            <h2>Delight is not resilience.</h2>
            <p class="lede">A beautiful empty state does not recover a failed payment. A resilient system can still be warm; it just cannot be only warm.</p>
        """, "notes": "Acknowledge the obvious objection: this is not an argument against craft."},
        {"layout": "grid3", "title": "Three practices", "budget": 2, "body": """
            <p class="kicker">What to do Monday</p>
            <h2>Three practices, no transformation program</h2>
            <div class="grid3">
              <div class="card"><h3>Worst-case walkthrough</h3><p>Once a sprint, walk the task with the network off, the data late, and the user new.</p></div>
              <div class="card"><h3>Degraded-state spec</h3><p>Every core screen gets an empty, slow, stale, and failed state — designed, not defaulted.</p></div>
              <div class="card"><h3>On-call in critique</h3><p>Invite the person who hears the 3 a.m. page to the design review.</p></div>
            </div>
        """, "notes": "Make the practices small enough to start. One slide, three actions."},
        {"layout": "close", "title": "Close", "budget": 1, "body": """
            <p class="kicker">Close</p>
            <h2>The best day is a demo.<br>The worst day is the product.</h2>
            <p class="lede">Design for the day you will never put in the launch video.</p>
        """, "notes": "Pause. End on the line. Do not add a thank-you slide."},
    ],
})

DECKS.append({
    "id": "workshop",
    "type": "Workshop",
    "title": "Design review that catches what CI cannot",
    "short": "A 90-minute workshop: evidence triangulation, two exercises, and three rules to take back.",
    "audience": "Product and engineering teams",
    "mode": "Live facilitation",
    "time": "90 min",
    "theme": "workshop",
    "slides": [
        {"layout": "title", "title": "Design review that catches what CI cannot", "budget": 2, "body": """
            <p class="kicker">Workshop · fictional case</p>
            <h1>Design review that catches what CI cannot</h1>
            <p class="lede">A 90-minute working session. Leave with a review plan and three guard rules.</p>
            <p class="meta">Facilitator: M. Chen · 12–20 participants · tables of four</p>
        """, "notes": "Start on time. State the output: a review plan and three rules, not a lecture."},
        {"layout": "default", "title": "Objective", "budget": 3, "body": """
            <p class="kicker">Objective</p>
            <h2>By the end, each table has:</h2>
            <div class="grid3">
              <div class="card"><h3>1 · A flow</h3><p>One real task mapped end to end, including the states.</p></div>
              <div class="card"><h3>2 · A plan</h3><p>Static, dynamic, and real-surface evidence for that flow.</p></div>
              <div class="card"><h3>3 · Three rules</h3><p>Guard rules that would have caught the failures you found.</p></div>
            </div>
        """, "notes": "Point to the worksheet. The output is tangible; the workshop is not a talk."},
        {"layout": "statement", "title": "Warm-up", "budget": 5, "body": """
            <p class="kicker">Warm-up · 5 min</p>
            <h2>A bug passed CI. Where would you look first?</h2>
            <p class="lede">Think for one minute, then share at your table. Write one place CI cannot see.</p>
        """, "notes": "Run a think-pair-share. Capture answers on a flip chart: interaction, data, device, content, state."},
        {"layout": "grid3", "title": "Concept", "budget": 8, "body": """
            <p class="kicker">Concept · evidence triangulation</p>
            <h2>Three kinds of evidence, not one</h2>
            <div class="grid3">
              <div class="card"><h3>Static</h3><p>Source, tokens, copy, structure. Cheap; blind to behavior.</p></div>
              <div class="card"><h3>Dynamic</h3><p>Built artifact, scripted probe, states. Catches behavior; misses context.</p></div>
              <div class="card"><h3>Real</h3><p>Device, keyboard, screen reader, projector, paper. Catches what the others cannot.</p></div>
            </div>
            <p class="note-box">A finding is strongest when two of the three agree. A single source is a hypothesis.</p>
        """, "notes": "Use a recent bug as the example. Ask which source would have caught it."},
        {"layout": "default", "title": "Example", "budget": 7, "body": """
            <p class="kicker">Example · 7 min</p>
            <h2>CI was green. The keyboard was trapped.</h2>
            <div class="two-col">
              <div class="card"><h3>What CI saw</h3><ul><li>Build passed</li><li>Snapshot passed</li><li>Contrast tokens passed</li></ul></div>
              <div class="card"><h3>What the walkthrough saw</h3><ul><li>Focus entered the modal</li><li>Escape closed the page, not the modal</li><li>Focus never returned to the trigger</li></ul></div>
            </div>
        """, "notes": "Tell the story briefly. The point: the check covered tokens, not interaction."},
        {"layout": "exercise", "title": "Exercise 1 — map the flow", "budget": 15, "body": """
            <p class="kicker">Exercise 1 · 15 min</p>
            <h2>Map one real task</h2>
            <div class="exercise"><span class="time">15 minutes · table of four</span><h3>Choose a task a real user does weekly.</h3><p>Map the steps, the states (empty, loading, error, partial), and the handoffs. Mark one place CI cannot see.</p></div>
            <p class="meta">Worksheet page 1. One flow per table. Work at the level of screens and states, not components.</p>
        """, "notes": "Circulate. Ask each table: what state did you almost forget? Timebox strictly."},
        {"layout": "exercise", "title": "Exercise 2 — write the criteria", "budget": 15, "body": """
            <p class="kicker">Exercise 2 · 15 min</p>
            <h2>Write acceptance criteria that can fail</h2>
            <div class="exercise"><span class="time">15 minutes · same table</span><h3>Take the riskiest step from Exercise 1.</h3><p>Write one criterion that fails today and passes when fixed. Name the evidence source and the surface.</p></div>
            <p class="meta">Worksheet page 2. A criterion without a source is a wish.</p>
        """, "notes": "Give an example: 'Keyboard-only user can dismiss the sheet and focus returns to the trigger.' Then let them work."},
        {"layout": "default", "title": "Share and feedback", "budget": 15, "body": """
            <p class="kicker">Share · 15 min</p>
            <h2>Three tables, three minutes each</h2>
            <div class="grid3">
              <div class="card"><h3>Show</h3><p>The flow and the riskiest step.</p></div>
              <div class="card"><h3>Tell</h3><p>The criterion and the evidence source.</p></div>
              <div class="card"><h3>Ask</h3><p>One thing the room would test differently.</p></div>
            </div>
        """, "notes": "Keep time. Capture one reusable rule per table on the shared board."},
        {"layout": "close", "title": "Close", "budget": 5, "body": """
            <p class="kicker">Close · 5 min</p>
            <h2>Three rules to take back</h2>
            <ol>
              <li>Review the flow, not only the screen.</li>
              <li>Write criteria that fail today.</li>
              <li>Put the real surface in the room.</li>
            </ol>
            <p class="meta">Worksheet, templates, and the reading list are in the shared folder.</p>
        """, "notes": "End on time. Ask for one sentence of feedback per table. Leave the templates."},
    ],
})

DECKS.append({
    "id": "business-review",
    "type": "Business review",
    "title": "Q3 business review — Lumen",
    "short": "A quarterly readout: revenue is up, SMB churn is the signal, and the ask is a decision.",
    "audience": "Executive team",
    "mode": "Live readout + written one-pager",
    "time": "20 min + 10 Q&A",
    "theme": "business",
    "slides": [
        {"layout": "title", "title": "Q3 business review — Lumen", "budget": 1, "body": """
            <p class="kicker">Business review · fictional case</p>
            <h1>Q3 FY26 business review</h1>
            <p class="lede">Revenue is up. SMB churn is the signal. The ask is a decision.</p>
            <p class="meta">Lumen · Executive team · October 2026</p>
        """, "notes": "Lead with the headline and the ask. Do not start with the agenda."},
        {"layout": "default", "title": "Headline", "budget": 1, "body": """
            <p class="kicker">Headline</p>
            <h2>Revenue +18%, but SMB churn doubled after the pricing change</h2>
            <div class="stats">
              <div class="stat"><b>$48.2M</b><span>ARR, +18% YoY</span></div>
              <div class="stat"><b>112%</b><span>NRR, down from 121%</span></div>
              <div class="stat"><b>4.8%</b><span>SMB monthly churn, up from 2.2%</span></div>
              <div class="stat"><b>14 mo</b><span>CAC payback, up from 11</span></div>
            </div>
        """, "notes": "The tension is the story: growth and churn in the same quarter. Pause on the churn number."},
        {"layout": "default", "title": "KPI dashboard", "budget": 2, "body": """
            <p class="kicker">KPI dashboard</p>
            <h2>Plan versus actual</h2>
            <table class="table">
              <thead><tr><th>Metric</th><th>Plan</th><th>Actual</th><th>Variance</th></tr></thead>
              <tbody>
                <tr><td>New ARR</td><td>$6.2M</td><td>$6.8M</td><td class="accent">+$0.6M</td></tr>
                <tr><td>Gross margin</td><td>80%</td><td>81%</td><td class="accent">+1 pt</td></tr>
                <tr><td>SMB churn</td><td>2.8%</td><td>4.8%</td><td>−2 pt</td></tr>
                <tr><td>CAC payback</td><td>12 mo</td><td>14 mo</td><td>−2 mo</td></tr>
              </tbody>
            </table>
        """, "notes": "Two numbers are good, two are bad. Do not average them into a single score."},
        {"layout": "grid3", "title": "Drivers", "budget": 2, "body": """
            <p class="kicker">Drivers</p>
            <h2>Three drivers explain the variance</h2>
            <div class="grid3">
              <div class="card"><h3>SMB churn</h3><p>Pricing change raised the entry tier 22%; churn concentrated in accounts under $6k ACV.</p></div>
              <div class="card"><h3>Enterprise expansion</h3><p>New ARR beat plan, but the sales cycle lengthened by 19 days.</p></div>
              <div class="card"><h3>Services mix</h3><p>Implementation revenue grew faster than subscription, lowering blended margin.</p></div>
            </div>
        """, "notes": "Name the drivers, then take the two that need a decision."},
        {"layout": "default", "title": "Driver 1 — SMB churn", "budget": 3, "body": """
            <p class="kicker">Driver 1</p>
            <h2>Churn is a pricing-packaging problem, not a product problem</h2>
            <table class="table">
              <thead><tr><th>Cohort</th><th>Churn</th><th>Reason</th><th>Action</th></tr></thead>
              <tbody>
                <tr><td>Under $6k ACV</td><td><b>7.1%</b></td><td>Price increase; low usage</td><td>Reintroduce a starter tier</td></tr>
                <tr><td>$6k–$20k</td><td>2.3%</td><td>Stable</td><td>Monitor</td></tr>
                <tr><td>Over $20k</td><td>0.9%</td><td>Expansion</td><td>Double down</td></tr>
              </tbody>
            </table>
        """, "notes": "The data says the problem is the low end. Do not propose a product rebuild."},
        {"layout": "default", "title": "Driver 2 — enterprise", "budget": 2, "body": """
            <p class="kicker">Driver 2</p>
            <h2>Enterprise is working; the cycle is the constraint</h2>
            <div class="grid2">
              <div class="card"><h3>What worked</h3><p>New ARR +$0.6M; 3 logos over $250k; NRR 128% in enterprise.</p></div>
              <div class="card"><h3>What slowed</h3><p>Security review added 19 days; two deals slipped into Q4.</p></div>
            </div>
        """, "notes": "This is the good news. The ask is to protect it, not to fix it."},
        {"layout": "default", "title": "Actions", "budget": 3, "body": """
            <p class="kicker">Actions</p>
            <h2>Four actions, each with an owner and a date</h2>
            <table class="table">
              <thead><tr><th>Action</th><th>Owner</th><th>Due</th><th>Measure</th></tr></thead>
              <tbody>
                <tr><td>Starter tier relaunch</td><td>Product</td><td>15 Nov</td><td>SMB churn ≤ 3.0%</td></tr>
                <tr><td>Security review playbook</td><td>Sales eng</td><td>8 Nov</td><td>Cycle −10 days</td></tr>
                <tr><td>Low-usage churn play</td><td>CS</td><td>30 Nov</td><td>Save rate ≥ 35%</td></tr>
                <tr><td>Services margin review</td><td>Finance</td><td>22 Nov</td><td>Blended margin ≥ 80%</td></tr>
              </tbody>
            </table>
        """, "notes": "Actions are specific and measurable. Do not ask for a task force."},
        {"layout": "grid3", "title": "Asks", "budget": 2, "body": """
            <p class="kicker">Asks</p>
            <h2>Three decisions from this room</h2>
            <div class="grid3">
              <div class="card"><h3>Headcount</h3><p>2 CS roles to run the low-usage save play.</p></div>
              <div class="card"><h3>Pricing exception</h3><p>Approve a starter tier below the current floor.</p></div>
              <div class="card"><h3>Board intro</h3><p>Two enterprise security leaders for the review playbook.</p></div>
            </div>
        """, "notes": "Be explicit. Each ask has an owner and a decision, not a discussion."},
        {"layout": "default", "title": "Next quarter", "budget": 2, "body": """
            <p class="kicker">Next quarter</p>
            <h2>What we will watch</h2>
            <div class="stats">
              <div class="stat"><b>3.0%</b><span>SMB monthly churn target</span></div>
              <div class="stat"><b>115%</b><span>NRR target</span></div>
              <div class="stat"><b>12 mo</b><span>CAC payback target</span></div>
              <div class="stat"><b>80%</b><span>Gross margin floor</span></div>
            </div>
        """, "notes": "Four leading indicators. Tie each to an action."},
        {"layout": "close", "title": "Appendix", "budget": 10, "body": """
            <p class="kicker">Appendix · Q&A</p>
            <h2>Backup</h2>
            <ul>
              <li>Cohort tables and definitions</li>
              <li>Pipeline by segment and slip reason</li>
              <li>Services margin bridge</li>
              <li>Written one-pager and decision log</li>
            </ul>
        """, "notes": "Q&A. Use the appendix; do not re-litigate the headline."},
    ],
})

DECKS.append({
    "id": "product-launch",
    "type": "Product launch",
    "title": "Atlas 2.0 — the field is the product",
    "short": "An eight-minute launch: offline-first field service, a three-scene demo, and a clear CTA.",
    "audience": "Customers, partners, and press",
    "mode": "Live demo + Q&A",
    "time": "8 min + 5 Q&A",
    "theme": "launch",
    "slides": [
        {"layout": "title", "title": "Atlas 2.0 — the field is the product", "budget": 1, "body": """
            <p class="kicker">Product launch · fictional case</p>
            <h1>Atlas 2.0</h1>
            <p class="lede">Field service that works when the signal does not.</p>
            <p class="meta">Launch · 2026 · 8 minutes</p>
        """, "notes": "Open with the promise: offline-first field service. 20 seconds."},
        {"layout": "default", "title": "The problem", "budget": 1, "body": """
            <p class="kicker">The problem</p>
            <h2>Field techs lose the signal, then lose the record</h2>
            <div class="stats">
              <div class="stat"><b>12%</b><span>jobs reworked because the record was incomplete</span></div>
              <div class="stat"><b>2.1h</b><span>per tech per week lost to paper workarounds</span></div>
              <div class="stat"><b>38%</b><span>of sites have no usable signal at the asset</span></div>
              <div class="stat"><b>1 in 5</b><span>photos never reach the office</span></div>
            </div>
        """, "notes": "One number per stat. The last one sets up the photo evidence feature."},
        {"layout": "statement", "title": "The insight", "budget": 1, "body": """
            <p class="kicker">The insight</p>
            <h2>The job does not pause when the network does.</h2>
            <p class="lede">Atlas 2.0 makes the device the system of record, then reconciles when the signal returns.</p>
        """, "notes": "The insight is the architecture: local-first, sync later. 45 seconds."},
        {"layout": "demo", "title": "Demo — three scenes", "budget": 3, "body": """
            <p class="kicker">Demo · 3 minutes</p>
            <h2>Dispatch, offline job, sync</h2>
            <div class="demo-grid">
              <div class="mock">
                <div class="bar"></div><div class="row"></div><div class="row"></div><div class="row short"></div>
                <div class="row"></div><div class="row short"></div>
              </div>
              <div>
                <ul>
                  <li><b>Dispatch:</b> the job arrives with asset history.</li>
                  <li><b>Offline:</b> checklist, photos, and signature complete with no signal.</li>
                  <li><b>Sync:</b> conflict-free merge; the office sees the job in seconds.</li>
                </ul>
              </div>
            </div>
        """, "notes": "Golden path only. Preload data. If the demo fails, switch to the recording and keep the story."},
        {"layout": "default", "title": "Value", "budget": 1, "body": """
            <p class="kicker">Pilot results</p>
            <h2>Less rework, fewer callbacks, faster close</h2>
            <div class="stats">
              <div class="stat"><b>18%</b><span>less rework in the pilot</span></div>
              <div class="stat"><b>2.1h</b><span>saved per tech per week</span></div>
              <div class="stat"><b>4.8/5</b><span>tech satisfaction, 3 customers</span></div>
              <div class="stat"><b>31%</b><span>faster job close</span></div>
            </div>
        """, "notes": "Pilot results, not promises. State the sample: three customers, 240 techs, eight weeks."},
        {"layout": "quote", "title": "Customer evidence", "budget": 1, "body": """
            <p class="kicker">Customer evidence</p>
            <blockquote class="quote">“The job used to end when the tech found signal. Now it ends when the work is done.”</blockquote>
            <p class="meta">— Director of field operations, pilot customer</p>
        """, "notes": "Let the quote do the work. Pause after it."},
        {"layout": "grid2", "title": "Availability", "budget": 1, "body": """
            <p class="kicker">Availability</p>
            <h2>Plans and timing</h2>
            <div class="grid2">
              <div class="card"><h3>Team</h3><p>$39 per tech/month; offline sync, photo evidence, standard reports.</p></div>
              <div class="card"><h3>Enterprise</h3><p>Custom; SSO, audit log, API, and priority sync.</p></div>
            </div>
            <p class="meta">General availability: 12 November 2026 · launch cohort capped at 25 customers.</p>
        """, "notes": "Price is a slide, not a secret. The cohort cap creates urgency without a fake timer."},
        {"layout": "close", "title": "CTA", "budget": 1, "body": """
            <p class="kicker">The ask</p>
            <h2>Join the launch cohort.</h2>
            <p class="lede">Book a 20-minute demo. Bring one real job and one dead zone.</p>
            <p class="meta">atlas.example/launch · demo@atlas.example</p>
        """, "notes": "One CTA. Do not add three links. Repeat the URL once."},
        {"layout": "statement", "title": "Close", "budget": 1, "body": """
            <p class="kicker">Close</p>
            <h2>The field is the product.</h2>
            <p class="lede">Build for the place where the signal ends.</p>
        """, "notes": "End on the line. No thank-you slide."},
    ],
})


def apply_visuals(decks):
    for deck in decks:
        for i, slide in enumerate(deck["slides"]):
            key = (deck["id"], i)
            if key not in VISUALS:
                continue
            kind, art = VISUALS[key]
            if kind == "cover":
                if "has-cover" not in slide.get("layout", ""):
                    slide["layout"] = slide.get("layout", "default") + " has-cover"
                if 'class="cover-art"' not in slide.get("body", ""):
                    slide["body"] = f'<div class="cover-art">{art}</div>' + slide.get("body", "")
            else:
                if 'class="figure"' in slide.get("body", ""):
                    continue
                body = slide.get("body", "")
                block = f'<div class="figure">{art}</div>'
                marker = body.find("</h2>")
                if marker != -1:
                    body = body[:marker + 5] + block + body[marker + 5:]
                else:
                    body = block + body
                slide["body"] = body


apply_visuals(DECKS)


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    for deck in DECKS:
        path = os.path.join(OUT, deck["id"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_deck(deck))
        print("wrote", path)


if __name__ == "__main__":
    main()
