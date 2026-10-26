// "When is my country next?" — UPR and Human Rights Committee (HRCttee) timeline.
import { loadJSON, esc } from "./app.js";

const $ = (s) => document.querySelector(s);
const MONTHS = ["January", "February", "March", "April", "May", "June", "July",
  "August", "September", "October", "November", "December"];
const SHORT = MONTHS.map((m) => m.slice(0, 3));
const START = 2016, END = 2036;

const today = new Date();
const T = today.getFullYear() + today.getMonth() / 12 + (today.getDate() - 1) / 365;

// "2026-05" | "2026-05-19" | "2025" -> {t, y, m, d, exact, text}
function parse(s) {
  const p = String(s).split("-").map(Number);
  const [y, m, d] = p;
  const t = y + ((m || 7) - 1) / 12 + ((d || 15) - 1) / 365;
  const text = d ? `${d} ${MONTHS[m - 1]} ${y}` : m ? `${MONTHS[m - 1]} ${y}` : `${y}`;
  return { t, y, m, d, text, past: t < T };
}

function expected(p, tentative, dialogue) {
  // a derived date that has passed
  if (p.past && tentative) return dialogue ? `Expected ${p.text}, not yet scheduled` : `Expected ${p.text}`;
  return p.text + (tentative ? ", tentative" : "");
}

function nextFmt(p, tentative, dialogue) {
  // {strong, rest} for the bold "Next ..." line
  if (p.past && tentative) return { strong: `Expected ${p.text}`, rest: dialogue ? ", not yet scheduled" : "" };
  return { strong: p.text, rest: tentative ? ", tentative" : "" };
}

// ---------------------------------------------------------------- events
function uprEvents(u) {
  const ev = [], rows = [];
  const c4 = u.cycle4, c5 = u.cycle5;
  if (c4.status === "date_not_set") return { ev, lead: [{ label: "Last review", strong: "Before November 2022 (third cycle)", rest: "" }, { label: "Next review", strong: "Date not set", rest: "" }], rows, note: "Date not set" };
  const e4 = parse(c4.exam);
  const next4 = c4.status === "upcoming";
  ev.push({ t: e4.t, kind: "review", tent: false, label: e4.text, tip: `UPR review (4th cycle, session ${c4.session}): ${e4.text}` });
  const a4 = parse(c4.adoption);
  ev.push({ t: a4.t, kind: "adoption", tent: next4, tip: `Outcome adopted by the Human Rights Council: ${a4.text}` });
  let last = null, next = null;
  if (!next4) {
    last = { label: "Last review", strong: e4.text, rest: `; outcome adopted ${a4.text}` };
  } else {
    last = { label: "Last review", strong: "Before November 2022 (third cycle)", rest: "" };
  }
  const deadlines = (x, tent) => {
    const sh = parse(x.stakeholders_deadline), nr = parse(x.national_report_deadline);
    ev.push({ t: sh.t, kind: "deadline", tent, tip: `Stakeholders' submissions deadline: ${sh.text}${tent ? " (predicted)" : ""}` });
    ev.push({ t: nr.t, kind: "deadline", tent, tip: `State's national report deadline: ${nr.text}${tent ? " (predicted)" : ""}` });
    rows.push(`Stakeholders' submissions deadline: ${sh.text}${tent ? " (predicted)" : ""}`);
    rows.push(`State's national report deadline: ${nr.text}${tent ? " (predicted)" : ""}`);
  };
  if (next4) {
    next = { label: "Next review", strong: e4.text, rest: ` (4th cycle); outcome adopted ${a4.text} (expected)` };
    deadlines(c4, false);
  }
  if (c5.status === "predicted") {
    const e5 = parse(c5.exam), a5 = parse(c5.adoption);
    ev.push({ t: e5.t, kind: "review", tent: true, label: e5.text, tip: `UPR review (5th cycle, predicted): ${e5.text}` });
    ev.push({ t: a5.t, kind: "adoption", tent: true, tip: `Outcome adopted (predicted): ${a5.text}` });
    if (!next4) {
      next = { label: "Next review", strong: e5.text, rest: `, predicted (5th cycle); outcome adopted ${a5.text} (predicted)` };
      deadlines(c5, true);
    } else {
      rows.push(`Following review: ${e5.text}, predicted (5th cycle)`);
    }
  } else if (c5.status === "date_not_set") {
    next = { label: "Next review", strong: "Date not set", rest: "" };
  }
  return { ev, lead: [last, next].filter(Boolean), rows };
}

