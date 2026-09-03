// World choropleth. Depends on globals `d3` and `topojson` (classic scripts).
import { scoreColor, esc, GRADE_ORDER, GRADE_COLOR } from "./app.js";

const W = 960, H = 500;

export async function drawMap({ mountSel, tooltipSel, countries, worldUrl, numA3Url }) {
  const [world, numA3] = await Promise.all([
    fetch(worldUrl).then((r) => r.json()),
    fetch(numA3Url).then((r) => r.json()),
  ]);

  const byA3 = new Map(countries.map((c) => [c.a3, c]));
  const feats = topojson.feature(world, world.objects.countries).features;

  const projection = d3.geoNaturalEarth1().fitExtent([[2, 2], [W - 2, H - 2]], { type: "Sphere" });
  const path = d3.geoPath(projection);

  const svg = d3
    .select(mountSel)
    .html("")
    .append("svg")
    .attr("viewBox", `0 0 ${W} ${H}`)
    .attr("role", "img")
    .attr("aria-label", "World map of assessed countries");

  svg.append("path").attr("class", "sphere").attr("d", path({ type: "Sphere" }));

  const tt = d3.select(tooltipSel);

  const g = svg.append("g");
  const paths = g
    .selectAll("path.country")
    .data(feats)
    .join("path")
    .attr("class", "country")
    .attr("d", path)
    .on("mousemove", (event, d) => {
      const rec = byA3.get(numA3[String(d.id)]);
      const name = rec ? rec.name : (d.properties && d.properties.name) || "";
      let html = `<strong>${esc(name)}</strong>`;
      if (rec && rec.assessed) {
        html += mechRows(rec);
      } else {
        html += `<div style="opacity:.75;margin-top:4px">Not yet assessed</div>`;
      }
      tt.html(html)
        .style("left", event.clientX + 14 + "px")
        .style("top", event.clientY + 14 + "px")
        .style("opacity", 1);
    })
    .on("mouseleave", () => tt.style("opacity", 0))
    .on("click", (event, d) => {
      const rec = byA3.get(numA3[String(d.id)]);
      if (rec && rec.assessed) location.href = `country.html?c=${rec.a3}`;
    });

  function mechRows(rec) {
    let s = "";
    for (const [k, label] of [["upr", "UPR"], ["hrc", "HR Committee"]]) {
      const m = rec[k];
      if (!m || m.score == null) continue;
      const bar = GRADE_ORDER.filter((gr) => m.grade_dist[gr])
        .map((gr) => `<span style="background:${GRADE_COLOR[gr]}">${gr} ${m.grade_dist[gr]}</span>`)
        .join("");
      s += `<div style="margin-top:6px"><b>${label}</b> — score ${m.score}/100<div class="tg">${bar}</div></div>`;
    }
    return s;
  }

  function paint(mechanism) {
    paths
      .classed("assessed", (d) => {
        const rec = byA3.get(numA3[String(d.id)]);
        return !!(rec && rec.assessed);
      })
      .attr("fill", (d) => {
        const rec = byA3.get(numA3[String(d.id)]);
        if (!rec || !rec.assessed) return "#e6e6e6";
        const m = rec[mechanism];
        return scoreColor(m ? m.score : null);
      });
  }

  paint("upr");
  return { paint };
}
