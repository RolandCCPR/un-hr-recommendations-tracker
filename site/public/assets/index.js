import { loadJSON, esc, distBar, scoreColor } from "./app.js";
import { drawMap } from "./map.js";

const $ = (s) => document.querySelector(s);

(async function () {
  const [countries, meta] = await Promise.all([
    loadJSON("data/countries.json"),
    loadJSON("data/meta.json"),
  ]);

  $("#generated").textContent = meta.generated;

  const map = await drawMap({
    mountSel: "#map",
    tooltipSel: "#tt",
    countries,
    worldUrl: "assets/world-110m.json",
    numA3Url: "assets/iso-numeric-a3.json",
  });

  // mechanism toggle
  document.querySelectorAll(".seg button").forEach((b) => {
    b.addEventListener("click", () => {
      document.querySelectorAll(".seg button").forEach((x) => x.setAttribute("aria-pressed", "false"));
      b.setAttribute("aria-pressed", "true");
      map.paint(b.dataset.mech);
      $("#map-cap").textContent =
        b.dataset.mech === "upr"
          ? "Shading: UPR 3rd-cycle implementation score (average grade, 1–5)."
          : b.dataset.mech === "hrc"
          ? "Shading: Human Rights Committee follow-up score (average grade, 1–5)."
          : "Shading: combined score — the average of a country's UPR and Human Rights Committee scores (1–5).";
    });
  });

  // assessed-country table (sortable)
  const assessed = countries.filter((c) => c.assessed);
  $("#country-count").textContent = assessed.length;
  const cell = (v) =>
    v == null
      ? '<span class="num none">—</span>'
      : `<span class="num" style="color:${scoreColor(v)}">${v.toFixed(2)}</span>`;

  let sortKey = "combined", sortDir = -1;
  const val = (c, k) =>
    k === "name" ? c.name
    : k === "upr" ? (c.upr ? c.upr.score : -1)
    : k === "hrc" ? (c.hrc ? c.hrc.score : -1)
    : k === "year" ? (c.hrc ? c.hrc.year : -1)
    : (c.combined == null ? -1 : c.combined);

  function render() {
    assessed.sort((a, b) => {
      const x = val(a, sortKey), y = val(b, sortKey);
      if (x < y) return -sortDir;
      if (x > y) return sortDir;
      return a.name.localeCompare(b.name);
    });
    $("#country-table tbody").innerHTML = assessed
      .map(
        (c) => `<tr onclick="location.href='country.html?c=${c.a3}'">
          <td class="cty">${esc(c.name)}</td>
          <td>${cell(c.upr ? c.upr.score : null)}</td>
          <td>${cell(c.hrc ? c.hrc.score : null)}</td>
          <td>${cell(c.combined)}</td>
          <td class="yr">${c.hrc ? c.hrc.year : ""}</td>
        </tr>`
      )
      .join("");
    document.querySelectorAll("#country-table th[data-k]").forEach((th) => {
      th.setAttribute("aria-sort",
        th.dataset.k !== sortKey ? "none" : sortDir === 1 ? "ascending" : "descending");
    });
  }
  document.querySelectorAll("#country-table th[data-k]").forEach((th) => {
    th.addEventListener("click", () => {
      if (sortKey === th.dataset.k) sortDir = -sortDir;
      else { sortKey = th.dataset.k; sortDir = th.dataset.k === "name" ? 1 : -1; }
      render();
    });
  });
  render();

  // mechanisms explainer
  $("#mech-explain").innerHTML = Object.values(meta.mechanisms)
    .map((m) => `<h3>${esc(m.name)}</h3><p>${esc(m.what)}</p>`)
    .join("");

  // scale table
  $("#scale tbody").innerHTML = meta.scale
    .map(
      (r) => `<tr>
      <td><span class="chip ${r.grade}">${r.grade}</span></td>
      <td>${esc(r.label)}</td>
      <td>${esc(r.meaning)}</td>
      <td style="text-align:right">${r.score}</td>
    </tr>`
    )
    .join("");

  $("#methodology").textContent = meta.methodology;
})();
