"""Hungary — implementation assessment of its 3rd-cycle (2021, A/HRC/49/8) UPR
recommendations, graded against the 4th-cycle documentation (session 53):
National Report A/HRC/WG.6/53/HUN/1, OHCHR Compilation /2 and Stakeholders'
Summary /3.

    python scripts/run_assess.py hungary

First pass for expert review. Quotes are verbatim from the three documents.
The National Report covers only the term of the previous Government (it states
that this "represent[s] very limited progress"); measures of the Government
formed on 12 May 2026 are not covered.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Equality & non-discrimination": (
        B, "Combat hate speech, hate crime and discrimination",
        "Hungary criminalised online aggression (January 2025) and denial or "
        "trivialisation of crimes against humanity (March 2025), made hate-crime "
        "training mandatory for all police and adopted a National Strategy "
        "against Antisemitism (June 2024); the Special Rapporteur on freedom "
        "of religion reports that anti-Muslim hatred remains widespread.",
        [
            ("Hungary", "1", "19", "Section 332 of the Criminal Code was supplemented with a new paragraph (2)"),
            ("Hungary", "1", "18", "The curriculum consists of four modules: hate crimes, indicators of discrimination, victims and intersectionality, and law enforcement duties"),
            ("Hungary", "1", "23", "In June 2024 Hungary adopted its National Strategy against Antisemitism"),
            ("Special Rapporteur on freedom of religion", "2", "15", "anti-Muslim hatred, or Islamophobia, and discrimination against Muslims remained widespread in Hungarian society"),
        ],
    ),
    "Violence against women": (
        B, "Prevent and respond to domestic and sexual violence",
        "Hungary introduced a preventive restraining order that survives "
        "release from prison (August 2025), extended victim-support rights, "
        "reviewed 31,139 police domestic-violence cases and created a network "
        "of specialised investigators, and funds 20 crisis centres; CEDAW "
        "still calls for a comprehensive law on gender-based violence.",
        [
            ("Hungary", "1", "49", "Act LXXII of 2009 was supplemented with a new type of restraining order (preventive restraining order)"),
            ("Hungary", "1", "45", "a nationwide review was conducted on the handling of reports and criminal proceedings related to domestic violence by the police, covering 31139 cases"),
            ("Committee on the Elimination of Discrimination against Women", "2", "61", "recommended that Hungary adopt a comprehensive law on gender-based violence against women"),
        ],
    ),
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments",
        "No ratification is reported; the National Report states only that "
        "Hungary is party to most conventions, and UNESCO and stakeholders "
        "continue to recommend ratification.",
        [
            ("Hungary", "1", "8", "Hungary is State Party to the majority of international and European human rights conventions and most of their protocols"),
            ("UNESCO", "2", "2", "recommended ratifying the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights"),
        ],
    ),
    "Right to education": (
        B, "Equal access to quality education, including for Roma and minority children",
        "Hungary adopted Act XCII of 2023 on anti-discrimination measures in "
        "public education (from January 2024), supports about 700 "
        "underperforming or segregated schools, runs a dropout early-warning "
        "system and 112 minority-run institutions; the Special Rapporteur on "
        "the right to education warns of widening inequality and Roma "
        "segregation.",
        [
            ("Hungary", "1", "69", "Act XCII of 2023 on anti-discrimination measures applicable in the field of public education entered into force on 1 January 2024"),
            ("Hungary", "1", "78", "provides methodological support to approximately 700 underperforming or segregated institutions"),
            ("Special Rapporteur on the right to education", "2", "44", "expressing serious concern about widening inequalities, curriculum rigidity, the marginalization of Roma students and the erosion of academic freedom"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        C, "Protect media freedom and pluralism, and academic freedom",
        "The National Report has no section on media pluralism or media "
        "regulation; the Special Rapporteur on freedom of expression still "
        "calls for a legal framework on media independence and a reformed "
        "Media Council, and the Special Rapporteur on the right to education "
        "reports an erosion of academic freedom.",
        [
            ("Special Rapporteur on freedom of expression", "2", "26", "recommended that Hungary adopt a legal and policy framework, through an inclusive multi-stakeholder process, to promote media independence and pluralism"),
            ("Special Rapporteur on freedom of expression", "2", "29", "called for the independence, transparency and accountability of the Media Council, including through legislative reforms"),
            ("Scholars at Risk", "3", "38", "urged Hungary to commit publicly to restoring academic freedom and related human rights"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Implement national action plans and strategies",
        "Hungary adopted a 2025-2027 action plan under the National Social "
        "Inclusion Strategy 2030, an Implementation Plan 2025-2026 for the "
        "women's action plan and a new National Disability Programme "
        "(2026-2036); the National Report calls overall progress very limited.",
        [
            ("Hungary", "1", "107", "the action plan for the years 2025–2027, adopted by Government Resolution No. 1219/2025"),
            ("Hungary", "1", "89", "The new NDP (2026–2036) aims to define the policy directions and identify the key areas of cross-sectoral and non-governmental cooperation"),
            ("Hungary", "1", "1", "overall, represent very limited progress toward fulfilling the recommendations"),
        ],
    ),
    "Racial discrimination": (
        B, "Prevent racism and racial hate crime, and implement anti-discrimination law",
        "Police hate-crime training became mandatory, a Handbook on handling "
        "hate crimes was issued and Criminal Code section 332 was extended in "
        "2025; stakeholders ask for vigorous prosecution and awareness "
        "campaigns.",
        [
            ("Hungary", "1", "18", "were made mandatory for all police personnel"),
            ("Hungary", "1", "21", "The Hungarian media law expressly prohibits publishing press and media content that incites hatred"),
            ("JS2", "3", "5", "recommended to take effective measures to prevent and combat hate speech, racial discrimination, and violence against Roma"),
        ],
    ),
    "Good governance & corruption": (
        B, "Strengthen the independence of the judiciary",
        "Act X of 2023 strengthened the National Judicial Council, made the "
        "allocation of cases in the Curia transparent and removed obstacles to "
        "preliminary references to the CJEU; the Helsinki Committee asks for "
        "its effective implementation.",
        [
            ("Hungary", "1", "25", "Act X of 2023 strengthened the role and powers of the National Judicial Council (OBT) in order to balance the powers of the President of the National Judicial Office (OBH)"),
            ("Hungary Helsinki Committee", "3", "12", "requested the effective implementation of the prerogatives of the National Judicial Council introduced by the 2023 judicial reform"),
        ],
    ),
    "Participation of women in political & public life": (
        C, "Increase women's participation in political and public life",
        "Hungary reports statistics (women are 40% of leaders) and a draft "
        "law on gender balance among directors of listed companies, but no "
        "measure to raise women's political representation.",
        [
            ("Hungary", "1", "36", "women accounted for 40% of leaders in Hungary in 2024"),
            ("Hungary", "1", "35", "a draft law was submitted to the National Assembly on 29 October 2024"),
        ],
    ),
    "Cooperation & consultation with civil society": (
        C, "Enable civil society and human rights defenders to work freely",
        "The National Report reports no new enabling measure and admits that "
        "the previous Government did not consult civil society on the report; "
        "stakeholders point to the Transparency of Public Life bill.",
        [
            ("Hungary", "1", "3", "The previous Government of Hungary failed to conduct consultations with civil society organizations regarding the current national report"),
            ("JS5", "3", "17", "formally withdraw the Transparency of Public Life bill to ensure that legislation does not restrict the lawful activities of civil society"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Strengthen the Commissioner for Fundamental Rights",
        "The Commissioner's budget rose from HUF 2.134 billion in 2021 to "
        "HUF 3.369 billion in 2026; however, the Commissioner was downgraded "
        "to B status by GANHRI in 2021 and the Special Rapporteur advises a "
        "thorough review of its functioning.",
        [
            ("Hungary", "1", "16", "Its budget increased from 2,134 billion HUF in 2021 to 3,369 billion HUF in 2026"),
            ("Special Rapporteur on freedom of religion", "2", "3", "had been downgraded to B status in 2021"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Combat trafficking in persons and protect victims",
        "Hungary implemented an action plan under the 2020-2023 national "
        "strategy (prevention programmes in care institutions), earmarked HUF "
        "1 billion under the Swiss-Hungarian programme, ran a referral "
        "mechanism exercise (July 2025) and provided for guardians for "
        "unaccompanied minors; CEDAW asks for adequate resources.",
        [
            ("Hungary", "1", "115", "introduced prevention programmes in the foster care network, children’s and group homes and juvenile correctional institutions"),
            ("Hungary", "1", "116", "1 billion HUF is earmarked for action to combat trafficking in human beings"),
            ("Committee on the Elimination of Discrimination against Women", "2", "38", "recommended that Hungary ensure sufficient human, technical and financial resources for the effective implementation and monitoring of the National Strategy against Trafficking in Human Beings for 2020–2023"),
        ],
    ),
    "Labour rights and right to work": (
        B, "Narrow the gender pay gap and improve women's employment",
        "The net gender pay gap fell from 15.1% (2021) to 13% (2025), wages "
        "rose in female-dominated public sectors and a working group was "
        "created to prepare transposition of the EU Pay Transparency "
        "Directive; transposition is not completed.",
        [
            ("Hungary", "1", "56", "The difference between the net average earnings of full-time employed men and women was 15,1% in 2021 and 13% in 2025"),
            ("Hungary", "1", "56", "including the creation of a working group to prepare transposition proposals"),
            ("Hungary", "1", "57", "The employer may not terminate the employment relationship by notice during the period of paternity leave, parental leave or carer worktime allowance"),
        ],
    ),
    "Constitutional & legislative framework": (
        C, "Review legislation affecting civil society, migrants and gender recognition",
        "The National Report describes no review; UNHCR recommends amending "
        "asylum legislation and stakeholders ask for repeal of laws "
        "restricting civil society.",
        [
            ("UNHCR", "2", "9", "recommended that Hungary amend its national legislation to safeguard the right to seek and enjoy asylum and the prohibition of refoulement"),
            ("JS5", "3", "17", "formally withdraw the Transparency of Public Life bill to ensure that legislation does not restrict the lawful activities of civil society"),
        ],
    ),
    "Freedom of association": (
        E, "Protect freedom of association, peaceful assembly and expression",
        "In 2025 Parliament adopted Act III of 2025 amending the Right of "
        "Assembly Act, which effectively bans Pride and other assemblies "
        "deemed to violate the 'child protection' laws, with fines for "
        "participants and criminal liability for organisers, later reinforced "
        "by a constitutional amendment: a measure contrary to the "
        "recommendation.",
        [
            ("JS4", "3", "14", "Hungary’s Parliament adopted, under an accelerated procedure and without meaningful consultation, Act III of 2025, amending Act LV of 2018 on the right of assembly"),
            ("OHCHR", "2", "73", "legislation passed that had resulted in arbitrary and discriminatory restrictions on the rights of LGBTIQ+ individuals to freedom of expression, peaceful assembly and privacy"),
        ],
    ),
    "Migrants": (
        C, "Protect the rights of migrants and refugees; end pushbacks",
        "The National Report contains no information on asylum or migration "
        "policy; stakeholders report continuing pushbacks and a state of "
        "crisis due to mass migration, and the Special Rapporteur on freedom "
        "of religion reports anti-migrant rhetoric.",
        [
            ("JS4", "3", "68", "ending the practice of pushbacks at Hungary’s borders"),
            ("JS4", "3", "67", "called to end the state of crisis due to mass migration"),
            ("Special Rapporteur on freedom of religion", "2", "78", "requested that Hungary confront the discriminatory anti-migrant and racist rhetoric that had marred the political and media space, had put asylum-seekers at risk of refoulement"),
        ],
    ),
    "Business & Human Rights": (
        D, "Business and human rights legislation and national action plan",
        "The documents contain no information on this ask.", [],
    ),
    "Rights related to marriage & family": (
        A, "Strengthen policies supporting the family",
        "Hungary doubled the family tax benefit (2025), exempted mothers of "
        "three children from personal income tax (October 2025) and raised "
        "the infant-care benefit to 100% of earnings (July 2021).",
        [
            ("Hungary", "1", "60", "The amount of family tax benefit doubled in 2025"),
            ("Hungary", "1", "61", "As of July 2021, the amount of the infant care benefit increased from 70% to 100% of the eligible gross earnings"),
        ],
    ),
    "Scope of international obligations": (
        C, "Respect asylum, non-refoulement and international judgments",
        "No measure is reported; UNHCR and stakeholders call for access to "
        "asylum and an end to pushbacks.",
        [
            ("JS4", "3", "68", "ending the practice of pushbacks at Hungary’s borders"),
            ("UNHCR", "2", "9", "recommended that Hungary amend its national legislation to safeguard the right to seek and enjoy asylum and the prohibition of refoulement"),
        ],
    ),
    "Refugees & asylum seekers": (
        C, "Respect non-refoulement and individual assessment in asylum procedures",
        "No measure is reported; UNHCR and stakeholders call for access to "
        "asylum and an end to pushbacks.",
        [
            ("JS4", "3", "68", "ending the practice of pushbacks at Hungary’s borders"),
            ("UNHCR", "2", "9", "recommended that Hungary amend its national legislation to safeguard the right to seek and enjoy asylum and the prohibition of refoulement"),
        ],
    ),
    "Legal & institutional reform": (
        B, "Strengthen the institutional human rights infrastructure",
        "A Human Rights Working Group monitors implementation of accepted "
        "UPR recommendations and a Human Rights Roundtable counts 76 civil "
        "society organisations.",
        [
            ("Hungary", "1", "17", "monitors the implementation of the fully or partially accepted recommendations"),
            ("Hungary", "1", "17", "Human Rights Roundtable currently has 76 civil society organizations as members"),
        ],
    ),
    "Human rights & poverty": (
        B, "Reduce poverty, especially among minorities",
        "The National Social Inclusion Strategy 2030 and its 2025-2027 action "
        "plan target poverty eradication and Roma inclusion; JS2 asks for "
        "targeted programmes on intergenerational poverty.",
        [
            ("Hungary", "1", "108", "The two fundamental objectives of the MNTFS2030 are the eradication of poverty and the promotion of the inclusion of the Roma community"),
            ("JS2", "3", "55", "recommended the development of targeted programs to reduce intergenerational poverty"),
        ],
    ),
    "Human rights education, trainings & awareness raising": (
        C, "Human rights education and awareness-raising",
        "The National Report cites only the 2020 curriculum revision, which "
        "predates the review period, and no new awareness-raising programme.",
        [
            ("Hungary", "1", "67", "civic knowledge became an independent subject with its own framework curriculum and textbooks"),
        ],
    ),
    "Discrimination against women": (
        B, "Promote gender equality in the labour market and implement CEDAW",
        "The pay gap narrowed and an implementation plan for 2025-2026 was "
        "adopted; CEDAW is deeply concerned about retrogressive movements and "
        "an equality policy based on the family role of women.",
        [
            ("Hungary", "1", "38", "Government Decision No. 393/2024 (XII.12.) promulgated the Implementation Plan for the years 2025–2026"),
            ("Committee on the Elimination of Discrimination against Women", "2", "59", "was deeply concerned about retrogressive movements seeking to exclude reference to gender from the political, educational and social discourse"),
        ],
    ),
    "Persons with disabilities: independence, inclusion": (
        B, "Inclusion and independent living of persons with disabilities",
        "Hungary established a State Secretariat for Disability Affairs "
        "(September 2024) and a Disability Coordination Committee, created "
        "682 supported-living places and is preparing a National Disability "
        "Programme 2026-2036.",
        [
            ("Hungary", "1", "91", "In September 2024 the State Secretariat for Disability Affairs was established"),
            ("Hungary", "1", "98", "resulting in the establishment of 682 supported living places by December 2023"),
        ],
    ),
    "Children: definition": (
        C, "Child-rights consultation and a single child-rights body",
        "No consultation on a child-rights framework or single child-rights "
        "body is reported; JS2 asks for a multi-stakeholder national strategy "
        "on violence against children.",
        [
            ("JS2", "3", "51", "developing and implementing a multi-stakeholder national strategy to prevent and address all forms of violence against children"),
        ],
    ),
    "Right to participate in public affairs & right to vote": (
        B, "Public consultation on legislation",
        "Since 2022 the government audit body fines ministries that omit the "
        "legally required public consultation; the 8-day minimum consultation "
        "period predates the review.",
        [
            ("Hungary", "1", "32", "if the government audit body reveals that an omission has occurred in relation to the consultation process"),
        ],
    ),
    "Economic, social & cultural rights - general measures of implementation": (
        B, "Sustainable development and youth employment",
        "Youth Guarantee Plus and a programme for jobseekers over 30 were "
        "launched to raise employment.",
        [
            ("Hungary", "1", "87", "Policies that have been adopted to further improve the employment rate include the Youth Guarantee Plus Programme"),
        ],
    ),
    "Human rights & climate change": (
        D, "Participation of women, children and persons with disabilities in climate action",
        "The documents contain no information on this ask.", [],
    ),
    "Conditions of detention": (
        C, "Reform detention with a human rights-based approach",
        "The National Report reports no detention reform; the CPT found "
        "continued ill-treatment in Tiszalök prison and pending "
        "investigations.",
        [
            ("European Committee for the Prevention of Torture", "3", "10", "physical ill-treatment at Tiszalök prison had continued despite the Committee’s (CPT) 2023 findings"),
            ("European Committee for the Prevention of Torture", "3", "11", "Criminal investigations into alleged prison staff misconduct, some dating back to 2020–2021, were still pending at the pre-trial stage"),
        ],
    ),
    "Children: family environment & alternative care": (
        B, "Support for the family and child care",
        "Hungary expanded nursery places (55,000 to 71,000 since 2022) and "
        "family benefits; nothing is reported on sharing its experience.",
        [
            ("Hungary", "1", "73", "Since 2022 the number of places providing nursery care has increased from 55000 to 71000"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        A, "Cooperate with UN human rights mechanisms",
        "Hungary upholds its standing invitation to special procedures, "
        "received three mandate holders and responded to all communications.",
        [
            ("Hungary", "1", "11", "Since the last UPR, Hungary received three mandate holders, and responded to all allegation letters and other communications"),
        ],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        B, "Permanent national mechanism for follow-up",
        "A Human Rights Working Group and Human Rights Roundtable monitor "
        "implementation of accepted recommendations; the National Report "
        "does not date the mechanism.",
        [
            ("Hungary", "1", "17", "monitors the implementation of the fully or partially accepted recommendations"),
        ],
    ),
    "Economic, social & cultural rights": (
        B, "Eliminate the disadvantages of the Roma population",
        "Complex Settlement Programmes reach 80 segregated localities and the "
        "Opportunity Kindergarten, School and Workshop programmes target "
        "early disadvantage.",
        [
            ("Hungary", "1", "110", "Complex Settlement Programmes, reaching 80 segregated localities, contribute to reducing territorial inequalities and residential segregation"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        C, "Investigate excessive use of force and ill-treatment by law enforcement",
        "The National Report is silent; the CPT reports continued "
        "ill-treatment allegations in prisons and slow investigations.",
        [
            ("European Committee for the Prevention of Torture", "3", "11", "Criminal investigations into alleged prison staff misconduct, some dating back to 2020–2021, were still pending at the pre-trial stage"),
        ],
    ),
    "Right to an adequate standard of living": (
        C, "Basic services and housing for refugees and migrants",
        "No measure is reported; stakeholders report that asylum seekers lack "
        "access to essential services.",
        [
            ("JS7", "3", "34", "inadequate access to healthcare was a systemic issue affecting foreign nationals in Hungary"),
        ],
    ),
    "Right to health": (
        C, "Access to health care for migrants, refugees and marginalised groups",
        "No measure is reported; JS7 documents inadequate access to health "
        "care for asylum seekers and detained migrants.",
        [
            ("JS7", "3", "34", "inadequate access to healthcare was a systemic issue affecting foreign nationals in Hungary"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        D, "Sexual and reproductive health education for youth",
        "The documents contain no information on this ask.", [],
    ),
    "Rights related to name, identity & nationality": (
        D, "Nationality for children who would otherwise be stateless",
        "The documents contain no information on this ask.", [],
    ),
    "Rule of law & impunity": (
        C, "End the state of danger and preserve the rule of law",
        "No end to the emergency regime is reported; stakeholders refer to an "
        "'ongoing emergency regime' and a state of crisis due to mass "
        "migration.",
        [
            ("EUROMIL", "3", "25", "under the ongoing emergency regime"),
            ("JS4", "3", "67", "called to end the state of crisis due to mass migration"),
        ],
    ),
    "Land & property rights": (
        D, "Resolve the issue of unclaimed Jewish property",
        "The documents contain no information on this ask.", [],
    ),
    "Advancement of women": (
        C, "National action plan on Women, Peace and Security",
        "A draft National Action Plan 2024-2028 is still awaiting "
        "interministerial consultation, five years after the recommendation.",
        [
            ("Hungary", "1", "55", "A draft NAP covering the period 2024–2028 has been prepared by the Ministry of Defence"),
            ("Hungary", "1", "55", "is in the final stage of preparation prior to the interministerial consultation procedure"),
        ],
    ),
}

KEYWORDS = [
    # --- Roma ---
    (r"Roma", B,
     "Combat discrimination against Roma and promote their inclusion",
     "The National Social Inclusion Strategy 2030 (action plan 2025-2027), the "
     "Opportunity Kindergarten/School/Workshop programmes and Roma police "
     "dialogue events were launched or continued; the Special Rapporteur "
     "reports that 51% of Roma children drop out of compulsory school and that "
     "segregation is increasing.",
     [("Hungary", "1", "110", "Complex Settlement Programmes, reaching 80 segregated localities, contribute to reducing territorial inequalities and residential segregation"),
      ("Special Rapporteur on freedom of religion", "2", "68", "51 per cent of Roma children dropping out while still in compulsory school")]),
    # --- migrants / refugees / asylum seekers in an equality framing ---
    (r"^(?!.*(Roma|hate|Commissioner))(?=.*(migrant|refugee|asylum))", C,
     "Prevent discrimination and xenophobia against migrants, refugees and asylum seekers",
     "The National Report contains no measure; UNHCR urges Hungary to address "
     "xenophobia against refugees, and the Special Rapporteur on freedom of "
     "religion reports anti-migrant rhetoric from high-level officials.",
     [("UNHCR", "2", "12", "urged Hungary to address discrimination and xenophobia, in particular against refugees and asylum-seekers"),
      ("Special Rapporteur on freedom of religion", "2", "78", "requested that Hungary confront the discriminatory anti-migrant and racist rhetoric that had marred the political and media space, had put asylum-seekers at risk of refoulement")]),
    (r"right of asylum", C,
     "Guarantee the right of asylum",
     "The National Report is silent on asylum; stakeholders report continuing pushbacks.",
     [("JS4", "3", "68", "ending the practice of pushbacks at Hungary’s borders")]),
    # --- media ---
    (r"Media Council|media independence", C,
     "Restore media independence and the independence of the Media Council",
     "The National Report has no media section; the Special Rapporteur on freedom of expression still asks for a reformed Media Council and a framework for media independence.",
     [("Special Rapporteur on freedom of expression", "2", "28", "revise the appointment procedure for the Chair of the Media Council to make it more transparent and inclusive"),
      ("Special Rapporteur on freedom of expression", "2", "29", "called for the independence, transparency and accountability of the Media Council, including through legislative reforms")]),
    (r"programmes in the Slovenian language|financing of media in minority", D,
     "Finance and broadcast minority-language media",
     "The documents contain no information on this ask.", []),
    (r"Slovenian language in public life|use of minority languages|visible bilingualism", B,
     "Promote the use of minority languages in public life",
     "Official documents and declarations have been available in Slovak, Serbian, Slovenian, Croatian, German and Romanian since 2022-2023, and Rába-region offices employ Slovenian speakers.",
     [("Hungary", "1", "106", "In the Rába Region all municipal offices have Slovenian-speaking staff")]),
    (r"visible bilingualism", A,
     "Visible bilingualism in the Rába region",
     "Bilingual signage appears on public institutions throughout the Rába region and municipal offices have Slovenian-speaking staff.",
     [("Hungary", "1", "106", "Bilingual signage appears on public institutions throughout the region")]),
    # --- LGBTI: legislation that remains and was reinforced ---
    (r"Equal Treatment Authority", C,
     "Re-establish the Equal Treatment Authority",
     "The National Report states that equal-treatment procedures are handled by the Commissioner for Fundamental Rights; the Authority was not re-established.",
     [("Hungary", "1", "16", "The activities of the Commissioner for Fundamental Rights include responsibilities related to equal treatment, within which administrative authority procedures may be conducted and sanctions imposed")]),
    (r"^(Implement additional measures aimed at the promotion of equal rights|Take concrete measures to prevent and prohibit discrimination against LGBTQI|Develop a national action plan to combat discrimination based on sexual|Make progress in the development of anti-discrimination legislation|Guarantee the right of children to comprehensive sexuality|Revert the current ban|Reform legislation that denies|Take steps to protect the rights of lesbian|Adopt a comprehensive strategy and action plan to counter violence|Act against discrimination based on sexual)", C,
     "Protect LGBTQI persons: anti-discrimination law, gender recognition, strategy and education",
     "The National Report cites only the pre-existing Equal Treatment Act, which "
     "already lists sexual orientation, and a police network of specialised "
     "investigators; no strategy, legal gender recognition or anti-discrimination "
     "reform is reported, and CEDAW notes unrecognised same-sex partnerships.",
     [("Hungary", "1", "101", "Section 8 of Act CXXV of 2003 on Equal Treatment and the Promotion of Equal Opportunities explicitly mentions sexual orientation as prohibited grounds of discrimination"),
      ("Committee on the Elimination of Discrimination against Women", "2", "74", "registered partnerships were not recognized under the joint and second parent adoption scheme")]),
    (r"^Support the adoption of the Council of the European Union", D,
     "Support Council of the EU conclusions on the children's rights strategy",
     "The documents contain no information on this ask.", []),
    (r"anti-paedophilia|anti-lesbian|promotion of homosexuality|legislation purporting to protect children|2020 amendments restricting adoptions|stigmatizing and discriminatory provisions|legislation that uses child protection|repealing laws that prohibit certain discussions|Abolish discriminatory legislative provisions vis|repealing any restrictive", E,
     "Repeal or revise the 'child protection'/anti-LGBTQI legislation and the adoption restrictions",
     "Hungary kept the 2021 'child protection' law, which the CJEU found to "
     "breach Article 2 TEU, and in March 2025 extended it through Act III of "
     "2025, which bans LGBTIQ-themed assemblies, followed by a constitutional "
     "amendment: measures contrary to the recommendation. Special procedures "
     "and OHCHR urged repeal.",
     [("Hungary", "1", "101", "the Court of Justice of the European Union found, among other things, a violation of Article 2 of the TEU due to the homophobic nature of the so-called “child protection” law"),
      ("Several special procedure mandate holders", "2", "71", "reiterated strong concerns about the legislative amendments introduced in March 2025, which effectively banned LGBTIQ-themed assemblies in Hungary"),
      ("JS5", "3", "64", "immediately repeal the amendments introduced by Act LXXIX of 2021")]),
    # --- Istanbul Convention / domestic violence ---
    (r"Istanbul Convention|Convention on Preventing and Combating Violence against Women", C,
     "Ratify the Istanbul Convention",
     "Hungary has not ratified the Istanbul Convention and the National Report does not mention it; JS9 recommends ratification.",
     [("JS9", "3", "43", "recommended to ratify the Council of Europe Convention on Preventing and Combating Violence against Women and Domestic Violence (the Istanbul Convention)")]),
    (r"^Strengthen the legal framework for the protection of women against domestic", B,
     "Strengthen the legal framework against domestic and sexual violence",
     "A preventive restraining order that extends beyond imprisonment was introduced (August 2025) and the offence of harassment was extended (March 2025); the Istanbul Convention has not been ratified.",
     [("Hungary", "1", "49", "Act LXXII of 2009 was supplemented with a new type of restraining order (preventive restraining order)"),
      ("Hungary", "1", "47", "supplementing it with a new basic case")]),
    # --- ratification-cluster specifics ---
    (r"Kampala", E,
     "Ratify the Kampala amendments to the Rome Statute",
     "Hungary has withdrawn from the Rome Statute of the International Criminal Court, a measure contrary to the recommendation; JS10 asks it to withdraw the instrument of withdrawal.",
     [("JS10", "3", "3", "withdraw the withdrawal instrument, or otherwise, re-ratify the Rome Statute of the International Criminal Court")]),
    # --- women ---
    (r"senior positions", B,
     "Increase women's representation in senior positions",
     "A bill on gender balance among directors of listed companies (EU Directive 2022/2381) was submitted to the National Assembly on 29 October 2024; no measure on political representation is reported.",
     [("Hungary", "1", "35", "a draft law was submitted to the National Assembly on 29 October 2024")]),
    (r"^Continue measures to promote gender equality and ensure the representation", C,
     "Promote gender equality and women's representation",
     "The National Report reports statistics on women in leadership but no measure to ensure representation.",
     [("Hungary", "1", "36", "women accounted for 40% of leaders in Hungary in 2024")]),
    (r"^Adopt measures to effectively comply with the provisions of the Convention", C,
     "Comply with the provisions of CEDAW",
     "CEDAW advises adopting comprehensive anti-discrimination legislation and is concerned about retrogressive movements; no such legislation is reported.",
     [("Committee on the Elimination of Discrimination against Women", "2", "7", "advised Hungary to adopt, with a clear time frame, comprehensive anti-discrimination legislation")]),
    (r"Security Council resolution|women, peace and security", C,
     "Adopt a National Action Plan on Women, Peace and Security",
     "A draft National Action Plan 2024-2028 exists but is still awaiting the interministerial consultation procedure; it has not been adopted.",
     [("Hungary", "1", "55", "A draft NAP covering the period 2024–2028 has been prepared by the Ministry of Defence"),
      ("Hungary", "1", "55", "is in the final stage of preparation prior to the interministerial consultation procedure")]),
    (r"national action plan against racial discrimination", D,
     "Finalise a national action plan against racial discrimination",
     "The documents contain no information on this ask.", []),
    (r"^Develop a national action plan to prevent and address all forms of violence against children", B,
     "National action plan on violence against children",
     "Stricter employment-suitability requirements for staff of child protection institutions were introduced (July 2024); no national action plan is reported, and JS2 asks for a multi-stakeholder strategy.",
     [("Hungary", "1", "63", "Since July 2024, new and more stringent employment requirements have been introduced for managers, professionals, and applicants in child protection institutions")]),
    (r"^Raise the age for marriage", C,
     "Raise the minimum age of marriage to 18 without exception",
     "No change is reported; UNESCO and CEDAW recommend removing all exceptions.",
     [("Committee on the Elimination of Discrimination against Women", "2", "36", "recommended that Hungary review the Civil Code to remove all exceptions to the legal minimum age of marriage of 18 years for both women and men")]),
    # --- defamation / CSOs ---
    (r"^Decriminalize defamation", B,
     "Decriminalise defamation",
     "A June 2023 amendment excludes liability for defamation and insult in the free discussion of public affairs in the press and media; the Special Rapporteur still recommends repealing criminal defamation.",
     [("Hungary", "1", "24", "As of June 2023, an amendment to the Criminal Code introduced decriminalization with regard to offenses committed through press products or media services"),
      ("Special Rapporteur on freedom of expression", "2", "19", "repeal the provision in the Criminal Code relating to defamation as a criminal offence")]),
    (r"civil society organizations can operate freely", C,
     "Allow civil society organisations to operate freely",
     "The National Report describes the existing framework only; stakeholders point to the Transparency of Public Life bill.",
     [("JS5", "3", "17", "formally withdraw the Transparency of Public Life bill to ensure that legislation does not restrict the lawful activities of civil society")]),
    (r"^(Broaden the scope of actions aimed at strengthening cooperation|Improve both formal and informal dialogue)", B,
     "Improve consultation and dialogue with civil society",
     "Since 2022 ministries that omit the legally required public consultation are fined, and the Human Rights Roundtable counts 76 civil society organisations; the previous Government did not consult civil society on the UPR report.",
     [("Hungary", "1", "32", "if the government audit body reveals that an omission has occurred in relation to the consultation process"),
      ("Hungary", "1", "3", "The previous Government of Hungary failed to conduct consultations with civil society organizations regarding the current national report")]),
    (r"^Ensure that civil society organizations operate in an enabling environment and have access to transit centres", D,
     "Civil society access to transit centres for migrants",
     "The documents contain no information on this ask.", []),
    # --- law enforcement ---
    (r"^Ensure that excessive use of force", C,
     "Investigate excessive use of force and ill-treatment by law enforcement",
     "The National Report is silent; the CPT reports continued allegations and slow investigations.",
     [("European Committee for the Prevention of Torture", "3", "11", "Criminal investigations into alleged prison staff misconduct, some dating back to 2020–2021, were still pending at the pre-trial stage")]),
    # --- academic freedom ---
    (r"academic freedom|university autonomy|autonomy of universities|scientific freedom", C,
     "Protect academic freedom and university autonomy",
     "Act XCI of 2024 on HUN-REN states the principle of scientific freedom, but the research network was institutionally altered several times and the Special Rapporteur on the right to education and Scholars at Risk report an erosion of academic freedom.",
     [("Hungary", "1", "80", "the Hungarian Research Network stipulates that HUNREN pursues its scientific research and innovation activities in research institutions, in accordance with the principle of scientific freedom"),
      ("Scholars at Risk", "3", "38", "urged Hungary to commit publicly to restoring academic freedom and related human rights")]),
]

FALLBACK = (D, "No information on this ask",
            "The documents contain no information on this ask.", [])
