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
    "suriname": dict(
        code="SUR", name="Suriname", short="Suriname",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/6",
        cycle3_review="2021-11-01", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/suriname/UPR39_Surinam_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/suriname/suriname.db",
        evidence_dir=ROOT / "countries/suriname/evidence",
        slug_prefix="suriname_cycle3",
        thematic_out="UPR39_Surinam_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/SUR/1", "2": "A/HRC/WG.6/53/SUR/2", "3": "A/HRC/WG.6/53/SUR/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/SUR/1",
            "**UN Compilation** — A/HRC/WG.6/53/SUR/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/SUR/3, OHCHR",
        ],
        headline="**Partial implementation (B)** is the dominant outcome, and Suriname gives a detailed National Report: it acceded to the Convention against Torture (16 November 2021) and abolished the death penalty in its Military Criminal Code (2021, **A**), adopted the Equal Treatment in Employment Act and the Act on Violence and Sexual Harassment in Employment (2022), the Children's Ombudsperson Act (2025), a National Social Protection Strategy 2024-2030, a National Education Policy Plan 2024-2031, a Multilingual Education Programme, a National Policy Plan for Persons with Disabilities 2025-2030, a national FPIC protocol (2025) and a Land Rights Project, and introduced the General Act for Persons with Disabilities in Parliament. **No relevant action (C)** persists on the remaining optional protocols (OP-CAT, OP-CEDAW, OP-CRPD, OP-ICESCR, the Second Optional Protocol), ICPPED, the national human rights institution (draft Act only), legislation on sexual orientation and gender identity, the minimum age of marriage, corporal punishment, child labour, a standing invitation to special procedures and the Collective Rights of Indigenous and Tribal Peoples Act (still a draft).",
    ),
    "greece": dict(
        code="GRC", name="Greece", short="Greece",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/5",
        cycle3_review="2021-11-01", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/greece/UPR39_Greece_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/greece/greece.db",
        evidence_dir=ROOT / "countries/greece/evidence",
        slug_prefix="greece_cycle3",
        thematic_out="UPR39_Greece_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/GRC/1", "2": "A/HRC/WG.6/53/GRC/2", "3": "A/HRC/WG.6/53/GRC/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/GRC/1",
            "**UN Compilation** — A/HRC/WG.6/53/GRC/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/GRC/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome, and Greece gives a detailed National Report: marriage equality (Law 5089/2024, **A**), bans on conversion therapy and non-consensual intersex surgery, repeal of simple defamation, a second National Action Plan against Racism and Intolerance (2026), the 2025 EU-aligned domestic-violence law with stalking and cyber-harassment offences, pay-transparency legislation (2026), a National Guardianship System for unaccompanied minors (2024), a National Strategy on Disability 2024-2030, new prison alternatives and a National Climate Law. **No relevant action (C)** persists on treaty ratification (ICRMW, OP-ICESCR, OP-CRC-IC), the rights of the Turkish Muslim minority, the protection of human rights defenders, and investigation of pushbacks. There are clear regressions or rejections (**E**): in July 2025 Greece suspended the registration of asylum applications of people arriving by sea and provided for returns without registration, the Human Rights Committee remains gravely concerned about pushbacks, and Greece restates that it recognises only a religious minority in Thrace.',
    ),
    "samoa": dict(
        code="WSM", name="Samoa", short="Samoa",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/7",
        cycle3_review="2021-11-02", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/samoa/UPR39_Samoa_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/samoa/samoa.db",
        evidence_dir=ROOT / "countries/samoa/evidence",
        slug_prefix="samoa_cycle3",
        thematic_out="UPR39_Samoa_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "", "2": "A/HRC/WG.6/53/WSM/2", "3": "A/HRC/WG.6/53/WSM/3"},
        sources=[
            "The **National Report** (A/HRC/WG.6/53/WSM/1) was not yet available at the time of assessment.",
            "**UN Compilation** — A/HRC/WG.6/53/WSM/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/WSM/3, OHCHR",
        ],
        headline="**No relevant action (C)** is the dominant outcome, and the evidence is thin on the State's own account: Samoa's National Report was not yet available, so 22 asks have no information in the documents (**D**). **Partial implementation (B)** appears where the documents record a concrete measure — strengthened primary health care and the Health Sector Plan 2021-2025, the Education Sector Plan 2025-2030, higher pensions from late 2025, a legal minimum marriage age of 18 and dedicated policies against gender-based violence. **No relevant action (C)** persists on treaty ratification (ICESCR, ICERD, OP-CAT, the Second Optional Protocol), a comprehensive anti-discrimination law, decriminalisation of same-sex relations, abortion, corporal punishment, the pending Child Protection Bill and the age of criminal responsibility.",
    ),
    "saint-vincent-and-the-grenadines": dict(
        code="VCT", name="Saint Vincent and the Grenadines", short="St Vincent & the Grenadines",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/10",
        cycle3_review="2021-11-03", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/saint-vincent-and-the-grenadines/UPR39_Saint_Vincent_Grenadines_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/saint-vincent-and-the-grenadines/saint-vincent-and-the-grenadines.db",
        evidence_dir=ROOT / "countries/saint-vincent-and-the-grenadines/evidence",
        slug_prefix="saint-vincent-and-the-grenadines_cycle3",
        thematic_out="UPR39_Saint_Vincent_Grenadines_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "", "2": "A/HRC/WG.6/53/VCT/2", "3": "A/HRC/WG.6/53/VCT/3"},
        sources=[
            "The **National Report** (A/HRC/WG.6/53/VCT/1) was not yet available at the time of assessment.",
            "**UN Compilation** — A/HRC/WG.6/53/VCT/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/VCT/3, OHCHR",
        ],
        headline="**No relevant action (C)** is the dominant outcome, with a thin evidence base on the State's own account because its National Report was not yet available. **Partial implementation (B)** appears where the documents record concrete measures: the 2023 amendment of the Prevention of Trafficking in Persons Act and a 2021-2025 action plan, a National Task Force on Gender-Based Violence (2024), a National Child Protection Policy, the national climate and adaptation framework, expanded social protection after the 2021 volcanic eruption and the new Belle Isle detention facility. **No relevant action (C)** persists on ICPPED, OP-CAT and the other unratified protocols, a comprehensive anti-discrimination law, decriminalisation of same-sex conduct (sections 146 and 148), the death penalty (a de facto moratorium since 1995 but one person on death row), the minimum age of marriage, a national human rights institution, the pending Sexual Offences Bill and criminalisation of marital rape and sexual harassment, and corporal punishment. Many asks have no information in the documents (**D**).",
    ),
    "hungary": dict(
        code="HUN", name="Hungary", short="Hungary",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/8",
        cycle3_review="2021-11-02", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/hungary/UPR39_Hungary_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/hungary/hungary.db",
        evidence_dir=ROOT / "countries/hungary/evidence",
        slug_prefix="hungary_cycle3",
        thematic_out="UPR39_Hungary_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/HUN/1", "2": "A/HRC/WG.6/53/HUN/2", "3": "A/HRC/WG.6/53/HUN/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/HUN/1",
            "**UN Compilation** — A/HRC/WG.6/53/HUN/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/HUN/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome (142 of 267 asks), and Hungary gives a National Report that admits "very limited progress": Act X of 2023 strengthened the National Judicial Council, a preventive restraining order that outlasts imprisonment (2025) and a review of 31,139 police domestic-violence cases, hate-crime training for all police, the National Strategy against Antisemitism (2024), the 2025 action plan under the Social Inclusion Strategy 2030, a partial decriminalisation of defamation (2023) and an Act on anti-discrimination in education (2024). **No relevant action (C)** covers 93 asks, notably media pluralism, civil-society space, asylum and pushbacks, the Istanbul Convention and the Women, Peace and Security plan. **Contrary measures (E)** apply to 16 asks: the \'child protection\' law kept and extended by Act III of 2025, which bans Pride and other LGBTIQ-themed assemblies (a constitutional amendment followed), and the withdrawal from the Rome Statute. Four asks reach **A** (support for the family, visible bilingualism in the Rába region, cooperation with special procedures).',
    ),
    "papua-new-guinea": dict(
        code="PNG", name="Papua New Guinea", short="Papua New Guinea",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/11",
        cycle3_review="2021-11-04", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/papua-new-guinea/UPR39_Papua_New_Guinea_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/papua-new-guinea/papua-new-guinea.db",
        evidence_dir=ROOT / "countries/papua-new-guinea/evidence",
        slug_prefix="papua-new-guinea_cycle3",
        thematic_out="UPR39_Papua_New_Guinea_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/PNG/1", "2": "A/HRC/WG.6/53/PNG/2", "3": "A/HRC/WG.6/53/PNG/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/PNG/1",
            "**UN Compilation** — A/HRC/WG.6/53/PNG/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/PNG/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome, and Papua New Guinea gives a detailed National Report: the death penalty was abolished in 2022-2023, the Disability Services Act 2025 was enacted, a costed GBV Strategy 2026-2035 and a sorcery-accusation action plan (2024-2029) were launched, the Strategic Plan on Human Rights 2024-2029 and a National Human Rights Policy (2026) were adopted, a 10% women-candidate quota was legislated for 2027, and health and education funding rose. **No relevant action (C)** persists on ratification of CAT, OP-CAT and ICPPED, a comprehensive anti-discrimination law, decriminalisation of same-sex relations, the minimum ages of marriage and criminal responsibility, an access-to-information law, a national action plan on business and human rights and an established national human rights institution (draft legislation only). Reported on-the-ground violence, forced evictions and pressure on journalists remain serious concerns.',
    ),
    "tajikistan": dict(
        code="TJK", name="Tajikistan", short="Tajikistan",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/12",
        cycle3_review="2021-11-04", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/tajikistan/UPR39_Tajikistan_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/tajikistan/tajikistan.db",
        evidence_dir=ROOT / "countries/tajikistan/evidence",
        slug_prefix="tajikistan_cycle3",
        thematic_out="UPR39_Tajikistan_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/TJK/1", "2": "A/HRC/WG.6/53/TJK/2", "3": "A/HRC/WG.6/53/TJK/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/TJK/1",
            "**UN Compilation** — A/HRC/WG.6/53/TJK/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/TJK/3, OHCHR",
        ],
        headline="**Partial implementation (B)** is the dominant outcome (145 of 234 asks), and Tajikistan gives a detailed National Report: the Equality and Elimination of All Forms of Discrimination Act (2022, **A**), the National Human Rights Strategy to 2038 (2023, **A**), a National Programme on the Protection of Children's Rights 2026-2030 (**A**), a complete ban on corporal punishment (2024), a new disability-rights Act (June 2026), a 92% budget increase for the Commissioner for Human Rights, amendments to the Domestic Violence Act and a State Programme 2025-2030, trafficking and child-labour plans, and amendments to the Criminal Code on online expression (May 2025). **No relevant action (C)** persists on criminalising domestic violence (still in the draft Criminal Code), the Convention on the Rights of Persons with Disabilities and other ratifications, torture investigations, religious freedom, LGBTI protection and a standing invitation to special procedures. **Contrary measures (E)** apply to 16 asks on civil society, media and political prisoners: the UN reports 700 NGOs liquidated in 18 months, about 20 journalists and bloggers imprisoned since 2022 and websites blocked.",
    ),
    "tanzania": dict(
        code="TZA", name="United Republic of Tanzania", short="Tanzania",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/13",
        cycle3_review="2021-11-05", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/tanzania/UPR39_Tanzania_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/tanzania/tanzania.db",
        evidence_dir=ROOT / "countries/tanzania/evidence",
        slug_prefix="tanzania_cycle3",
        thematic_out="UPR39_Tanzania_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/TZA/1", "2": "A/HRC/WG.6/53/TZA/2", "3": "A/HRC/WG.6/53/TZA/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/TZA/1",
            "**UN Compilation** — A/HRC/WG.6/53/TZA/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/TZA/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome (143 of 252 asks), and Tanzania gives a detailed National Report on socio-economic and service measures: health financing (TZS 1.31 to 3.104 trillion), school construction and a Re-Entry Guideline for pregnant girls, the Second National Plan of Action on violence against women and children (2024/25-2028/29), a National Action Plan on persons with albinism, the Mama Samia legal aid campaign and amendments to the Media Services Act and related laws. **Fully implemented (A)** are the ban on expelling pregnant schoolgirls, birth registration, older persons, climate participation and rural communication infrastructure. **No relevant action (C)** persists on ratifying the Convention against Torture and other treaties, the death penalty (a de facto moratorium only), child marriage (the Law of Marriage Act is still only under consultation), decriminalisation of same-sex relations, corporal punishment and the second National Human Rights Action Plan. **Contrary measures (E)** apply to 14 asks on freedom of expression, assembly, political participation and indigenous peoples: the nationwide internet shutdown after the 29 October 2025 elections, the shutdown of more than 80,000 websites (May 2025), reported lethal force, arrests and enforced disappearances (which the State rejects), disqualification of opposition candidates and the position that no group is indigenous.',
    ),
    "antigua-and-barbuda": dict(
        code="ATG", name="Antigua and Barbuda", short="Antigua & Barbuda",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/15",
        cycle3_review="2021-11-08", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/antigua-and-barbuda/UPR39_Antigua_and_Barbuda_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/antigua-and-barbuda/antigua-and-barbuda.db",
        evidence_dir=ROOT / "countries/antigua-and-barbuda/evidence",
        slug_prefix="antigua-and-barbuda_cycle3",
        thematic_out="UPR39_Antigua_and_Barbuda_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/ATG/1", "2": "A/HRC/WG.6/53/ATG/2", "3": "A/HRC/WG.6/53/ATG/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/ATG/1",
            "**UN Compilation** — A/HRC/WG.6/53/ATG/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/ATG/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome, and Antigua and Barbuda submitted a detailed National Report: the High Court decriminalised consensual same-sex relations in July 2022 (**A**, though the provisions were not formally repealed), ILO Conventions 190 and 183 were ratified in 2022, maternity leave rose to 14 weeks, a National Child Protection Policy (2021), a Sexual Offenders Registry (2022), a GBV Action Plan (2023), a shelter partnership, prison upgrades, higher pensions (2025-2026) and large climate-resilience financing were reported. **No relevant action (C)** persists on the unratified treaties and protocols (ICPPED, OP-CAT, the Second Optional Protocol), a national human rights institution, a national reporting mechanism, anti-discrimination legislation, criminalisation of marital rape, abortion, corporal punishment in schools and formal abolition of the death penalty (a de facto moratorium since 1991). No trafficking conviction has ever been secured.',
    ),
    "eswatini": dict(
        code="SWZ", name="Eswatini", short="Eswatini",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/14",
        cycle3_review="2021-11-08", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/eswatini/UPR39_Eswatini_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/eswatini/eswatini.db",
        evidence_dir=ROOT / "countries/eswatini/evidence",
        slug_prefix="eswatini_cycle3",
        thematic_out="UPR39_Eswatini_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/SWZ/1", "2": "A/HRC/WG.6/53/SWZ/2", "3": "A/HRC/WG.6/53/SWZ/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/SWZ/1",
            "**UN Compilation** — A/HRC/WG.6/53/SWZ/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/SWZ/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome (107 of 222 asks) alongside a large block of **No relevant action (C)** (93 asks). B reflects concrete measures in the National Report: the Commission on Human Rights and Public Administration Bill introduced in Parliament (2026), the Legal Aid Act (2025), a reconstituted Judicial Service Commission, the National Disability Plan of Action 2024-2028 and a National Disability Advisory Council, a GBV Coordination Mechanism, the Sexual, Reproductive, Maternal, Newborn, Child, Adolescent Health and Nutrition Strategy 2024-2028, education reforms (primary dropout down from 6.5% to 4.8%) and higher social grants. C persists on ratification (OP-CAT, OP-CEDAW, the Second Optional Protocol and others), the death penalty, same-sex relations and anti-discrimination law for sexual orientation and gender identity, corporal punishment, the Family Law Bills (the Marriages Bill is still not enacted, so the marriage age stays at 16), political parties, torture and accountability for the 2021 unrest and the killing of Thulani Maseko. **Contrary measures (E)** apply to seven asks: the Government obtained a Supreme Court judgment (August 2024) upholding the Suppression of Terrorism Act and the Sedition and Subversive Activities Act and made no reform, and the UN reports excessive force against protests. Water and sanitation (and part of GBV and inclusive education) were referred to a mid-term report that was not reviewed here, so water asks are **D**.',
    ),
    "trinidad-and-tobago": dict(
        code="TTO", name="Trinidad and Tobago", short="Trinidad & Tobago",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/16",
        cycle3_review="2021-11-09", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/trinidad-and-tobago/UPR39_Trinidad and Tobago_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/trinidad-and-tobago/trinidad-and-tobago.db",
        evidence_dir=ROOT / "countries/trinidad-and-tobago/evidence",
        slug_prefix="trinidad-and-tobago_cycle3",
        thematic_out="UPR39_Trinidad and Tobago_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "", "2": "A/HRC/WG.6/53/TTO/2", "3": "A/HRC/WG.6/53/TTO/3"},
        sources=[
            "The **National Report** (A/HRC/WG.6/53/TTO/1) was not yet available at the time of assessment.",
            "**UN Compilation** — A/HRC/WG.6/53/TTO/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/TTO/3, OHCHR",
        ],
        headline="**No relevant action (C)** is the dominant outcome, with a thin evidence base on the State's own account because its National Report was not yet available (14 asks are **D**). **Partial implementation (B)** appears where the documents record concrete measures: the 2023 National Strategic Action Plan on gender-based and sexual violence, anti-trafficking plans, shelters and a first conviction, a National Climate Change Policy, near-universal free education and a comprehensive social protection system. **No relevant action (C)** persists on the mandatory death penalty (48 people under sentence of death in 2026, no moratorium), treaty ratification, refugee legislation, an anti-discrimination law, a national human rights institution and prison conditions. There is a clear regression (**E**): consensual same-sex relations were re-criminalised in 2025 when the Court of Appeal reinstated sections 13 and 16 of the Sexual Offences Act, and repeated States of Emergency since 2024 have expanded police powers.",
    ),
    "thailand": dict(
        code="THA", name="Thailand", short="Thailand",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/17",
        cycle3_review="2021-11-10", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/thailand/UPR39_Thailand_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/thailand/thailand.db",
        evidence_dir=ROOT / "countries/thailand/evidence",
        slug_prefix="thailand_cycle3",
        thematic_out="UPR39_Thailand_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/THA/1", "2": "A/HRC/WG.6/53/THA/2", "3": "A/HRC/WG.6/53/THA/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/THA/1",
            "**UN Compilation** — A/HRC/WG.6/53/THA/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/THA/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is the dominant outcome (141 of 278 asks), and Thailand adopted the largest number of new laws and plans of the 13 countries: the Marriage Equality Act (in force 23 January 2025, which also raised the marriage age to 18, **A**), the Prevention and Suppression of Torture and Enforced Disappearance Act (2023, **A**), ratification of the Convention on Enforced Disappearance (2024, **A**), a complete ban on corporal punishment of children in all settings (March 2025, **A**), restoration of the NHRCT to A status (2022, **A**), the Personal Data Protection Act (**A**), criminalisation of sexual harassment (December 2025), the Ethnic Groups Act (September 2025), a stateless-persons fast-track (121,471 granted status) and a National Referral Mechanism for trafficking. **No relevant action (C)** persists on lèse-majesté, sedition, defamation and computer-crime laws (HRW counts at least 1,997 people prosecuted since 2014), the death penalty, OP-CAT and ILO Conventions 87 and 98, refugee law, an anti-discrimination law (still a draft) and the Anti-SLAPP bill (still a draft). 26 asks are **D**, including all asks on the non-profit organisations bill, COVID-19 measures and sexual education. The one **contrary measure (E)** is the continued return of refugees: a mass expulsion of asylum-seekers to Myanmar on 25 June 2024 and the return of 40 Uyghur men in February 2025.',
    ),
    "ireland": dict(
        code="IRL", name="Ireland", short="Ireland",
        cycle3_session="39th", cycle3_symbol="A/HRC/49/18",
        cycle3_review="2021-11-10", cycle4_review="November 2026 (session 53)",
        thematic=ROOT / "countries/ireland/UPR39_Ireland_Thematic_List_of_Recommendations.docx",
        db=ROOT / "countries/ireland/ireland.db",
        evidence_dir=ROOT / "countries/ireland/evidence",
        slug_prefix="ireland_cycle3",
        thematic_out="UPR39_Ireland_Thematic_List_of_Recommendations_ASSESSED.docx",
        c4_docs={"1": "A/HRC/WG.6/53/IRL/1", "2": "A/HRC/WG.6/53/IRL/2", "3": "A/HRC/WG.6/53/IRL/3"},
        sources=[
            "**National Report** — A/HRC/WG.6/53/IRL/1",
            "**UN Compilation** — A/HRC/WG.6/53/IRL/2, OHCHR",
            "**Stakeholders' Summary** — A/HRC/WG.6/53/IRL/3, OHCHR",
        ],
        headline='**Partial implementation (B)** is by far the dominant outcome (182 of 260 asks), with 19 asks fully met (**A**) and 44 at **No relevant action (C)**. Ireland reports a dense set of concrete measures in the review period: the National Action Plan Against Racism 2023-2027 (March 2023) with a Special Rapporteur on Racial Equality, the Criminal Justice (Hate Offences) Act 2024, endorsement of the IHRA definition of antisemitism, the National Traveller and Roma Inclusion Strategy II and the National LGBTIQ+ Inclusion Strategy II, the National Human Rights Strategy for Disabled People 2025-2030 and accession to the Optional Protocol to the CRPD (October 2024), the Third National Strategy on domestic, sexual and gender-based violence and the new agency Cuan, the Birth Information and Tracing Act 2022, an independent review of civil legal aid, the National Strategy for Women and Girls 2025-2030 and the Mental Health Act 2026. **C** persists on ICPPED and OP-ICESCR (under consideration), incorporation of ICERD, amendment of the 1989 Incitement to Hatred Act (hate speech reform was dropped), a legislative ban on racial profiling, conversion practices, direct provision, a second business and human rights plan and redress for mixed-race children in institutions. The seven **contrary** asks (**E**) all concern the Migrant Workers Convention, which Ireland states it has no plans to sign or ratify.',
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
