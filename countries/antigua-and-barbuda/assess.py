"""Antigua and Barbuda — implementation assessment of its 3rd-cycle (2021,
A/HRC/49/15) UPR recommendations, graded against the 4th-cycle documentation
(session 53): National Report A/HRC/WG.6/53/ATG/1, OHCHR Compilation /2 and
Stakeholders' Summary /3.

    python scripts/run_assess.py antigua-and-barbuda

First pass for expert review. Quotes are verbatim from the three documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding treaties and optional protocols",
        "Antigua and Barbuda has ratified 7 of the 9 core treaties and reports "
        "no new core-treaty or optional-protocol ratification (ICPPED, "
        "OP-ICCPR, OP-ICESCR, OP-CAT and the Second Optional Protocol remain "
        "outstanding), though it ratified ILO Conventions 190 and 183 in 2022.",
        [
            ("Antigua and Barbuda", "1", "23", "Antigua and Barbuda has ratified 7 out of the 9-core international human rights instruments"),
            ("UNESCO", "2", "2", "recommended that Antigua and Barbuda ratify the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights"),
            ("CGNK", "3", "2", "recommended that Antigua and Barbuda ratify the Convention on Enforced Disappearances (CED)"),
        ],
    ),
    "Equality & non-discrimination": (
        C, "Legislate against discrimination, including on sexual orientation",
        "Same-sex relations were decriminalised by the High Court in July 2022 "
        "and the Constitution was interpreted to protect against discrimination "
        "on grounds of sexual orientation; no anti-discrimination legislation "
        "has been enacted.",
        [
            ("Antigua and Barbuda", "1", "73", "the Constitution has been interpreted to extend protection from discrimination based on sexual orientation"),
            ("United Nations country team", "2", "5", "the Constitution of Antigua and Barbuda prohibited discrimination on the grounds of race, sex or creed"),
        ],
    ),
    "Children: definition": (
        B, "Strengthen child protection institutions and legislation",
        "Antigua and Barbuda adopted a National Child Protection Policy (2021), "
        "reformed juvenile justice (Child Justice Act 2015, amended 2018) and "
        "reopened a rehabilitation centre (2025); corporal punishment remains "
        "lawful in schools.",
        [
            ("United Nations country team", "2", "50", "had adopted the National Child Protection Policy (2021)"),
            ("Antigua and Barbuda", "1", "69", "The Child Justice (Amendment) Act 2018 also brought significant reform, shifting the age of criminal responsibility from 8 to 12 years of age"),
            ("UNESCO", "2", "14", "the Education Act of 2008 allowed for the use of corporal punishment in schools (article 50 (2))"),
        ],
    ),
    "Advancement of women": (
        B, "Promote women's empowerment and participation",
        "Women's representation rose (two women elected to the House in 2026, "
        "seven senators) and the Directorate of Gender Affairs runs "
        "empowerment programmes; a national gender equality policy is still "
        "in final draft.",
        [
            ("Antigua and Barbuda", "1", "9", "The results of the general election saw the election of two female members of the House of Representatives"),
            ("Antigua and Barbuda", "1", "64", "A final draft of the policy document has been prepared and is expected to be presented to the Cabinet for approval"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        C, "Establish a Paris-Principles national human rights institution",
        "Antigua and Barbuda has only considered restructuring the "
        "Ombudsman's office and sought technical assistance; no institution "
        "exists.",
        [
            ("Antigua and Barbuda", "1", "72", "Antigua and Barbuda has considered establishing an independent Human Rights Institution, possibly through restructuring the office of the Ombudsman, and has sought technical assistance for mapping this transition"),
            ("United Nations country team", "2", "7", "did not have a national human rights institution compliant with the principles relating to the status of national institutions for the promotion and protection of human rights"),
        ],
    ),
    "Discrimination against women": (
        B, "Eliminate discrimination against women",
        "The Constitution guarantees equality and gender-mainstreaming efforts "
        "continue, but there is no comprehensive statutory definition of "
        "discrimination against women.",
        [
            ("United Nations country team", "2", "9", "domestic legislation did not contain a comprehensive statutory definition of discrimination against women"),
        ],
    ),
    "Conditions of detention": (
        B, "Eliminate prison overcrowding and improve conditions",
        "Antigua and Barbuda added 170 beds and container units at His "
        "Majesty's Prison, built new sanitation and recruited 42 correctional "
        "officers; the prison still holds about twice its design capacity.",
        [
            ("Antigua and Barbuda", "1", "75", "The first phase of major upgrades saw the addition of 170 new beds"),
            ("Antigua and Barbuda", "1", "77", "The prison also recruited 42 new correctional officers in 2025"),
            ("JS4", "3", "5", "which had a design capacity of 150 but held approximately 300 prisoners as of 2024"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Strengthen anti-trafficking measures and victim assistance",
        "A Trafficking in Persons Prevention Unit investigates cases (13 "
        "suspects in 2024), a 2025 National Action Plan exists and victims "
        "receive services; no conviction has ever been secured.",
        [
            ("Antigua and Barbuda", "1", "37", "the Trafficking in Persons Prevention Unit initiated investigations of 13 suspects in nine cases"),
            ("ECLJ", "3", "7", "no individual had ever been convicted of human trafficking in Antigua and Barbuda and no victim had been formally identified"),
        ],
    ),
    "Death penalty": (
        C, "Abolish the death penalty",
        "The death penalty remains on the statute books for murder and "
        "treason; no execution has taken place since 1991 and no one is on "
        "death row.",
        [
            ("Antigua and Barbuda", "1", "35", "Antigua and Barbuda has not had an execution under the death penalty since 1991"),
            ("United Nations country team", "2", "10", "no formal legislative abolition had been enacted"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        C, "Decriminalise abortion",
        "Abortion remains criminalised except where the pregnant woman's life is at risk.",
        [("United Nations country team", "2", "29", "abortion remained criminalized in Antigua and Barbuda under the Offences Against the Person Act, except in limited circumstances where the continuation of pregnancy posed a risk to the life of the pregnant woman")],
    ),
    "Human rights & climate change": (
        B, "Climate resilience policies and participation",
        "Antigua and Barbuda adopted the Agenda for SIDS (2024), runs the "
        "UNDP EnGenDER community resilience project, benefits from the "
        "US$12.3 million Early Warning for All programme and led the ITLOS "
        "advisory-opinion request.",
        [
            ("Antigua and Barbuda", "1", "27", "led to the adoption of the Antigua and Barbuda Agenda for SIDS (ABAS)"),
            ("Antigua and Barbuda", "1", "32", "US12.3-Million-dollar Early Warning for All (EW4ALL) initiative funded by the Green Climate Fund (GCF)"),
        ],
    ),
    "Right to education": (
        B, "Resource education initiatives and invest in education",
        "Public education is free, CSEC examination fees are covered (2026) "
        "and tertiary education is tuition-free; comprehensive sexuality "
        "education has not been implemented.",
        [
            ("Antigua and Barbuda", "1", "68", "have also been made tuitionfree by the Government"),
            ("JS1", "3", "10", "no comprehensive sexuality education in line with international standards had been implemented"),
        ],
    ),
    "Cooperation with international organizations": (
        B, "Seek OHCHR technical assistance",
        "Treaty reports are being drafted with development-partner support and "
        "technical assistance was sought for the national institution; no "
        "dedicated reporting unit exists.",
        [
            ("Antigua and Barbuda", "1", "23", "The reports for the Convention Against Torture and the Convention on the Elimination of Racial Discrimination are being drafted with support from development partners"),
            ("Antigua and Barbuda", "1", "80", "The country does not have a dedicated unit or mechanism for monitoring and reporting on Human Rights"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Strengthen laws and policies against sexual and gender-based violence",
        "The Workplace Violence and Harassment (Prevention) Bill is before "
        "Parliament, a Sexual Offenders Registry was created (2022) and a "
        "model Sexual Offences Court operates; marital rape is not fully "
        "criminalised.",
        [
            ("Antigua and Barbuda", "1", "78", "Parliament is presently tabling the Workplace Violence and Harassment (Prevention) Bill"),
            ("United Nations country team", "2", "49", "marital rape was not fully criminalized in all circumstances under section 3 (1) of the Sexual Offences Act"),
        ],
    ),
    "Human rights & poverty": (
        B, "Social programmes and poverty alleviation",
        "The HAPPI housing programme has delivered 111 homes, pensions were raised "
        "in 2025 and 2026 and food assistance continues.",
        [
            ("Antigua and Barbuda", "1", "39", "The programme has delivered 111 homes across the island so far"),
            ("Antigua and Barbuda", "1", "43", "In April 2025, the Government increased the minimum pension payable from EC$350.00 to EC$500"),
        ],
    ),
    "Violence against women": (
        B, "Prevent violence against women and girls",
        "The SARC one-stop centre, a police Special Victims Support Unit, a "
        "2023 GBV Action Plan and a Cabinet-approved shelter partnership exist; "
        "the national action plan was never formally endorsed and GBV remains pervasive.",
        [
            ("Antigua and Barbuda", "1", "60", "In 2023, the Directorate developed a new Gender Based Violence Action Plan"),
            ("United Nations country team", "2", "45", "the plan was never formally endorsed by the relevant national authorities"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        C, "Criminalise torture and exclude evidence obtained by torture",
        "Torture is criminalised by the Suppression of Torture Act 1993 "
        "(pre-dating the review) and exclusion of evidence rests on the "
        "Constitution and common law; there is no explicit statutory provision.",
        [
            ("Antigua and Barbuda", "1", "33", "no specific law formally prohibiting the introduction of evidence obtained under torture"),
            ("United Nations country team", "2", "13", "there was no explicit statutory provision declaring such evidence inadmissible, as that relied on judicial doctrines and common law"),
        ],
    ),
    "Right to health": (
        B, "Strengthen health-care access and resources",
        "A dedicated NCD department, free HPV cervical cancer screening, a "
        "planned renal centre and a 2026 transition to national health "
        "insurance advance access.",
        [
            ("Antigua and Barbuda", "1", "46", "Women between the ages of 30 and 65 in Antigua and Barbuda are eligible for free HPV Cervical Cancer screening"),
            ("United Nations country team", "2", "28", "the scheme would be transformed into a national health insurance scheme in 2026"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        C, "Draft regulations under the Disabilities and Equal Opportunities Act",
        "The Disability and Equal Opportunities Act 2017 and a tribunal "
        "exist, but the clarifying regulations have not been drafted; the "
        "only 2025 measure cited is a service-dog amendment which the report "
        "itself says is not a regulation.",
        [
            ("Antigua and Barbuda", "1", "57", "an amendment was proposed in Parliament to regulate the registration and use of service dogs for visually impaired persons, which, though not a regulation"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        C, "Extend a standing invitation to special procedures",
        "No standing invitation has been issued despite repeated recommendations.",
        [("United Nations country team", "2", "4", "had not issued a standing invitation for special procedures, despite repeated recommendations")],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        C, "Establish a national mechanism for reporting and follow-up",
        "The report states the country has no dedicated unit or mechanism for "
        "human-rights reporting and no system for tracking UPR recommendations.",
        [("Antigua and Barbuda", "1", "80", "there is no comprehensive system in place for tracking the progress on the recommendations")],
    ),
    "Inter-State cooperation and assistance": (
        B, "Seek international assistance to mitigate climate impacts",
        "Antigua and Barbuda secured Green Climate Fund financing and led the "
        "ITLOS advisory-opinion request.",
        [("Antigua and Barbuda", "1", "28", "requested a clarifying Advisory Opinion from the International Tribunal for the Law of the Sea")],
    ),
    "Right to development": (
        B, "Promote sustainable development and living standards",
        "Housing, renewable energy and resilience-financing programmes were launched.",
        [("Antigua and Barbuda", "1", "49", "The Government continues to promote climate-adaptive development through the Sustainable Island Resource Framework Fund")],
    ),
    "Right to social security": (
        B, "Allocate more resources to social protection",
        "The National Social Protection Act 2020 exists and minimum pensions were raised in 2025 and 2026.",
        [("Antigua and Barbuda", "1", "43", "In 2026, a 5% increase in payments for pensioners across the board through the ABSSS was approved")],
    ),
    "Persons with disabilities: accessibility, mobility": (
        B, "Integrate children with disabilities in regular schools",
        "The Ministry of Education is training specialist teachers and screening children to integrate them in the broader school network.",
        [("Antigua and Barbuda", "1", "55", "continues to work toward integrating children with disabilities into the broader school network")],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        D, "Open, merit-based selection of treaty-body candidates",
        "The documents contain no information on this ask.", [],
    ),
    "Constitutional & legislative framework": (
        C, "Repeal capital punishment from national legislation",
        "No legislative repeal has been enacted.",
        [("United Nations country team", "2", "10", "no formal legislative abolition had been enacted")],
    ),
    "Legal & institutional reform": (
        C, "Establish a unit to collect human-rights data and prepare reports",
        "The State has acknowledged the need for such a unit but none exists.",
        [("United Nations country team", "2", "3", "had acknowledged the need to establish a specialized unit dedicated to the collection of human rights data")],
    ),
    "Good governance & corruption": (
        B, "Implement the anti-corruption proposal",
        "The Integrity in Public Life Act is in force and enforcement of asset declarations was renewed.",
        [("United Nations country team", "2", "36", "renewed enforcement of asset declaration requirements for persons in public life")],
    ),
    "Administration of justice & fair trial": (
        B, "Reduce pretrial detention and the criminal-justice backlog",
        "Backlog-reduction reforms were announced in November 2025, but pretrial detention can last up to five years.",
        [("Antigua and Barbuda", "1", "77", "announced several reforms aimed at reducing the backlog in the Criminal Justice system"),
         ("United Nations country team", "2", "15", "pretrial detention had been extended for up to five years")],
    ),
    "Rights related to marriage & family": (
        D, "Remove exceptions to the minimum age of marriage",
        "The documents contain no information on this ask.", [],
    ),
    "Human rights education, trainings & awareness raising": (
        C, "Revise the Health and Family Life Education curriculum",
        "No comprehensive sexuality education aligned with international guidance has been implemented.",
        [("JS1", "3", "10", "no comprehensive sexuality education in line with international standards had been implemented")],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        D, "National human rights action plan",
        "The documents contain no information on this ask.", [],
    ),
    "Budget & resources (for human rights implementation)": (
        D, "Build capacity of duty bearers",
        "The documents contain no information on this ask.", [],
    ),
    "Economic & political crisis, natural disasters or other emergencies": (
        B, "Ensure well-being in crises and disasters",
        "Early-warning, disaster-law review and community resilience projects were launched.",
        [("Antigua and Barbuda", "1", "32", "there will be a complete review and update of disaster legislation")],
    ),
    "Persons with disabilities: protection and safety in situations of risk": (
        D, "Access to information for persons with disabilities in emergencies",
        "The documents contain no information on this ask.", [],
    ),
}

KEYWORDS = [
    # --- ratification-cluster specifics ---
    (r"ILO Maternity Protection Convention", A,
     "Ratify ILO Maternity Protection Convention 2000",
     "Antigua and Barbuda ratified ILO Convention 183 in May 2022 and extended maternity leave to 14 weeks.",
     [("Antigua and Barbuda", "1", "21", "also ratified ILO Convention 183 – Maternity Protection, 2000, in May 2022")]),
    (r"Cultural Property|Hague|Optional Protocol to the Convention on the Rights of the Child|Declaration on Children, Youth and Climate|American Convention", D,
     "Ratify other instruments",
     "The documents contain no information on these instruments.", []),
    (r"Second Optional Protocol|ratify the Second", C,
     "Ratify the Second Optional Protocol (abolition)",
     "The Second Optional Protocol has not been ratified; JS4 recommends ratification.",
     [("JS4", "3", "2", "recommended the ratification of the Second Optional Protocol to the International Covenant on Civil and Political Rights")]),
    (r"moratorium", B,
     "Establish a moratorium on the death penalty",
     "A de facto moratorium has been in place since 1991, no one is on death row and the country voted for the UN moratorium resolution in 2024; no formal moratorium exists.",
     [("JS4", "3", "4", "a de facto moratorium had been in place since 1991 and no person was currently under sentence of death"),
      ("Antigua and Barbuda", "1", "35", "leaving no inmates on death row")]),
    (r"awareness-raising campaigns|dissuasive effects|public debates", D,
     "Awareness-raising on the death penalty",
     "The documents contain no information on awareness-raising on the death penalty.", []),
    (r"State review and discussion", B,
     "State review of the death penalty",
     "The Prime Minister stated in March 2025 he was not in favour of the death penalty; no formal review is reported.",
     [("JS4", "3", "4", "the Prime Minister's public statement of March 2025 that he was not in favour of the death penalty")]),
    # --- same-sex relations ---
    (r"decriminali[sz]e|Repeal sections 12 and 15|Reform the Sexual Offences Act|indecency statutes|consensual sexual", A,
     "Decriminalise consensual same-sex relations",
     "The High Court struck down sections 12 and 15 of the Sexual Offences Act in July 2022, decriminalising consensual same-sex relations; the provisions have not been formally repealed by legislation.",
     [("Antigua and Barbuda", "1", "17", "striking down sections 12 and 15 of the Sexual Offences Act of 1995, which criminalised same-sex sexual relations and ascribed custodial criminal sentences"),
      ("United Nations country team", "2", "52", "had not been formally repealed by legislative amendment, but rather rendered unenforceable through the Court’s declaration of unconstitutionality")]),
    (r"Repeal sections 12 and 15", B,
     "Repeal sections 12 and 15 of the Sexual Offences Act",
     "The provisions were declared unconstitutional and are unenforceable but were not formally repealed.",
     [("United Nations country team", "2", "52", "had not been formally repealed by legislative amendment")]),
    (r"Prohibit discrimination based on sexual orientation and gender identity, including|Prohibit discrimination based on sexual orientation and gender identity and decrimina", B,
     "Prohibit discrimination on grounds of sexual orientation and gender identity",
     "Same-sex relations were decriminalised and the Constitution was interpreted to protect against discrimination on grounds of sexual orientation, but no legislation prohibits it.",
     [("Antigua and Barbuda", "1", "73", "the Constitution has been interpreted to extend protection from discrimination based on sexual orientation")]),
    (r"national policy to promote tolerance|end the discrimination and stigmatization|Strengthen its commitment to the principles of equality", B,
     "Promote tolerance and combat stigmatisation of LGBTI+ persons",
     "The draft National Gender Equality and Social Inclusion Policy was consulted with LGBTQ+ organisations.",
     [("Antigua and Barbuda", "1", "74", "Consultation on the draft National Gender Equality and Social Inclusion Policy also includes representatives from organisations that represent the interests of LGBTQ+ persons")]),
    (r"regulatory changes to ensure the inclusion", D,
     "Regulatory inclusion of LGBTI persons",
     "The documents contain no information on this ask.", []),
    (r"combat discrimination and violence against women and children|full enjoyment of human rights", B,
     "Combat discrimination and violence against women and children",
     "A GBV Action Plan (2023), the SARC and a gender policy in final draft advance this ask.",
     [("Antigua and Barbuda", "1", "60", "In 2023, the Directorate developed a new Gender Based Violence Action Plan")]),
    (r"Disabilities and Equal Opportunities Act", B,
     "Strengthen the Disabilities and Equal Opportunities Act",
     "The Act (2017) establishes a rights framework and a complaints tribunal; the regulations are outstanding.",
     [("Antigua and Barbuda", "1", "57", "This Act sets out the rights framework for persons living with disabilities and establishes a specialised tribunal for complaints")]),
    # --- children ---
    (r"corporal punishment|right to punish|right to inflict|punish children", C,
     "Prohibit corporal punishment of children",
     "The Education Act 2008 allows corporal punishment in schools; only its use as a judicial sentence is prohibited.",
     [("UNESCO", "2", "14", "the Education Act of 2008 allowed for the use of corporal punishment in schools (article 50 (2))")]),
    (r"budgetary needs for children|independent mechanism for monitoring", D,
     "Children's budget and rights-monitoring mechanism",
     "The documents contain no information on this ask.", []),
    # --- women ---
    (r"temporary special measures", D,
     "Temporary special measures for women",
     "The documents contain no information on this ask.", []),
    (r"national gender policy", B,
     "Adopt a national gender policy",
     "A National Gender Equality and Social Inclusion Policy has a final draft awaiting Cabinet approval.",
     [("Antigua and Barbuda", "1", "64", "A final draft of the policy document has been prepared and is expected to be presented to the Cabinet for approval")]),
    (r"Repeal discriminatory provisions against women|Convention on the Elimination of All Forms of Discrimination against Women into", D,
     "Repeal discriminatory legislation / incorporate CEDAW",
     "The documents contain no information on this ask.", []),
    (r"comprehensive definition of discrimination against women", C,
     "Incorporate a definition of discrimination against women",
     "There is no comprehensive statutory definition.",
     [("United Nations country team", "2", "9", "domestic legislation did not contain a comprehensive statutory definition of discrimination against women")]),
    (r"independent|Establish a mandate to promote and protect women", C,
     "Mandate to promote and protect women's rights",
     "No independent mandate has been established; the Directorate of Gender Affairs is a government department.",
     [("Antigua and Barbuda", "1", "58", "holds the primary mandate in Antigua and Barbuda for mainstreaming")]),
    # --- detention ---
    (r"State report into prison conditions", D,
     "Commission a State report on prison conditions",
     "The documents contain no information on this ask.", []),
    # --- trafficking ---
    (r"Implement legislation to address modern slavery", C,
     "Implement anti-slavery legislation",
     "There has never been a conviction for trafficking.",
     [("ECLJ", "3", "7", "no individual had ever been convicted of human trafficking in Antigua and Barbuda")]),
    # --- sexual harassment / marital rape ---
    (r"marital rape|classify marital", C,
     "Criminalise marital rape",
     "Marital rape is not fully criminalised.",
     [("United Nations country team", "2", "49", "marital rape was not fully criminalized in all circumstances under section 3 (1) of the Sexual Offences Act")]),
    # --- education ---
    (r"comprehensive sexuality education", C,
     "Comprehensive sexuality education",
     "No comprehensive sexuality education in line with international standards has been implemented.",
     [("JS1", "3", "10", "no comprehensive sexuality education in line with international standards had been implemented")]),
    # --- cooperation ---
    (r"specific unit staffed|specific unit responsible", C,
     "Establish a specific unit for reporting and human-rights data",
     "The report states the country has no dedicated reporting unit.",
     [("Antigua and Barbuda", "1", "80", "The country does not have a dedicated unit or mechanism for monitoring and reporting on Human Rights")]),
    (r"Special Rapporteur on the issue of human rights obligations", D,
     "Invite the Special Rapporteur on the environment",
     "The documents contain no information on this ask.", []),
    (r"Harmonize the legislation on torture", C,
     "Harmonise torture legislation with the Convention",
     "The Suppression of Torture Act 1993 pre-dates the review and no reform is reported.",
     [("Antigua and Barbuda", "1", "34", "enacted the Suppression of Torture Act in that same year")]),
    (r"older women|National Policy on Ageing", B,
     "Policies for older women",
     "The National Policy on Ageing and the GRACE programme provide care for older persons.",
     [("Antigua and Barbuda", "1", "41", "provides free at-home care for the elderly")]),
    (r"^Abolish death penalty and ratify", C,
     "Abolish the death penalty and ratify the Second Optional Protocol",
     "Abolition has not been enacted and the Second Optional Protocol is unratified; only a de facto moratorium (since 1991) exists.",
     [("United Nations country team", "2", "10", "no formal legislative abolition had been enacted")]),
    (r"^Develop public policies to combat gender-based violence", B,
     "Public policies against gender-based violence",
     "A GBV Action Plan (2023), the SARC and a Cabinet-approved shelter partnership advance the policy ask; no temporary special measures are reported.",
     [("Antigua and Barbuda", "1", "60", "In 2023, the Directorate developed a new Gender Based Violence Action Plan")]),
]

FALLBACK = (
    D, "Miscellaneous",
    "No rule matched and the evidence base contains no specific information on this recommendation.",
    [],
)
