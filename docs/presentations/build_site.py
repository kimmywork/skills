#!/usr/bin/env python3
"""Build the presentation gallery and inferred requirement documents.

Run after build_decks.py:

    python3 docs/presentations/build_decks.py
    python3 docs/presentations/build_site.py
"""

from __future__ import annotations

import html
import os

from build_decks import DECKS

OUT = os.path.dirname(os.path.abspath(__file__))
REQ = os.path.join(OUT, "requirement")

THUMBS = {
    "academic-defense": "marsh.jpg",
    "series-a-pitch": "coast.jpg",
    "incident-postmortem": "server.jpg",
    "architecture-review": "server2.jpg",
    "keynote": "keynote-stage.jpg",
    "workshop": "sticky.jpg",
    "business-review": "meeting.jpg",
    "product-launch": "engineer.jpg",
}

BRIEFS = {
    "academic-defense": {
        "audience": "Thesis committee; one external examiner; 20 minutes plus questions.",
        "intent": "Defend the claim and leave with a clear recommendation and acknowledged limits.",
        "decision": "Accept the thesis, require revisions, or approve the monitoring recommendation.",
        "success": "The committee can restate the question, the two results, and the main limitation without reading the slides.",
        "narrative": "Question → why it matters → method → two results → interpretation → limitations → recommendation.",
        "evidence": "36 fixed transects, monthly; drone photogrammetry at 4 cm/px; salinity loggers at three depths; storm dates from tide gauges. All numbers are fictional for the showcase; replace them with the real study before use.",
        "language": "Formal academic register; assertion headlines; define terms once; never read the slides.",
        "visual": "Light paper, navy accent, serif display; one chart or table per result; grayscale-safe; body text sized for the room.",
        "time": "20 minutes plus 5 minutes Q&A. One to three minutes per slide. Must-cut: the why-it-matters detail and method detail; protect the two results, limitations, and recommendation.",
        "risks": "Overclaiming self-healing; hiding the one-site, nine-month limit; being surprised by storm-sequencing questions.",
        "open": "Replace fictional numbers with the real study; confirm committee format and whether the appendix is allowed.",
        "verification": "Check every number against the study; run the 20-minute hard stop; print the deck and read the grayscale hierarchy.",
    },
    "series-a-pitch": {
        "audience": "Series A investors in a partner meeting; 10 minutes plus Q&A.",
        "intent": "Earn a second meeting and advance to diligence.",
        "decision": "Advance to a partner meeting; request data-room access.",
        "success": "An investor can repeat the wedge, the traction, and the ask in one sentence.",
        "narrative": "Problem → insight → product → market → traction → model → competition → team → ask.",
        "evidence": "Bottom-up TAM, 14 production utilities, $1.2M ARR, 132% NRR, 9-month CAC payback. All metrics are fictional; label assumptions and sources before use.",
        "language": "Spoken, short sentences; one number per slide; no adjective without a number.",
        "visual": "Dark, teal accent, large numerals; one idea per slide; charts with axis, baseline, and source. Cover uses a coastal aerial photograph; no borrowed dashboard.",
        "time": "10 minutes plus 5 Q&A; about one minute per slide. Must-cut: competition detail and team detail; protect traction and the ask.",
        "risks": "TAM inflation; unsupported NRR; a pitch that ends without a clear ask.",
        "open": "Replace fictional metrics; confirm fund stage and check size; decide whether to include a live product demo.",
        "verification": "Read the slide titles as an argument; check every metric against the data room; rehearse the ask.",
    },
    "incident-postmortem": {
        "audience": "Engineering and operations leadership; incident responders.",
        "intent": "Learn, agree actions, and restore trust without assigning blame.",
        "decision": "Approve the six actions and owners; accept the residual risk until closed.",
        "success": "The room can explain the trigger, the amplifier, and the systemic gap.",
        "narrative": "Impact → timeline → root cause → contributing factors → strengths → actions → metrics → lesson.",
        "evidence": "Timeline, logs, config diff, gateway trace. The incident and numbers are fictional; reconcile with the written report before delivery.",
        "language": "Blameless, plain, past tense; separate trigger from amplifier; no euphemism.",
        "visual": "Light, red accent, monospace timeline; one timeline and one action table; readable in print. Cover uses a night operations photograph, not a server room.",
        "time": "15 minutes plus 10 Q&A. Must-cut: log detail and individual action rows; protect impact, root cause, and actions.",
        "risks": "Blame framing; actions without owners; hiding a contributing factor.",
        "open": "Replace fictional data; confirm legal and communications review; decide whether to include customer quotes.",
        "verification": "Check every claim against the written report; read the timeline aloud; confirm owners and dates.",
    },
    "architecture-review": {
        "audience": "Staff engineers and the architecture board.",
        "intent": "Approve phase 1 of the streaming migration.",
        "decision": "Approve phase 1; fund two engineers and a game day.",
        "success": "The board can state the trade-off and the one-hour rollback.",
        "narrative": "Context → requirements → options → trade-offs → recommendation → migration → risks → decision.",
        "evidence": "2.4B events/day, six-hour freshness, cost ceiling, 90-day replay. Metrics are fictional; validate against current telemetry and cost data.",
        "language": "Technical and precise; define exactly-once and replay; no vendor marketing.",
        "visual": "Dark blue, cyan accent; one table or diagram per slide; monospace for constraints. Cover uses an engineering review photograph, not a data-center rack.",
        "time": "25 minutes plus 10 Q&A. Must-cut: option C detail and vendor comparison; protect trade-offs, migration, risks, and the decision.",
        "risks": "Straw-man options; ignoring on-call load; no rollback.",
        "open": "Replace fictional metrics; confirm vendor constraints; add the real topology diagram.",
        "verification": "Check the trade-off table against the requirements; walk the rollback; rehearse the decision ask.",
    },
    "keynote": {
        "audience": "Product and design conference; mixed seniority.",
        "intent": "Leave with one idea and three practices.",
        "decision": "Try one practice in the next sprint.",
        "success": "The audience can repeat 'the worst day is the product' and name one practice.",
        "narrative": "Hook → one idea → evidence → pattern → counterpoint → practices → close.",
        "evidence": "Three fictional stories, each with one concrete detail. Do not invent statistics; use the speaker's own evidence.",
        "language": "Spoken, short sentences, repetition, pauses; no jargon; one idea.",
        "visual": "Dark warm, amber accent, large serif; minimal text; one image or metaphor per slide. Cover uses a stage photograph instead of a decorative SVG.",
        "time": "12 minutes; one to two minutes per slide. Must-cut: third example detail; protect the hook, the idea, and the close.",
        "risks": "Too many ideas; a therapy tone; no action.",
        "open": "Replace fictional stories with the speaker's own; confirm stage and AV.",
        "verification": "Read the titles; time the talk; record one run and cut 10%.",
    },
    "workshop": {
        "audience": "Product and engineering teams; 12–20 participants at tables of four.",
        "intent": "Leave with a review plan and three guard rules.",
        "decision": "Adopt one rule in the next review.",
        "success": "Each table produces a flow, a criterion that can fail, and a rule.",
        "narrative": "Objective → warm-up → concept → example → exercise 1 → exercise 2 → share → close.",
        "evidence": "One real bug that passed CI; a keyboard walkthrough example; no fictional metrics.",
        "language": "Facilitator voice; short instructions; timeboxes; ask, don't tell.",
        "visual": "Light warm, green accent; exercise cards; large timers; minimal slides.",
        "time": "90 minutes; 15-minute exercises. Must-cut: example detail; protect the exercises and the share.",
        "risks": "Lecture creep; one table dominates; no tangible output.",
        "open": "Confirm room layout, table size, and whether teams bring a real flow.",
        "verification": "Run the timeboxes; check every exercise has an output; collect one-sentence feedback.",
    },
    "business-review": {
        "audience": "Executive team; 20 minutes plus Q&A.",
        "intent": "Decide on SMB pricing and CS headcount.",
        "decision": "Approve the starter tier, two CS roles, and a board intro.",
        "success": "The room agrees on the churn driver and the three asks.",
        "narrative": "Headline → KPI → drivers → churn → enterprise → actions → asks → next quarter.",
        "evidence": "ARR, NRR, churn, CAC payback, cohort tables. Metrics are fictional; reconcile with finance before delivery.",
        "language": "Answer-first, plain, numbers with definitions; no hedging.",
        "visual": "Light corporate, green/amber/red; one dashboard or table per slide; print-safe. Cover uses a team reviewing charts, not a workshop photograph.",
        "time": "20 minutes plus 10 Q&A. Must-cut: cohort detail and definitions; protect the headline, churn, and asks.",
        "risks": "Averaging good and bad news; actions without owners; asks without decisions.",
        "open": "Replace fictional metrics; confirm attendee list and decision rights.",
        "verification": "Check the KPI table against finance; read the headline alone; rehearse the ask.",
    },
    "product-launch": {
        "audience": "Customers, partners, and press; 8 minutes plus Q&A.",
        "intent": "Join the launch cohort or book a demo.",
        "decision": "Sign up for the cohort or book a demo.",
        "success": "The audience can state the offline-first value and the single CTA.",
        "narrative": "Problem → insight → demo → value → evidence → availability → CTA → close.",
        "evidence": "Pilot results: 3 customers, 240 techs, 8 weeks. Fictional; label the sample and replace before use.",
        "language": "Spoken, energetic, concrete; no feature list; one CTA.",
        "visual": "Bright, coral/blue; product mockups; one demo path; captions for the demo. Cover uses a field technician with a tablet, not a laboratory photograph.",
        "time": "8 minutes plus 5 Q&A. Must-cut: pricing detail; protect the demo, value, and CTA.",
        "risks": "Demo failure; feature tour; multiple CTAs.",
        "open": "Replace fictional pilot data; prepare a fallback recording; confirm pricing and legal review.",
        "verification": "Run the demo with the network off; time the demo; check the CTA appears once.",
    },
}

