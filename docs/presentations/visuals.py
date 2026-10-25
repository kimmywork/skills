"""Inline SVG art and per-deck layout overrides for the presentation decks."""

import base64
import html
import os


def photo(filename: str, alt: str) -> str:
    path = os.path.join(os.path.dirname(__file__), "assets", filename)
    data = base64.b64encode(open(path, "rb").read()).decode("ascii")
    return f'<img class="photo" src="data:image/jpeg;base64,{data}" alt="{html.escape(alt)}">'


def svg_marsh() -> str:
    return """<svg class="art-svg" viewBox="0 0 720 420" aria-hidden="true">
<rect width="720" height="420" fill="#dfe8ea"/>
<circle cx="585" cy="78" r="44" fill="#f2c14e" opacity=".85"/>
<path d="M0 238 Q170 214 360 228 T720 220 V420 H0Z" fill="#7aa6a0"/>
<path d="M0 300 Q170 280 360 292 T720 288 V420 H0Z" fill="#4f7f78"/>
<path d="M0 340 Q170 320 360 332 T720 328 V420 H0Z" fill="#2f5d57"/>
<g stroke="#2f5d57" stroke-width="3" stroke-linecap="round" opacity=".85">
<path d="M70 330v-46M86 334v-62M102 330v-40M118 336v-54M134 330v-44M150 334v-58M166 330v-48M182 336v-60M198 330v-42M214 334v-56M230 330v-46M246 336v-52M262 330v-40M278 334v-58M294 330v-48M310 336v-54M326 330v-44M342 334v-60M358 330v-46M374 336v-52M390 330v-40M406 334v-58M422 330v-48M438 336v-54M454 330v-44M470 334v-60M486 330v-46M502 336v-52M518 330v-40M534 334v-58M550 330v-48M566 336v-54M582 330v-44M598 334v-60M614 330v-46M630 336v-52"/>
</g>
<g fill="#1f4e79">
<circle cx="90" cy="266" r="5"/><circle cx="190" cy="270" r="5"/><circle cx="290" cy="264" r="5"/><circle cx="390" cy="272" r="5"/><circle cx="490" cy="266" r="5"/><circle cx="590" cy="270" r="5"/>
</g>
<path d="M56 284 H664" stroke="#f4f1e9" stroke-width="2" stroke-dasharray="6 8" opacity=".8"/>
<text x="56" y="400" fill="#f4f1e9" font-family="ui-monospace,monospace" font-size="14" letter-spacing="2">36 TRANSECTS · MONTHLY · 9 MONTHS</text>
</svg>"""



def svg_incident() -> str:
    return """<svg class="art-svg" viewBox="0 0 720 280" role="img" aria-label="Checkout failures stay near the baseline, then spike at 09:18 when the gateway throttles, and recover by 09:59.">
<rect width="720" height="280" fill="#fffdfa"/>
<g stroke="#ddd6ca" stroke-width="1">
<path d="M56 36V214H684"/><path d="M56 88H684M56 150H684" opacity=".8"/>
</g>
<path d="M56 196H300L364 52L428 190H684" fill="none" stroke="#b3261e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="364" cy="52" r="6" fill="#b3261e"/>
<text x="380" y="44" fill="#b3261e" font-family="ui-monospace,monospace" font-size="13">GATEWAY THROTTLE</text>
<g fill="#5f5a52" font-family="ui-monospace,monospace" font-size="12">
<text x="56" y="246">09:12</text><text x="332" y="246">09:18</text><text x="640" y="246">09:59</text>
</g>
</svg>"""


