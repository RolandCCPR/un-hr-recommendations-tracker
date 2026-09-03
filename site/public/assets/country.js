import { loadJSON, esc, mdInline, chip, distBar, scoreColor } from "./app.js";

const $ = (s) => document.querySelector(s);
const a3 = new URLSearchParams(location.search).get("c");

function miniChips(dist) {
  return ["A", "B", "C", "D", "E"]
    .filter((g) => dist[g])
    .map((g) => `<span class="chip ${g}">${g}</span>`)
    .join("");
}

function block(b) {
  const recs = b.recommendations
    .map(
      (r) =>
        `<li><strong>${esc(r.paragraph)}</strong> <span class="by">(${esc(r.by)}, ${esc(
          r.position.replace(/_/g, "-")
        )})</span><br>${esc(r.text)}</li>`
    )
    .join("");
  return `<div class="block">
    <div class="bhead">
      ${chip(b.grade)}
      <span class="paras">${esc(b.paras)}</span>
      <span class="sum">${esc(b.summary)}</span>
    </div>
    <div class="meaning">Grade ${b.grade} — ${esc(b.meaning)}</div>
    <div class="rationale">${esc(b.rationale)}</div>
    ${
      b.evidence.length
        ? `<ul class="evidence">${b.evidence.map((e) => `<li>${esc(e)}</li>`).join("")}</ul>`
        : ""
    }
    <div class="pos">${b.n} recommendation${b.n > 1 ? "s" : ""} · position: ${esc(b.position)}</div>
    <details class="recs"><summary>Show the ${b.n} individual recommendation${
    b.n > 1 ? "s" : ""
  }</summary><ol>${recs}</ol></details>
  </div>`;
}

function uprSection(upr) {
  const m = upr.meta;
  const themes = upr.themes
    .map((t) => {
      const dist = {};
      t.blocks.forEach((b) => (dist[b.grade] = (dist[b.grade] || 0) + b.n));
      return `<details class="theme">
        <summary>${esc(t.theme)}<span class="mini">${miniChips(dist)}</span></summary>
        <div class="body">${t.blocks.map(block).join("")}</div>
      </details>`;
    })
    .join("");
  return `
    <h2>Universal Periodic Review — ${esc(m.cycle)} recommendations</h2>
    <p class="note">Recommendations in <strong>${esc(m.co_symbol)}</strong>, assessed against the
      documentation for the ${esc(m.review)} review.</p>
    ${m.headline ? `<p class="lead">${mdInline(m.headline)}</p>` : ""}
    <p class="note"><strong>Sources.</strong> ${m.sources.map(mdInline).join(" · ")}</p>
    ${themes}`;
}

function hrcSection(hrc) {
  const m = hrc.meta;
  const paras = hrc.paragraphs
    .map(
      (p) => `<div class="hrc-para">
        <h3>Paragraph ${esc(p.para)} — ${esc(p.title)}</h3>
        <div class="rec"><em>Recommendation:</em> ${esc(p.recommendation)}</div>
        ${p.limbs
          .map(
            (l) => `<div class="hrc-limb">
              <div class="lh">${chip(l.grade)}<span class="name">${esc(l.limb)}</span>
                <span class="meaning">— ${esc(l.meaning)}</span></div>
              <p class="ev">${esc(l.eval)}</p>
            </div>`
          )
          .join("")}
      </div>`
    )
    .join("");
  return `
    <h2>Human Rights Committee — follow-up to ${esc(m.co_symbol)}</h2>
    <p class="note">Concluding observations adopted at the ${esc(m.session)}. Committee's
      evaluation: <strong>${esc(m.assessment_symbol)}</strong>, ${esc(m.assessment_date)}.</p>
    <p class="note">${esc(m.round)}</p>
    ${paras}`;
}

(async function () {
  if (!a3) {
    $("#content").innerHTML = "<p>No country selected. <a href='index.html'>Back to the map</a >.</p>";
    return;
  }
  let data, meta;
  try {
    [data, meta] = await Promise.all([loadJSON(`data/${a3}.json`), loadJSON("data/meta.json")]);
  } catch (e) {
    $("#content").innerHTML = `<p>No assessment is available for this country yet.
      <a href="index.html">Back to the map</a>.</p>`;
    return;
  }

  document.title = `${data.name} — Implementation Tracker`;
  $("#crumbs").innerHTML = `<a href="index.html">◂ Map</a>`;
  $("#country-name").textContent = data.name;
  $("#generated").textContent = meta.generated;

  const um = data.upr.meta, hm = data.hrc.meta;
  $("#summary").innerHTML = `
    <div class="box">
      <div class="lbl">Universal Periodic Review</div>
      <div class="big" style="color:${scoreColor(um.score)}">${um.score.toFixed(2)}<span style="font-size:1rem;color:var(--muted)"> / 5</span></div>
      <div>${um.n} recommendations · ${esc(um.cycle)}</div>
      ${distBar(um.grade_dist)}
    </div>
    <div class="box">
      <div class="lbl">Human Rights Committee</div>
      <div class="big" style="color:${scoreColor(hm.score)}">${hm.score.toFixed(2)}<span style="font-size:1rem;color:var(--muted)"> / 5</span></div>
      <div>${hm.n} graded limbs · ${esc(hm.co_symbol)}</div>
      ${distBar(hm.grade_dist)}
    </div>`;

  $("#content").innerHTML = uprSection(data.upr) + hrcSection(data.hrc);
})();
