#!/usr/bin/env python3
import json, argparse

TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Weaver CCI Label">
  <defs>
    <style><![CDATA[
      .card {{ fill:#fff; stroke:#e5e7eb; stroke-width:2; rx:24; }}
      .title {{ font: 700 28px/1.2 system-ui, -apple-system, Segoe UI, Roboto; fill:#111827; }}
      .subtitle {{ font: 500 16px/1.3 system-ui; fill:#6b7280; }}
      .big {{ font: 800 72px/1 system-ui; fill:#111827; }}
      .small {{ font: 600 16px/1 system-ui; fill:#374151; }}
      .barbg {{ fill:#e5e7eb; }}
      .human {{ fill:#10b981; }}
      .ai {{ fill:#3b82f6; }}
      .footer {{ font: 500 14px/1.2 system-ui; fill:#6b7280; }}
    ]]></style>
  </defs>

  <rect class="card" x="8" y="8" width="{card}" height="{card}" rx="24" />

  <text class="title" x="{pad}" y="{pad_plus_30}">Weaver CCI™</text>
  <text class="subtitle" x="{pad}" y="{pad_plus_58}">{title}</text>

  <!-- Big percentages -->
  <text class="big" x="{pad}" y="{pad_plus_160}">{human_pct}%</text>
  <text class="small" x="{pad}" y="{pad_plus_190}">Human</text>

  <text class="big" x="{mid_x}" y="{pad_plus_160}">{ai_pct}%</text>
  <text class="small" x="{mid_x}" y="{pad_plus_190}">AI</text>

  <!-- Bars -->
  <rect class="barbg" x="{pad}" y="{pad_plus_220}" width="{bar_w}" height="18" rx="9"/>
  <rect class="human" x="{pad}" y="{pad_plus_220}" width="{bar_w_human}" height="18" rx="9"/>

  <rect class="barbg" x="{pad}" y="{pad_plus_250}" width="{bar_w}" height="18" rx="9"/>
  <rect class="ai" x="{pad}" y="{pad_plus_250}" width="{bar_w_ai}" height="18" rx="9"/>

  <!-- Footer -->
  <text class="footer" x="{pad}" y="{size_minus_28}">Work: {work_id} • v{version}</text>
</svg>"""

def render(data, size=512, pad=32):
    human = float(data["human_pct"])
    ai = float(data["ai_pct"])
    # ensure sums visually fit
    card = size - 16
    mid_x = pad + (size - pad*2) * 0.5
    bar_w = size - pad*2
    bar_w_human = bar_w * (human/100.0)
    bar_w_ai = bar_w * (ai/100.0)

    return TEMPLATE.format(
        size=size, card=card, pad=pad,
        pad_plus_30=pad+30, pad_plus_58=pad+58,
        pad_plus_160=pad+160, pad_plus_190=pad+190,
        pad_plus_220=pad+220, pad_plus_250=pad+250,
        bar_w=bar_w, bar_w_human=bar_w_human, bar_w_ai=bar_w_ai,
        mid_x=mid_x, size_minus_28=size-28,
        title=data.get("title",""),
        human_pct=int(round(human)),
        ai_pct=int(round(ai)),
        work_id=data.get("work_id",""),
        version=data.get("version","0.1.0")
    )

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cci_json", help="CCI result JSON from compute_cci.py")
    ap.add_argument("--out", default="label.svg", help="Output SVG path")
    ap.add_argument("--size", type=int, default=512, help="Square size px (default 512)")
    args = ap.parse_args()
    with open(args.cci_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    svg = render(data, size=args.size)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {args.out}")