def svg_architecture() -> str:
    return """<svg class="art-svg" viewBox="0 0 760 320" aria-hidden="true">
<rect width="760" height="320" fill="#0b1220"/>
<g font-family="ui-monospace,monospace" font-size="12" fill="#e8eef7">
<rect x="36" y="120" width="112" height="64" rx="8" fill="#111b2e" stroke="#60a5fa"/>
<text x="56" y="157">Ingest</text>
<rect x="206" y="70" width="112" height="64" rx="8" fill="#111b2e" stroke="#60a5fa"/>
<text x="224" y="107">Kafka</text>
<rect x="206" y="180" width="112" height="64" rx="8" fill="#111b2e" stroke="#60a5fa"/>
<text x="228" y="217">Backfill</text>
<rect x="386" y="120" width="112" height="64" rx="8" fill="#111b2e" stroke="#60a5fa"/>
<text x="412" y="157">Flink</text>
<rect x="566" y="70" width="150" height="64" rx="8" fill="#111b2e" stroke="#60a5fa"/>
<text x="586" y="107">Warehouse</text>
<rect x="566" y="180" width="150" height="64" rx="8" fill="#111b2e" stroke="#60a5fa"/>
<text x="600" y="217">Product API</text>
</g>
<g stroke="#60a5fa" stroke-width="2" fill="none">
<path d="M148 152H206"/><path d="M262 134V180"/><path d="M318 152H386"/><path d="M498 140L566 102"/><path d="M498 164L566 202"/>
</g>
<g fill="#60a5fa"><path d="M206 152l-9-5v10z"/><path d="M386 152l-9-5v10z"/><path d="M566 102l-10-1 5 9z"/><path d="M566 202l-10 1 5-9z"/></g>
<text x="36" y="56" fill="#60a5fa" font-family="ui-monospace,monospace" font-size="14" letter-spacing="3">PHASE 1 · STREAMING PATH</text>
</svg>"""




def svg_dashboard() -> str:
    return """<svg class="art-svg" viewBox="0 0 760 340" aria-hidden="true">
<rect width="760" height="340" fill="#ffffff"/>
<g>
<rect x="36" y="36" width="200" height="86" rx="8" fill="#f5f7f8" stroke="#dce3e8"/>
<text x="54" y="64" fill="#5d6b78" font-family="ui-monospace,monospace" font-size="11">ARR</text>
<text x="54" y="96" fill="#0b5d4f" font-family="ui-monospace,monospace" font-size="28">$48.2M</text>
<rect x="252" y="36" width="200" height="86" rx="8" fill="#f5f7f8" stroke="#dce3e8"/>
<text x="270" y="64" fill="#5d6b78" font-family="ui-monospace,monospace" font-size="11">NRR</text>
<text x="270" y="96" fill="#b45309" font-family="ui-monospace,monospace" font-size="28">112%</text>
<rect x="468" y="36" width="256" height="86" rx="8" fill="#f5f7f8" stroke="#dce3e8"/>
<text x="486" y="64" fill="#5d6b78" font-family="ui-monospace,monospace" font-size="11">SMB CHURN</text>
<text x="486" y="96" fill="#b3261e" font-family="ui-monospace,monospace" font-size="28">4.8%</text>
</g>
<g stroke="#dce3e8" stroke-width="1"><path d="M36 160H724M36 220H724M36 280H724"/></g>
<g fill="#0b5d4f">
<rect x="70" y="214" width="38" height="66"/><rect x="130" y="190" width="38" height="90"/><rect x="190" y="170" width="38" height="110"/><rect x="250" y="150" width="38" height="130"/>
</g>
<g fill="#b45309" opacity=".8"><rect x="340" y="200" width="38" height="80"/><rect x="400" y="230" width="38" height="50"/></g>
<path class="chart-line" d="M500 240 L560 220 L620 226 L680 190 L724 178" fill="none" stroke="#0b5d4f" stroke-width="3"/>
<text x="36" y="322" fill="#5d6b78" font-family="ui-monospace,monospace" font-size="12">ARR · NRR · SMB CHURN · COHORT TREND</text>
</svg>"""



