"""Samoa — implementation assessment of its 3rd-cycle (2021, A/HRC/49/7)
UPR recommendations, graded against the 4th-cycle documentation (session 53):
OHCHR Compilation A/HRC/WG.6/53/WSM/2 and Stakeholders' Summary /3. Samoa's
National Report (/1) was not yet available at the time of assessment, so the
evidence base is thin on the State's own account and many asks are graded D.

    python scripts/run_assess.py samoa

First pass for expert review. Quotes are verbatim from the documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments",
        "The documents show that several core treaties and protocols remain "
        "unratified (ICESCR, ICERD, ICRMW, the Optional Protocols to the "
        "ICCPR, the CAT and the CRPD) and no ratification in the review period "
        "is reported.",
        [
            ("Committee on Enforced Disappearances; United Nations country team", "2", "2", "recommended that Samoa ratify the International Covenant on Economic, Social and Cultural Rights and the International Convention on the Elimination of All Forms of Racial Discrimination"),
            ("OMB/NHRI", "3", "2", "recommended that Samoa ratify and incorporate into domestic law ICERD, ICESCR, ICRMW, ICCPR-OP 1, ICCPR-OP 2"),
        ],
    ),
    "Equality & non-discrimination": (
        C, "Adopt comprehensive anti-discrimination protection",
        "Samoa has no comprehensive constitutional or statutory prohibition of "
        "discrimination; the NHRI, a disability organisation and the CRPD "
        "Committee all call for it, and no measure is reported.",
        [
            ("OMB/NHRI", "3", "15", "Samoa's Constitution did not include a comprehensive definition of gender equality or explicitly prohibited discrimination based on gender, sexual orientation, disability or HIV status"),
            ("Committee on the Rights of Persons with Disabilities", "2", "14", "recommended that Samoa explicitly recognize disability among prohibited grounds of discrimination"),
        ],
    ),
    "Right to health": (
        B, "Strengthen health services and access",
        "Samoa strengthened primary health care, expanded surveillance and "
        "targeted immunization recovery and has a Health Sector Plan "
        "2021-2025; however the 2025 dengue outbreak strained the system, "
        "health workers fell in number and rural access remains uneven.",
        [
            ("United Nations country team", "2", "45", "Samoa had advanced the right to health through strengthened primary healthcare, expanded surveillance and targeted immunization recovery"),
            ("JS2", "3", "47", "the Samoa Health Sector Plan 2021–2025 set out a comprehensive framework to strengthen service delivery, improve access to care, and enhance health system performance"),
            ("OMB/NHRI", "3", "7", "The number of doctors and nurses working in hospitals dropped between 2024–2025"),
        ],
    ),
    "Right to physical & moral integrity": (
        B, "Prevent and respond to domestic and gender-based violence",
        "The NHRI commends dedicated policies and strategies against "
        "gender-based and family violence, and a national prevention framework "
        "exists, but prevention is under-resourced and unevenly implemented "
        "and violence remains pervasive.",
        [
            ("OMB/NHRI", "3", "16", "commending Samoa on implementation of dedicated policies and strategies to combat GBV and family violence"),
            ("United Nations country team", "2", "61", "prevention efforts were underresourced and unevenly implemented"),
        ],
    ),
    "Violence against women": (
        C, "Legislate against and respond to violence against women",
        "The Crimes Act 2013 and Family Safety Act 2013 pre-date the review "
        "period; implementation is uneven, the NHRI asks for amendment of the "
        "Family Safety Act, and survivor services remain under-funded.",
        [
            ("ICAAD", "3", "30", "the implementation of these legislative reforms had been uneven and undermined by the continued reliance on customary practices to mitigate sentences in GBV cases"),
            ("OMB/NHRI", "3", "17", "recommended Samoa to amend the Family Safety Act 2013 to include economic violence and coercive control in the definition of violence"),
            ("JS3", "3", "61", "survivors of domestic and gender-based violence faced barriers in reporting abuse and accessing protection services"),
        ],
    ),
    "Children: definition": (
        C, "Strengthen child protection and legislation",
        "The Child Protection Bill remains pending, parents retain a legal "
        "right to 'reasonable punishment' and the legal definition of the "
        "child is not harmonised.",
        [
            ("United Nations country team", "2", "65", "the adoption of the Child Protection Bill remained pending"),
            ("OMB/NHRI", "3", "10", "parents had a legal right to administer 'reasonable punishment' to their children"),
        ],
    ),
    "Human rights & climate change": (
        D, "Mainstream human rights in climate action",
        "The documents contain no information on measures taken by Samoa on "
        "this ask.",
        [],
    ),
    "Discrimination against women": (
        C, "Increase women's participation and equality",
        "Women remain under-represented in parliament, Cabinet and local "
        "governance, and village by-laws restrict access to matai titles, an "
        "eligibility requirement for Parliament.",
        [
            ("United Nations country team", "2", "60", "women remained underrepresented in the parliament, Cabinet, State-owned enterprises and local governance structures"),
            ("OMB/NHRI", "3", "18", "some villages had by-laws and cultural practices that restricted women's access to matai titles"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        C, "Adopt disability legislation and inclusion measures",
        "A disability bill is still awaited and the CRPD Committee finds no "
        "comprehensive legal and policy framework; a disability organisation "
        "reports a legal vacuum and inaccessible justice.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "70", "the absence of a comprehensive and coherent legal and policy framework to give full effect to the Convention on the Rights of Persons with Disabilities"),
            ("NOLA", "3", "28", "Samoa lacked a comprehensive and enforceable legal framework for disability rights"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Social protection and living standards",
        "Old-age and disability pensions were increased in late 2025, but "
        "Samoa has not established a social protection floor.",
        [
            ("OMB/NHRI", "3", "5", "Pensions were available to the elderly and persons with disabilities, both of which had increased in late 2025"),
            ("OMB/NHRI", "3", "5", "Samoa had not established a social protection floor"),
        ],
    ),
    "Constitutional & legislative framework": (
        C, "Align domestic law with international commitments",
        "The CRPD and CED Committees find domestic law not aligned with the "
        "Conventions and the NHRI says much work remains to integrate CRPD "
        "obligations; no harmonising measure is reported.",
        [
            ("OMB/NHRI", "3", "19", "much work remained to be done to integrate Samoa's obligations under the CRPD into domestic constitutional and legal frameworks"),
            ("Committee on Enforced Disappearances", "2", "11", "called upon Samoa to incorporate the International Convention for the Protection of All Persons from Enforced Disappearance into domestic legislation"),
        ],
    ),
    "Administration of justice & fair trial": (
        D, "Judicial independence and training of law-enforcement officials",
        "The documents contain no information on measures by Samoa on this ask; "
        "the United Nations country team only recommends strengthening "
        "judicial independence.",
        [],
    ),
    "Right to education": (
        B, "Strengthen access to quality and universal education",
        "Samoa provides free primary and secondary schooling and is "
        "implementing the Education Sector Plan 2025-2030, but hidden costs, "
        "rural disparities and the absence of an enforceable right to "
        "inclusive education persist.",
        [
            ("JS2", "3", "52", "Samoa's commitment to ensuring inclusive and equitable education, including the provision of free primary and secondary schooling and ongoing reforms under the Education Sector Plan 2025–2030"),
            ("NOLA", "3", "70", "there was no enforceable legal guarantee of inclusive education in Samoa"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        B, "Cooperate with OHCHR and request technical support",
        "An OHCHR Human Rights Adviser has been part of the Resident "
        "Coordinator multi-country office in Samoa since 2022, and Samoa "
        "engaged with the CRPD and CED Committees; the initial CAT report "
        "remains overdue.",
        [
            ("OHCHR", "2", "9", "An OHCHR Human Rights Adviser has been part of the Resident Coordinator multi-country office in Samoa since 2022"),
            ("United Nations country team", "2", "5", "the initial report of Samoa to the Committee against Torture remained overdue"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        C, "Resource the Office of the Ombudsman / NHRI",
        "The Office of the Ombudsman retains A status but is constrained by "
        "budget and staff limits and has had no appointed Ombudsman since "
        "2023.",
        [
            ("OMB/NHRI", "3", "3", "The work of the OMB/NHRI continued to be challenged by budgetary and human resource limitations"),
            ("United Nations country team", "2", "16", "there had not been an officially appointed Ombudsman in Samoa since 2023"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        C, "Strengthen anti-trafficking law and enforcement",
        "Samoa has no stand-alone trafficking law or national action plan and "
        "there is little data; no measure is reported.",
        [
            ("Committee on Enforced Disappearances", "2", "41", "the Crimes Act 2013 did not include comprehensive anti-trafficking provisions and the State did not have stand-alone legislation and a national action plan on trafficking in persons"),
        ],
    ),
    "Children: juvenile justice": (
        C, "Raise the age of criminal responsibility",
        "The age of criminal responsibility remains 10 years and no change is "
        "reported.",
        [
            ("OMB/NHRI", "3", "11", "the age of criminal responsibility was 10 years and recommended that Samoa raise the age of criminal responsibility to at least 14 years of age"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        B, "Submit overdue treaty-body reports",
        "Samoa has been reviewed by the Committee on Enforced Disappearances "
        "and the CRPD Committee; its initial report to the Committee against "
        "Torture is still overdue.",
        [
            ("United Nations country team", "2", "5", "the initial report of Samoa to the Committee against Torture remained overdue"),
        ],
    ),
    "Inter-State cooperation and assistance": (
        D, "Seek international assistance on climate and COVID-19",
        "The documents contain no information on this ask.", [],
    ),
    "Right to development": (
        D, "Operationalize the national development plan",
        "The documents contain no information on this ask.", [],
    ),
    "Human rights & the environment": (
        D, "Human-rights-based approaches in environmental policy",
        "The documents contain no information on measures by Samoa on this ask.", [],
    ),
    "Right to social security": (
        B, "Establish a State-sponsored social welfare system",
        "Pensions for older persons and persons with disabilities were "
        "increased in late 2025, but there is no social protection floor.",
        [
            ("OMB/NHRI", "3", "5", "Pensions were available to the elderly and persons with disabilities, both of which had increased in late 2025"),
            ("OMB/NHRI", "3", "5", "Samoa had not established a social protection floor"),
        ],
    ),
    "Economic & political crisis, natural disasters or other emergencies": (
        D, "Rights-based approach in disaster planning",
        "The documents contain no information on this ask.", [],
    ),
    "Trade union rights": (
        D, "Guarantee workers' rights and freedom of association",
        "The documents contain no information on this ask.", [],
    ),
    "Business & Human Rights": (
        D, "Adopt a national action plan on business and human rights",
        "The documents contain no information on this ask.", [],
    ),
}

KEYWORDS = [
    (r"Second Optional Protocol|abolish the death penalty|death penalty", C,
     "Abolish the death penalty / ratify the Second Optional Protocol",
     "Samoa has not ratified the Second Optional Protocol and the "
     "Constitution still retains the death penalty.",
     [("JS1; CGNK", "3", "23", "recommended Samoa to ratify ICCPR-OP 2"),
      ("CGNK", "3", "29", "regretted that Samoa still retains the death penalty in its constitution")]),
    (r"awareness-raising campaigns on the death penalty", D,
     "Awareness-raising on the death penalty",
     "The documents contain no information on this ask.", []),
    (r"Optional Protocol to the Convention against Torture", C,
     "Ratify OP-CAT",
     "Several bodies recommended ratification of the OP-CAT; no ratification is reported.",
     [("Committee on the Rights of Persons with Disabilities, Committee on Enforced Disappearances and United Nations country team", "2", "2", "recommended that Samoa ratify the Optional Protocol to the Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment")]),
    (r"Forced Labour Convention|Protocol of 2014", D,
     "Ratify the 2014 Protocol to the ILO Forced Labour Convention",
     "The documents contain no information on this ask.", []),
    (r"Protocol to Prevent, Suppress and Punish Trafficking", C,
     "Ratify the Palermo trafficking protocol",
     "The NHRI and civil society urge ratification of the Protocol; none is reported.",
     [("ECLJ", "3", "25", "urged Samoa to ratify the Protocol to Prevent, Suppress and Punish Trafficking in Persons Especially Women and Children")]),
    (r"Prevention and Punishment of the Crime of Genocide", C,
     "Ratify the Genocide Convention",
     "A civil-society submission recommends ratification; none is reported.",
     [("CGNK", "3", "24", "nothing hindered the ratification of the Convention on the Prevention and Punishment of the Crime of Genocide")]),
    (r"Optional Protocol to the Convention on the Elimination of All Forms of Discrimination against Women", D,
     "Ratify the Optional Protocol to CEDAW",
     "The documents contain no information on this ask.", []),
    (r"^Continue to implement effective measures to further promote and protect human rights", B,
     "Continue implementing measures to promote and protect human rights",
     "Samoa engaged with the CRPD and CED Committees and hosts an OHCHR Human Rights Adviser; the documents also record the ratification gaps above.",
     [("OHCHR", "2", "9", "An OHCHR Human Rights Adviser has been part of the Resident Coordinator multi-country office in Samoa since 2022")]),
    (r"same-sex|sexual relations between men|consensual sexual relations|consenting adults|sections 67, 68", C,
     "Decriminalize consensual same-sex relations",
     "The Crimes Act 2013 still criminalises consensual same-sex relations.",
     [("JS3", "3", "72", "the Crimes Act 2013 criminalized consensual same-sex relations")]),
    (r"trans persons|transgender", D,
     "Health needs of trans persons",
     "The documents contain no information on this ask.", []),
    (r"abortion|voluntary interruption of pregnancy", C,
     "Decriminalize abortion",
     "Abortion remains unlawful outside narrow statutory exceptions.",
     [("United Nations country team", "2", "46", "pursuant to the Crimes Act 2013, abortion was illegal unless it was performed to preserve the mother's life, physical or mental health")]),
    (r"family life education curriculum|comprehensive sexuality education|sexual (and )?reproductive health", B,
     "Sexual and reproductive health policy and education",
     "Family Life Education is delivered in schools and a National Sexual and "
     "Reproductive Health Policy exists, but its content has not been aligned "
     "with international technical guidance.",
     [("SFHA", "3", "48", "appreciated efforts by the Ministry of Education, Sports and Culture in delivering Family Life Education in schools, but expressed concerns that its implementation and contents may have not followed the UN International Technical Guidelines on Sexuality Education")]),
    (r"Mental Health Act", C,
     "Review the Mental Health Act",
     "The mental health legislation remains non-compliant with the CRPD.",
     [("NOLA", "3", "46", "mental health legislation remained non-compliant with human rights standards")]),
    (r"maternal mortality", D,
     "Reduce maternal mortality", "The documents contain no information on this ask.", []),
    (r"national referral system|Inter-agency", C,
     "Establish a national referral system for survivors of violence",
     "A civil-society organisation reiterates the recommendation to implement the Essential Services Guide; no system is reported.",
     [("SFHA", "3", "50", "reiterated its recommendation that Samoa should implement the “Inter-Agency Essential Services Guide” to establish a national referral system for survivors of violence")]),
    (r"corporal punishment", C,
     "Prohibit corporal punishment",
     "The Infants Ordinance 1961 still permits 'reasonable punishment' and corporal punishment is not prohibited in all settings.",
     [("CCI", "3", "65", "the Infants Ordinance 1961 permitted “reasonable punishment” by parents and caregivers")]),
    (r"minimum legal age for marriage|age of marriage|marriage as 18", B,
     "Set the minimum marriage age at 18",
     "A legislative reform set the minimum age at 18, but marriage of minors with one parent's consent may still occur under the Marriage Ordinance 1961.",
     [("CCI", "3", "39", "the legal minimum age of marriage in Samoa was 18 years for both males and females, following legislative reform"),
      ("OMB/NHRI", "3", "13", "marriage of minors under 18 years may occur with the consent of one parent or guardian")]),
    (r"Child Care and Protection Bill", C,
     "Adopt the Child Care and Protection Bill",
     "The bill's adoption remained pending.",
     [("United Nations country team", "2", "65", "the adoption of the Child Protection Bill remained pending")]),
    (r"child labour", C,
     "Enforce child-labour law",
     "A low minimum working age and the absence of laws against use of children in illicit activities persist.",
     [("OMB/NHRI", "3", "12", "the low minimum working age and lack of laws prohibiting use of children in illicit activities increased vulnerability to trafficking and exploitation")]),
    (r"age of criminal responsibility", C,
     "Raise the age of criminal responsibility",
     "The age of criminal responsibility remains 10 years.",
     [("OMB/NHRI", "3", "11", "the age of criminal responsibility was 10 years")]),
    (r"all climate change policies consider the needs|meaningful participation of women, children, persons with disabilities|involvement of vulnerable groups", C,
     "Include vulnerable groups in climate policy",
     "The CRPD Committee reports limited participation of persons with disabilities in climate policymaking.",
     [("Committee on the Rights of Persons with Disabilities", "2", "59", "the limited participation of persons with disabilities in climate change policymaking")]),
    (r"disaster risk reduction", C,
     "Disaster risk reduction policy",
     "Disaster management rests on the pre-existing Disaster and Emergency Management Act 2007 and National Disaster Management Plan, which the CRPD Committee says are not disability-inclusive.",
     [("Committee on the Rights of Persons with Disabilities", "2", "59", "mainstream disability into all climate policies and plans, including the Disaster and Emergency Management Act 2007 and the National Disaster Management Plan")]),
    (r"hidden costs", C,
     "Remove hidden costs of education",
     "Hidden costs (transport, uniforms, materials) persist, especially in rural areas.",
     [("JS2", "3", "52", "hidden costs including transportation, uniforms, learning materials, and other school-related expenses")]),
    (r"students with disabilities|universal access to education", C,
     "Inclusive education for students with disabilities",
     "There is no enforceable legal guarantee of inclusive education.",
     [("NOLA", "3", "70", "there was no enforceable legal guarantee of inclusive education in Samoa")]),
    (r"Ombudsman", C,
     "Resource the Office of the Ombudsman",
     "The Office is under-resourced and the Ombudsman post has been vacant since May 2023.",
     [("OMB/NHRI", "3", "3", "the position of Ombudsman remained vacant since May 2023")]),
    (r"State of Human Rights Report", D,
     "Follow up the State of Human Rights Report 2015", "The documents contain no information on this ask.", []),
    (r"overdue reports", B,
     "Submit overdue treaty-body reports",
     "Samoa was reviewed by the CED and the CRPD Committee; its initial CAT report is still overdue.",
     [("United Nations country team", "2", "5", "the initial report of Samoa to the Committee against Torture remained overdue")]),
    (r"independence of the judici", D,
     "Judicial independence", "The documents contain no information on measures by Samoa on this ask.", []),
    (r"human rights training for law enforcement", D,
     "Human-rights training for law-enforcement officials", "The documents contain no information on this ask.", []),
    (r"women in rural areas|rural areas", B,
     "Improve health care in rural areas",
     "The country team notes strengthened primary health care but calls for more rural health personnel and services.",
     [("United Nations country team", "2", "45", "making more health personnel available in rural areas and increasing access to services in rural areas")]),
    (r"decriminaliz.*defamation|freedom of expression", C,
     "Freedom of expression", "Defamation remains criminalised and freedom of expression and access to information are narrowing.",
     [("OMB/NHRI", "3", "21", "freedom of expression and access to information were further narrowing in Samoa")]),
]

FALLBACK = (
    D, "Miscellaneous",
    "No rule matched and the evidence base contains no specific information on this recommendation.",
    [],
)
