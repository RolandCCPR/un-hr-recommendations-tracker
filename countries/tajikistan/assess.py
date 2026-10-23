"""Tajikistan — implementation assessment of its 3rd-cycle (2021, A/HRC/49/12)
UPR recommendations, graded against the 4th-cycle documentation (session 53):
National Report A/HRC/WG.6/53/TJK/1, OHCHR Compilation /2 and Stakeholders'
Summary /3.

    python scripts/run_assess.py tajikistan

First pass for expert review. Quotes are verbatim from the three documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Constitutional & legislative framework": (
        B, "Bring legislation into line with international human rights obligations",
        "Tajikistan adopted the Equality and Elimination of All Forms of "
        "Discrimination Act (2022), a new Rights and Social Protection of "
        "Persons with Disabilities Act (2026), amended the Domestic Violence "
        "Act (2024), aligned the torture definition with the Convention "
        "against Torture and adopted new counter-terrorism and "
        "counter-extremism acts; the Criminal Code reform remains in draft.",
        [
            ("Tajikistan", "1", "30", "On 19 July 2022, the Equality and Elimination of All Forms of Discrimination Act was adopted"),
            ("Tajikistan", "1", "30", "a new Rights and Social Protection of Persons with Disabilities Act was adopted, introducing the human rights model of disability"),
            ("Tajikistan", "1", "62", "New versions of the Counter-Terrorism Act of December 2021"),
        ],
    ),
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments",
        "No ratification of the instruments in question is reported; the UN "
        "country team and UNESCO continue to recommend ratification.",
        [
            ("United Nations country team", "2", "2", "recommended that Tajikistan ratify outstanding international human rights instruments"),
            ("UNESCO", "2", "4", "recommended that Tajikistan ratify the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        C, "Guarantee freedom of expression and media freedom",
        "Tajikistan amended articles 179(3) and 307(1) of the Criminal Code "
        "(May 2025) to remove penalties for 'liking' extremist content; "
        "stakeholders report a steep deterioration of press freedom and a "
        "narrowing of civic space.",
        [
            ("United Nations country team", "2", "39", "Tajikistan had amended legislation to remove criminal penalties for “liking” social media content deemed extremist"),
            ("HFHR PCP", "3", "50", "an ongoing narrowing of civic space marked by growing restrictions on freedom of expression, association and assembly"),
        ],
    ),
    "Right to education": (
        B, "Expand access to quality and inclusive education",
        "Tajikistan extended compulsory schooling to 11 years (2024), adopted "
        "the Policy Framework for Inclusive Education up to 2045, a "
        "preschool development programme 2026-2030 and opened 212 new "
        "educational facilities in 2023.",
        [
            ("Tajikistan", "1", "164", "completing full general secondary education (11 years) became compulsory for everyone"),
            ("Tajikistan", "1", "165", "The Policy Framework for Inclusive Education for the period up to 2045"),
            ("United Nations country team", "2", "67", "compulsory schooling extended to 11 years"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Adopt and implement national human rights and development plans",
        "A national action plan 2023-2026 was approved by presidential decree "
        "and an updated CEDAW action plan 2025-2032 is being implemented; the "
        "UN country team urges plans with clear indicators and timelines.",
        [
            ("Tajikistan", "1", "28", "a national action plan for the period 2023–2026 was approved by a presidential decree on 1 April 2023"),
            ("Tajikistan", "1", "18", "the Government began implementing an updated national action plan for the period 2025–2032"),
            ("United Nations country team", "2", "8", "urged the Government to ensure systematic follow-up to international human rights recommendations through national action plans with clear indicators, timelines and measurable results"),
        ],
    ),
    "Rule of law & impunity": (
        C, "Investigate torture and deaths in custody; protect lawyers and defenders",
        "The UN country team reports that torture and ill-treatment remain "
        "persistent and that victims do not receive effective remedies; JS10 "
        "reports that judges rarely order investigations.",
        [
            ("United Nations country team", "2", "27", "torture and ill-treatment remained persistent and that, in practice, victims did not receive effective remedies or adequate compensation"),
            ("JS10", "3", "30", "Judges rarely ordered thorough investigations into allegations of torture and ill-treatment"),
        ],
    ),
    "Equality & non-discrimination": (
        C, "Protect religious minorities, LGBTI persons and people living with HIV from discrimination",
        "The 2022 Equality Act does not list sexual orientation or gender "
        "identity; the CESCR and civil society report continuing "
        "discrimination and police abuse of LGBT+ persons.",
        [
            ("COC Netherlands", "3", "93", "the law did not explicitly include sexual orientation and gender identity (SOGI) as protected grounds"),
            ("JS11", "3", "90", "police often arbitrarily detained LGBT+ people"),
            ("Committee on Economic, Social and Cultural Rights", "2", "93", "called upon the Government to provide effective protection against all forms of discrimination and violence based on sexual orientation and gender identity"),
        ],
    ),
    "Right to health": (
        B, "Increase health funding and improve maternal and child health",
        "The 2026 health budget rises 16.1% (2.6% of GDP), two perinatal "
        "centres opened and a cancer programme 2025-2029 was approved; the UN "
        "country team notes health spending remains low with over 65% "
        "out-of-pocket.",
        [
            ("Tajikistan", "1", "149", "representing an increase of 16.1% over 2025 and equivalent to 2.6% of GDP"),
            ("United Nations country team", "2", "64", "health spending in Tajikistan had remained low, at 2.5 per cent of gross domestic product, with over 65 per cent of the costs paid out of pocket"),
        ],
    ),
    "Participation of women in political & public life": (
        B, "Increase women's representation in political and public life",
        "Gender quotas of 30-40% and preferential scoring were introduced in "
        "public service recruitment; patriarchal norms continue to limit "
        "women's participation.",
        [
            ("United Nations country team", "2", "75", "Tajikistan had introduced gender quotas of 30 to 40 per cent and preferential scoring in public service recruitment"),
            ("United Nations country team", "2", "76", "persistent patriarchal norms in Tajikistan continued to limit the participation of women in public and political life"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Strengthen the Commissioner for Human Rights in line with the Paris Principles",
        "The Commissioner's budget rose 92% (2022-2025), staff reached 58 and "
        "its regional offices moved to the national budget; the institution "
        "remains at B status and the UN country team asks for revision of "
        "its law.",
        [
            ("Tajikistan", "1", "11", "Its budget has almost doubled, increasing by 92%, from 1,987,864 somoni in 2022 to 3,821,662 somoni in 2025"),
            ("Tajikistan", "1", "9", "has been accredited with category B status"),
            ("United Nations country team", "2", "10", "revise the Law on the Commissioner for Human Rights to ensure full compliance with the principles relating to the status of national institutions"),
        ],
    ),
    "Conditions of detention": (
        B, "Improve prison conditions and allow independent monitoring",
        "The Commissioner's monitoring group was enlarged to 30 members "
        "including civil society, and a Penal Correction System Reform "
        "Strategy to 2030 is being implemented; JS1 asks for access for all "
        "independent monitors.",
        [
            ("Tajikistan", "1", "85", "Since 2025, the group’s membership has been increased to 30 people to include representatives from civil society"),
            ("Tajikistan", "1", "82", "The Penal Correction System Reform Strategy in the period up to 2030 is being implemented"),
            ("JS1", "3", "34", "advised the government to allow independent monitoring of all detention facilities"),
        ],
    ),
    "Discrimination against women": (
        B, "Promote gender equality and combat discrimination against women",
        "The Act on State Guarantees of Equal Rights was amended (2022), the "
        "list of jobs closed to women was cut by 140 entries (2023) and the "
        "Labour Code now bans sexual harassment (2026); wage gaps and "
        "stereotypes persist.",
        [
            ("Tajikistan", "1", "174", "the Act on State Guarantees of Equal Rights for Men and Women and Equal Opportunities was amended to introduce a modern definition of gender"),
            ("Tajikistan", "1", "128", "the list of work in which the use of women’s labour is prohibited was reduced by 140 entries (from 334 to 194)"),
            ("United Nations country team", "2", "76", "Women remained overrepresented in informal and low-paid sectors and faced wage gaps"),
        ],
    ),
    "Persons with disabilities: independence, inclusion": (
        B, "Rights and inclusive education of persons with disabilities",
        "A new Rights and Social Protection of Persons with Disabilities Act "
        "(June 2026) introduced the human rights model; the CRPD has still "
        "not been ratified.",
        [
            ("Tajikistan", "1", "197", "a new Rights and Social Protection of Persons with Disabilities Act was adopted"),
            ("Tajikistan", "1", "198", "more than 7,300 children with disabilities were attending school"),
            ("JS11", "3", "82", "ratification remained pending"),
        ],
    ),
    "Children: definition": (
        B, "Protect children from violence",
        "Corporal punishment was banned in all settings (2024) and a National "
        "Programme on the Protection of Children's Rights 2026-2030 was "
        "adopted; the UN country team calls for an enforceable child "
        "protection framework.",
        [
            ("Tajikistan", "1", "189", "the adoption in 2024 of the Act on the Responsibility for the Education and Upbringing of the Child, which provides for a complete prohibition of corporal punishment of children in all settings"),
            ("United Nations country team", "2", "21", "recommended establishing a comprehensive and enforceable national child protection framework"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        B, "Cooperate with UN human rights mechanisms",
        "Tajikistan reports timely treaty-body reporting and an action plan "
        "for follow-up to special procedures 2026-2027; L4L notes that it "
        "rarely responds to special procedure communications.",
        [
            ("Tajikistan", "1", "15", "by submitting reports in a timely manner and implementing the recommendations received"),
            ("L4L", "3", "3", "it rarely responded to communications by special procedure mandate holders"),
        ],
    ),
    "Right to participate in public affairs & right to vote": (
        C, "Political participation, opposition and credible elections",
        "The National Report describes only electoral-law training; OSCE-ODIHR "
        "cancelled its needs assessment for the 2025 elections for lack of "
        "assurances on accreditation.",
        [
            ("OSCE-ODIHR", "3", "49", "eventually cancelled the mission due to the continuing lack of assurances that ODIHR experts and international observers would receive the accreditation needed"),
            ("Tajikistan", "1", "111", "conducted a series of training sessions on electoral law for university students, graduate students and civil servants"),
        ],
    ),
    "Arbitrary arrest & detention": (
        C, "Prevent arbitrary detention and release political detainees",
        "The National Report restates existing custody safeguards (72-hour "
        "limit, lawyer from detention); journalists, lawyers and activists "
        "remain imprisoned.",
        [
            ("Tajikistan", "1", "73", "Detention without a court decision is limited to 72 hours for adults and 48 hours for minors"),
            ("JS10", "3", "33", "reduce the period of detention before the remand hearing from the current 72 to 48"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        C, "Extend a standing invitation to special procedures",
        "No standing invitation is reported; Tajikistan states that it "
        "responds to visit requests, but L4L reports that it rarely replies "
        "to communications.",
        [
            ("Tajikistan", "1", "23", "responds promptly to their requests to visit the country"),
            ("L4L", "3", "3", "it rarely responded to communications by special procedure mandate holders"),
        ],
    ),
    "Administration of justice & fair trial": (
        B, "Strengthen the justice system, access to justice and independence of lawyers",
        "The Legal Aid Centre moved to full State funding (2024), the Bar "
        "and Advocacy Act was amended (January 2024) and judicial training "
        "was expanded; JS3 asks for judicial independence from the "
        "executive.",
        [
            ("Tajikistan", "1", "93", "The Centre has gradually transitioned to full State funding (60% in 2022 and 100% by 2024)"),
            ("Tajikistan", "1", "92", "amendments were made to the Bar and Advocacy Act to strengthen the legal status and independence of lawyers"),
            ("JS3", "3", "47", "ensure the independence of the judicial system and judges from the executive branch"),
        ],
    ),
    "Children: protection against exploitation": (
        B, "Eliminate the worst forms of child labour",
        "The National Programme for the Elimination of the Worst Forms of "
        "Child Labour 2024-2028 was approved with strict monitoring of "
        "employers.",
        [
            ("Tajikistan", "1", "121", "In August 2024, the Government approved the National Programme for the Elimination of the Worst Forms of Child Labour for the period 2024–2028"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Combat gender-based violence",
        "The Domestic Violence Act was amended (2024), a State Programme "
        "2025-2030 adopted and an Interdepartmental Council created "
        "(February 2025); the Criminal Code criminalisation remains in draft.",
        [
            ("Tajikistan", "1", "87", "significant amendments were made to the Prevention of Domestic Violence Act, which broadened the definition of violence and established the right of victims to free medical and legal assistance"),
            ("Tajikistan", "1", "31", "the Interdepartmental Council on the Prevention of Domestic Violence was established under the Government of Tajikistan"),
        ],
    ),
    "Advancement of women": (
        B, "Protect women's rights and provide complaint mechanisms",
        "A Resource Centre with a helpline, 29 medical and social support "
        "units for victims of violence and a public council 'Women of "
        "Tajikistan' were established.",
        [
            ("Tajikistan", "1", "172", "The Committee for Women and the Family has established the Resource Centre on the Prevention of Domestic Violence and Gender Equality, which operates a helpline"),
            ("Tajikistan", "1", "188", "Twenty-nine units providing medical and social support have been established"),
        ],
    ),
    "Right to development": (
        B, "Sustainable development and social security",
        "Poverty fell from 56% (2010) to under 20% and a Social Protection "
        "Development Strategy up to 2040 was approved (2022).",
        [
            ("Tajikistan", "1", "41", "the poverty rate fell from 56% in 2010 to less than 20% in recent years"),
            ("Tajikistan", "1", "135", "The Social Protection Development Strategy for the period up to 2040 was approved by a government decision of 29 November 2022"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        B, "Strengthen the fight against torture",
        "Supreme Court Decision No. 32 (December 2025) guides compensation for "
        "torture victims and interrogation rooms are being equipped with "
        "audiovisual recording; JS10 reports torture remains widespread.",
        [
            ("Tajikistan", "1", "78", "adopted Decision No. 32, which provided courts with clear guidance on the compensation for harm suffered by victims of torture"),
            ("JS10", "3", "30", "torture and ill-treatment remained widespread in Tajikistan, especially in police custody and pre-trial detention"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Prevent trafficking and forced labour",
        "National Plans to Combat Trafficking 2022-2024 and 2025-2027, "
        "increased funding for shelters, 626 victims identified (2023-2025); "
        "the Special Rapporteur notes limited implementation in practice.",
        [
            ("Tajikistan", "1", "114", "National Plan to Combat Trafficking in Persons for the period 2025–2027"),
            ("Tajikistan", "1", "116", "626 victims were identified, 317 of whom were referred to specialized State shelters and NGOs"),
            ("Special Rapporteur on trafficking in persons, especially women and children", "2", "48", "remained concerned about the limited implementation in practice of measures to ensure the human rights of trafficked persons"),
        ],
    ),
    "Right to social security": (
        B, "Improve social protection",
        "A Social Entrepreneurship Act entered into force (January 2025), "
        "targeted social assistance covers more than 15% of households and "
        "day-care centres for persons with disabilities reached 59; CESCR "
        "asks for universal coverage.",
        [
            ("Tajikistan", "1", "138", "More than 15% of households are covered by the programme"),
            ("Committee on Economic, Social and Cultural Rights", "2", "58", "develop a social security system that ensured universal coverage"),
        ],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        B, "Standing national mechanism for follow-up",
        "A Government Commission on Compliance with International Human "
        "Rights Obligations coordinates reporting and follow-up.",
        [
            ("Tajikistan", "1", "24", "Tajikistan has a well-established national mechanism for implementation, reporting and follow-up"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        B, "Align counter-terrorism and counter-extremism rules with the ICCPR",
        "New counter-terrorism and counter-extremism acts, a 2026 strategy "
        "and the May 2025 amendments were adopted; the UN country team and "
        "Special Rapporteurs still ask for a review of definitions.",
        [
            ("Tajikistan", "1", "62", "New versions of the Counter-Terrorism Act of December 2021"),
            ("United Nations country team", "2", "31", "review counter-terrorism legislation to align with international standards"),
        ],
    ),
    "Human rights & climate change": (
        B, "Participation in climate and disaster risk reduction",
        "Women, children and persons with disabilities are involved through "
        "the Women and Water Forum, rural-women adaptation grants and a "
        "disability needs analysis.",
        [
            ("Tajikistan", "1", "58", "The State actively promotes the participation of women in climate-related decisionmaking"),
            ("Tajikistan", "1", "60", "a situational analysis was conducted of the needs of persons with disabilities during climate-related emergencies"),
        ],
    ),
    "Good governance & corruption": (
        C, "Combat corruption",
        "The National Report mentions only a Code of Ethics for Judges.",
        [
            ("Tajikistan", "1", "91", "A Code of Ethics for Judges is in force, aimed at preventing the risks of corruption and enhancing public confidence in the justice system"),
        ],
    ),
    "Human rights & poverty": (
        B, "Reduce poverty",
        "National-line poverty fell to 19.8% in 2024.",
        [
            ("Tajikistan", "1", "143", "the poverty rate, measured against the national poverty line, fell to 19.8% in 2024"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Improve living standards of the most vulnerable",
        "Poverty fell to 19.8% in 2024, a Housing Code with social rental "
        "arrangements entered into force (2022) and targeted social "
        "assistance reaches 419,000 children.",
        [
            ("Tajikistan", "1", "143", "the poverty rate, measured against the national poverty line, fell to 19.8% in 2024"),
            ("Tajikistan", "1", "145", "the entry into force in 2022 of the new Housing Code, which introduced the concept of social rental arrangements for those in need"),
        ],
    ),
    "Safe drinking water & sanitation": (
        B, "Reduce disparities in water and sanitation",
        "A State Programme for Drinking Water Supply and Sanitation 2025-2029 "
        "was adopted; 73% of rural schools have safe drinking water.",
        [
            ("Tajikistan", "1", "146", "In 2025, the State Programme for Drinking Water Supply and Sanitation for the period 2025–2029 was adopted"),
            ("Tajikistan", "1", "147", "The proportion of schools with access to safe drinking water reached 93% in urban areas and 73% in rural areas"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        B, "Health services for women and children",
        "A State Programme on Reproductive Health 2023-2027 was approved.",
        [
            ("Tajikistan", "1", "30", "The State Programme on Reproductive Health for the period 2023–2027 has been approved"),
        ],
    ),
    "Human rights education, trainings & awareness raising": (
        B, "Human rights awareness-raising and training",
        "2024 was declared the Year of Legal Literacy and a legal literacy "
        "course was introduced in higher education.",
        [
            ("Tajikistan", "1", "109", "The year 2024 was declared the Year of Legal Literacy in the country"),
            ("Tajikistan", "1", "110", "A legal literacy course has been introduced in higher education institutions"),
        ],
    ),
    "Violence against women": (
        B, "Eliminate gender-based violence against women",
        "The Domestic Violence Act was amended (2024) and a State Programme "
        "2025-2030 adopted.",
        [
            ("Tajikistan", "1", "87", "significant amendments were made to the Prevention of Domestic Violence Act, which broadened the definition of violence and established the right of victims to free medical and legal assistance"),
        ],
    ),
    "Economic, social & cultural rights - general measures of implementation": (
        B, "Skills and economic participation of youth and women",
        "A presidential grants programme for women entrepreneurs and a State "
        "Employment Promotion Programme 2023-2027 were launched.",
        [
            ("Tajikistan", "1", "185", "15 million somoni are allocated to fund 200 presidential grants"),
        ],
    ),
    "Right to food": (
        B, "Protect people at risk of food insecurity",
        "A Food Safety Programme 2024-2028 was approved and the National "
        "School Meal Programme serves more than 450,000 children.",
        [
            ("Tajikistan", "1", "144", "the National School Meal Programme already serves more than 450,000 children in 2,000 elementary schools"),
        ],
    ),
    "Children: juvenile justice": (
        B, "Prevent juvenile delinquency and extremist recruitment of juveniles",
        "A Juvenile Justice Reform Programme 2023-2027 was adopted and a "
        "Unified Information Centre for the Prevention of Extremism was "
        "established.",
        [
            ("Tajikistan", "1", "95", "The Juvenile Justice Reform Programme for the period 2023–2027 has been adopted"),
        ],
    ),
    "Refugees & asylum seekers": (
        C, "Regulations on refugee status determination",
        "No such regulation is reported; the UN country team asks for quality "
        "refugee status determination and fair access to the territory.",
        [
            ("United Nations country team", "2", "98", "ensure quality refugee status determination"),
            ("Tajikistan", "1", "204", "the repeal of the provision in article 499 of the Code of Administrative Offences on the mandatory expulsion of refugees"),
        ],
    ),
    "Liberty & security of the person": (
        C, "End transnational repression and forced repatriation",
        "No measure is reported; JS3 asks to end extrajudicial expulsions.",
        [
            ("JS3", "3", "97", "put an end to the practice of extrajudicial expulsions"),
        ],
    ),
}

KEYWORDS = [
    # --- ratification ---
    (r"Second Optional Protocol", C,
     "Ratify the Second Optional Protocol to the ICCPR",
     "Tajikistan has not ratified the Protocol; it keeps its moratorium and an inter-departmental working group on abolition; JS2 asks for a timeline.",
     [("United Nations country team", "2", "2", "the Second Optional Protocol to the International Covenant on Civil and Political Rights, aiming at the abolition of the death penalty"),
      ("Tajikistan", "1", "72", "An interdepartmental working group tasked with examining the social and legal aspects of the abolition of the death penalty continues its work")]),
    (r"^(Abolish the death penalty and ratify|Ratify the Second Optional Protocol to the International Covenant on Civil and Political Rights and fully abolish|Adopt the necessary measures to move towards the abolition)", B,
     "Abolish the death penalty (and ratify the Second Optional Protocol)",
     "Tajikistan keeps an indefinite moratorium (since 2004), endorsed a joint declaration of foreign ministers proclaiming Central Asia and Mongolia a death-penalty-free region and runs a working group on abolition; the penalty remains in law and the Protocol is not ratified.",
     [("Tajikistan", "1", "72", "An indefinite moratorium on the use of the death penalty has been in place in Tajikistan since 2004"),
      ("Tajikistan", "1", "31", "Tajikistan has endorsed the joint declaration of foreign ministers proclaiming Central Asia and Mongolia a death penalty-free region"),
      ("UPR BCU", "3", "20", "Tajikistan continued to retain the death penalty in law")]),
    (r"^(Take all necessary steps to abolish the death penalty|Completely abolish the death penalty|Fully abolish the death penalty)", B,
     "Abolish the death penalty",
     "Tajikistan keeps an indefinite moratorium (since 2004), endorsed the joint declaration on a death-penalty-free Central Asia and Mongolia and runs a working group on abolition; the penalty remains in law.",
     [("Tajikistan", "1", "72", "An indefinite moratorium on the use of the death penalty has been in place in Tajikistan since 2004"),
      ("Tajikistan", "1", "31", "Tajikistan has endorsed the joint declaration of foreign ministers proclaiming Central Asia and Mongolia a death penalty-free region")]),
    (r"^(Retain the moratorium|Establish a moratorium)", A,
     "Retain the moratorium on the death penalty",
     "An indefinite moratorium has been in place since 2004, replaced by life imprisonment or 25 years' deprivation of liberty.",
     [("Tajikistan", "1", "72", "An indefinite moratorium on the use of the death penalty has been in place in Tajikistan since 2004")]),
    (r"timeline with concrete steps", C,
     "Set a timeline for abolition of the death penalty",
     "No timeline is reported; JS2 asks for one with completion no later than 2027.",
     [("JS2", "3", "18", "publicize a timeline for abolishing the death penalty")]),
    (r"awareness-raising campaigns on the death penalty", D,
     "Awareness-raising and public debate on the death penalty",
     "The documents contain no information on this ask.", []),
    (r"^(Ratify|Consider acceding to) the International Convention for the Protection of All Persons", D,
     "Ratify the Convention on Enforced Disappearance",
     "The documents contain no information on this ask.", []),
    (r"Convention on the Rights of Persons with Disabilities", B,
     "Ratify the Convention on the Rights of Persons with Disabilities",
     "Tajikistan signed the CRPD in 2018, prepared ratification through a national road map and adopted a CRPD-aligned disability law in June 2026, but has not ratified the Convention.",
     [("Tajikistan", "1", "25", "Tajikistan is currently preparing to ratify the Convention"),
      ("JS11", "3", "82", "ratification remained pending")]),
    (r"Optional Protocol to the Convention against Torture", B,
     "Ratify the Optional Protocol to the Convention against Torture",
     "A working group was set up to facilitate accession and to explore a national preventive mechanism ('Ombudsman Plus' model); the Protocol is not ratified.",
     [("Tajikistan", "1", "27", "A working group has been set up to facilitate accession to the Optional Protocol to the Convention against Torture"),
      ("Tajikistan", "1", "31", "Ratification of the Optional Protocol to the Convention against Torture is under consideration")]),
    (r"^Consider ratification of the core human rights instruments", B,
     "Consider ratifying the remaining core instruments",
     "Working groups were set up on the CRPD, OPCAT and the two statelessness conventions; none is ratified.",
     [("Tajikistan", "1", "26", "an interdepartmental working group on accession to the 1954 Convention relating to the Status of Stateless Persons and the 1961 Convention on the Reduction of Statelessness commenced its work")]),
    (r"^Request technical support from the Office", D,
     "Request OHCHR technical support for ratification",
     "The documents contain no information on this ask.", []),
    # --- anti-discrimination law ---
    (r"^Adopt a comprehensive anti-discrimination law that provides|^Introduce comprehensive anti-discrimination legislation and legal framework|ratify the bill on equality", A,
     "Adopt comprehensive anti-discrimination legislation",
     "The Equality and Elimination of All Forms of Discrimination Act was adopted on 19 July 2022, defines direct and indirect discrimination and gives a right to compensation; the Commissioner is the competent body.",
     [("Tajikistan", "1", "34", "The Equality and Elimination of All Forms of Discrimination Act defines direct and indirect discrimination"),
      ("United Nations country team", "2", "22", "had adopted the Law on equality and elimination of all forms of discrimination, establishing a comprehensive legal framework prohibiting direct, indirect and multiple discrimination")]),
    (r"LGBTI\+ persons from discrimination|gender identity and sexual orientation, and end the practice|prohibit all forms of discrimination and repeal policies|different sexual orientations|reprisals for LGBTI|Hold accountable officials, public figures and authors", C,
     "Protect LGBTI persons in law and practice",
     "The 2022 Equality Act does not list sexual orientation or gender identity; the CESCR and civil society report arbitrary detention and ill-treatment of LGBT+ persons and no measure is reported.",
     [("COC Netherlands", "3", "93", "the law did not explicitly include sexual orientation and gender identity (SOGI) as protected grounds"),
      ("JS11", "3", "90", "police often arbitrarily detained LGBT+ people")]),
    (r"^Adopt comprehensive anti-discrimination legislation to protect the rights of vulnerable groups|violence against women and children, and on the basis of|combat all forms of discrimination and violence, including domestic violence, based on gender", B,
     "Combat discrimination and violence, including on grounds of gender, disability and HIV status",
     "The 2022 Equality Act, the 2024 Domestic Violence Act amendments and the 2026 disability and labour reforms address gender, disability and employment discrimination; sexual orientation and gender identity are not covered.",
     [("Tajikistan", "1", "34", "The Equality and Elimination of All Forms of Discrimination Act defines direct and indirect discrimination"),
      ("COC Netherlands", "3", "93", "the law did not explicitly include sexual orientation and gender identity (SOGI) as protected grounds")]),
    (r"persons living with HIV/AIDS", B,
     "Address stigmatisation and discrimination against people living with HIV",
     "The Health Code was amended (December 2025) and the Supreme Court issued guidance (December 2023) on HIV transmission cases; mandatory testing and criminal liability remain.",
     [("Tajikistan", "1", "155", "persons living with HIV who are receiving antiretroviral therapy and have achieved an undetectable viral load are considered not to present a risk to their sexual partners"),
      ("Human Rights Center TJ", "3", "64", "Laws such as mandatory testing of people living with HIV allowed discriminatory treatment toward certain groups")]),
    # --- domestic violence ---
    (r"^(Criminalize all forms|Criminalize domestic violence in all|Criminalize domestic violence and marital|Classify domestic|Introduce legislation to criminalize all forms|Prioritize the enactment|Amend article 53|Criminalize child)", C,
     "Criminalise domestic violence and other gender-based violence",
     "Domestic violence has been incorporated into the draft Criminal Code, which remains unadopted; stakeholders note that it is still not a criminal offence.",
     [("Tajikistan", "1", "31", "The criminalization of domestic violence has been incorporated into the draft Criminal Code"),
      ("JS5", "3", "71", "domestic violence has yet to be recognized as a criminal offence in Tajikistan")]),
    (r"^Criminalize child, early and forced marriage", D,
     "Criminalise child, early and forced marriage",
     "The documents contain no information on this ask.", []),
    (r"^Implement fully the law on the prevention of domestic violence|^(Develop an action plan to eliminate all forms of gender-based|Develop a comprehensive strategy and action plan)|^Address domestic violence and guarantee|^Sustain efforts to prevent domestic violence|^Strengthen the legal framework to prevent domestic violence|^Criminalize domestic and intimate partner violence|measures to criminalize such actions", B,
     "Prevent and respond to domestic violence",
     "The Domestic Violence Act was amended (2024) to broaden the definition of violence, a State Programme 2025-2030 and an Interdepartmental Council (February 2025) were created, support centres expanded and 21 prevention-officer posts introduced; the offence is not yet in the Criminal Code.",
     [("Tajikistan", "1", "87", "significant amendments were made to the Prevention of Domestic Violence Act, which broadened the definition of violence and established the right of victims to free medical and legal assistance"),
      ("Tajikistan", "1", "31", "the Interdepartmental Council on the Prevention of Domestic Violence was established under the Government of Tajikistan"),
      ("JS5", "3", "71", "domestic violence has yet to be recognized as a criminal offence in Tajikistan")]),
    # --- torture / detention ---
    (r"^Bring the criminal legislation into line with the provisions of the Convention against Torture", A,
     "Align the criminal definition of torture with the Convention against Torture",
     "The definition in article 143(1) of the Criminal Code has been brought fully into line with article 1 of the Convention.",
     [("Tajikistan", "1", "76", "The definition of torture in article 143 (1) of the Criminal Code has been brought fully into line with article 1 of the Convention against Torture")]),
    (r"^Revise the Criminal Code to include the criminalization of enforced disappearance", D,
     "Criminalise enforced disappearance",
     "The documents contain no information on this ask.", []),
    (r"investigated and prosecuted and perpetrators convicted|thorough and impartial investigations|systematic investigations into any allegation", C,
     "Investigate and prosecute torture and ill-treatment",
     "The UN country team reports that victims do not receive effective remedies and courts have no established practice of excluding evidence obtained by torture; JS10 reports that judges rarely order investigations.",
     [("United Nations country team", "2", "27", "torture and ill-treatment remained persistent and that, in practice, victims did not receive effective remedies or adequate compensation"),
      ("JS10", "3", "30", "Judges rarely ordered thorough investigations into allegations of torture and ill-treatment")]),
    # --- death penalty etc done; counter-terror ---
    (r"countering violent extremism", B,
     "Review counter-extremism legislation",
     "Articles 179(3) and 307(1) of the Criminal Code were amended in May 2025 to remove the risk of unjustified prosecution for online activity; vague extremism definitions remain.",
     [("Tajikistan", "1", "30", "amendments to articles 179 (3) and 307 (1) of the Criminal Code were adopted, thereby addressing the risk of unjustified prosecution for online activity"),
      ("Special Rapporteur on freedom of religion or belief", "2", "16", "review the vague definitions of “extremism”")]),
    # --- religion ---
    (r"freedom of religion or belief|law on freedom of conscience|religious organizations", C,
     "Review laws affecting freedom of religion or belief",
     "The 2022 amendments to the Freedom of Conscience and Religious Associations Act restrict founders and staff; the Special Rapporteur and civil society ask for review and report raids on minority churches.",
     [("Tajikistan", "1", "99", "In July 2022, amendments were made to the Freedom of Conscience and Religious Associations Act"),
      ("Special Rapporteur on freedom of religion or belief", "2", "14", "review the Freedom of Conscience and Religious Associations Act and the Act on Regulating Traditions, Celebrations and Rituals with a view to bringing them into compliance with international standards"),
      ("ECLJ", "3", "63", "Baptist, Evangelical, and Pentecostal churches being raided, threatened, fined, and their members arrested")]),
    (r"alternative to military service", C,
     "Alternative service for conscientious objectors",
     "No alternative service is reported; JS6 asks for legislation recognising conscientious objection.",
     [("JS6", "3", "12", "promptly adopt legislation recognizing the right to conscientious objection to military service")]),
    (r"promoting tolerance, protecting religious rights", B,
     "Promote tolerance and religious diversity",
     "Annual conferences, round tables and training of more than 500 imam-khatibs on tolerance and legal literacy were held; 66 of the 4,000 registered religious organisations are non-Islamic.",
     [("Tajikistan", "1", "103", "Training sessions were organized for more than 500 imam-khatibs, aimed at fostering tolerance and legal literacy"),
      ("Tajikistan", "1", "101", "more than 900 conferences, 4,350 round tables and 92,000 meetings with the public have been held")]),
    # --- expression / civil society ---
    (r"insulting or libelling|ensure access to information and the exercise of freedom|Align national legislation with international standards to effectively guarantee|^Review legislation and policies to create a free and safe environment", C,
     "Align expression and information laws with international standards",
     "Defamation and false-publication offences remain in the Criminal Code and the Information Code is still to be adopted; only the May 2025 amendment on 'liking' extremist content was made.",
     [("JS14", "3", "6", "repeal articles 137 and 330 of the Criminal Code which criminalise defamation"),
      ("JS3", "3", "9", "advised accelerating the adoption of the Information Code of the Republic of Tajikistan")]),
    (r"^(Amend legislation which undermines the rights to freedom of expression|Eliminate from legislation all provisions that undermine freedom of expression)", B,
     "Amend legislation undermining freedom of expression",
     "Criminal Code articles 179(3) and 307(1) were amended in May 2025; defamation and false-publication offences remain.",
     [("Tajikistan", "1", "30", "amendments to articles 179 (3) and 307 (1) of the Criminal Code were adopted, thereby addressing the risk of unjustified prosecution for online activity"),
      ("JS14", "3", "6", "repeal articles 137 and 330 of the Criminal Code which criminalise defamation")]),
    (r"^(Take measures to foster a safe, respectful and enabling environment for civil society|Refrain from imposing restrictions on civil society|Guarantee that human rights defenders|Allow civil society, including|Cease reprisals|Consider adopting new legal and policy measures that foster an enabling environment for civil society|Review the law on public associations)", E,
     "Protect civil society and human rights defenders; remove restrictions on associations",
     "In November 2023 the Minister of Justice announced that 700 NGOs had been liquidated within 18 months, and rights defenders, journalists and activists have been imprisoned: measures contrary to the recommendations.",
     [("United Nations country team", "2", "41", "700 non-governmental organizations in Tajikistan had been liquidated over an 18-month period"),
      ("Special Rapporteur on the situation of human rights defenders", "2", "41", "signalled a deteriorating environment for civil society and human rights defence in Tajikistan"),
      ("HRW", "3", "53", "an end to all politically motivated closures of NGOs and civil society organizations")]),
    (r"^(Terminate the practices of arbitrary blocking|Strengthen the right to freedom of expression and refrain from blocking|Create and maintain an enabling environment for the free use)", E,
     "End blocking of websites and online surveillance",
     "Stakeholders report internet shutdowns, blocking of independent media websites and bans on outlets, which run contrary to the recommendation.",
     [("JS14", "3", "55", "end censorship practices, particularly during protests, including internet shutdowns, throttling and blockage of independent media websites"),
      ("CPJ", "3", "56", "banning media outlets, blocking their websites, threatening them with closure over legitimate reporting")]),
    (r"^(Release all|Uphold rights to freedom of expression, association and assembly, and of religion and belief, including through ending the detention|Guarantee the rights to freedom of expression, assembly and peaceful association, as well as the freedom of the press, first of all by releasing|Stop harassment of journalists|Ensure the freedom of the media by protecting journalists)", E,
     "Release imprisoned journalists and activists; stop harassment of journalists",
     "Around 20 independent journalists and bloggers have been imprisoned since 2022, often on terrorism or extremism charges, and HRW and JS14 call for the release of those imprisoned over the GBAO protests.",
     [("United Nations country team", "2", "43", "around 20 independent journalists and bloggers had been imprisoned, often on terrorism- or extremism-related charges"),
      ("HRW", "3", "58", "immediately and unconditionally release all HRDs, lawyers, journalists, and civil society activists imprisoned")]),
    (r"^Extend the measure of releasing detainees", C,
     "Extend amnesty releases to political prisoners",
     "The June 2026 Amnesty Act applies to 18,038 convicted persons, with leniency for women and minors; no release of political prisoners is reported.",
     [("Tajikistan", "1", "88", "In June 2026, the President signed the Amnesty Act, which applies to 18,038 convicted persons"),
      ("HRW", "3", "58", "immediately and unconditionally release all HRDs, lawyers, journalists, and civil society activists imprisoned")]),
    (r"^Duly address allegations of systemic persecution|^Prohibit any surveillance of lawyers|Operative and Search Activity Act|^Review the legislation and practices dedicated to criminalizing and prosecuting political dissent", C,
     "Address persecution of dissent and lawyers",
     "The National Report contains no reply; L4L reports harassment and detention of lawyers, and HFHR PCP reports intimidation, surveillance and long sentences on politically motivated charges.",
     [("L4L", "3", "44", "attempts to harass and disrupt the work of lawyers in Tajikistan"),
      ("HFHR PCP", "3", "50", "an ongoing narrowing of civic space marked by growing restrictions on freedom of expression, association and assembly")]),
    (r"accreditation schemes", D,
     "Refrain from accreditation schemes that undermine independent media",
     "The documents contain no information on this ask.", []),
    (r"^Ensure that lawyers are guaranteed full independence", B,
     "Guarantee the independence and safety of lawyers",
     "The Bar and Advocacy Act was amended in January 2024 to strengthen the legal status and independence of lawyers; L4L reports continuing harassment.",
     [("Tajikistan", "1", "92", "amendments were made to the Bar and Advocacy Act to strengthen the legal status and independence of lawyers"),
      ("L4L", "3", "45", "ensure that sufficient safeguards are in place, both in law and in practice, to guarantee the full independence and safety of lawyers")]),
    (r"dialogue with civil society and non-governmental organizations to deepen the necessary reform of the prison", B,
     "Dialogue with civil society on prison reform",
     "Civil society representatives joined the Commissioner's monitoring group (2025) and the NGO list for prison visits was expanded in 2022.",
     [("Tajikistan", "1", "85", "Since 2025, the group’s membership has been increased to 30 people to include representatives from civil society"),
      ("Tajikistan", "1", "108", "the list of non-governmental organizations (NGOs) participating in the Monitoring Group of the Office of the Human Right Commission for visits to closed institutions was significantly expanded")]),
    # --- plans ---
    (r"^(Continue its ongoing efforts to adopt the national strategy|Speed up the adoption of the national human rights strategy)", A,
     "Adopt a national human rights strategy",
     "The National Human Rights Strategy up to 2038 was adopted on 5 August 2023, with an action plan 2023-2026.",
     [("Tajikistan", "1", "30", "On 5 August 2023 the National Human Rights Strategy for the period up to 2038 was adopted")]),
    (r"national policy and strategy on children", A,
     "Adopt a comprehensive national policy and strategy on children",
     "A National Programme on the Protection of Children's Rights 2026-2030 was adopted in June 2026.",
     [("Tajikistan", "1", "190", "the adoption in June 2026 of the National Programme on the Protection of Children’s Rights for the period 2026–2030")]),
    (r"Guiding Principles on Business and Human Rights", D,
     "National action plan on business and human rights",
     "The documents contain no information on this ask.", []),
    # --- children / other ---
    (r"awareness campaigns on the harmful effects of child, early", D,
     "Awareness campaigns on child, early and forced marriage",
     "The documents contain no information on this ask.", []),
    (r"registered at birth", B,
     "Register all children at birth",
     "A new Civil Registry Act (January 2025) simplified birth registration, more than 249,000 children were registered free of charge and a 2025 law removed time limits for late registration.",
     [("Tajikistan", "1", "191", "A new Civil Registry Act has been in effect since January 2025, simplifying birth registration procedures"),
      ("United Nations country team", "2", "101", "removed time limits for birth registration and allowed for late registration")]),
    # --- political participation ---
    (r"civic education", B,
     "Civic education and understanding of democracy",
     "Electoral-law training for students and civil servants and a legal literacy course in higher education were introduced; 2024 was the Year of Legal Literacy.",
     [("Tajikistan", "1", "111", "conducted a series of training sessions on electoral law for university students, graduate students and civil servants"),
      ("Tajikistan", "1", "110", "A legal literacy course has been introduced in higher education institutions")]),
    # --- NHRI-related in other clusters ---
    (r"Office of the Commissioner for Human Rights", B,
     "Strengthen the Office of the Commissioner for Human Rights",
     "The Commissioner's budget rose 92% (2022-2025), staff reached 58 and it was given anti-discrimination powers; it remains at B status.",
     [("Tajikistan", "1", "11", "Its budget has almost doubled, increasing by 92%, from 1,987,864 somoni in 2022 to 3,821,662 somoni in 2025"),
      ("Tajikistan", "1", "9", "has been accredited with category B status")]),
]

FALLBACK = (D, "No information on this ask",
            "The documents contain no information on this ask.", [])