GLOBAL_VISUAL_CSS = """
.cover-art{position:absolute;inset:0;z-index:0;overflow:hidden;border-radius:inherit}
.cover-art svg,.cover-art img{display:block;width:100%;height:100%;object-fit:cover}
.figure img{display:block;width:100%;height:auto}
.slide.has-cover{padding:0;overflow:hidden;justify-content:flex-end}
.slide.has-cover > *:not(.cover-art){position:relative;z-index:1}
.slide.has-cover .kicker,.slide.has-cover h1,.slide.has-cover h2,.slide.has-cover .lede,.slide.has-cover .meta{padding-left:clamp(24px,4vw,64px);padding-right:clamp(24px,4vw,64px)}
.slide.has-cover .meta{padding-bottom:clamp(24px,4vw,56px)}
.slide.has-cover::after{content:"";position:absolute;left:0;right:0;bottom:0;height:64%;z-index:0;pointer-events:none;background:linear-gradient(to top,var(--card) 10%,transparent)}
.slide.has-cover > *:not(.cover-art){z-index:1}
.figure{margin-top:16px;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--bg)}
.figure svg{display:block;width:100%;height:auto}
.figure-row{display:grid;grid-template-columns:1.05fr .95fr;gap:24px;align-items:center}
.figure-row .figure{margin-top:0}
@keyframes rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes grow{from{transform:scaleY(.15)}to{transform:scaleY(1)}}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.slide.active > *:not(.cover-art){animation:rise .45s ease both}
.slide.active > *:nth-child(3){animation-delay:.05s}
.slide.active .bars i{animation:grow .7s cubic-bezier(.2,.8,.2,1) both;transform-origin:bottom}
.slide.active .chart-line{stroke-dasharray:600;stroke-dashoffset:600;animation:draw 1.2s ease both}
.slide.active .phone-art{animation:float 5s ease-in-out infinite}
.slide.active .timeline > div{animation:rise .5s ease both}
.slide.active .timeline > div:nth-child(2){animation-delay:.06s}
.slide.active .timeline > div:nth-child(3){animation-delay:.12s}
.slide.active .timeline > div:nth-child(4){animation-delay:.18s}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}
"""

DECK_EXTRA = {
    "academic-defense": """
      body[data-deck="academic-defense"] .slide{border-radius:2px;border-left:5px solid var(--accent)}
      body[data-deck="academic-defense"] .figure{background:#fffdf8;border-radius:2px;width:fit-content;max-width:100%;margin:16px auto 0}
      body[data-deck="academic-defense"] .figure svg{height:400px;width:auto}
    """,
    "series-a-pitch": """
      body[data-deck="series-a-pitch"] .stage{padding:0;background:radial-gradient(circle at 78% 12%,rgba(94,234,212,.12),transparent 42%)}
      body[data-deck="series-a-pitch"] .slide{width:100%;height:100%;max-height:none;aspect-ratio:auto;border:0;border-radius:0;background:transparent;padding:clamp(28px,5vw,72px)}
      body[data-deck="series-a-pitch"] .card,body[data-deck="series-a-pitch"] .stat{background:rgba(255,255,255,.04);border-radius:0}
      body[data-deck="series-a-pitch"] .stat b{font-size:clamp(40px,4.8vw,76px)}
      body[data-deck="series-a-pitch"] .figure{border-color:#24303b;background:#0b0f14;border-radius:0}
    """,
    "incident-postmortem": """
      body[data-deck="incident-postmortem"] .slide{border-radius:0;border-top:4px solid var(--accent)}
      body[data-deck="incident-postmortem"] .kicker,
      body[data-deck="incident-postmortem"] .stat b,
      body[data-deck="incident-postmortem"] .timeline b,
      body[data-deck="incident-postmortem"] .table{font-family:var(--font-mono)}
      body[data-deck="incident-postmortem"] .card,
      body[data-deck="incident-postmortem"] .stat,
      body[data-deck="incident-postmortem"] .figure{border-radius:0;background:#fffdfa}
    """,
    "architecture-review": """
      body[data-deck="architecture-review"] .stage{padding:0}
      body[data-deck="architecture-review"] .slide{width:100%;height:100%;max-height:none;aspect-ratio:auto;border:0;border-radius:0;background-image:linear-gradient(rgba(96,165,250,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(96,165,250,.07) 1px,transparent 1px);background-size:32px 32px}
      body[data-deck="architecture-review"] .kicker,
      body[data-deck="architecture-review"] .table{font-family:var(--font-mono)}
      body[data-deck="architecture-review"] .card,
      body[data-deck="architecture-review"] .stat,
      body[data-deck="architecture-review"] .figure{border-radius:2px;border-color:#22314a;background:#0b1220}
      body[data-deck="architecture-review"] .figure{width:fit-content;max-width:100%;margin:16px auto 0}
      body[data-deck="architecture-review"] .figure svg{height:360px;width:auto}
    """,
    "keynote": """
      body[data-deck="keynote"] .stage{padding:0;background:#12100d}
      body[data-deck="keynote"] .slide{width:100%;height:100%;max-height:none;aspect-ratio:auto;border:0;border-radius:0;background:#12100d}
      body[data-deck="keynote"] .slide.has-cover h1{font-size:clamp(48px,7vw,96px)}
      body[data-deck="keynote"] .slide.has-cover .lede{color:#e8dcc8}
      body[data-deck="keynote"] .slide.has-cover::after{height:72%;background:linear-gradient(to top,#12100d 18%,rgba(18,16,13,.72) 46%,transparent)}
    """,
    "workshop": """
      body[data-deck="workshop"] .slide{background:#fffdf7;border-radius:18px}
      body[data-deck="workshop"] .exercise{border-left-width:8px;border-radius:4px 14px 14px 4px}
      body[data-deck="workshop"] .exercise .time{font-size:clamp(14px,1.4vw,20px);letter-spacing:.06em}
      body[data-deck="workshop"] .card{border-radius:4px 14px 14px 4px}
      body[data-deck="workshop"] .figure{background:#fffdf7;border-radius:4px}
    """,
    "business-review": """
      body[data-deck="business-review"] .slide{background:#fff;border-radius:4px}
      body[data-deck="business-review"] .card,
      body[data-deck="business-review"] .stat,
      body[data-deck="business-review"] .figure{border-radius:4px;background:#fff}
      body[data-deck="business-review"] .table td:last-child{font-family:var(--font-mono);font-weight:700}
    """,
    "product-launch": """
      body[data-deck="product-launch"] .stage{background:linear-gradient(160deg,#fff7f2,#ffe4d6 55%,#e7f0fb)}
      body[data-deck="product-launch"] .slide{background:#fff;border-radius:28px;box-shadow:0 18px 40px rgba(196,37,92,.08)}
      body[data-deck="product-launch"] .slide.has-cover{padding:var(--pad);justify-content:center}
      body[data-deck="product-launch"] .slide.has-cover .kicker,
      body[data-deck="product-launch"] .slide.has-cover h1,
      body[data-deck="product-launch"] .slide.has-cover .lede,
      body[data-deck="product-launch"] .slide.has-cover .meta{padding-left:0;padding-right:0}
      body[data-deck="product-launch"] .slide.has-cover .lede,
      body[data-deck="product-launch"] .slide.has-cover .meta{max-width:34ch}
    """,
}