REQ_TEMPLATE = """# __TITLE__ — Presentation Requirements

> Source: [`../__ID__.html`](../__ID__.html) · Type: __TYPE__ · Audience: __AUDIENCE__ · Mode: __MODE__ · Time: __TIME__
> Fictional case. The deck is the current implementation; this file captures the brief, structure, and acceptance.

## 1. Audience and intent

__AUDIENCE_TEXT__

**Intent:** __INTENT__

**Decision or action:** __DECISION__

**Success:** __SUCCESS__

## 2. Narrative

__NARRATIVE__

### Slide sequence

| # | Slide | Budget | Purpose / speaker cue |
|---:|---|---:|---|
__SLIDES__

## 3. Evidence and fact-check

__EVIDENCE__

**Fact-check gate:** confirm names, numbers, dates, and comparisons before layout. A precise number without a date and source is a liability.

## 4. Language and delivery

__LANGUAGE__

## 5. Visual and accessibility

__VISUAL__

## 6. Time and structure

__TIMING__

**Q&A:** prepare the ten most likely questions and one honest answer for each. Do not improvise a fact.

## 7. Verification

- **Titles-only read:** read the slide titles in order. The argument must hold without the body.
- **Timed run:** rehearse to a hard stop, record it, and cut from the must-cut list.
- **Evidence:** every number and comparison has a source, date, and range where relevant.
- **Visual:** check at presentation size, in grayscale, and in the exported file.
- **Accessibility:** alt text, reading order, contrast, color-not-alone, reduced motion, captions/transcript.
- **Print:** one slide per page, notes hidden, no clipped content.
- __CASE_VERIFICATION__

## 8. Non-goals and open questions

**Risks:** __RISKS__

**Open:** __OPEN__
"""

