# Weaver CCI™ — Creative Composition Index

Weaver CCI™ is the first open framework for measuring and displaying how much of a creative work is human vs. AI.
Think of it as a nutrition label for authorship: clear, standardized, and portable.

With AI transforming publishing, art, research, journalism, and more, creators and audiences alike need trust, transparency, and proof. Weaver CCI™ provides exactly that, through a combination of:
- A transparent scoring model that blends metadata, signals, and detection.
- A universal schema for describing human and AI contributions.
- Label generators (SVG and Web Component) to display results anywhere.
- Optional links to immutable ledgers for long-term proof.

---

## Why Weaver CCI™ Matters

### 🔒 Protection
Authors, researchers, and creators can prove the nature of their contributions, preventing disputes and establishing credibility.

### 👁 Transparency
Readers, students, publishers, and clients can see at a glance how much is human vs. AI. No guessing, no hiding.

### 🌍 Standards
By open-sourcing the framework, we’re encouraging adoption across industries — publishing, academia, journalism, design — just as Creative Commons became the standard for licensing.

### 💡 Evolution
Weights, categories, and integrations can adapt as AI tools evolve. Weaver CCI™ is built to be updated, versioned, and governed by the community.

---

## Features

- **Schema (JSON):** Standardized format for describing contribution signals.
- **Scoring Engine (CLI in Python):** Computes weighted percentages of human vs. AI input.
- **Label Generator (SVG):** Produces square, portable visual labels for embedding in print, ebooks, or PDFs.
- **Web Component:** Drop a live `<weaver-cci-label>` into any webpage; lightweight and responsive.
- **API Spec (OpenAPI):** Minimal endpoints for integrating with your own systems.

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-org/weaver-cci.git
cd weaver-cci
```

### 2. Install Python dependencies

```bash
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
```

### 3. Run the Scorer

```bash
python cli/compute_cci.py examples/example_submission.json --out cci_result.json
```

### 4. Generate a Label

```bash
python labels/svg_label.py cci_result.json --out label.svg --size 512
```

### 5. Use the Web Component

```bash
cd labels/web-component
npm install
npx http-server .
```

Open `index.html` in your browser.

---

## Example Label

Here’s a 512×512 square label output:

- **Left:** Human contribution %
- **Right:** AI contribution %
- **Bars:** visual reinforcement
- **Footer:** work ID and version

---

## Example Submission

```json
{
  "work_id": "work-001",
  "title": "Example Work",
  "creator": { "name": "John Weaver", "contact": "john@example.com" },
  "timestamps": { "started_at": "2025-09-01T12:00:00Z", "finalized_at": "2025-09-15T17:30:00Z" },
  "signals": {
    "human_conception": 0.9,
    "human_curation": 0.7,
    "ai_generation": 0.3,
    "ai_structure": 0.2,
    "ai_voice_emulation": 0.1
  },
  "provenance": { "tools": ["editor:word", "model:gpt"], "commit_log_hash": "abc123" }
}
```

**Result:** 72% Human, 28% AI

---

## Roadmap

- ✅ JSON schema and scorer
- ✅ SVG + Web Component labels
- 🔄 API reference implementation (Node + Python backends)
- 🔄 Optional blockchain anchoring (Truth Ledger™ integration)
- 🔄 Publisher + journal plug-ins (WordPress, Overleaf, JATS XML)
- 🔄 Mobile SDKs

---

## Contributing

We welcome pull requests! Ideas for improvement include:
- Better weighting models
- New categories of contribution
- Localization of labels into other languages
- Improved visual designs

Fork the repo, make changes in a feature branch, and submit a PR.

---

## License

This repository is licensed under the Apache 2.0 License.

The “Weaver CCI™” name and logo are protected marks of the American AI Publishers Association (AAPA).

✨ With Weaver CCI™, we can make authorship transparent, fair, and future-proof.

---

> “Like a nutrition label for authorship.”

---

## What the CCI shows

- **Human (%)** — aggregated human contribution
- **AI (%)** — aggregated AI contribution
- Optional category breakdowns:
  - Human Conception
  - Human Curation/Editing
  - AI Generation
  - AI Structural Guidance
  - AI Voice Emulation

---

## Quick start

### 1) Install (Python tools)

```bash
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
# no extra deps required for CLI/SVG
```

### 2) Run the scorer (from examples)

```bash
python cli/compute_cci.py examples/example_submission.json --out cci_result.json
```

### 3) Generate a square SVG label

```bash
python labels/svg_label.py cci_result.json --out label.svg
```

### 4) Try the Web Component locally

```bash
cd labels/web-component
npm install
# simple dev server (optional): npx http-server .
# or just open index.html in a browser
```

---

## Inputs

Provide creation metadata as `examples/example_submission.json` shows. The scorer computes category scores and overall Human/AI percentages with a transparent weighted model.

## Outputs

- A normalized JSON result with final percentages
- A 1:1 square SVG label (defaults to 512×512; scalable) or a web component `<weaver-cci-label>` you can drop into any page.

---

## API

See `spec/openapi.yaml` for a minimal API to submit metadata and receive a CCI result + label.

---

## License

See LICENSE (Apache-2.0 suggested). “Weaver CCI” name and logo are trademarks — adjust to your needs.

---

## How to use (quick recap)

- Compute: `python cli/compute_cci.py examples/example_submission.json --out cci_result.json`
- Generate square SVG label: `python labels/svg_label.py cci_result.json --out label.svg --size 512`
- Embed on web: include `<weaver-cci-label human="72" ai="28" title="My Title" work="ABC-123"></weaver-cci-label>`