VISUALS = {
    ("academic-defense", 0): ("cover", photo("marsh.jpg", "Reed marsh at dusk, the study site")),
    ("academic-defense", 3): ("figure", svg_marsh()),
    ("series-a-pitch", 0): ("cover", photo("coast.jpg", "Aerial view of a coastal city")),
    ("incident-postmortem", 0): ("cover", photo("server.jpg", "Night operations desk with monitoring screens")),
    ("incident-postmortem", 1): ("figure", svg_incident()),
    ("architecture-review", 0): ("cover", photo("server2.jpg", "Engineers reviewing a system diagram on a whiteboard")),
    ("architecture-review", 1): ("figure", svg_architecture()),
    ("keynote", 0): ("cover", photo("keynote-stage.jpg", "Warm amber stage lights on a dark stage")),
    ("keynote", 1): ("cover", photo("hospital-night.jpg", "Dark hospital corridor at night")),
    ("keynote", 2): ("cover", photo("keynote-idea.jpg", "Warm stage lights in haze")),
    ("keynote", 7): ("cover", photo("keynote-stage.jpg", "Warm amber stage lights on a dark stage")),
    ("workshop", 0): ("cover", photo("sticky.jpg", "Team collaborating with sticky notes")),
    ("business-review", 0): ("cover", photo("meeting.jpg", "Business team reviewing charts at a conference table")),
    ("business-review", 2): ("figure", svg_dashboard()),
    ("product-launch", 0): ("cover", photo("engineer.jpg", "Field technician reviewing a job on a tablet outdoors")),
}
