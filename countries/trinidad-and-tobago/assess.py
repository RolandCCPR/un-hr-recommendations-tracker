"""Trinidad and Tobago — implementation assessment of its 3rd-cycle (2021,
A/HRC/49/16) UPR recommendations, graded against the 4th-cycle documentation
(session 53): OHCHR Compilation A/HRC/WG.6/53/TTO/2 and Stakeholders'
Summary /3. The National Report (/1) was not yet available at the time of
assessment, so the evidence on the State's own measures is thin.

    python scripts/run_assess.py trinidad-and-tobago

First pass for expert review. Quotes are verbatim from the documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments",
        "The documents show that CAT, ICPPED, ICRMW, the Second Optional "
        "Protocol to the ICCPR and the CRC communications procedure remain "
        "unratified and the First Optional Protocol to the ICCPR has not been "
        "re-acceded to; no ratification in the review period is reported.",
        [
            ("United Nations country team", "2", "2", "recommended that Trinidad and Tobago ratify all outstanding international human rights instruments"),
            ("Human Rights Committee", "2", "3", "recommended reacceding to the Optional Protocol to the International Covenant on Civil and Political Rights"),
            ("JS2", "3", "2", "had not ratified the Second Optional Protocol to the International Covenant on Civil and Political Rights"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Strengthen anti-trafficking law, victim protection and prosecution",
        "Trinidad and Tobago adopted a National Plan of Action, established "
        "specialised support units and shelters, improved victim "
        "identification and secured a first conviction under the Trafficking "
        "in Persons Act; prosecution rates remain low and official complicity "
        "is reported.",
        [
            ("ECLJ", "3", "15", "including the adoption of a National Plan of Action, enhanced victim identification and awareness-raising initiatives, the establishment of specialized support units and shelters"),
            ("ECLJ", "3", "15", "the first conviction secured under the Trafficking in Persons Act"),
            ("United Nations country team", "2", "27", "enforcement outcomes remained inadequate"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Implement legislation and policy against gender-based violence",
        "Cabinet approved the National Strategic Action Plan on gender-based "
        "and sexual violence (2023-2027), clinical guidelines were adopted, a "
        "central GBV registry was launched and the judiciary introduced a "
        "Gender Equality Protocol; rates remain high and enforcement and "
        "protection are weak.",
        [
            ("JS2", "3", "27", "in 2023, the Cabinet approved a National Strategic Action Plan"),
            ("United Nations country team", "2", "40", "the adoption of the 2023–2027 national strategic action plan and clinical guidelines on intimate partner violence and sexual violence"),
            ("ICAAD", "3", "28", "the judiciary had introduced the Gender Equality Protocol for Judicial Officers"),
        ],
    ),
    "Refugees & asylum seekers": (
        C, "Enact refugee legislation and an asylum procedure",
        "There is still no refugee legislation or status-determination "
        "procedure; a High Court ruling declared the Refugee Convention "
        "inapplicable (2023); an updated refugee policy and a 2026 Migration "
        "Registration Framework offer only partial progress.",
        [
            ("Human Rights Committee", "2", "53", "the absence of a comprehensive legislative and institutional framework for the protection of refugees and asylum-seekers"),
            ("United Nations experts", "2", "52", "the High Court ruling declaring the Convention relating to the Status of Refugees inapplicable in Trinidad and Tobago"),
            ("United Nations country team", "2", "51", "progress on the regularization of and school access for migrants, refugees and asylum-seekers following an updated refugee policy"),
        ],
    ),
    "Equality & non-discrimination": (
        C, "Adopt comprehensive anti-discrimination legislation",
        "There is no comprehensive anti-discrimination law; sexual "
        "orientation and gender identity are not protected grounds and the "
        "Equal Opportunity Act amendment has been pending for over a decade.",
        [
            ("Human Rights Committee", "2", "14", "did not afford full and effective protection against direct, indirect and intersectional discrimination"),
            ("ILO Committee of Experts", "2", "50", "the proposed inclusion of sexual orientation as a protected ground in the Equal Opportunity Act had remained pending for over a decade"),
        ],
    ),
    "Death penalty": (
        C, "Abolish the death penalty or establish a moratorium",
        "The mandatory death penalty for murder and treason remains, courts "
        "continue to impose death sentences, 48 people were under sentence of "
        "death in 2026 and the State told the Human Rights Committee it did not "
        "plan to consider a moratorium until violent crime was under control.",
        [
            ("Human Rights Committee", "2", "15", "the death penalty remained mandatory for murder, leading to a large number of persons on death row"),
            ("JS2", "3", "9", "domestic law retained the mandatory death penalty for murder and treason and that 48 individuals were under sentence of death as of 2026"),
            ("Human Rights Committee", "2", "15", "the State did not plan to consider abolishing the death penalty or even establishing an official moratorium until violent crime was under control"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        C, "Adopt disability legislation",
        "A persons-with-disabilities bill and national strategy are still "
        "'under development'; no comprehensive disability law exists.",
        [
            ("United Nations country team", "2", "48", "a persons with disabilities bill and a comprehensive national strategy were under development"),
            ("Committee on the Rights of Persons with Disabilities", "2", "47", "the apparent absence of comprehensive disability legislation"),
        ],
    ),
    "Conditions of detention": (
        C, "Improve prison conditions and reduce pretrial detention",
        "Conditions remain inadequate despite ongoing reforms; most prison "
        "infrastructure projects remain unfinished and remand detention is "
        "prolonged; a 2026 Parole Bill has been introduced.",
        [
            ("Human Rights Committee", "2", "18", "despite ongoing reforms, detention conditions remained inadequate"),
            ("JS2", "3", "10", "most prison infrastructure projects remained unfinished despite significant public expenditure"),
            ("United Nations country team", "2", "18", "the 2026 Parole Bill sought to introduce an early release system"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        C, "Establish a Paris-Principles national human rights institution",
        "No compliant institution exists; there is no clarity or progress on "
        "converting the Equal Opportunity Commission.",
        [
            ("Human Rights Committee", "2", "7", "there was a lack of clarity and progress on plans to convert the Commission into a national human rights institution"),
            ("QuFo; JS4; JS5", "3", "5", "the continued absence of an independent National Human Rights Institution (NHRI) compliant with the Paris Principles"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        C, "Legalise abortion and expand sexuality education",
        "Abortion remains criminalised except to save the woman's life and "
        "the State has no intention to modify the law; implementation gaps "
        "persist in sexual and reproductive health services.",
        [
            ("Human Rights Committee", "2", "44", "abortion continued to be criminalized, except when there was a direct threat to the woman’s life"),
            ("United Nations country team", "2", "32", "implementation gaps persisted"),
        ],
    ),
    "Human rights & climate change": (
        B, "Climate policy and participation",
        "Trinidad and Tobago adopted a National Climate Change Policy, "
        "submitted its second NDC and strengthened disaster preparedness; "
        "participation of marginalised groups remains limited.",
        [
            ("United Nations country team", "2", "37", "the adoption of the National Climate Change Policy, the submission of the second nationally determined contribution and strengthened disaster preparedness"),
            ("United Nations country team", "2", "37", "the limited participation of marginalized groups"),
        ],
    ),
    "Right to health": (
        B, "Strengthen health services including HIV/AIDS",
        "Sexual and reproductive health services are integrated into "
        "universal health coverage and maternal, neonatal and infant mortality "
        "fell; HIV prevention remains insufficient for key populations.",
        [
            ("Christian Council International", "3", "20", "reported progress in reducing maternal, neonatal and infant mortality and noted universal skilled birth attendance"),
            ("JS5", "3", "19", "prevention measures remained insufficient, particularly for key populations"),
        ],
    ),
    "Violence against women": (
        B, "Protect women from violence and strengthen services",
        "Specialised police mechanisms, a central GBV registry and the "
        "Domestic Violence Act exist; underreporting, resource constraints and "
        "weak protection-order enforcement persist.",
        [
            ("United Nations country team", "2", "39", "specialized mechanisms within the police service and the launch of the Central Registry on Gender-based Violence (Umbono System)"),
            ("Human Rights Committee", "2", "43", "emergency protection orders reportedly could not be granted to persons of the same sex as the perpetrator"),
        ],
    ),
    "Children: definition": (
        B, "Child protection legislation and policy",
        "The Human Rights Committee notes efforts to abolish child marriage, "
        "raise the minimum marriage age to 18 and prohibit corporal "
        "punishment in schools; the national child policy implementation "
        "plan is not reported.",
        [
            ("Human Rights Committee", "2", "45", "noting efforts to abolish child marriage, raise the minimum marriage age to 18 and prohibit the corporal punishment of children in schools"),
        ],
    ),
    "Right to education": (
        B, "Strengthen access to quality education",
        "Education is free and compulsory with almost universal access; "
        "retention challenges, early pregnancy and below-benchmark spending "
        "persist.",
        [
            ("UNESCO", "2", "33", "the Education Act provided for non-discrimination in education and guaranteed free, compulsory schooling"),
            ("United Nations country team", "2", "34", "access to education was almost universal, retention challenges persisted"),
        ],
    ),
    "Human rights education, trainings & awareness raising": (
        B, "Human rights training for officials",
        "Capacity-building for law enforcement and public officials was "
        "delivered through UN technical assistance but is project-dependent "
        "and not institutionalised.",
        [
            ("United Nations country team", "2", "10", "human rights training remained project-dependent and was not systematically institutionalized"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Improve living standards and social programmes",
        "Trinidad and Tobago has a comprehensive social protection system, "
        "but poverty remains multidimensional and uneven.",
        [
            ("United Nations country team", "2", "31", "poverty remained multidimensional and uneven, affecting 41.6% of children"),
        ],
    ),
    "Children: protection against exploitation": (
        C, "Prohibit child marriage and eliminate child labour",
        "The ILO Committee of Experts urges adoption of the list of hazardous "
        "work for children, pending since 2004; the minimum marriage age was "
        "raised to 18.",
        [
            ("ILO Committee of Experts", "2", "46", "to ensure the adoption in the very near future of the list of hazardous types of work prohibited to children under 18 years of age"),
        ],
    ),
    "Advancement of women": (
        B, "Promote gender parity and women's empowerment",
        "Women's representation increased in government, local government, "
        "the judiciary and law enforcement (including the first woman Police "
        "Commissioner); women remain under-represented in senior decision-making.",
        [
            ("Human Rights Committee", "2", "42", "welcomed the measures to increase the representation of women in political life"),
            ("ICAAD", "3", "30", "the appointment of the first female Commissioner of Police"),
        ],
    ),
    "Constitutional & legislative framework": (
        C, "Harmonise national legislation with international commitments",
        "Gaps remain between domestic law and the ICCPR, and reservations "
        "remain in force.",
        [
            ("Human Rights Committee", "2", "6", "gaps remained between the domestic legal framework and the International Covenant on Civil and Political Rights"),
        ],
    ),
    "Right to social security": (
        B, "Strengthen the social protection network",
        "Social protection programmes provide financial, food and housing "
        "support but remain inadequate and poorly targeted.",
        [
            ("United Nations country team", "2", "30", "social protection programmes provided for financial, food and housing support, they remained inadequate"),
        ],
    ),
    "Human rights & poverty": (
        B, "Strengthen poverty-eradication institutions",
        "Social welfare policies exist but poverty remains multidimensional.",
        [
            ("United Nations country team", "2", "31", "a comprehensive social protection system"),
        ],
    ),
    "Migrants": (
        C, "Harmonise the Immigration Act and end pretrial custody of migrants",
        "Discriminatory immigration provisions remain and irregular entrants "
        "are detained without clear limits.",
        [
            ("Human Rights Committee", "2", "14", "discriminatory provisions in immigration law"),
        ],
    ),
    "Good governance & corruption": (
        B, "Curb corruption and strengthen transparent procurement",
        "The Human Rights Committee welcomed steps to prevent and combat "
        "corruption, but the whistle-blower protection bill is delayed and "
        "enforcement is weak.",
        [
            ("Human Rights Committee", "2", "9", "welcomed the steps taken to prevent and combat corruption among persons exercising public functions"),
            ("Human Rights Committee", "2", "9", "delays in adopting the whistle-blower protection bill"),
        ],
    ),
    "Rule of law & impunity": (
        C, "Investigate unlawful killings by police",
        "Investigations of police misconduct face significant delays; an "
        "estimated 55 police killings occurred in 2025.",
        [
            ("Human Rights Committee", "2", "17", "significant delays in investigations into serious police misconduct, which had yielded limited results"),
            ("United Nations country team", "2", "21", "An estimated 55 police killings had occurred in 2025"),
        ],
    ),
    "Right to life": (
        C, "Combat violent crime while respecting rights",
        "Violent crime remains high; repeated States of Emergency since 2024 "
        "have expanded police powers and are reported not to be yielding results.",
        [
            ("United Nations country team", "2", "17", "there continued to be high levels of violent crime in Trinidad and Tobago"),
            ("JS4", "3", "4", "State of Emergency had been repeatedly in effect"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        D, "Open, merit-based selection of treaty-body candidates",
        "The documents contain no information on this ask.", [],
    ),
    "Right to development": (
        D, "Promote infrastructure and rural development",
        "The documents contain no information on this ask.", [],
    ),
    "Business & Human Rights": (
        D, "Implement the Guiding Principles on Business and Human Rights",
        "The documents contain no information on this ask.", [],
    ),
    "Discrimination against women": (
        C, "Adopt a comprehensive definition of discrimination against women",
        "CEDAW identifies shortcomings in the definition of discrimination "
        "against women; no amendment is reported.",
        [
            ("Committee on the Elimination of Discrimination against Women", "2", "38", "shortcomings in the definition of discrimination against women"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        C, "Extend a standing invitation to special procedures",
        "No standing invitation has been extended and no country visit has "
        "taken place.",
        [
            ("United Nations country team", "2", "5", "had not extended a standing invitation to the special procedure mandate holders and had not hosted a country visit"),
        ],
    ),
    "Cooperation & follow up with the Universal Periodic Review (UPR)": (
        D, "Strengthen implementation and monitoring of UPR recommendations",
        "The documents contain no information on this ask.", [],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        D, "Establish a permanent national mechanism for reporting and follow-up",
        "The documents contain no information on this ask.", [],
    ),
    "Right to adequate housing": (
        D, "Fulfil the rights to housing and health",
        "The documents contain no information on this ask.", [],
    ),
}

KEYWORDS = [
    # --- ratification-cluster specifics ---
    (r"Optional Protocol to the Convention on the Elimination of All Forms of Discrimination|Optional Protocols to the Convention on the Rights of the Child on the involvement", D,
     "Ratify OP-CEDAW / OPs to the CRC",
     "The documents contain no information on the status of these protocols.", []),
    (r"Request technical support from OHCHR", D,
     "Request OHCHR support for ratification",
     "The documents contain no information on a request for OHCHR support.", []),
    (r"awareness-raising campaigns on the death penalty|Promote a public debate", D,
     "Awareness-raising and public debate on the death penalty",
     "The documents contain no information on awareness-raising or public debate on the death penalty.", []),
    # --- same-sex relations: recriminalised in 2025 (regression) ---
    (r"same-sex|sections 13 and 16|consensual sexual relations", E,
     "Decriminalise consensual same-sex relations",
     "Consensual same-sex relations were re-criminalised in 2025 when the "
     "Court of Appeal reinstated sections 13 and 16 of the Sexual Offences "
     "Act, overturning the 2018 ruling; the Government maintained that the "
     "question rested with the Privy Council.",
     [("United Nations country team", "2", "49", "heightened concerns following the recriminalization of consensual same-sex relations in March 2025"),
      ("JS5", "3", "8", "following the 2025 Court of Appeal decision criminalizing same-sex sexual relations between adults that overturned the 2018 High Court ruling")]),
    (r"Equal Opportunity|sexual orientation, gender identity and living with HIV|sexual orientation and gender", C,
     "Prohibit discrimination on grounds of sexual orientation and gender identity",
     "Sexual orientation and gender identity are still not protected grounds; the Equal Opportunity Act amendment has been pending for over a decade.",
     [("ILO Committee of Experts", "2", "50", "the proposed inclusion of sexual orientation as a protected ground in the Equal Opportunity Act had remained pending for over a decade")]),
    (r"equal pay for work of equal value|gender wage gap", C,
     "Equal pay for work of equal value",
     "The Employment Standards Bill, needed to enshrine equal pay, has not been adopted.",
     [("ILO Committee of Experts", "2", "29", "swift adoption of the Employment Standards Bill")]),
    # --- gender / violence ---
    (r"national strategic action plan to end sexual and gender", B,
     "Adopt the national gender policy and the national strategic action plan",
     "The National Strategic Action Plan on gender-based and sexual violence 2023-2027 was approved by Cabinet; the status of a national gender policy is not reported and CEDAW notes delays in adopting gender equality frameworks.",
     [("JS2", "3", "27", "in 2023, the Cabinet approved a National Strategic Action Plan")]),
    # --- detention ---
    (r"Review and update the Miscellaneous Provisions \(Prisons\) Act", C,
     "Review and update the Prisons Act 2014",
     "JS2 recommends the review; no update is reported.",
     [("JS2", "3", "10", "reviewing and updating the Miscellaneous Provisions (Prisons) Act, 2014")]),
    (r"Strengthen the criminal justice system and improve the situation in prisons|reforms to the judicial and penitentiary system", B,
     "Reform the criminal justice and penitentiary system",
     "Reforms are ongoing and a 2026 Parole Bill has been introduced, but delays and overcrowding persist.",
     [("United Nations country team", "2", "18", "the 2026 Parole Bill sought to introduce an early release system with structured supervision")]),
    # --- SRHR ---
    (r"Provide effective access for women to comprehensive information and services on sexual and reproductive", B,
     "Access to sexual and reproductive health information and services",
     "Services are integrated into universal health coverage under the National Sexual and Reproductive Health Policy, with gaps in implementation.",
     [("United Nations country team", "2", "32", "sexual and reproductive health and rights services were integrated into universal health coverage, pursuant to the National Sexual and Reproductive Health Policy")]),
    # --- children ---
    (r"national child p|white paper", D,
     "Adopt the national child policy",
     "The documents contain no information on the national child policy or its implementation plan.", []),
    (r"child labour", C,
     "Prevent and eliminate child labour",
     "The list of hazardous work prohibited to children has been pending since 2004.",
     [("ILO Committee of Experts", "2", "46", "to ensure the adoption in the very near future of the list of hazardous types of work prohibited to children under 18 years of age")]),
    # --- institutions ---
    (r"Special Reserve Police and Municipal Police Complaints Authority", D,
     "Enact the police complaints authority bill",
     "The documents contain no information on enactment of this bill; the Police Complaints Authority is reported to have limited powers and resources.", []),
    (r"migrants, asylum seekers and refugees|Ensure that all children, including migrants", B,
     "Access to education and services for migrant and refugee children",
     "School access for migrants, refugees and asylum-seekers progressed following an updated refugee policy.",
     [("United Nations country team", "2", "51", "progress on the regularization of and school access for migrants, refugees and asylum-seekers following an updated refugee policy")]),
    (r"Ensure the rights granted to asylum seekers|non-refoulement|guarantee the effective protection of migrants", C,
     "Protect asylum-seekers and migrants",
     "No refugee legislation exists; UN experts warned of deportations and the Human Rights Committee of harmful detention practices.",
     [("Human Rights Committee", "2", "53", "increasing numbers of deportations of individuals seeking international protection and harmful detention practices affecting adults and children")]),
]

FALLBACK = (
    D, "Miscellaneous",
    "No rule matched and the evidence base contains no specific information on this recommendation.",
    [],
)
