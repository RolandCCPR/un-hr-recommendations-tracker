// Shared helpers for both pages.
export const GRADE_COLOR = { A: "#1a9850", B: "#91cf60", C: "#fee08b", D: "#cfd4da", E: "#d73027" };
export const GRADE_ORDER = ["A", "B", "C", "D", "E"];

// Continuous 0-100 -> red..yellow..green (piecewise, mirrors d3.interpolateRdYlGn roughly)
export function scoreColor(s) {
  if (s == null) return "#e6e6e6";
  const stops = [
    [0, [215, 48, 39]],
    [25, [244, 109, 67]],
    [50, [254, 224, 139]],
    [70, [166, 217, 106]],
    [100, [26, 152, 80]],
  ];
  s = Math.max(0, Math.min(100, s));
  for (let i = 1; i < stops.length; i++) {
    if (s <= stops[i][0]) {
      const [x0, c0] = stops[i - 1], [x1, c1] = stops[i];
      const t = (s - x0) / (x1 - x0);
      const c = c0.map((v, k) => Math.round(v + t * (c1[k] - v)));
      return `rgb(${c[0]},${c[1]},${c[2]})`;
    }
  }
  return "rgb(26,152,80)";
}

export function chip(grade) {
  return `<span class="chip ${grade}">${grade}</span>`;
}

export function distBar(dist) {
  const total = GRADE_ORDER.reduce((a, g) => a + (dist[g] || 0), 0) || 1;
  const bar = GRADE_ORDER
    .map((g) => {
      const n = dist[g] || 0;
      if (!n) return "";
      return `<i class="${g}" style="width:${(100 * n) / total}%" title="${g}: ${n}"></i>`;
    })
    .join("");
  const legend = GRADE_ORDER.filter((g) => dist[g])
    .map((g) => `<span><b style="background:${GRADE_COLOR[g]}"></b>${g}&nbsp;${dist[g]}</span>`)
    .join("");
  return `<div class="distbar">${bar}</div><div class="distlegend">${legend}</div>`;
}

export function esc(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

// Escape, then render **bold** and `code` inline markdown.
export function mdInline(s) {
  return esc(s)
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/`([^`]+)`/g, "<code>$1</code>");
}

export async function loadJSON(path) {
  const r = await fetch(path);
  if (!r.ok) throw new Error(`${path}: ${r.status}`);
  return r.json();
}