function hrcEvents(h, countryName) {
  const ev = [], rows = [];
  let last = null, next = null, note = null;
  if (!h.reviews.length) {
    last = { label: "Last dialogue", strong: "No dialogue over the last 10 years", rest: "" };
  }
  h.reviews.forEach((r, i) => {
    const d = parse(r.dialogue[0].slice(0, 10));
    ev.push({ t: d.t, kind: "review", tent: false, label: `${SHORT[d.m - 1]} ${d.y}`, tip: `HRCttee dialogue: ${MONTHS[d.m - 1]} ${d.y}${r.no_state_report ? " (without a State report)" : ""}` });
    if (i === h.reviews.length - 1) {
      last = { label: "Last dialogue", strong: `${MONTHS[d.m - 1]} ${d.y}`, rest: r.no_state_report ? " (without a State report)" : "" };
      if (r.follow_up_due) {
        const f = parse(r.follow_up_due);
        ev.push({ t: f.t, kind: "followup", tent: !!r.follow_up_tentative, tip: `Follow-up information due: ${f.text}${r.follow_up_tentative ? " (tentative)" : ""}` });
        rows.push(`Follow-up information due: ${f.text}${r.follow_up_tentative ? " (tentative)" : ""}`);
      }
    }
  });
  const n = h.next;
  if (n) {
    const dlg = parse(n.dialogue), lo = parse(n.loipr_adoption);
    const ngoL = parse(n.ngo_loipr_deadline), ngoD = parse(n.ngo_dialogue_deadline);
    const stated = n.basis === "stated_report_due+1y" ? n.state_report_due : null;
    const sr = parse(n.state_report_due);
    const loAdopted = n.loipr_source === "adopted";
    const showNgoL = !(loAdopted && lo.past);
    if (showNgoL) ev.push({ t: ngoL.t, kind: "ngo", tent: true, tip: `NGO deadline for the LOIPR: ${expected(ngoL, true)}` });
    ev.push({ t: lo.t, kind: "loipr", tent: !loAdopted, tip: `LOIPR: ${loAdopted ? "adopted " + lo.text : expected(lo, true)}` });
    ev.push({ t: sr.t, kind: "report", tent: !stated, tip: `State report due: ${stated ? sr.text : expected(sr, n.state_report_source === "calculated" || n.state_report_source === "stated_year")}` });
    ev.push({ t: ngoD.t, kind: "ngo", tent: true, tip: `NGO deadline for the dialogue: ${expected(ngoD, true)}` });
    const onList = !!n.on_future_list;  // on the Committee's undated "Future Sessions" list
    const noDate = (x) => (onList ? x.replace(", not yet scheduled", ", no date set") : x);
    ev.push({ t: dlg.t, kind: "review", tent: true, label: `${SHORT[dlg.m - 1]} ${dlg.y}`, tip: `HRCttee dialogue: ${noDate(expected(dlg, true, true))}` });
    next = { label: "Next dialogue", ...nextFmt(dlg, true, true) };
    if (onList && next.rest) next.rest = noDate(next.rest);
    if (showNgoL) rows.push(`NGO deadline for the LOIPR: ${expected(ngoL, true)}`);
    rows.push(`LOIPR: ${loAdopted ? "adopted " + lo.text : expected(lo, true)}`);
    rows.push(`State report due: ${stated ? sr.text : expected(sr, n.state_report_source === "calculated" || n.state_report_source === "stated_year")}`);
    rows.push(`NGO deadline for the dialogue: ${expected(ngoD, true)}`);
    // the calculated dialogue date has passed without a dialogue
    const my = (p) => `${MONTHS[p.m - 1]} ${p.y}`;
    if (onList) {
      note = `The Committee has placed ${countryName} on its list for a future session, but no date has been set.`;
    } else if (dlg.past && n.basis === "stated_report_due+1y") {
      note = `The Committee set the State report's due date at ${my(sr)}, and we calculated the dialogue as one year later. But the dialogue did not take place and has not been scheduled.`;
    } else if (dlg.past && n.basis === "loipr_adopted+2y" && loAdopted) {
      note = `The Committee adopted its list of issues in ${my(lo)}, and we calculated the dialogue as two years later. But the dialogue did not take place and has not been scheduled.`;
    }
  }
  return { ev, lead: [last, next].filter(Boolean), rows, note };
}

