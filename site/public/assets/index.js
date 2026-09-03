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
          ? "Shading: UPR 3rd-cycle implementation score (0–100)."
          : "Shading: Human Rights Committee follow-up score (0–100).";
    });
  });

  // assessed-country cards
  const assessed = countries.filter((c) => c.assessed).sort((a, b) => a.name.localeCompare(b.name));
  $("#cards").innerHTML = assessed
    .map((c) => {
      const u = c.upr, h = c.hrc;
      return `<a class="card" href="country.html?c=${c.a3}">
        <h3>${esc(c.name)}</h3>
        <div class="scores">
          <div>UPR<b style="color:${scoreColor(u.score)}">${u.score}</b>${u.n} recs</div>
          <div>HR Cttee<b style="color:${scoreColor(h.score)}">${h.score}</b>${h.n} items</div>
        </div>
        ${distBar(u.grade_dist)}
      </a>`;
    })
    .join("");

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
