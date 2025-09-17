class WeaverCCILabel extends HTMLElement {
  static get observedAttributes() { return ['human', 'ai', 'title', 'work']; }
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.size = parseInt(this.getAttribute('size') || '256', 10);
  }
  attributeChangedCallback() { this.render(); }
  connectedCallback() { this.render(); }

  render() {
    const human = Number(this.getAttribute('human') || 50);
    const ai = Number(this.getAttribute('ai') || 50);
    const title = this.getAttribute('title') || '';
    const work = this.getAttribute('work') || '';
    const size = this.size;
    const pad = 16;
    const card = size - 8;
    const barW = size - pad*2;
    const barHuman = barW * (human/100);
    const barAI = barW * (ai/100);
    const midX = pad + (size - pad*2) * 0.5;

    const svg = `
<svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Weaver CCI Label">
  <defs>
    <style><![CDATA[
      .card { fill:#fff; stroke:#e5e7eb; stroke-width:2; rx:20; }
      .title { font:700 16px system-ui; fill:#111827; }
      .subtitle { font:500 12px system-ui; fill:#6b7280; }
      .big { font:800 40px system-ui; fill:#111827; }
      .small { font:600 12px system-ui; fill:#374151; }
      .barbg { fill:#e5e7eb; }
      .human { fill:#10b981; }
      .ai { fill:#3b82f6; }
      .footer { font:500 10px system-ui; fill:#6b7280; }
    ]]></style>
  </defs>
  <rect class="card" x="4" y="4" width="${card}" height="${card}" rx="20"/>
  <text class="title" x="${pad}" y="${pad+20}">Weaver CCI™</text>
  <text class="subtitle" x="${pad}" y="${pad+38}">${title}</text>

  <text class="big" x="${pad}" y="${pad+100}">${Math.round(human)}%</text>
  <text class="small" x="${pad}" y="${pad+120}">Human</text>

  <text class="big" x="${midX}" y="${pad+100}">${Math.round(ai)}%</text>
  <text class="small" x="${midX}" y="${pad+120}">AI</text>

  <rect class="barbg" x="${pad}" y="${pad+140}" width="${barW}" height="12" rx="6"/>
  <rect class="human" x="${pad}" y="${pad+140}" width="${barHuman}" height="12" rx="6"/>

  <rect class="barbg" x="${pad}" y="${pad+160}" width="${barW}" height="12" rx="6"/>
  <rect class="ai" x="${pad}" y="${pad+160}" width="${barAI}" height="12" rx="6"/>

  <text class="footer" x="${pad}" y="${size-12}">Work: ${work} • v0.1.0</text>
</svg>`;
    this.shadowRoot.innerHTML = svg;
  }
}
customElements.define('weaver-cci-label', WeaverCCILabel);