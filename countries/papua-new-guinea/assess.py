"""Papua New Guinea — implementation assessment of its 3rd-cycle (2021,
A/HRC/49/11) UPR recommendations, graded against the 4th-cycle documentation
(session 53): National Report A/HRC/WG.6/53/PNG/1, OHCHR Compilation /2 and
Stakeholders' Summary /3.

    python scripts/run_assess.py papua-new-guinea

First pass for expert review. Quotes are verbatim from the three documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments",
        "PNG is still only reviewing the implications of ratifying CAT, OP-CAT, "
        "OP-CEDAW and ICPPED; no ratification in the review period is reported "
        "and the Rome Statute remains unratified.",
        [
            ("Papua New Guinea", "1", "7", "continues to review its legal, policy and institutional frameworks to assess the implications of ratifying additional international human rights instruments"),
            ("Office on Genocide Prevention and the Responsibility to Protect", "2", "6", "Papua New Guinea had yet to ratify the Rome Statute of the International Criminal Court"),
        ],
    ),
    "Death penalty": (
        A, "Abolish the death penalty / establish a moratorium",
        "Parliament amended the Criminal Code to abolish the death penalty and "
        "replace it with life imprisonment (2022-2023), meeting the core of the "
        "abolition recommendation; the Second Optional Protocol remains unratified.",
        [
            ("Papua New Guinea", "1", "118", "In 2023, Parliament passed an amendment of the Criminal Code to abolish the death penalty and replace it with life imprisonment"),
            ("United Nations country team", "2", "13", "Parliament had amended the Criminal Code to repeal the death penalty and replace it with life imprisonment"),
        ],
    ),
    "Equality & non-discrimination": (
        C, "Adopt comprehensive anti-discrimination protection",
        "There is no comprehensive anti-discrimination law, no constitutional "
        "amendment on sexual orientation or gender identity, and consensual "
        "same-sex conduct between men remains criminalised.",
        [
            ("United Nations country team", "2", "56", "no constitutional amendment had been adopted to include sexual orientation or gender identity or expression among the prohibited grounds of discrimination"),
            ("Amnesty International", "3", "10", "it did not have a comprehensive antidiscrimination"),
        ],
    ),
    "Right to education": (
        B, "Improve access to and quality of education",
        "PNG is implementing the National Education Plan 2020-2029 with higher "
        "funding, a free-education policy and rising enrolment; however free "
        "education is not yet anchored in the Education Act, indirect costs "
        "remain and tens of thousands of children are out of school.",
        [
            ("Papua New Guinea", "1", "84", "Education sector funding increased to K4.435 billion in 2025, representing a 12 per cent increase over the previous year"),
            ("UNESCO", "2", "36", "UNESCO reported that the Education Act did not guarantee free primary and secondary education"),
            ("Papua New Guinea", "1", "95", "approximately 53,289 primary school-aged children remained out of school in 2021"),
        ],
    ),
    "Violence against women": (
        B, "Prevent, investigate and prosecute violence against women",
        "PNG launched the costed National Strategy to Prevent and Respond to "
        "Gender-Based Violence 2026-2035 (March 2026), amended the Family "
        "Protection Act in 2022 and runs Family and Sexual Violence Units; "
        "violence remains pervasive and accountability very weak.",
        [
            ("Papua New Guinea", "1", "38", "the National Strategy to Prevent and Respond to Gender-Based Violence 2026-2035, launched by the Prime Minister in March 2026"),
            ("United Nations Population Fund; United Nations country team", "2", "44", "Accountability remained extremely weak, with conviction rates as low as 0.5% in some regions"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Fund and enforce measures against sexual and gender-based violence",
        "The GBV Strategy is to be funded at about K180 million a year, "
        "secretariats and Family and Sexual Violence Units are in place, and "
        "sorcery-accusation violence is addressed by NAPSARV 2024-2029 and "
        "new Criminal Code offences; enforcement and resourcing gaps persist.",
        [
            ("Papua New Guinea", "1", "39", "The implementation of the Strategy is to be funded at approximately K180 million per year over the next 10 years"),
            ("Papua New Guinea", "1", "42", "Amendments to the Criminal Code Act introduced new provisions (Sections 520A-520G) criminalising the activities of persons commonly known as glassman or glassmeri"),
            ("Amnesty International", "3", "47", "police lacked adequate capacity and resources to address the high rates of violence"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Establish a Paris-Principles national human rights institution",
        "Draft enabling legislation has been endorsed by the National "
        "Executive Council and a constitutional amendment is being finalised, "
        "but no institution has been established.",
        [
            ("United Nations country team", "2", "11", "draft enabling legislation endorsed by the National Executive Council"),
            ("Papua New Guinea", "1", "12", "The Government is finalizing a draft Constitutional amendment and enabling legislation to establish a national human rights institution"),
            ("Several submissions", "3", "6", "noted the absence of a National Human Rights Institution (NHRI) in line with the Principles Relating to the Status of National Human Rights Institutions"),
        ],
    ),
    "Participation of women in political & public life": (
        B, "Increase women's political participation",
        "In 2026 Parliament required parties to endorse at least 10% women "
        "candidates from the 2027 elections, with penalties; women hold under "
        "3% of seats.",
        [
            ("Papua New Guinea", "1", "32", "The amendments require all political parties to endorse at least 10% women candidates beginning with the 2027 elections"),
            ("Papua New Guinea", "1", "31", "women's representation in the National Parliament remains below 3 per cent (3 out of 118 members)"),
        ],
    ),
    "Right to health": (
        B, "Improve access to health care",
        "The National Health Plan 2021-2030 is being implemented, health "
        "financing rose from K2.5 billion (2022) to K3.2 billion (2026) and "
        "the UHC index and worker density increased; infrastructure, workforce "
        "and rural access gaps remain.",
        [
            ("Papua New Guinea", "1", "65", "the Universal Health Coverage Service Coverage Index increased from 41 in 2019 to 46 in 2023"),
            ("Papua New Guinea", "1", "67", "Health sector funding increased from approximately K2.5 billion in 2022 to K3.2 billion in 2026"),
            ("Papua New Guinea", "1", "71", "In 2023, only 54% of health posts were operational"),
        ],
    ),
    "Human rights & climate change": (
        B, "Climate adaptation and participation",
        "PNG applies the Climate Change (Management) Act 2015 and a National "
        "Adaptation Plan and enacted the Protected Areas Act 2024; the UN "
        "country team reports some progress on participation but no meaningful "
        "participation guarantee in the 2024 Act.",
        [
            ("Papua New Guinea", "1", "114", "Guided by the Climate Change (Management) Act 2015 and the National Adaptation Plan"),
            ("United Nations country team", "2", "39", "some progress in embedding participation and inclusion in climate-related policy processes"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        B, "Submit overdue treaty reports and seek assistance",
        "PNG submitted its combined second and third CRC report in 2024 and "
        "created the NMIRF in 2023, but long reporting delays persist and "
        "CEDAW and CRPD reports are outstanding.",
        [
            ("Papua New Guinea", "1", "8", "In 2024, PNG submitted its Combined Second and Third Periodic Report under the Convention on the Rights of the Child"),
            ("United Nations country team", "2", "7", "lengthy delays in reporting to the treaty bodies"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        C, "Investigate police torture and ill-treatment",
        "The police Internal Investigation Unit pre-dates the review period; "
        "new allegations of excessive force arose in 2026 and officers in the "
        "2016 student shooting case were not prosecuted.",
        [
            ("United Nations country team", "2", "16", "allegations of excessive use of force and ill-treatment by security officers in 2026"),
            ("Amnesty International", "3", "19", "the individual police officers had not been prosecuted in this case"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        C, "Access-to-information law and freedom of expression",
        "PNG has a constitutional guarantee and a Right to Information Policy "
        "but still lacks an access-to-information law, and the Cybercrime Act "
        "is used against critical expression.",
        [
            ("United Nations country team", "2", "26", "still lacked an access to information law"),
            ("JS2", "3", "27", "the use of the Cybercrime Act (2016) to silence criticism, creating a chilling effect"),
        ],
    ),
    "Discrimination against women": (
        B, "Gender equality policy and social inclusion",
        "The Gender Equality and Women's Empowerment Policy 2025-2035 was "
        "adopted and GESI approaches are applied across the public sector; "
        "barriers to women's economic participation persist.",
        [
            ("Papua New Guinea", "1", "26", "the adoption of the Gender Equality and Women's Empowerment Policy 2025-2035"),
            ("Papua New Guinea", "1", "36", "women continue to face barriers in accessing finance, markets and formal employment opportunities"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Promote the rights of persons with disabilities",
        "Parliament unanimously enacted the Disability Services Act 2025 and "
        "an Office for Disability Services is being set up; the National "
        "Disability Policy expired in 2025 and services remain concentrated in "
        "urban centres.",
        [
            ("Papua New Guinea", "1", "100", "The National Parliament unanimously enacted the Disability Services Act 2025"),
            ("Papua New Guinea", "1", "102", "The Government is working to update the National Disability Policy, which expired in 2025"),
        ],
    ),
    "Business & Human Rights": (
        C, "Develop a national action plan on business and human rights",
        "PNG only says it will consider developing a national action plan; "
        "the UN country team recommends adopting one.",
        [
            ("Papua New Guinea", "1", "139", "It will consider development of a national action plan on business and human rights"),
            ("United Nations country team", "2", "41", "recommended adopting a national action plan on business and human rights"),
        ],
    ),
    "Human rights & the environment": (
        B, "Environmental protection and large-scale projects",
        "The Protected Areas Act 2024 and environmental impact assessment "
        "systems exist, but extractive-sector concerns persist (Porgera, "
        "Wafi-Golpu, Panguna) and exploration continued in the Bismarck Sea.",
        [
            ("Papua New Guinea", "1", "109", "The Protected Areas Act 2024 establishes a national framework for the declaration, management and expansion of protected areas"),
            ("United Nations country team", "2", "41", "human rights concerns in the extractive sector persisted"),
        ],
    ),
    "Good governance & corruption": (
        B, "Strengthen the Independent Commission Against Corruption",
        "ICAC became operational in 2023 and has built cooperation with other "
        "agencies, but it faced major leadership disputes and resourcing "
        "constraints.",
        [
            ("Papua New Guinea", "1", "19", "The ICAC became operational during the reporting period"),
            ("United Nations country team", "2", "21", "faced major internal leadership disputes and system constraints"),
        ],
    ),
    "Administration of justice & fair trial": (
        B, "Expand legal aid and strengthen the justice system",
        "The Public Solicitor's Office now operates in 19 of 22 provinces "
        "(Jiwaka opened in 2025), Community Justice Centres were established "
        "and a new National and Supreme Court Complex opened; three provinces "
        "still lack an office.",
        [
            ("Papua New Guinea", "1", "119", "The Office of the Public Solicitor is currently established in 19 of the country's 22 provinces"),
            ("Papua New Guinea", "1", "120", "operationalisation of the new National and Supreme Court Complex in Port Moresby"),
        ],
    ),
    "Rights related to marriage & family": (
        C, "End child marriage and abolish exceptions to the minimum age",
        "PNG is only reviewing and harmonising the Marriage Act; the minimum "
        "age exceptions remain (16 or 14 with a court order for girls).",
        [
            ("Papua New Guinea", "1", "59", "continues to review and harmonise the legal framework relating to marriage, including the Marriage Act (Chapter 280)"),
            ("Amnesty International", "3", "50", "the age of consent for marriage remained at 16 (or 14 years with a court order) for girls"),
        ],
    ),
    "Children: protection against exploitation": (
        B, "Protect children against abuse and exploitation",
        "PNG implements the Ending Violence Against Children Roadmap and child "
        "protection procedures and set up a Special Parliamentary Committee on "
        "Children and Youth Wellbeing in 2025; child protection laws remain "
        "largely unenforced and few children are registered.",
        [
            ("Papua New Guinea", "1", "55", "The Government is implementing the national Ending Violence Against Children (EVAC) Roadmap"),
            ("Papua New Guinea", "1", "57", "The Special Parliamentary Committee on Children and Youth Wellbeing was established in 2025"),
        ],
    ),
    "Economic, social & cultural rights - general measures of implementation": (
        B, "Strengthen economic, social and cultural rights policies",
        "PNG implements Vision 2050 and the Medium-Term Development Plan IV "
        "with investments in services; implementation constraints remain.",
        [
            ("Papua New Guinea", "1", "123", "implementation of Vision 2050, the Medium-Term Development Plan IV (2023-2027) and sector-specific policies aligned with the Sustainable Development Goals"),
        ],
    ),
    "Children: juvenile justice": (
        C, "Raise the minimum age of criminal responsibility",
        "The minimum age of criminal responsibility remains 10 and PNG is "
        "only reviewing the legislation.",
        [
            ("United Nations country team", "2", "47", "the minimum age of criminal responsibility remained 10 years under the Juvenile Justice Act 2014"),
            ("Papua New Guinea", "1", "64", "continues to review legal frameworks to raise the minimum age of criminal responsibility to 14 years"),
        ],
    ),
    "Constitutional & legislative framework": (
        B, "Align forestry projects with human rights",
        "The Protected Areas Act 2024 reinforces free, prior and informed "
        "consent, but it provides no explicit human rights safeguards for "
        "forestry projects.",
        [
            ("Papua New Guinea", "1", "111", "The Protected Areas Act 2024 reinforces the principle of free, prior and informed consent"),
            ("United Nations country team", "2", "39", "or provide explicit human rights safeguards for forestry projects"),
        ],
    ),
    "Human rights education, trainings & awareness raising": (
        B, "Improve civil registration through awareness",
        "The Civil Registration and Identity Management Act 2024, online ward "
        "registration and a National Identity Programme are being scaled up.",
        [
            ("Papua New Guinea", "1", "62", "The Government is scaling up the National Identity Programme, online ward registration and linkages with maternity medical systems"),
        ],
    ),
    "2030 Agenda & other voluntary commitments": (
        B, "Address socioeconomic challenges with international assistance",
        "PNG reports its 2025 Voluntary National Review and development plans "
        "while citing resource constraints.",
        [
            ("Papua New Guinea", "1", "88", "The 2025 VNR records improvements in enrolment, gender parity and alternative learning pathways"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Implement a national human rights action plan",
        "The Strategic Plan on Human Rights 2024-2029 was launched in August "
        "2024 and a National Human Rights Policy in July 2026.",
        [
            ("Papua New Guinea", "1", "13", "the Strategic Plan on Human Rights 2024–2029 which was launched in August 2024"),
            ("Papua New Guinea", "1", "14", "In July 2026, the Government launched the National Human Rights Policy"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        B, "Birth registration for all children",
        "The Civil Registration and Identity Management Act 2024 was enacted "
        "and registration is being scaled up, but only 7% of children under "
        "five hold a birth certificate.",
        [
            ("Papua New Guinea", "1", "61", "The Government enacted the Civil Registration and Identity Management Act 2024"),
            ("United Nations country team", "2", "48", "only 7% of children under 5 years of age had a birth certificate"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        B, "Open invitation to special procedures",
        "PNG has had a standing invitation since 2011 but several visit "
        "requests remain pending and the last visit was in 2014.",
        [
            ("Papua New Guinea", "1", "10", "PNG has a standing invitation for Special Procedures since 2011"),
            ("United Nations country team", "2", "8", "several requests for country visits remained pending"),
        ],
    ),
    "International criminal & humanitarian law (including crimes against humanity, war crimes, genocide)": (
        C, "Appoint a responsibility-to-protect focal point",
        "The UN Office on Genocide Prevention repeats a recommendation made in "
        "the previous cycle; no appointment is reported.",
        [
            ("Office on Genocide Prevention and the Responsibility to Protect", "2", "12", "recommended appointing a senior-level national focal point on the responsibility to protect"),
        ],
    ),
    "Right to participate in public affairs & right to vote": (
        C, "Guarantee the integrity of electoral processes",
        "The 2022 elections were marked by violence and displacement, and "
        "preparations for 2027 are only at the planning stage.",
        [
            ("CSOLC4UPR", "3", "64", "it increased following violence associated with 2022 elections"),
            ("Papua New Guinea", "1", "140", "The Government will continue preparations for peaceful, safe, inclusive and credible 2027 national election"),
        ],
    ),
    "Refugees & asylum seekers": (
        C, "Strengthen protection of refugees and asylum-seekers",
        "UNHCR reports gaps in the national refugee framework, seven "
        "reservations to the Refugee Convention and poor detention conditions.",
        [
            ("UNHCR", "2", "57", "gaps in the national refugee framework, limited institutional capacity for asylum-seeker identification"),
        ],
    ),
}

KEYWORDS = [
    # --- treaties ---
    (r"Optional Protocol to the Convention on the Rights of the Child on the involvement", C,
     "Ratify OP-CRC-AC",
     "The UN country team recommends ratification of the Optional Protocols to the CRC; none is reported.",
     [("United Nations country team", "2", "3", "ratify the Optional Protocols to the Convention on the Rights of the Child on the involvement of children in armed conflict and on the sale of children, child prostitution and child pornography")]),
    (r"Optional Protocol to the Convention on the Elimination of All Forms of Discrimination", C,
     "Ratify OP-CEDAW",
     "PNG is still reviewing the implications of ratifying OP-CEDAW.",
     [("Papua New Guinea", "1", "7", "the Optional Protocol to CEDAW (OP-CEDAW)")]),
    (r"Take further steps to implement the Convention on the Elimination of All Forms of Discrimination", B,
     "Implement CEDAW",
     "The Gender Equality and Women's Empowerment Policy 2025-2035 and a 2026 party-candidate quota advance CEDAW implementation, but CEDAW reporting is outstanding.",
     [("Papua New Guinea", "1", "26", "the adoption of the Gender Equality and Women's Empowerment Policy 2025-2035")]),
    (r"Convention on the Rights of the Child", A,
     "Ratify the Convention on the Rights of the Child",
     "PNG is a party to the CRC and submitted its combined second and third periodic report in 2024.",
     [("Papua New Guinea", "1", "8", "In 2024, PNG submitted its Combined Second and Third Periodic Report under the Convention on the Rights of the Child")]),
    (r"Rome Statute", C,
     "Ratify the Rome Statute",
     "The Rome Statute remains unratified.",
     [("Office on Genocide Prevention and the Responsibility to Protect", "2", "6", "Papua New Guinea had yet to ratify the Rome Statute of the International Criminal Court"),
      ("JS8", "3", "3", "recommended that Papua New Guinea accede the Rome Statue of the International Criminal Court")]),
    (r"Protocol to Prevent, Suppress and Punish Trafficking", B,
     "Ratify the Palermo trafficking protocol",
     "PNG has decided to ratify the UN Convention against Transnational Organized Crime and is going through the domestic process; the Protocol remains unratified.",
     [("Papua New Guinea", "1", "49", "The Government has decided to ratify the United Nations Convention against Transnational Organized Crime")]),
    (r"Request technical support from the Office of the United Nations High Commissioner", B,
     "Request OHCHR technical support",
     "PNG welcomes OHCHR technical assistance and has hosted an OHCHR human rights adviser since 2008.",
     [("OHCHR", "2", "2", "has maintained a field presence in Papua New Guinea since 2008"),
      ("Papua New Guinea", "1", "10", "welcomes continued technical assistance from OHCHR")]),
    # --- death penalty ---
    (r"Second Optional Protocol", B,
     "Ratify the Second Optional Protocol (abolition)",
     "The death penalty was abolished in 2022-2023 but PNG is still only reviewing the implications of ratifying the Second Optional Protocol.",
     [("Papua New Guinea", "1", "118", "The Government will continue to review the implications of ratifying the Second Optional Protocol to the ICCPR")]),
    (r"awareness-raising campaigns on the death penalty", D,
     "Awareness-raising on the death penalty",
     "The documents contain no information on awareness-raising campaigns on the death penalty.", []),
    # --- equality ---
    (r"stigma and discrimination against persons affected by leprosy", B,
     "Tackle stigma against persons affected by leprosy",
     "PNG runs a National Leprosy Control Programme and a skin-disease project; progress is partial.",
     [("United Nations country team", "2", "34", "partial progress in Papua New Guinea in reducing leprosy-related stigma"),
      ("Papua New Guinea", "1", "80", "National Leprosy Control Programme")]),
    (r"combat discrimination and violence against women and children", B,
     "Combat discrimination and violence against women and children",
     "PNG adopted a gender equality policy, a GBV strategy and child protection roadmap.",
     [("Papua New Guinea", "1", "37", "the National Strategy to Prevent and Respond to GenderBased Violence 2026-2035")]),
    (r"Accede to the Convention relating to the Status of Stateless Persons", C,
     "Accede to the statelessness conventions",
     "PNG says further legal and policy review is needed on accession.",
     [("Papua New Guinea", "1", "52", "Further legal and policy review is needed on accession to the Convention relating to the Status of Stateless Persons"),
      ("United Nations country team", "2", "4", "had yet to accede to the Convention relating to the Status of Stateless Persons and the Convention on the Reduction of Statelessness")]),
    # --- education ---
    (r"Convention against Discrimination in Education", C,
     "Ratify the Convention against Discrimination in Education",
     "UNESCO encourages ratification; none is reported.",
     [("UNESCO", "2", "5", "UNESCO encouraged the ratification of the Convention against Discrimination in Education")]),
    (r"national strategy on out-of-school children", C,
     "Adopt a national strategy on out-of-school children",
     "No national strategy is reported; PNG lists school-fee support and FODE alternative pathways and acknowledges that out-of-school children remain a challenge.",
     [("Papua New Guinea", "1", "95", "out-of-school children remain a challenge")]),
    (r"children who dropped out of school due to the COVID-19", B,
     "Bring back children who dropped out because of COVID-19",
     "PNG says attendance was restored after the pandemic through awareness and community programmes, but many children remain out of school.",
     [("Papua New Guinea", "1", "94", "school attendance was restored and classes have been back to normal")]),
    (r"Provide more training and resources to schools and teachers", B,
     "Train teachers for inclusive education",
     "Teacher training on inclusive education and Special Education Resource Centres were established.",
     [("Papua New Guinea", "1", "97", "The Government has established and supported Special Education Resource Centres (SERCs) across the country")]),
    # --- health ---
    (r"Decriminalize abortion", C,
     "Decriminalise abortion",
     "A stakeholder reports abortion is highly restricted; no reform is reported.",
     [("Amnesty International", "3", "34", "abortion was highly restricted and only permitted when a woman's life was at risk")]),
    (r"sexual reproductive health|sexual and reproductive health", B,
     "Sexual and reproductive health services",
     "PNG implements a National Sexual and Reproductive Health Policy, a Family Planning Policy and an HPV vaccination programme; access remains inequitable.",
     [("Papua New Guinea", "1", "72", "implementation of the National Sexual and Reproductive Health Policy, Family Planning Policy, National Youth and Adolescent Health Policy")]),
    # --- violence / gender ---
    (r"gender policy and an action plan", A,
     "Develop a national gender policy and action plan",
     "The Gender Equality and Women's Empowerment Policy 2025-2035 and the costed GBV Strategy 2026-2035 were adopted.",
     [("Papua New Guinea", "1", "26", "the adoption of the Gender Equality and Women's Empowerment Policy 2025-2035"),
      ("Papua New Guinea", "1", "38", "The Strategy provides a properly costed framework for prevention, response, coordination and accountability")]),
    # --- torture ---
    # --- disability ---
    (r"disability authority bill", A,
     "Enact the disability bill",
     "Parliament unanimously enacted the Disability Services Act 2025.",
     [("Papua New Guinea", "1", "100", "The National Parliament unanimously enacted the Disability Services Act 2025")]),
    # --- environment / projects ---
    (r"large-scale projects meet environmental standards", C,
     "Ensure large-scale projects meet environmental standards",
     "The UN country team reports persistent extractive-sector concerns and continued exploration despite a stated moratorium.",
     [("United Nations country team", "2", "41", "exploration continued in the Bismarck Sea")]),
]

FALLBACK = (
    D, "Miscellaneous",
    "No rule matched and the evidence base contains no specific information on this recommendation.",
    [],
)