INDEX = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="Eight fictional presentation decks: academic defense, Series A pitch, incident postmortem, architecture review, keynote, workshop, business review, and product launch.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23161616'/%3E%3Ctext x='16' y='22' text-anchor='middle' font-family='Georgia,serif' font-size='18' fill='%23f4f1e9'%3EP%3C/text%3E%3C/svg%3E">
<title>Presentation decks — eight occasions, one skill</title>
<style>
  :root{
    --paper:#f5f1e8;--card:#fffdf7;--ink:#171717;--muted:#5f5a52;--line:#d8d1c3;
    --accent:#9a4508;--accent-soft:#f3e3d2;--dark:#161616;--dark-fg:#f4f1e9;
    --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
    --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  }
  [data-theme="dark"]{
    --paper:#14120e;--card:#1c1914;--ink:#f4f1e9;--muted:#a8a294;--line:#332d22;
    --accent:#f0a955;--accent-soft:#3a2a14;--dark:#0b0a08;--dark-fg:#f4f1e9;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 var(--sans);-webkit-font-smoothing:antialiased}
  a{color:inherit}
  :focus-visible{outline:2px solid var(--accent);outline-offset:3px}
  .wrap{width:min(100% - 48px,1180px);margin-inline:auto}
  .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
  .kicker{margin:0 0 12px;font:700 11px/1.2 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}
  .topbar{position:sticky;top:0;z-index:20;background:var(--paper);border-bottom:1px solid var(--line)}
  .topbar-inner{display:flex;align-items:center;gap:24px;min-height:64px}
  .brand{display:inline-flex;align-items:center;gap:10px;min-height:44px;text-decoration:none;font:700 18px/1 var(--serif)}
  .brand-mark{width:22px;height:22px;border-radius:6px;background:var(--ink);color:var(--paper);display:grid;place-items:center;font:700 12px/1 var(--mono)}
  .nav{display:flex;gap:20px;margin-left:8px}
  .nav a{display:inline-flex;align-items:center;min-height:44px;text-decoration:none;color:var(--muted);font-size:13px;font-weight:600}
  .nav a:hover{color:var(--ink)}
  .nav .spacer{flex:1}
  .topbar-actions{margin-left:auto;display:flex;align-items:center;gap:10px}
  .icon-btn{width:44px;height:44px;border-radius:50%;border:1px solid var(--line);background:transparent;color:var(--ink);cursor:pointer;display:grid;place-items:center;font:600 17px/1 var(--sans)}
  .icon-btn:hover{border-color:var(--ink);background:var(--card)}
  .hero{padding:76px 0 44px;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:56px;align-items:center}
  .hero h1{margin:0 0 16px;font:600 clamp(46px,6.8vw,86px)/.94 var(--serif);letter-spacing:-.045em;max-width:11ch}
  .hero h1 em{font-style:italic;color:var(--accent)}
  .hero p{color:var(--muted);max-width:56ch;font-size:17px}
  .hero-meta{display:flex;flex-wrap:wrap;gap:10px 24px;border-top:1px solid var(--line);padding-top:18px;margin-top:24px;color:var(--muted);font-size:12px}
  .hero-meta b{color:var(--ink);font:700 15px/1 var(--mono);margin-right:4px}
  .hero-art{background:var(--dark);color:var(--dark-fg);border-radius:22px;padding:22px;box-shadow:0 24px 60px rgba(30,26,18,.16);position:relative;min-height:320px;overflow:hidden}
  .hero-art .slide-stack{display:flex;flex-direction:column;gap:10px}
  .mini{background:#1e1e1e;border:1px solid #333;border-radius:10px;padding:14px 16px;display:flex;align-items:center;gap:12px}
  .mini:nth-child(2){margin-left:22px}.mini:nth-child(3){margin-left:44px}
  .mini i{display:block;width:28px;height:28px;border-radius:7px;background:var(--accent);flex:none}
  .mini img{display:block;width:58px;height:44px;border-radius:7px;object-fit:cover;flex:none}
  .mini b{display:block;font:600 13px/1.2 var(--sans)}
  .mini span{display:block;color:#a8a397;font-size:10.5px;margin-top:3px}
  .hero-art .caption{position:absolute;left:22px;bottom:18px;color:#a8a397;font:600 10px/1.4 var(--mono);letter-spacing:.08em;text-transform:uppercase}
  .principles{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;padding:18px 0;border-block:1px solid var(--line)}
  .principle b{display:block;font-size:11.5px;line-height:1.3}
  .principle span{display:block;color:var(--muted);font-size:10.5px;line-height:1.4;margin-top:3px}
  section{padding:70px 0}
  .section-head{max-width:720px;margin-bottom:28px}
  .section-head h2{margin:0 0 12px;font:600 clamp(32px,4.5vw,54px)/.98 var(--serif);letter-spacing:-.035em}
  .section-head p{margin:0;color:var(--muted);font-size:16px;max-width:62ch}
  .deck-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:18px}
  .deck-card{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:0;min-height:0;overflow:hidden;transition:transform .14s ease,border-color .14s ease,box-shadow .14s ease}
  .deck-thumb{display:block;height:154px;overflow:hidden;background:var(--paper);border-bottom:1px solid var(--line)}
  .deck-thumb img{display:block;width:100%;height:100%;object-fit:cover}
  .deck-body{display:flex;flex-direction:column;flex:1;padding:16px 18px 18px}
  .proof-card{padding:18px;overflow:visible;min-height:150px;justify-content:flex-start}
  .proof-card .deck-top{padding-bottom:9px;border-bottom:1px solid var(--line);margin-bottom:12px;font-size:9.5px}
  .proof-card h3{margin:0 0 8px}
  .proof-card p{font-size:13px}
  .deck-card:hover{transform:translateY(-3px);border-color:var(--accent);box-shadow:0 14px 30px rgba(30,26,18,.08)}
  .deck-top{display:flex;justify-content:space-between;gap:10px;color:var(--muted);font:600 10px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase}
  .deck-card h3{margin:10px 0 8px;font:600 23px/1.07 var(--serif);letter-spacing:-.02em}
  .deck-card h3 a{text-decoration:none}
  .deck-card h3 a:hover{color:var(--accent)}
  .deck-card p{margin:0;color:var(--muted);font-size:13px;flex:1}
  .deck-meta{display:flex;flex-wrap:wrap;gap:8px 12px;margin-top:14px;color:var(--muted);font-size:10.5px}
  .deck-actions{display:flex;flex-wrap:wrap;gap:14px;margin-top:14px;padding-top:12px;border-top:1px solid var(--line)}
  .deck-actions a{display:inline-flex;align-items:center;min-height:44px;text-decoration:none;font:700 12px/1 var(--sans)}
  .deck-actions a:first-child{color:var(--accent)}
  .deck-actions a:last-child{color:var(--muted)}
  .deck-actions a:hover{text-decoration:underline;text-underline-offset:3px}
  .loop{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:24px}
  .step{border:1px solid var(--line);border-radius:12px;background:var(--card);padding:16px}
  .step b{display:block;font:600 12px/1.3 var(--sans)}
  .step span{display:block;color:var(--muted);font-size:11px;line-height:1.45;margin-top:4px}
  .req{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}
  .req p{color:var(--muted)}
  .req-links{display:grid;grid-template-columns:1fr 1fr;gap:8px}
  .req-link{display:grid;grid-template-columns:minmax(0,1fr) 112px;align-items:center;gap:10px;padding:11px 13px;border:1px solid var(--line);border-radius:8px;background:var(--card);text-decoration:none;font-size:12.5px;font-weight:600}
  .req-link span{color:var(--muted);font:600 9.5px/1 var(--mono);letter-spacing:.02em;white-space:nowrap;text-align:right}
  .req-link:hover{border-color:var(--accent);color:var(--accent)}
  .install{--panel-bg:#161616;--panel-fg:#f4f1e9;--panel-muted:#b8aa96;--panel-line:#444;--panel-code:#0b0b0b;background:var(--panel-bg);color:var(--panel-fg);border-radius:22px;padding:clamp(24px,4vw,44px);display:grid;grid-template-columns:1fr 1fr;gap:30px;align-items:center;min-width:0}
  [data-theme="dark"] .install{--panel-bg:#f4f1e9;--panel-fg:#171717;--panel-muted:#5f5a52;--panel-line:#d8d1c3;--panel-code:#ece7db}
  .install > *{min-width:0}
  .install h2{margin:0 0 10px;font:600 clamp(30px,4vw,48px)/.98 var(--serif);letter-spacing:-.03em}
  .install p{color:var(--panel-muted);max-width:48ch}
  .install .btn{display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border-radius:999px;border:1px solid var(--panel-line);color:var(--panel-fg);text-decoration:none;font:700 12px/1 var(--sans);margin:6px 8px 0 0}
  .install .btn:hover{border-color:var(--panel-fg)}
  .cmd{display:block;max-width:100%;background:var(--panel-code);border:1px solid var(--panel-line);border-radius:10px;padding:14px;overflow-x:auto;font:12px/1.7 var(--mono);color:var(--panel-fg);white-space:nowrap;margin-bottom:10px}
  .cmd-row{display:flex;align-items:stretch;gap:8px;margin-bottom:10px}
  .cmd-row .cmd{margin-bottom:0;flex:1;min-width:0}
  .copy-btn{min-height:44px;padding:0 16px;border-radius:10px;border:1px solid var(--panel-line);background:var(--panel-code);color:var(--panel-fg);font:700 11px/1 var(--sans);cursor:pointer;white-space:nowrap;flex:none}
  .copy-btn:hover{border-color:var(--panel-fg)}
  footer{border-top:1px solid var(--line);padding:26px 0 44px;color:var(--muted);font-size:12px}
  .footer-inner{display:flex;flex-wrap:wrap;gap:12px 24px;justify-content:space-between}
  .footer-inner a{color:var(--ink);text-decoration:none;font-weight:600}
  .footer-inner a:hover{color:var(--accent)}
  @media (max-width:960px){
    .hero,.req,.install{grid-template-columns:1fr}
    .principles{grid-template-columns:repeat(3,1fr)}
    .loop{grid-template-columns:1fr 1fr}
    .nav{display:none}
  }
  @media (max-width:600px){
    .wrap{width:min(100% - 36px,1180px)}
    .hero h1{font-size:clamp(44px,13vw,70px)}
    .principles{grid-template-columns:1fr 1fr}
    .loop{grid-template-columns:1fr}
    .req-links{grid-template-columns:1fr}
    .deck-grid{grid-template-columns:1fr}
  }
</style>
</head>
<body>
<header class="topbar">
  <div class="wrap topbar-inner">
    <a class="brand" href="#top"><span class="brand-mark" aria-hidden="true">P</span><span>presentation</span></a>
    <nav class="nav" aria-label="Primary">
      <a href="#decks">Decks</a>
      <a href="#proof">What it proves</a>
      <a href="#loop">Production</a>
      <a href="#requirements">Requirements</a>
    </nav>
    <div class="topbar-actions">
      <button class="icon-btn" id="themeBtn" type="button" aria-pressed="false">
        <span aria-hidden="true" id="themeIcon">☾</span>
        <span class="sr-only" id="themeLabel">Switch to dark theme</span>
      </button>
    </div>
  </div>
</header>
<main id="top">
  <section class="hero wrap">
    <div>
      <p class="kicker">Presentation skill · fictional cases</p>
      <h1>Eight decks. Eight <em>occasions.</em></h1>
      <p>A presentation is an argument an audience can follow and act on. These decks are built to be inspected: narrative, evidence, language, time, visual design, and speaker notes in one self-contained file each.</p>
      <div class="hero-meta">
        <span><b>8</b> decks</span><span><b>8</b> occasion types</span><span><b>3</b> modes</span><span><b>1</b> file each</span>
      </div>
    </div>
    <div class="hero-art" aria-hidden="true">
      <div class="slide-stack">
        <div class="mini"><img src="assets/marsh.jpg" alt=""><div><b>Academic defense</b><span>evidence · limits · Q&amp;A</span></div></div>
        <div class="mini"><img src="assets/coast.jpg" alt=""><div><b>Series A pitch</b><span>traction · ask · 10 min</span></div></div>
        <div class="mini"><img src="assets/server.jpg" alt=""><div><b>Incident postmortem</b><span>timeline · root cause · actions</span></div></div>
      </div>
      <div class="caption">one idea per slide · one source per number</div>
    </div>
  </section>

  <div class="principles wrap" aria-label="What these decks prove">
    <div class="principle"><b>Narrative</b><span>One takeaway; an arc the titles can carry.</span></div>
    <div class="principle"><b>Evidence</b><span>Numbers with sources, dates, and comparisons.</span></div>
    <div class="principle"><b>Language</b><span>Spoken, written, and slide registers.</span></div>
    <div class="principle"><b>Time</b><span>Budgets, must-cuts, Q&amp;A, rehearsal.</span></div>
    <div class="principle"><b>Visual</b><span>Projection scale, honest charts, grayscale.</span></div>
    <div class="principle"><b>Access</b><span>Alt text, reading order, captions, contrast.</span></div>
  </div>

  <section class="wrap" id="decks">
    <div class="section-head">
      <p class="kicker">The decks</p>
      <h2>Pick the occasion.</h2>
      <p>Each card opens a self-contained HTML deck. Use ← → to navigate, N for speaker notes, and print to PDF for a handout. The requirements link explains the brief behind the deck.</p>
    </div>
    <div class="deck-grid">
__CARDS__
    </div>
  </section>

  <section class="wrap" id="proof">
    <div class="section-head">
      <p class="kicker">What it proves</p>
      <h2>Different rooms, same discipline.</h2>
      <p>The deck changes; the standards do not. These cases cover evidence, persuasion, learning, governance, demo, and craft.</p>
    </div>
    <div class="deck-grid">
      <article class="deck-card proof-card"><div class="deck-top"><span>Evidence</span><span>Academic</span></div><h3>Defend a claim, not a method</h3><p>One question, two results, explicit limits, and a recommendation the committee can act on.</p></article>
      <article class="deck-card proof-card"><div class="deck-top"><span>Persuasion</span><span>Pitch</span></div><h3>Make the ask inevitable</h3><p>Bottom-up market, traction, a business model, and a specific ask — one number per slide.</p></article>
      <article class="deck-card proof-card"><div class="deck-top"><span>Learning</span><span>Postmortem</span></div><h3>Learn without blaming</h3><p>Impact, timeline, trigger, amplifier, actions with owners, and a systemic lesson.</p></article>
      <article class="deck-card proof-card"><div class="deck-top"><span>Decision</span><span>Architecture</span></div><h3>Make the trade-off explicit</h3><p>Options, criteria, a recommendation, a migration plan, and a rollback the board can trust.</p></article>
      <article class="deck-card proof-card"><div class="deck-top"><span>Story</span><span>Keynote</span></div><h3>One idea, one action</h3><p>A hook, a single idea, three pieces of evidence, three practices, and a close that lands.</p></article>
      <article class="deck-card proof-card"><div class="deck-top"><span>Teaching</span><span>Workshop</span></div><h3>Make the room do the work</h3><p>Objective, warm-up, concept, example, two exercises, share, and three rules to take back.</p></article>
      <article class="deck-card proof-card"><div class="deck-top"><span>Governance</span><span>Business review</span></div><h3>Surface the variance</h3><p>Headline, KPI table, drivers, actions, and three asks with owners and dates.</p></article>
      <article class="deck-card proof-card"><div class="deck-top"><span>Launch</span><span>Product</span></div><h3>Demo the value, not the features</h3><p>Problem, insight, three-scene demo, pilot evidence, availability, one CTA.</p></article>
    </div>
  </section>

  <section class="wrap" id="loop">
    <div class="section-head">
      <p class="kicker">Production loop</p>
      <h2>Built like a deck, not a document.</h2>
      <p>The same loop the presentation skill asks for: fix the stage, settle one sample, write in batches, check a contact sheet, and keep one source for the notes and the time budget.</p>
    </div>
    <div class="loop">
      <div class="step"><b>1 · Stage + tokens</b><span>16:9, type scale, color roles, safe margins.</span></div>
      <div class="step"><b>2 · Skeleton + sample</b><span>One slide proves the layout before thirty follow.</span></div>
      <div class="step"><b>3 · Section data</b><span>Title, budget, notes; generate counter and notes.</span></div>
      <div class="step"><b>4 · Contact sheet</b><span>Batch screenshots; inspect the sheet, then the page.</span></div>
      <div class="step"><b>5 · Assets + facts</b><span>Official source first; comparison matches the claim.</span></div>
    </div>
  </section>

  <section class="wrap" id="requirements">
    <div class="req">
      <div>
        <p class="kicker">Context</p>
        <h2>The decks have requirements, not just slides.</h2>
        <p>Each case has an inferred requirements document: audience, intent, narrative, evidence, language, visual rules, time budget, verification, and open questions. Read it before a redesign or a review.</p>
        <p><a href="requirement/README.html">Read the review verdict and coverage matrix →</a></p>
      </div>
      <div class="req-links">
__REQ_LINKS__
      </div>
    </div>
  </section>

  <section class="wrap">
    <div class="install">
      <div>
        <h2>Use the skill.</h2>
        <p>The presentation skill is part of the <code>design</code> bundle. It covers live, written, and hybrid presentations, from a ten-minute pitch to a ninety-minute workshop.</p>
        <a class="btn" href="https://skills.kimmy.fun/design/skills/presentation/SKILL.html">Read SKILL.md</a>
        <a class="btn" href="requirement/README.html">Requirements</a>
      </div>
      <div>
        <div class="cmd-row">
          <code class="cmd" id="installCmd">npx skills add kimmywork/skills --skill presentation</code>
          <button class="copy-btn" id="copyBtn" type="button" aria-describedby="copyStatus">Copy</button>
        </div>
        <span class="sr-only" id="copyStatus" aria-live="polite"></span>
        <code class="cmd">claude plugin install design@kimmywork-skills</code>
        <p class="small">Fictional cases. Each deck is one self-contained HTML file with speaker notes and a time budget. Photos via Unsplash; credits in <a href="assets/CREDITS.html">assets/CREDITS</a>.</p>
      </div>
    </div>
  </section>
</main>
<footer>
  <div class="wrap footer-inner">
    <span><a href="https://github.com/kimmywork/skills">kimmywork/skills</a> · <code>design/skills/presentation</code></span>
    <span><a href="requirement/README.html">Requirements</a> · <a href="assets/CREDITS.html">Image credits</a></span>
  </div>
</footer>
<script>
(function(){
  "use strict";
  var root = document.documentElement;
  var themeBtn = document.getElementById("themeBtn");
  var themeIcon = document.getElementById("themeIcon");
  var themeLabel = document.getElementById("themeLabel");
  var stored = null;
  try { stored = localStorage.getItem("presentation-theme"); } catch (e) {}
  var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  var initial = stored || (prefersDark ? "dark" : "light");

  function setTheme(theme){
    root.setAttribute("data-theme", theme);
    var dark = theme === "dark";
    themeBtn.setAttribute("aria-pressed", String(dark));
    themeIcon.textContent = dark ? "☀" : "☾";
    themeLabel.textContent = dark ? "Switch to light theme" : "Switch to dark theme";
    try { localStorage.setItem("presentation-theme", theme); } catch (e) {}
  }
  setTheme(initial);
  themeBtn.addEventListener("click", function(){
    setTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark");
  });

  var copyBtn = document.getElementById("copyBtn");
  var cmd = document.getElementById("installCmd");
  var status = document.getElementById("copyStatus");
  function fallback(text, done){
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); } catch (e) {}
    document.body.removeChild(ta);
    done();
  }
  if (copyBtn && cmd) {
    copyBtn.addEventListener("click", function(){
      var text = cmd.textContent.trim();
      function done(){
        copyBtn.textContent = "Copied";
        status.textContent = "Install command copied";
        setTimeout(function(){ copyBtn.textContent = "Copy"; status.textContent = ""; }, 2000);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function(){ fallback(text, done); });
      } else {
        fallback(text, done);
      }
    });
  }
})();
</script>
</body>
</html>
"""


def md(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def speaker_cue(text: str) -> str:
    text = " ".join(str(text).split())
    first = text.split(". ")[0]
    return first if first.endswith(".") else first + "."


def render_requirement(deck: dict) -> str:
    b = BRIEFS[deck["id"]]
    slides = []
    for i, s in enumerate(deck["slides"], 1):
        slides.append(
            f"| {i} | {md(s.get('title', ''))} | {s.get('budget', 1)} | {md(speaker_cue(s.get('notes', '')))} |"
        )
    out = REQ_TEMPLATE
    out = out.replace("__TITLE__", deck["title"])
    out = out.replace("__ID__", deck["id"])
    out = out.replace("__TYPE__", deck["type"])
    out = out.replace("__AUDIENCE__", deck["audience"])
    out = out.replace("__MODE__", deck["mode"])
    out = out.replace("__TIME__", deck["time"])
    out = out.replace("__AUDIENCE_TEXT__", b["audience"])
    out = out.replace("__INTENT__", b["intent"])
    out = out.replace("__DECISION__", b["decision"])
    out = out.replace("__SUCCESS__", b["success"])
    out = out.replace("__NARRATIVE__", b["narrative"])
    out = out.replace("__SLIDES__", "\n".join(slides))
    out = out.replace("__EVIDENCE__", b["evidence"])
    out = out.replace("__LANGUAGE__", b["language"])
    out = out.replace("__VISUAL__", b["visual"])
    out = out.replace("__TIMING__", b["time"] + f" (total budget: {sum(s.get('budget', 1) for s in deck['slides'])} minutes)")
    out = out.replace("__CASE_VERIFICATION__", b["verification"])
    out = out.replace("__RISKS__", b["risks"])
    out = out.replace("__OPEN__", b["open"])
    return out


def render_index() -> str:
    cards = []
    req_links = []
    for d in DECKS:
        thumb = THUMBS.get(d["id"], "")
        cards.append(
            f'''<article class="deck-card">
  <a class="deck-thumb" href="{d["id"]}.html" tabindex="-1" aria-hidden="true"><img src="assets/{thumb}" alt=""></a>
  <div class="deck-body">
    <div class="deck-top"><span>{html.escape(d["type"])}</span><span>{html.escape(d["mode"])}</span></div>
    <h3><a href="{d["id"]}.html">{html.escape(d["title"])}</a></h3>
    <p>{html.escape(d["short"])}</p>
    <div class="deck-meta"><span>{html.escape(d["audience"])}</span><span>{html.escape(d["time"])}</span></div>
    <div class="deck-actions"><a href="{d["id"]}.html">Open deck →</a><a href="requirement/{d["id"]}.html">Requirements</a></div>
  </div>
</article>'''
        )
        req_links.append(
            f'<a class="req-link" href="requirement/{d["id"]}.html">{html.escape(d["short"].split(":")[0])} <span>{d["id"]}</span></a>'
        )
    out = INDEX.replace("__CARDS__", "\n".join(cards))
    out = out.replace("__REQ_LINKS__", "\n".join(req_links))
    return out


REQUIREMENT_README = """# Presentation Deck Requirements

These documents reverse-engineer the requirements behind the eight fictional decks in `docs/presentations/`. The deck is the current implementation; the requirement captures the brief, narrative, evidence, visual rules, time budget, and acceptance so a redesign or review does not lose context.

## Review verdict

The set is suitable as a **presentation-skill showcase**: it covers evidence, persuasion, learning, decision, story, teaching, governance, and launch. It is not a product deck library; every case is fictional and every number must be replaced before real use.

## Coverage

| Deck | Type | Audience | Decision / action | Mode | Time | What it proves |
|---|---|---|---|---|---|---|
| [academic-defense](academic-defense.html) | Academic defense | Thesis committee | Pass / revise | Live + Q&A | 20 + 5 | Assertion–evidence, limits, Q&A |
| [series-a-pitch](series-a-pitch.html) | Series A pitch | Investors | Advance to diligence | Live | 10 + 5 | Narrative, traction, ask |
| [incident-postmortem](incident-postmortem.html) | Incident postmortem | Engineering leadership | Approve actions | Hybrid | 15 + 10 | Timeline, root cause, accountability |
| [architecture-review](architecture-review.html) | Architecture review | Architecture board | Approve phase 1 | Live + Q&A | 25 + 10 | Trade-offs, migration, risk |
| [keynote](keynote.html) | Keynote | Conference | Try one practice | Live | 12 | One idea, story, stagecraft |
| [workshop](workshop.html) | Workshop | Product teams | Adopt one rule | Live facilitation | 90 | Objective, exercises, feedback |
| [business-review](business-review.html) | Business review | Executive team | Approve asks | Live + written | 20 + 10 | KPI, variance, decisions |
| [product-launch](product-launch.html) | Product launch | Customers / press | Join cohort / demo | Live demo | 8 + 5 | Demo, value, CTA |

## Shared standards

- One-sentence takeaway; titles-only read must hold.
- One number per claim; source, date, range.
- Comparison must match the claim.
- Time budget per slide; must-cut list; Q&A buffer.
- Visual system chosen for the room, not the laptop.
- A photograph is used only when it is the subject of the cover or story slide; evidence slides use the occasion's surface. Do not reuse a photograph across occasions.
- Alt text, reading order, contrast, color-not-alone, reduced motion.
- Speaker notes are part of the deck; the deck is the source of truth.

## How to use

Read the case requirement before changing the deck. If the deck and the requirement disagree, record the conflict; do not silently choose one. Replace fictional data with real, sourced data before any real delivery.
"""


def main() -> None:
    os.makedirs(REQ, exist_ok=True)
    for deck in DECKS:
        path = os.path.join(REQ, deck["id"] + ".md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_requirement(deck))
        print("wrote", path)
    with open(os.path.join(REQ, "README.md"), "w", encoding="utf-8") as f:
        f.write(REQUIREMENT_README)
    print("wrote", os.path.join(REQ, "README.md"))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index())
    print("wrote", os.path.join(OUT, "index.html"))


if __name__ == "__main__":
    main()
