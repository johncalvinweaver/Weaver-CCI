#!/usr/bin/env python3
import json, argparse, sys
VERSION = "0.1.0"

# Weights: adjust as policy evolves
W_HUMAN_CONCEPTION = 0.50
W_HUMAN_CURATION   = 0.25
W_AI_GENERATION    = 0.15
W_AI_STRUCTURE     = 0.06
W_AI_VOICE         = 0.04

def clamp01(x): return max(0.0, min(1.0, float(x)))

def compute(payload):
    s = payload["signals"]
    hc = clamp01(s["human_conception"])
    he = clamp01(s["human_curation"])
    ag = clamp01(s["ai_generation"])
    asg = clamp01(s["ai_structure"])
    ave = clamp01(s["ai_voice_emulation"])

    human_score = hc*W_HUMAN_CONCEPTION + he*W_HUMAN_CURATION
    ai_score    = ag*W_AI_GENERATION + asg*W_AI_STRUCTURE + ave*W_AI_VOICE

    # Normalize to percentages (sum to 100)
    total = human_score + ai_score
    if total == 0:
        human_pct, ai_pct = 50.0, 50.0
    else:
        human_pct = (human_score / total) * 100.0
        ai_pct    = (ai_score / total) * 100.0

    return {
        "work_id": payload["work_id"],
        "title": payload.get("title",""),
        "human_pct": round(human_pct, 1),
        "ai_pct": round(ai_pct, 1),
        "categories": {
            "human_conception": round(hc*100, 1),
            "human_curation": round(he*100, 1),
            "ai_generation": round(ag*100, 1),
            "ai_structure": round(asg*100, 1),
            "ai_voice_emulation": round(ave*100, 1)
        },
        "version": VERSION
    }

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="submission JSON")
    ap.add_argument("--out", help="write result JSON")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        payload = json.load(f)

    result = compute(payload)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        print()