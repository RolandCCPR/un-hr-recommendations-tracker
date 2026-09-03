"""First-pass implementation assessment of the 347 cycle-3 UPR recommendations
to the United States, graded on the adapted Human Rights Committee A-E scale.

Evidence base (cycle-4 pre-sessional documents, both in ``evidence/``):
  * A/HRC/WG.6/50/USA/2  - OHCHR Compilation of UN information (28 Aug 2025)
  * A/HRC/WG.6/50/USA/3  - OHCHR Summary of 155 stakeholders' submissions (1 Sep 2025)

Method: recommendations are assessed by thematic cluster (their primary OHCHR
theme), because most are near-duplicate asks from different States. Each cluster
carries a default grade, a rationale, and one or more verbatim quotes from the
evidence with the attributed body/organisation. Keyword rules then override
individual recommendations whose substance diverges (Paris Agreement, ICC/Rome
Statute, death-penalty moratorium, asylum, LGBTI, FPIC, DEI).

Quotes are taken verbatim from the two OHCHR reports; the body/organisation is
named as the report names it (UN treaty bodies and special procedures in
document /2; NGO acronyms - expanded where the report's stakeholder list allows
- in document /3).

This is a structured first pass for expert review, not an authoritative verdict.
Idempotent: re-run any time.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

from recommendations.models import Grade
from recommendations.repository import RecommendationRepository

ROOT = Path(__file__).resolve().parent.parent

# A quote = (organisation/body as named in the report, doc "2" or "3", para, text)
Quote = tuple[str, str, str, str]


def _sym(doc: str) -> str:
    return f"A/HRC/WG.6/50/USA/{doc}"


_DOC_NAME = {"2": "UN Compilation", "3": "Stakeholders' Summary"}


def fmt_evidence(quotes: list[Quote]) -> str:
    # Malawi-style: lead with the document, then the paragraph, then the body
    # that made the statement, then the verbatim quote.
    return "\n".join(
        f'{_DOC_NAME[doc]} ({_sym(doc)}), para. {para} — {org}: "{text}"'
        for org, doc, para, text in quotes
    )


def fmt_sources(quotes: list[Quote]) -> str:
    seen: list[str] = []
    for _org, doc, para, _text in quotes:
        s = f"{_sym(doc)} para. {para}"
        if s not in seen:
            seen.append(s)
    return "; ".join(seen)


# --- cluster defaults: primary theme -> (grade, rationale, [quotes]) ----------
CLUSTERS: dict[str, tuple[Grade, str, list[Quote]]] = {
    "Ratification of & accession to international instruments": (
        Grade.C,
        "The United States ratified none of the treaties covered by these "
        "recommendations in the review period and did not reconsider its ICCPR "
        "reservations.",
        [
            ("Committee on the Elimination of Racial Discrimination", "2", "2",
             "encouraged the United States of America to consider ratifying the "
             "international human rights treaties that it had not yet ratified, "
             "including the International Covenant on Economic, Social and Cultural "
             "Rights, the Convention on the Elimination of All Forms of "
             "Discrimination against Women, the Convention on the Rights of the "
             "Child, ... the Convention on the Rights of Persons with Disabilities "
             "and the International Convention for the Protection of All Persons "
             "from Enforced Disappearance"),
            ("Human Rights Committee", "2", "3",
             "recommended that the United States reconsider its position regarding "
             "the reservations, declarations and understandings that it had lodged "
             "at the time of ratification of the International Covenant on Civil "
             "and Political Rights"),
            ("Several stakeholders (OHCHR summary)", "3", "2",
             "the United States of America (USA) had not yet ratified several "
             "international human rights treaties, notwithstanding repeated "
             "recommendations to that effect"),
        ],
    ),
    "Administration of justice & fair trial": (
        Grade.C,
        "No federal legislation on police use of force or accountability was "
        "enacted and the 2022 accountable-policing executive order was reversed.",
        [
            ("International Independent Expert Mechanism to Advance Racial Justice "
             "and Equality in Law Enforcement", "2", "18",
             "the existing regulatory framework on the use of force was conducive "
             "to the early and unjustified use of force, including lethal force, "
             "by law enforcement officers"),
            ("Amnesty International", "3", "21",
             "regretted the lack of action by Congress to pass the George Floyd "
             "Justice in Policing Act"),
            ("JS5 (Physicians for Human Rights; Omega Research Foundation)", "3", "35",
             "Executive Order 14148 reversed policies linked to Executive Order "
             "14074 on advancing effective, accountable policing and criminal "
             "justice practices"),
        ],
    ),
    "Death penalty": (
        Grade.E,
        "Directly contrary measures: the federal death penalty was reinstated and "
        "the 2021 moratorium reversed; executions resumed and expanded.",
        [
            ("Human Rights Committee", "2", "20",
             "recommended establishing a de jure moratorium on the death penalty "
             "at the federal level and taking steps towards its abolition"),
            ("The Dui Hua Foundation", "3", "15",
             "Executive Order 14164 reinstating capital punishment for federal "
             "crimes, for which a moratorium had been imposed in 2021, and "
             "instructing the Attorney-General to preserve it"),
            ("United Nations High Commissioner for Human Rights", "2", "20",
             "regretted the execution of a man in Alabama by suffocation using "
             "nitrogen gas, warning that it might amount to torture or cruel, "
             "inhuman and degrading treatment"),
        ],
    ),
    "Equality & non-discrimination": (
        Grade.C,
        "No comprehensive federal anti-discrimination legislation was adopted; "
        "supported recommendations to combat systemic racial discrimination were "
        "not implemented.",
        [
            ("Special Rapporteur on minority issues", "2", "15",
             "recommended adopting comprehensive national human rights legislation "
             "to include international human rights obligations, particularly on "
             "the recognition of the right to equality without discrimination"),
            ("Human Rights Watch", "3", "9",
             "the USA had not implemented UPR supported recommendations to combat "
             "systemic racial discrimination, further entrenching discriminatory "
             "practices"),
        ],
    ),
    "Migrants": (
        Grade.E,
        "Measures run directly counter to these recommendations: asylum access "
        "was severely curtailed, detention without due process expanded and "
        "family separation resumed.",
        [
            ("Human Rights Committee", "2", "69",
             "measures adopted to address migration challenges excessively "
             "restricted protection of the right to seek asylum and increased the "
             "risk of breaches of the principle of refoulement"),
            ("Several special procedure mandate holders", "2", "64",
             "the misuse of the Alien Enemies Act by the Government of the United "
             "States to deny due process and enable arbitrary deportations, "
             "involving enforced disappearances"),
            ("JS47", "3", "90",
             "at the US-Mexico border, asylum had been all but eliminated; "
             "migration enforcement escalated focusing on mass deportations"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        Grade.C,
        "Some special-procedure visits took place in 2021-2024, but no standing "
        "invitation was issued and cooperation deteriorated sharply in 2025.",
        [
            ("Several special procedure mandate holders", "2", "8",
             "condemned the United States sanctions against Francesca Albanese, "
             "Special Rapporteur on the situation of human rights in the "
             "Palestinian territories occupied since 1967, as a direct attack on "
             "the integrity of the United Nations human rights system"),
            ("Several United Nations experts", "2", "5",
             "alarmed by the escalating attacks by the United States on the "
             "international architecture of human rights"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        Grade.E,
        "The 2022 Dobbs decision removed the federal constitutional right to "
        "abortion; the Women's Health Protection Act did not pass and stakeholders "
        "report none of the supported SRHR recommendations were implemented.",
        [
            ("Several special procedure mandate holders", "2", "43",
             "the United States Supreme Court decision to strike down Roe v. Wade "
             "represented a setback for the rule of law and for gender equality"),
            ("JS3", "3", "57",
             "none of the supported recommendations on sexual health and "
             "reproductive rights had been implemented"),
            ("Human Rights Committee", "2", "43",
             "recommended adopting the Women's Health Protection Act"),
        ],
    ),
    "Racial discrimination": (
        Grade.C,
        "No national action plan against racism was adopted; systemic racism is "
        "still reported as persistent.",
        [
            ("Special Rapporteur on racism", "2", "12",
             "racially marginalized groups continued to experience persistent "
             "systemic racism"),
            ("Presbyterian Church (USA)", "3", "9",
             "racial discrimination remained pervasive"),
        ],
    ),
    "Right to health": (
        Grade.C,
        "No move toward universal healthcare or nationwide Medicaid expansion; "
        "health inequities persist and 2025 brought cancellation of health grants.",
        [
            ("Human Rights Watch", "3", "60",
             "systemic racism and the cost barriers of the predominantly "
             "for-profit health care system played a huge part in health "
             "inequities"),
            ("JS9; Human Rights Watch", "3", "59",
             "reported cancellation of grants for substance use and mental health "
             "programmes"),
        ],
    ),
    "International criminal & humanitarian law (including crimes against humanity, war crimes, genocide)": (
        Grade.E,
        "Contrary measures: sanctions on the ICC, transfer of cluster munitions, "
        "and pardons for contractors convicted of war crimes. Mostly 'noted'.",
        [
            ("Several special procedure mandate holders", "2", "25",
             "condemned the executive order imposing sanctions on the "
             "International Criminal Court ... by sanctioning the Court, the "
             "United States weakened the post-Nuremberg commitment to "
             "international criminal justice"),
            ("Special Rapporteur on torture and other cruel, inhuman or degrading "
             "treatment or punishment", "2", "23",
             "urged the United States to reconsider its decision to transfer "
             "cluster munitions to a third country as those weapons posed a "
             "serious and indiscriminate threat to civilians"),
            ("Several special procedure mandate holders", "2", "24",
             "the pardons granted to four private security contractors convicted "
             "for war crimes in a third country violated United States "
             "obligations under international law"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        Grade.C,
        "No national human rights institution has been established.",
        [
            ("Committee on the Elimination of Racial Discrimination", "2", "9",
             "reiterated its recommendation that the United States create a "
             "national human rights institution in accordance with the ... Paris "
             "Principles"),
            ("JS61; Elizka Relief Foundation", "3", "7",
             "the USA had not established a National Human Rights Institution "
             "(NHRI), resulting in a critical gap in the country's human rights "
             "protection framework"),
        ],
    ),
    "Discrimination against women": (
        Grade.C,
        "Persistent discrimination in wages, employment and education is reported; "
        "no federal equal-pay legislation was enacted and DEI policies were "
        "revoked in 2025.",
        [
            ("Elizka Relief Foundation", "3", "75",
             "persistent discrimination against women across various sectors such "
             "as wages, employment, and education"),
            ("Abshar; IESW", "3", "51",
             "recommended enacting federal legislation enforcing equal pay for "
             "equal work"),
        ],
    ),
    "Human rights education, trainings & awareness raising": (
        Grade.C,
        "Recommended human-rights and anti-bias training was not institutionalised; "
        "book bans and curriculum restrictions cut the other way.",
        [
            ("Special Rapporteur on racism", "2", "46",
             "recommended ... training all teachers and school staff in racial "
             "equality, implicit bias and non-discrimination standards"),
            ("Human Rights Watch", "3", "14",
             "regretted the growing movement that prevented educating students "
             "about structural racism, including banning books or censoring "
             "classroom discussions of race, sexuality and gender"),
        ],
    ),
    "Unilateral coercive measures": (
        Grade.C,
        "Unilateral sanctions regimes were maintained and expanded; all 'noted'.",
        [
            ("IPLSA (International Probono Legal Services Association)", "3", "30",
             "their prolonged and unchecked application raised concerns regarding "
             "compliance with international law and human rights standards ... "
             "thereby creating de facto perpetual states of emergency in those "
             "countries"),
            ("ADVT (Association for Defending Victims of Terrorism)", "3", "31",
             "recommended the USA to immediately lift all unilateral sanctions "
             "that negatively affect civilian populations"),
        ],
    ),
    "Right to life": (
        Grade.C,
        "No federal gun-violence legislation was enacted; the White House Office "
        "of Gun Violence Prevention was shut down in 2025.",
        [
            ("Human Rights Committee", "2", "19",
             "recommended that the United States prevent and reduce gun violence "
             "by strengthening legislative and policy measures requiring "
             "background checks for all private acquisitions and transfers of "
             "firearms and ammunition"),
            ("FOR-USA (Fellowship of Reconciliation-USA)", "3", "19",
             "In March 2025, the Gun Violence Federal Health Advisory and the "
             "White House Office of Gun Violence Prevention were shut down"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        Grade.C,
        "Some special-procedure visits occurred in 2021-2024, but no standing "
        "invitation was issued and a mandate holder was sanctioned in 2025.",
        [
            ("Several special procedure mandate holders", "2", "8",
             "condemned the United States sanctions against Francesca Albanese ... "
             "as a direct attack on the integrity of the United Nations human "
             "rights system"),
        ],
    ),
    "Violence against women": (
        Grade.C,
        "Persistent violence against women is still recorded as a serious concern, "
        "with Indigenous women and girls disproportionately affected and no "
        "comprehensive data; 2025 brought funding cuts.",
        [
            ("Human Rights Committee", "2", "53",
             "expressed concern about the persistence of violence against women "
             "and about Indigenous women and girls being disproportionally "
             "affected by violence, homicide and disappearances"),
            ("GFG (Global Freedom Group)", "3", "70",
             "reported funding cuts to the Violence Against Women Act and domestic "
             "violence programmes"),
        ],
    ),
    "Human rights & counter-terrorism": (
        Grade.B,
        "Twenty-five detainees were transferred from Guantanamo Bay since the last "
        "review and some conditions improved, but 15 men remain in indefinite "
        "detention and the facility is not closed.",
        [
            ("Amnesty International", "3", "28",
             "15 men were still arbitrarily and indefinitely detained at "
             "Guantanamo Bay, following the transfer of 25 detainees since the "
             "previous review"),
            ("Special Rapporteur on the promotion and protection of human rights "
             "and fundamental freedoms while countering terrorism", "2", "28",
             "urged the United States to close the Guantanamo Bay detention "
             "facility, while preserving it to ensure independent and effective "
             "investigation of torture"),
            ("Human Rights Committee", "2", "28",
             "recommended expediting the transfer of detainees designated for "
             "transfer from that facility and putting an end to administrative "
             "detention without charge or trial"),
        ],
    ),
    "Right to participate in public affairs & right to vote": (
        Grade.C,
        "Federal voting-rights legislation did not pass; state-level restrictions "
        "increased with a disproportionate impact on racially marginalised "
        "voters.",
        [
            ("Human Rights Committee", "2", "35",
             "expressed concern at the increasing number of legislative "
             "initiatives and practices at the state level limiting the right to "
             "vote, including partisan gerrymandering, restrictions on voting by "
             "mail and burdensome voter identification"),
            ("Special Rapporteur on minority issues; Special Rapporteur on racism",
             "2", "36",
             "recommended adopting the Freedom to Vote and the John R. Lewis "
             "Voting Rights Advancement Act"),
        ],
    ),
    "Inter-State cooperation and assistance": (
        Grade.C,
        "No relevant change; most of these recommendations were 'noted'.",
        [
            ("Several United Nations experts", "2", "5",
             "alarmed by the escalating attacks by the United States on ... "
             "multilateralism, the principles of sovereign equality and "
             "self-determination"),
        ],
    ),
    "Human rights & climate change": (
        Grade.E,
        "Contrary measures: renewed withdrawal from the Paris Agreement and 2025 "
        "executive orders reviving fossil fuels and abolishing decarbonisation "
        "targets.",
        [
            ("Human Rights Committee", "2", "50",
             "recommended that the United States intensify efforts to prevent and "
             "mitigate the effects of climate change and environmental "
             "degradation"),
            ("JS3", "3", "67",
             "the elimination of 70 climate change initiatives and the abolition "
             "of federal targets to reduce emissions and decarbonise by 2035"),
            ("GAF (Geneva Agape Foundation)", "3", "67",
             "several 2025 Executive Orders revisited some measures to reduce "
             "carbon dioxide emissions, increased the leasing of public lands to "
             "oil and gas development"),
        ],
    ),
    "Freedom of thought, conscience & religion": (
        Grade.C,
        "Religious intolerance and Islamophobia are reported to have risen; the "
        "recommended amendment of the Civil Rights Act was not made.",
        [
            ("Special Rapporteur on minority issues", "2", "59",
             "recommended amending the Civil Rights Act of 1964 to cover "
             "discrimination based on religion or belief"),
            ("JS33 (Othering & Belonging Institute; Council on American-Islamic "
             "Relations)", "3", "88",
             "an increase in Islamophobia in the USA through prejudicial views, "
             "discriminatory language, violence, and policing, profiling, "
             "surveillance, torture, and detention along racial/ethnic religious "
             "lines"),
        ],
    ),
    "Right to peaceful assembly": (
        Grade.E,
        "Contrary measures: disproportionate policing of protests, new laws "
        "criminalising protest, and deportation/visa action against student "
        "protesters.",
        [
            ("Special Rapporteur on the rights to freedom of peaceful assembly "
             "and of association", "2", "33",
             "authorities and law enforcement entities had responded "
             "disproportionately to peaceful student-led protests, with "
             "vilification, criminalization, sanctions, arrests, detentions and "
             "the use of excessive force"),
            ("Amnesty International", "3", "37",
             "the introduction of bills restricting the right to protest, "
             "criminalising specific forms of protest, and the use of vague and "
             "broad laws to suppress protest movements"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        Grade.C,
        "The Human Rights Committee still recommends redoubling efforts and "
        "stakeholders report continuing failures in victim identification.",
        [
            ("Human Rights Committee", "2", "38",
             "recommended that the United States redouble its efforts to combat "
             "trafficking in persons by improving victim identification, "
             "strengthening its preventive measures"),
            ("JS22", "3", "49",
             "reported failures in identifying and supporting victims and securing "
             "criminal convictions"),
        ],
    ),
    "Human rights & poverty": (
        Grade.C,
        "Around 40 million people live in poverty; stakeholders report no measures "
        "on the structural drivers and expanding criminalisation of poverty.",
        [
            ("Independent Expert on the enjoyment of human rights by persons with "
             "albinism", "2", "39",
             "income inequalities remained high in the United States, with some 40 "
             "million people reportedly living in poverty"),
            ("Special Rapporteur on racism", "2", "39",
             "referred to reports of the criminalization of poverty, which trapped "
             "people in the criminal justice system"),
        ],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        Grade.C,
        "No inter-agency federal body for follow-up to UN recommendations was "
        "established. Both 'noted'.",
        [
            ("Special Rapporteur on minority issues", "2", "10",
             "recommended establishing an inter-agency federal body responsible "
             "for implementation of and follow-up to United Nations human rights "
             "mechanisms' recommendations"),
        ],
    ),
    "Business & Human Rights": (
        Grade.C,
        "No updated national action plan; mandatory human-rights due-diligence "
        "legislation was not adopted.",
        [
            ("Several special procedure mandate holders", "2", "51",
             "urged businesses in the United States to reaffirm their commitment "
             "to diversity, equity and inclusion principles, uphold their human "
             "rights responsibilities under the Guiding Principles on Business and "
             "Human Rights"),
            ("JS65", "3", "69",
             "requested the USA to require businesses to conduct human rights due "
             "diligence in conflict-affected contexts and develop policies to "
             "protect human rights defenders"),
        ],
    ),
    "Right to physical & moral integrity": (
        Grade.C,
        "No federal use-of-force legislation and reversal of the 2022 "
        "accountable-policing executive order.",
        [
            ("International Independent Expert Mechanism to Advance Racial Justice "
             "and Equality in Law Enforcement; Special Rapporteur on minority "
             "issues; High Commissioner", "2", "17",
             "expressed concern about police killings of and violence and "
             "brutality towards African Americans"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        Grade.E,
        "Stakeholders and special procedures report a decline in freedom of "
        "expression: visa revocations for speech, use of the Espionage Act, and "
        "pressure on journalists.",
        [
            ("Several submissions (OHCHR summary)", "3", "36",
             "a decline in freedom of opinion and expression, including "
             "unjustified restrictions on media content, narrowing digital "
             "spaces, and threats against journalists and whistleblowers"),
            ("Special Rapporteur on the right to education", "2", "33",
             "warned that those attacks signalled an erosion of intellectual "
             "freedom and democratic principles in educational settings"),
        ],
    ),
    "Human rights defenders": (
        Grade.C,
        "No policy framework to protect human rights defenders was adopted.",
        [
            ("JS65", "3", "69",
             "requested the USA to ... develop policies to protect human rights "
             "defenders"),
        ],
    ),
    "Cooperation & follow up with the Universal Periodic Review (UPR)": (
        Grade.C,
        "No cycle-3 UPR mid-term report and no dedicated national follow-up "
        "mechanism.",
        [
            ("Special Rapporteur on minority issues", "2", "10",
             "recommended establishing an inter-agency federal body responsible "
             "for implementation of and follow-up to United Nations human rights "
             "mechanisms' recommendations"),
        ],
    ),
    "Constitutional & legislative framework": (
        Grade.C,
        "No relevant constitutional or legislative reform; recommendation 'noted'.",
        [
            ("JS15", "3", "8",
             "the 1798 Alien Enemies Act being used to deport natives, citizens "
             "and foreigners without a hearing or standard process"),
        ],
    ),
    "Human rights & toxics / hazardous wastes": (
        Grade.C,
        "Toxic-waste clean-up in disproportionately affected communities was still "
        "being urged; no national plan. 'Noted'.",
        [
            ("Special Rapporteur on racism", "2", "49",
             "recommended urgently cleaning up toxic waste and environmental "
             "contamination, particularly in areas where it was having a "
             "disproportionate impact on marginalized racial and ethnic groups, "
             "including in the overseas territories"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        Grade.C,
        "No specific federal offence of torture was enacted; rendition-programme "
        "victims remain uncompensated.",
        [
            ("Human Rights Committee", "2", "21",
             "the United States should review its position regarding the "
             "establishment of a specific offence of torture, enact legislation "
             "prohibiting torture in line with international law"),
            ("Special Rapporteur on ... human rights ... while countering "
             "terrorism", "2", "27",
             "none of the former detainees had been compensated for the "
             "systematic crimes of extraordinary rendition, torture, cruel, "
             "inhuman and degrading treatment and arbitrary detention"),
        ],
    ),
    "Arbitrary arrest & detention": (
        Grade.C,
        "No indication of change; recommendation 'noted'.",
        [
            ("Committee on the Elimination of Racial Discrimination", "2", "26",
             "highlighted the continued arbitrary detention of non-citizens at "
             "the Guantanamo Bay facility, without effective and equal access to "
             "the ordinary criminal justice system"),
        ],
    ),
    "Legal & institutional reform": (
        Grade.C,
        "The composite reforms sought saw no relevant legislative action.",
        [
            ("International Independent Expert Mechanism to Advance Racial Justice "
             "and Equality in Law Enforcement", "2", "30",
             "systemic racism had manifested in the disproportionate "
             "incarceration and harsher sentencing of Black individuals, "
             "perpetuating structural inequality and limiting access to justice"),
        ],
    ),
    "Labour rights and right to work": (
        Grade.C,
        "Forced prison labour continues and the right to work is reported to have "
        "worsened, with mass terminations of federal employees in 2025.",
        [
            ("Special Rapporteur on racism", "2", "30",
             "referred to reports of poorly paid or unpaid forced labour by "
             "prisoners, who were disproportionately from racially marginalized "
             "groups"),
            ("Elizka Relief Foundation", "3", "50",
             "observed a worsening of the right to work, including reduction and "
             "terminations of federal employees and precarious employment of "
             "migrants"),
        ],
    ),
    "Right to adequate housing": (
        Grade.C,
        "Governments at all levels are reported to have failed to meet the right "
        "to housing; laws banning sleeping in public spaces spread.",
        [
            ("Committee on the Elimination of Racial Discrimination; Human Rights "
             "Committee", "2", "42",
             "expressed concern about the high number of persons belonging to "
             "racial and ethnic minorities affected by homelessness and "
             "recommended abolishing laws and policies that criminalized "
             "homelessness"),
            ("Human Rights Watch", "3", "53",
             "governments at all levels had failed to meet the right to housing"),
        ],
    ),
    "Right to an adequate standard of living": (
        Grade.C,
        "No measures to address structural poverty and inequality; the situation "
        "is reported to have deteriorated.",
        [
            ("Special Rapporteur on racism", "2", "39",
             "expressed concern about significant racial income and wealth gaps, "
             "driven by employment-related discrimination, systemic racism and "
             "historical government divestment"),
        ],
    ),
    "Right to education": (
        Grade.C,
        "Systemic funding inequities persist, book bans expanded, and the "
        "Department of Education is reported to be being dismantled.",
        [
            ("Special Rapporteur on the right to education", "2", "45",
             "identified systemic inequalities in the education system, including "
             "inequitable funding, overreliance on standardized testing, "
             "discriminatory disciplinary practices and the diversion of public "
             "funds to private and charter schools"),
            ("JS6", "3", "62",
             "expressed concern at the dismantling of the Education Department"),
        ],
    ),
    "Advancement of women": (
        Grade.C,
        "Persistent gender inequality in the workforce and leadership is reported, "
        "aggravated by the 2025 DEI revocation.",
        [
            ("IPWR (Institute for Protection of Women's Rights)", "3", "76",
             "the persistent gender inequality in the workforce ... Women, "
             "particularly women of colour, were significantly underrepresented "
             "in leadership roles and high-paying occupations"),
        ],
    ),
    "Children: definition": (
        Grade.C,
        "Racial disparities in the child-welfare system persist; recommended "
        "due-process protections for parents were not adopted.",
        [
            ("Committee on the Elimination of Racial Discrimination", "2", "54",
             "expressed concern about the disproportionate number of children "
             "from racial and ethnic minorities removed from their families and "
             "placed in foster care"),
            ("Human Rights Committee", "2", "54",
             "recommended increasing due process protections for parents and "
             "reviewing the factors triggering child welfare interventions, in "
             "particular poverty and lack of financial resources"),
        ],
    ),
    "Indigenous peoples": (
        Grade.E,
        "Contrary measures: the Tribal self-determination executive order was "
        "revoked in 2025; treaties remain unhonoured and FPIC is not guaranteed.",
        [
            ("Committee on the Elimination of Racial Discrimination; Human Rights "
             "Committee", "2", "58",
             "recommended that the United States honour the treaties entered into "
             "with Indigenous Peoples, guarantee, in law and in practice, the "
             "principle of free, prior and informed consent"),
            ("Several submissions (OHCHR summary)", "3", "83",
             "Executive Order 14112, which had expanded access of Tribal Nations "
             "to federal funding and self-determination in education, healthcare "
             "and land management, was revoked in March 2025"),
        ],
    ),
}

_FALLBACK = (
    Grade.D,
    "No cluster rule matched and the evidence base contains no specific "
    "information on this recommendation.",
    [],
)

# Short action phrase per theme, shown in parentheses after the rec numbers.
SUMMARIES: dict[str, str] = {
    "Ratification of & accession to international instruments":
        "Ratify outstanding international human rights treaties",
    "Administration of justice & fair trial":
        "Police use of force, racial profiling and accountability",
    "Death penalty": "Federal moratorium on / abolition of the death penalty",
    "Equality & non-discrimination":
        "Comprehensive anti-discrimination legislation",
    "Migrants": "Asylum access, immigration detention and deportations",
    "Cooperation with human rights mechanisms & requests for technical assistance":
        "Rescind ICC sanctions and re-engage with UN mechanisms",
    "Sexual & reproductive health and rights":
        "Access to abortion and maternal health care",
    "Racial discrimination": "Combat systemic racism and hate speech",
    "Right to health": "Equitable, affordable access to health care",
    "International criminal & humanitarian law (including crimes against humanity, war crimes, genocide)":
        "ICC, accountability for war crimes and drone strikes",
    "National Human Rights Institution (NHRI)":
        "Establish a Paris-Principles-compliant NHRI",
    "Discrimination against women":
        "Combat discrimination against women in work, pay and public life",
    "Human rights education, trainings & awareness raising":
        "Human rights and anti-bias training and education",
    "Right to life": "Prevent gun violence",
    "Unilateral coercive measures": "Lift unilateral sanctions / embargoes",
    "Cooperation & Follow up with Special Procedures":
        "Standing invitation to special procedures and visit requests",
    "Violence against women": "Eliminate violence against women and girls",
    "Human rights & counter-terrorism":
        "Close Guantanamo and end indefinite detention",
    "Right to participate in public affairs & right to vote":
        "Protect voting rights and restore Voting Rights Act protections",
    "Inter-State cooperation and assistance":
        "International cooperation and non-interference",
    "Human rights & climate change": "Climate-change mitigation and adaptation",
    "Freedom of thought, conscience & religion":
        "Combat religious intolerance and Islamophobia",
    "Right to peaceful assembly": "Protect the right to peaceful assembly",
    "Human trafficking & contemporary forms of slavery":
        "Combat trafficking in persons",
    "Human rights & poverty": "Address poverty, inequality and its criminalisation",
    "National Mechanisms for Reporting & Follow-up (NMRF)":
        "Establish a national reporting and follow-up mechanism",
    "Business & Human Rights":
        "Business and human rights, including mandatory due diligence",
    "Right to physical & moral integrity": "End excessive use of force",
    "Freedom of opinion and expression & access to information":
        "Protect freedom of expression, journalists and whistle-blowers",
    "Human rights defenders": "Protect human rights defenders",
    "Cooperation & follow up with the Universal Periodic Review (UPR)":
        "UPR follow-up mechanism and mid-term report",
    "Constitutional & legislative framework": "Reform the Alien Enemies Act",
    "Human rights & toxics / hazardous wastes":
        "Clean up toxic contamination affecting minority communities",
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)":
        "Criminalise torture and provide redress for rendition victims",
    "Arbitrary arrest & detention": "End arbitrary detention",
    "Legal & institutional reform": "Legal and institutional reforms",
    "Labour rights and right to work":
        "Working conditions, minimum wage and forced prison labour",
    "Right to adequate housing":
        "Realise the right to housing and decriminalise homelessness",
    "Right to an adequate standard of living":
        "Reduce poverty and racial income and wealth gaps",
    "Right to education": "Equitable, quality public education",
    "Advancement of women": "Women's participation in work and leadership",
    "Children: definition":
        "Racial equity in child welfare and parental due process",
    "Indigenous peoples":
        "Honour Indigenous treaties and guarantee free, prior and informed consent",
}
_FALLBACK_SUMMARY = "Miscellaneous"

# --- keyword overrides: (regex on text, grade, rationale, [quotes]) ----------
KEYWORDS: list[tuple[str, Grade, str, list[Quote]]] = [
    (
        r"Paris Agreement|Paris Climate",
        Grade.E,
        "The United States rejoined the Paris Agreement in 2021 but withdrew again "
        "in 2025 - a reversal of the step recommended.",
        [
            ("Several United Nations experts", "2", "5",
             "expressed concern over the country's withdrawal from key "
             "international agreements and institutions, including the Paris "
             "Agreement, the Human Rights Council and World Health Organization"),
            ("Several submissions (OHCHR summary)", "3", "6",
             "Recommendations were made to the USA to re-engage with the Human "
             "Rights Council, reverse the decisions to withdraw from the Paris "
             "Climate Agreement"),
        ],
    ),
    (
        r"(re-?engage|rejoin|resume|reconsider the withdrawal from|return to)"
        r"[\w\s,]{0,60}Human Rights Council",
        Grade.E,
        "The United States withdrew from the Human Rights Council in 2025, "
        "contrary to the recommendation to re-engage.",
        [
            ("Several United Nations experts", "2", "5",
             "expressed concern over the country's withdrawal from key "
             "international agreements and institutions, including the Paris "
             "Agreement, the Human Rights Council and World Health Organization"),
            ("Several submissions (OHCHR summary)", "3", "6",
             "Recommendations were made to the USA to re-engage with the Human "
             "Rights Council"),
        ],
    ),
    (
        r"International Criminal Court|Rome Statute|Executive Order (No\. )?13928",
        Grade.E,
        "The recommendation was to lift or rescind the sanctions on the "
        "International Criminal Court; instead the United States maintained them "
        "and in 2025 imposed further sanctions (Executive Order 14203), including "
        "against the Court's judges and staff.",
        [
            ("Several special procedure mandate holders", "2", "25",
             "condemned the executive order imposing sanctions on the "
             "International Criminal Court ... by sanctioning the Court, the "
             "United States weakened the post-Nuremberg commitment to "
             "international criminal justice"),
            ("Several submissions (OHCHR summary)", "3", "6",
             "Recommendations were made to the USA to ... rescind the Executive "
             "Order 14203 sanctioning the ICC and its staff"),
            ("United Nations High Commissioner for Human Rights", "2", "25",
             "expressed concerns about sanctions against judges of the Court and "
             "called for the prompt reconsideration and withdrawal of those "
             "measures"),
        ],
    ),
    (
        r"death penalty|moratorium on executions|capital punishment|Second Optional Protocol",
        Grade.E,
        "Executive Order 14164 (2025) reinstated and directed preservation of the "
        "federal death penalty, reversing the 2021 moratorium; executions "
        "resumed.",
        [
            ("Human Rights Committee", "2", "20",
             "recommended establishing a de jure moratorium on the death penalty "
             "at the federal level and taking steps towards its abolition"),
            ("The Dui Hua Foundation", "3", "15",
             "Executive Order 14164 reinstating capital punishment for federal "
             "crimes, for which a moratorium had been imposed in 2021"),
        ],
    ),
    (
        r"free, prior and informed consent|indigenous|treaties (entered into|with).*[Ii]ndigenous|tribal",
        Grade.E,
        "Executive Order 14112 on Tribal self-determination and funding was "
        "revoked in March 2025; FPIC is still not guaranteed in law or practice.",
        [
            ("Committee on the Elimination of Racial Discrimination; Human Rights "
             "Committee", "2", "58",
             "recommended that the United States honour the treaties entered into "
             "with Indigenous Peoples, guarantee, in law and in practice, the "
             "principle of free, prior and informed consent"),
            ("Several submissions (OHCHR summary)", "3", "83",
             "Executive Order 14112, which had expanded access of Tribal Nations "
             "to federal funding and self-determination ... was revoked in March "
             "2025"),
        ],
    ),
    (
        r"diversity, equity and inclusion|\bDEI\b|affirmative action",
        Grade.E,
        "2025 executive orders revoked diversity, equity and inclusion "
        "programmes; affirmative action in college admissions was struck down.",
        [
            ("Several special procedure mandate holders", "2", "52",
             "deeply concerned about the Government's revocation of diversity, "
             "equity and inclusion policies, warning that it had undermined "
             "workplace inclusivity and reinforced structural inequalities and "
             "discrimination"),
            ("Special Rapporteur on racism", "2", "47",
             "recommended considering the reinstatement of affirmative action in "
             "college admissions in both state and federal law"),
        ],
    ),
    (
        r"sexual orientation|gender identity|lesbian, gay|transgender|LGBT",
        Grade.E,
        "2025 executive orders and state-level actions targeting LGBTI people are "
        "retrogressive; the Equality Act did not pass.",
        [
            ("Independent Expert on protection against violence and discrimination "
             "based on sexual orientation and gender identity", "2", "62",
             "concerned by a widespread set of state-level legislative, executive "
             "and judicial actions aimed at regression in the protection of the "
             "human rights of LGBT persons"),
            ("Human Rights Watch", "3", "89",
             "the USA had enacted policies that reinforced discrimination against "
             "LGBT people"),
        ],
    ),
    (
        r"asylum|refoulement|non-refoulement|immigration detention|family separation|family reunification",
        Grade.E,
        "Access to asylum was severely curtailed, detention without due process "
        "expanded and family separation resumed - directly contrary measures.",
        [
            ("Human Rights Committee", "2", "69",
             "measures adopted to address migration challenges excessively "
             "restricted protection of the right to seek asylum and increased the "
             "risk of breaches of the principle of refoulement"),
            ("JS47", "3", "90",
             "at the US-Mexico border, asylum had been all but eliminated"),
        ],
    ),
    (
        r"(eliminat|combat|eradicat|prevent|address|end).{0,40}violence against women"
        r"|violence against women and girls|gender-based violence|domestic violence",
        Grade.B,
        "The Violence Against Women Act was reauthorised in 2022 with expanded "
        "tribal-jurisdiction provisions - a concrete step - but implementation "
        "gaps persist and 2025 brought funding cuts.",
        [
            ("Human Rights Committee", "2", "53",
             "recommended intensifying efforts to prevent, combat and eradicate "
             "all forms of violence against women and girls, paying special "
             "attention to women from minority and marginalized groups"),
            ("GFG (Global Freedom Group)", "3", "70",
             "reported funding cuts to the Violence Against Women Act and domestic "
             "violence programmes"),
        ],
    ),
]


# Short action phrase per keyword rule, aligned by index to KEYWORDS above.
KW_SUMMARIES = [
    "Rejoin / remain in the Paris Agreement",
    "Re-engage with the Human Rights Council",
    "Rescind sanctions on the International Criminal Court",
    "Federal moratorium on / abolition of the death penalty",
    "Honour Indigenous treaties and guarantee free, prior and informed consent",
    "Maintain diversity, equity and inclusion measures and affirmative action",
    "Prohibit discrimination based on sexual orientation and gender identity",
    "Protect access to asylum and non-refoulement; limit immigration detention",
    "Eliminate violence against women and girls",
]
assert len(KW_SUMMARIES) == len(KEYWORDS), "KW_SUMMARIES out of sync with KEYWORDS"


def choose(theme_primary: str, text: str):
    grade, rationale, quotes = CLUSTERS.get(theme_primary, _FALLBACK)
    summary = SUMMARIES.get(theme_primary, _FALLBACK_SUMMARY)
    for i, (pattern, g, r, q) in enumerate(KEYWORDS):
        if re.search(pattern, text, re.IGNORECASE):
            grade, rationale, quotes, summary = g, r, q, KW_SUMMARIES[i]
    return grade, summary, rationale, quotes


def main() -> None:
    repo = RecommendationRepository(ROOT / "recommendations.db")
    recs = repo.list()
    rows_out = []
    tally: dict[str, int] = {}
    for rec in recs:
        primary = (rec.themes or "").split(";")[0].strip()
        grade, summary, rationale, quotes = choose(primary, rec.text)
        sources = fmt_sources(quotes)
        evidence = fmt_evidence(quotes)
        repo.set_grade(rec.id, grade, rationale=rationale, sources=sources,
                       evidence=evidence, action=summary)
        tally[grade.value] = tally.get(grade.value, 0) + 1
        rows_out.append(
            {
                "paragraph": rec.paragraph,
                "recommending_state": rec.recommending_state,
                "position": rec.position.value,
                "primary_theme": primary,
                "action_summary": summary,
                "grade": grade.value,
                "grade_label": grade.label,
                "text": rec.text,
                "rationale": rationale,
                "sources": sources,
                "evidence_quotes": evidence,
            }
        )

    rows_out.sort(
        key=lambda r: int(r["paragraph"].split(".")[1])
        if r["paragraph"] and "." in r["paragraph"] else 0
    )
    out_csv = ROOT / "output" / "us_cycle3_implementation_assessment.csv"
    out_csv.parent.mkdir(exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows_out[0].keys()))
        w.writeheader()
        w.writerows(rows_out)

    print(f"Assessed {len(recs)} recommendations.")
    for g in Grade:
        if tally.get(g.value):
            print(f"  {g.value:<13} {tally[g.value]:>3}   {g.label}")
    print(f"\nCSV written: {out_csv.relative_to(ROOT)}")
    repo.close()


if __name__ == "__main__":
    main()