// ------------------------------------------------------------------ chart
const SYM = {
  review: (x, y, c, tent) => `<circle cx="${x}" cy="${y}" r="7" ${fill(c, tent)}/>`,
  adoption: (x, y, c, tent) => `<circle cx="${x}" cy="${y}" r="3.2" ${fill(c, tent)}/>`,
  loipr: (x, y, c, tent) => `<path d="M${x},${y - 7} L${x + 7},${y + 6} L${x - 7},${y + 6} Z" ${fill(c, tent)}/>`,
  deadline: (x, y, c, tent) => `<rect x="${x - 5}" y="${y - 5}" width="10" height="10" ${fill(c, tent)}/>`,
  report: (x, y, c, tent) => `<rect x="${x - 5}" y="${y - 5}" width="10" height="10" ${fill(c, tent)}/>`,
  ngo: (x, y, c, tent) => `<rect x="${x - 3.5}" y="${y - 3.5}" width="7" height="7" ${fill("#7b8794", true)}/>`,
  followup: (x, y, c, tent) => `<path d="M${x},${y - 7} L${x + 6},${y} L${x},${y + 7} L${x - 6},${y} Z" ${fill(c, tent)}/>`,
};
function fill(c, tent) {
  return tent ? `fill="var(--bg)" stroke="${c}" stroke-width="2"` : `fill="${c}" stroke="${c}" stroke-width="1"`;
}

function chart(rowsDef) {
  const W = 900, L = 92, R = 24, rowH = 84, top = 24;
  const H = top + rowsDef.length * rowH + 30;
  const x = (t) => L + ((Math.min(Math.max(t, START), END + 1) - START) / (END + 1 - START)) * (W - L - R);
  let svg = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Timeline of review and dialogue dates" xmlns="http://www.w3.org/2000/svg">`;
  // future shading + year grid
  svg += `<rect x="${x(T)}" y="${top - 10}" width="${W - R - x(T)}" height="${H - top - 14}" fill="var(--panel)"/>`;
  for (let y = START; y <= END + 1; y++) {
    const xx = x(y);
    svg += `<line x1="${xx}" y1="${top - 10}" x2="${xx}" y2="${H - 24}" stroke="var(--line)" stroke-width="${y % 2 ? 0.5 : 1}"/>`;
    if (y <= END && y % 2 === 0) svg += `<text x="${xx + (W - L - R) / (END + 1 - START) / 2}" y="${H - 8}" text-anchor="middle" font-size="11" fill="var(--muted)">${y}</text>`;
  }
  svg += `<line x1="${x(T)}" y1="${top - 10}" x2="${x(T)}" y2="${H - 24}" stroke="#d73027" stroke-width="1.5" stroke-dasharray="4 3"/>`;
  svg += `<text x="${x(T) + 4}" y="${top - 12}" font-size="10" fill="#d73027">today</text>`;
  rowsDef.forEach((r, i) => {
    const cy = top + i * rowH + rowH / 2 - 6;
    svg += `<line x1="${L}" y1="${cy}" x2="${W - R}" y2="${cy}" stroke="${r.color}" stroke-opacity=".35" stroke-width="2"/>`;
    svg += `<text x="6" y="${cy + 4}" font-size="13" font-weight="600" fill="var(--ink)">${esc(r.name)}</text>`;
    if (r.note) {
      svg += `<text x="${(L + W - R) / 2}" y="${cy - 14}" text-anchor="middle" font-size="12" fill="var(--muted)">${esc(r.note)}</text>`;
    }
    // labels: stagger when close
    const labelled = r.ev.filter((e) => e.label && e.t >= START && e.t <= END + 1).sort((a, b) => a.t - b.t);
    let prevX = -99, up = true;
    r.ev.filter((e) => e.t >= START && e.t <= END + 1).sort((a, b) => a.t - b.t).forEach((e) => {
      svg += `<g>${SYM[e.kind](x(e.t), cy, r.color, e.tent)}<title>${esc(e.tip)}</title></g>`;
    });
    labelled.forEach((e) => {
      const xx = x(e.t);
      if (xx - prevX < 62) up = !up; else up = true;
      prevX = xx;
      svg += `<text x="${xx}" y="${up ? cy - 14 : cy + 24}" text-anchor="middle" font-size="11" font-weight="600" fill="var(--ink)">${esc(e.label)}${e.tent ? "*" : ""}</text>`;
    });
    // arrows for events outside the axis
    const after = r.ev.filter((e) => e.t > END + 1).length;
    if (after) svg += `<text x="${W - R - 2}" y="${cy + 24}" text-anchor="end" font-size="11" fill="var(--muted)">later dates beyond ${END} ▸</text>`;
  });
  svg += `</svg>`;
  return svg;
}

