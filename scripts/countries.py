"""Registry of the countries assessed and shared helpers.

Each country's 3rd-cycle recommendations (from its OHCHR UPR38 Thematic List of
Recommendations) are graded against its 4th-cycle pre-sessional documents
(National report /1, OHCHR Compilation /2, Stakeholders' Summary /3, session 52,
May 2026).
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COUNTRIES: dict[str, dict] = {
    "united-states": dict(
        code="USA", name="United States of America", short="US",
        cycle3_session="36th", cycle3_symbol="A/HRC/46/15",
        cycle3_review="2020-11-09", cycle4_review="November 2025 (session 50)",
        thematic=ROOT / "UPR36_United_States_of_America_Thematic_List_of_Recommendations.docx",
        db=ROOT / "recommendations.db",
        evidence_dir=ROOT / "evidence",
        slug_prefix="US_cycle3",
        thematic_out="UPR36_US_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"2": "A/HRC/WG.6/50/USA/2", "3": "A/HRC/WG.6/50/USA/3"},
        sources=[
            "**UN Compilation** — A/HRC/WG.6/50/USA/2, OHCHR, 28 August 2025 "
            "(UN treaty bodies and special procedures)",
            "**Stakeholders' Summary** — A/HRC/WG.6/50/USA/3, OHCHR, "
            "1 September 2025 (155 civil-society and NHRI submissions)",
            "The US **National Report** (A/HRC/WG.6/50/USA/1) was not yet "
            "available at the time of assessment.",
        ],
        headline="No recommendation met the threshold for **A**. The result is "
        "dominated by inaction (**C**) and by 2025 measures running directly "
        "counter to the recommendation (**E**).",
    ),
    "denmark": dict(
        code="DNK", name="Denmark", short="Denmark",
        cycle3_session="38th", cycle3_symbol="A/HRC/48/10",
        cycle3_review="2021-05-06", cycle4_review="7 May 2026 (session 52)",
        thematic=ROOT / "countries/denmark/UPR38_Denmark_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/denmark/denmark.db",
        evidence_dir=ROOT / "countries/denmark/evidence",
        slug_prefix="denmark_cycle3",
        thematic_out="UPR38_Denmark_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/52/DNK/1", "2": "A/HRC/WG.6/52/DNK/2", "3": "A/HRC/WG.6/52/DNK/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/52/DNK/1, 20 February 2026",
            "**UN Compilation** — A/HRC/WG.6/52/DNK/2, OHCHR, 6 February 2026 "
            "(UN treaty bodies, UNHCR, UNESCO)",
            "**Stakeholders' Summary** — A/HRC/WG.6/52/DNK/3, OHCHR, "
            "28 January 2026 (16 submissions + the Danish Institute for Human Rights)",
        ],
        headline='Denmark reports concrete follow-up on many recommendations, so **partial implementation (B)** is the dominant outcome (ratification of the Enforced Disappearance Convention, a consent-based rape law, action plans on racism, trafficking and intimate-partner violence). Persistent gaps remain (no stand-alone torture offence, the retained "Parallel Society" laws) and asylum externalisation is a clear regression (**E**).',
    ),
    "namibia": dict(
        code="NAM", name="Namibia", short="Namibia",
        cycle3_session="38th", cycle3_symbol="A/HRC/48/4",
        cycle3_review="2021-05-05", cycle4_review="4 May 2026 (session 52)",
        thematic=ROOT / "countries/namibia/UPR38_Namibia_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/namibia/namibia.db",
        evidence_dir=ROOT / "countries/namibia/evidence",
        slug_prefix="namibia_cycle3",
        thematic_out="UPR38_Namibia_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/52/NAM/1", "2": "A/HRC/WG.6/52/NAM/2", "3": "A/HRC/WG.6/52/NAM/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/52/NAM/1",
            "**UN Compilation** — A/HRC/WG.6/52/NAM/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/52/NAM/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome: within the review period Namibia enacted or launched a concrete on-point measure across most themes (the Marriage Act 2024, the Access to Information Act 2022, ILO Conventions No. 190 and No. 156, a National Disability Council Act amendment, the Social Protection Policy 2021-2030, a revised National Housing Policy, GBV law reform, free tertiary education from 2026, a large fall in maternal mortality). **No relevant action (C)** remains for the long-stalled asks — a comprehensive anti-discrimination law, the Torture Bill, OP-CAT, decriminalisation of same-sex relations and SOGI protection, a standing invitation and recognition of Indigenous Peoples. (No cycle-3 recommendation captures the 2024 consolidated Marriage Act, which bars recognition of foreign same-sex marriages and reverses the 2023 Supreme Court judgment — a real-world regression that falls outside the graded set.)',
    ),
    "paraguay": dict(
        code="PRY", name="Paraguay", short="Paraguay",
        cycle3_session="38th", cycle3_symbol="A/HRC/48/9",
        cycle3_review="2021-05-04", cycle4_review="6 May 2026 (session 52)",
        thematic=ROOT / "countries/paraguay/UPR38_Paraguay_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/paraguay/paraguay.db",
        evidence_dir=ROOT / "countries/paraguay/evidence",
        slug_prefix="paraguay_cycle3",
        thematic_out="UPR38_Paraguay_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/52/PRY/1", "2": "A/HRC/WG.6/52/PRY/2", "3": "A/HRC/WG.6/52/PRY/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/52/PRY/1",
            "**UN Compilation** — A/HRC/WG.6/52/PRY/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/52/PRY/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome: Paraguay reports a concrete on-point measure in the review period across most themes (the SIMORE Plus follow-up system, monetary poverty down from ~26% to ~20%, a universal old-age pension, Inter-American Court land-restitution compliance with 637 Indigenous consultations, judicial digitalisation, 100% school-meals coverage, a new women\'s prison plus a 2024 alternatives-to-detention protocol, 2025 treaty ratifications, the Indigenous Languages Act, disability-certification reform, online birth registration). **No relevant action (C)** persists on the long-standing asks — a comprehensive anti-discrimination law, a migration law, abortion, criadazgo, the minimum marriage age, the journalist-protection bill — and there are clear regressions (**E**): the 2024 NGO "Garrote" law and Ministry-of-Education restrictions on gender and sexuality education.',
    ),
}


def get(slug: str) -> dict:
    try:
        return COUNTRIES[slug]
    except KeyError:
        raise SystemExit(f"unknown country '{slug}'; choose from {list(COUNTRIES)}")


def out_dir(slug: str) -> Path:
    d = get(slug)["db"].parent / "output"
    d.mkdir(parents=True, exist_ok=True)
    return d