const LEGEND = `<div class="next-legend">
  <span><svg width="16" height="16"><circle cx="8" cy="8" r="6" fill="#444"/></svg> UPR review / HRCttee dialogue</span>
  <span><svg width="16" height="16"><circle cx="8" cy="8" r="6" fill="var(--bg)" stroke="#444" stroke-width="2"/></svg> tentative or predicted</span>
  <span><svg width="16" height="16"><circle cx="8" cy="8" r="3" fill="#444"/></svg> outcome adopted (UPR)</span>
  <span><svg width="16" height="16"><path d="M8,2 L14,14 L2,14 Z" fill="#444"/></svg> LOIPR</span>
  <span><svg width="16" height="16"><rect x="3" y="3" width="10" height="10" fill="#444"/></svg> deadline: State report / stakeholders</span>
  <span><svg width="16" height="16"><rect x="4" y="4" width="7" height="7" fill="var(--bg)" stroke="#7b8794" stroke-width="2"/></svg> NGO deadline</span>
  <span><svg width="16" height="16"><path d="M8,1 L14,8 L8,15 L2,8 Z" fill="#444"/></svg> follow-up due</span>
  <span>* tentative or predicted date</span>
</div>`;

// ------------------------------------------------------------------ render
function render(c, generated) {
  const out = $("#next-result");
  if (!c) { out.innerHTML = ""; return; }
  if (!c.upr && !c.hrc) {
    out.innerHTML = `<p class="note">${esc(c.name)}: neither mechanism applies — it is not reviewed under the UPR and is not party to the Covenant.</p>`;
    return;
  }
  const rows = [];
  let upr = null, hrc = null;
  if (c.upr) {
    upr = uprEvents(c.upr);
    rows.push({ name: "UPR", color: "#1f5c8b", ev: upr.ev, note: upr.note });
  }
  if (c.hrc) {
    hrc = hrcEvents(c.hrc, c.name);
    hrc.hnote = hrc.note;
    rows.push({ name: "HRCttee", color: "#b5651d", ev: hrc.ev, note: c.hrc.reviews.length ? null : "No dialogue over the last 10 years" });
  }
  let html = `<h3>${esc(c.name)}</h3><div class="next-chart">${chart(rows)}</div>${LEGEND}`;
  const col = (title, o) => o
    ? `<div><h4>${title}</h4>${o.lead.map((l) => `<p class="next-lead">${esc(l.label)}: <strong>${esc(l.strong)}</strong>${esc(l.rest)}</p>`).join("")}` +
      (o.rows.length ? `<ul class="next-dates">${o.rows.map((r) => `<li>${esc(r)}</li>`).join("")}</ul>` : "") +
      (o.hnote ? `<p class="note">${esc(o.hnote)}</p>` : "") + `</div>`
    : "";
  html += `<div class="next-details">${col("UPR", upr)}${col("HRCttee", hrc)}</div>`;
  if (!c.hrc) html += `<p class="note">${esc(c.name)} is not party to the International Covenant on Civil and Political Rights, so it has no HRCttee row.</p>`;
  if (!c.upr) html += `<p class="note">${esc(c.name)} is not reviewed under the UPR.</p>`;
  out.innerHTML = html;
}

(async function () {
  const sec = $("#next-section");
  if (!sec) return;
  const data = await loadJSON("data/calendar.json");
  const list = data.countries.slice().sort((a, b) => a.name.localeCompare(b.name));
  const sel = $("#next-country");
  sel.insertAdjacentHTML("beforeend", list.map((c) => `<option value="${esc(c.a3)}">${esc(c.name)}</option>`).join(""));
  const g = new Date(data.generated + "T00:00:00");
  $("#next-note").textContent =
    `Data as of ${g.getDate()} ${MONTHS[g.getMonth()]} ${g.getFullYear()}. UPR dates from the OHCHR calendar; ` +
    `HRCttee dates from the Committee's concluding observations and session lists.`;
  sel.addEventListener("change", () => render(list.find((c) => c.a3 === sel.value), data.generated));
})();
