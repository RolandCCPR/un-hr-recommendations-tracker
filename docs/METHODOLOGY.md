# How this tracker was built — methodology in plain terms

*A record of every step, so the method can be checked or challenged. Nothing here
is a secret formula: it is downloading UN documents, copying the relevant text,
and applying one consistent grading rule.*

---

## 1. What the tracker contains

Two things, on the same A–E scale:

- **Human Rights Committee follow-up gradings** for **114 countries** — the
  Committee's *own* grades, copied out of its reports.
- **A Universal Periodic Review (UPR) implementation assessment** for **4
  countries** (United States, Denmark, Namibia, Paraguay) — our assessment,
  produced with AI from the UN reports.

Everything feeds one database, one score per country, and one world map.

---

## 2. Where the documents came from

All documents are public and come from the UN Office of the High Commissioner for
Human Rights (OHCHR).

- **Human Rights Committee follow-up:** the UN Treaty Body Database
  (`tbinternet.ohchr.org`). We opened the list of *"Follow-up Report of the
  Special Rapporteur on follow-up on Concluding Observations"* for the ICCPR and
  downloaded every one of them — 120 documents in all, from the Committee's 98th
  session (2010) to its 145th (2026). Each PDF was converted to plain text. Only
  the reports from the 109th session (2013) on are used, because that is when the
  Committee began grading A–E in a table (before then it wrote "reply
  satisfactory / not satisfactory" in prose).
- **UPR (4 countries):** each country's OHCHR UPR page. We took the country's
  3rd-cycle recommendations from its OHCHR *"Thematic List of Recommendations"*
  Word file, and the three pre-sessional reports prepared for its 4th-cycle
  review: the **National Report** (…/1), the **OHCHR Compilation of UN
  information** (…/2) and the **Summary of Stakeholders' submissions** (…/3).

The downloaded text of every report is kept in the project
(`training/ccpr_followup/reports/`, `countries/*/evidence/`) so anyone can
re-check what we read.

---

## 3. The Human Rights Committee grades (114 countries) — extraction step by step

These grades are **not ours** — the Committee assigned them and we transcribed
them. A script (`scripts/hrc_extract.py`) does the transcription so it is exactly
repeatable. Here is what it does, in order.

1. **Collect the reports.** From the UN Treaty Body Database we downloaded all
   120 *"Follow-up Report of the Special Rapporteur"* documents for the ICCPR
   (Committee sessions 98–145) as PDFs, and converted each to plain text with
   `pdftotext`. We then work only with sessions **109 onward** (2013), which is
   when the Committee started using the A–E table.

2. **Split each report into countries.** Older reports cover several countries
   at once; from 2019 each country gets its own short report. In every case, a
   country's section is marked by its Concluding Observations symbol —
   `CCPR/C/<country code>/CO/<number>`. We cut the text at each such symbol, so
   each slice is one country's evaluation.

3. **Keep the most recent evaluation only.** A country can appear in several
   reports over the years (different review cycles) and, within one report,
   across two or three rounds as the State sends more information. We take the
   **highest session number** for each country and, inside that report, the
   **last** grade summary line. The earlier rounds are kept and shown on the
   country page under "Earlier follow-up rounds".

4. **Read the grades from the summary line.** Every evaluation prints a line
   such as *"Additional information required on paragraphs 21 [B], 31 [B] [C]
   [A] and 43 [B]"*. Each bracketed letter is the Committee's grade for one part
   of a priority recommendation. We read those directly. (Where that line was
   damaged by the PDF conversion — a handful of old reports — we read the grades
   from the body of the text or, for one country, entered them by hand from the
   PDF; all such cases are listed in the script.)

5. **Read the wording verbatim.** For each priority Concluding Observation we
   copy, unchanged: the recommendation text (everything between "Paragraph N:"
   and "Summary of the … reply"), and the Committee's evaluation paragraph
   (everything after the last "Committee's evaluation" heading, up to
   "Recommended action"). The recommendation's lettered scope — e.g.
   "(a), (b) and (c)" — is shown as the label on the grade line.

6. **Normalise the letters.** The Committee sometimes writes `B1`/`B2` or
   `C1`/`C2` to point at a sub-part of a lettered paragraph. We collapse these to
   plain `A`, `B`, `C`, `D`, `E`.

7. **Clean up conversion litter.** `pdftotext` drops page headers and footers
   into the running text — document symbols like `CCPR/C/120/2`, print codes like
   `GE.19-07495`, and the country name repeated at page breaks. We strip these
   out. The words themselves are never changed. (We also re-ran the conversion
   in UTF-8 so accented characters — Länder, Türkiye — come through correctly.)

8. **Fix one recurring layout problem.** In 10 evaluations (Madagascar, Mexico,
   Niger, Senegal) the scope "(a), (b) and (c)" was stuck at the front of the
   explanation text; we move it onto the grade line so those pages match every
   other country.

9. **Add missing titles.** Reports before 2019 have no short topic title for
   each Concluding Observation. We wrote one ourselves for those ~19 countries —
   short, neutral, in the Committee's own style — and flagged them as ours on the
   page and in the site's methodology note.

10. **Exclusions.** 121 countries appear in the reports. We leave out six that
    only received a blanket `D` for never filing any follow-up report (Burundi,
    Côte d'Ivoire, Sudan, Sierra Leone, Chad, Venezuela), and Kosovo (no ISO
    code, not on the world map). 121 − 7 = **114**.

11. **Dates.** Each report states the session and dates it was adopted; we take
    the year from there. Seven old reports do not, so we set the year from a
    small session→year table in the script (e.g. the 112th session = 2014).

12. **Check.** We opened the source PDFs for a spread of countries — clean modern
    ones and messy old multi-country ones — and compared the extracted grades,
    titles and wording line by line. We have not hand-verified all ~500 grade
    rows, but the summary counts (about 175 B, 190 C, 18 A, 18 E, 11 D) match the
    pattern seen across the whole corpus.

---

## 4. The UPR implementation assessment (4 countries)

This part **is** our assessment. For each country:

1. We took every 3rd-cycle recommendation and **grouped them by theme** (using
   OHCHR's own thematic labels), because most are near-duplicate asks from
   different States. Number ranges are collapsed for readability.
2. For each theme we **read the three 4th-cycle reports** for what the State
   actually did since the last review.
3. We assigned one **A–E grade** per theme (splitting a theme where its parts
   diverge), using this rule:
   - **A** — the core of the recommendation is essentially done (a law is in
     force, a treaty is ratified, the thing asked for exists).
   - **B** — a concrete, on-point measure was adopted in the review period but
     it is incomplete (not yet in force, no results yet, only part of the ask).
   - **C** — only the pre-existing framework, a stalled or rejected bill, or no
     action.
   - **D** — the reports say nothing on this point.
   - **E** — a new measure runs against the recommendation, or the State
     rejects it.
4. Every grade is backed by **verbatim quotations** from the reports, with the
   UN body or organisation named, shown on the country page and in the database.

The UPR grading is a **first-pass assessment for expert review**, not a final
verdict.

---

## 5. How the AI was "trained" to grade, and what it learned

"Trained" here does not mean machine learning. It means the AI studied ~15 years
of the Committee's own practice and distilled the working rules — the same way a
new staff member would learn by reading past files.

**The study.**

1. We read **every Human Rights Committee follow-up report ever published**
   (~143 documents, 2010–2026) and pulled out **every A–E grade the Committee
   has given** (~800), together with the sentence explaining each one.
2. We tabulated them. The clear pattern: **B and C together are about 86%** of
   all grades ever given; **A is rare (~5%)**, and **D and E are very rare**
   (D has almost disappeared as States now engage with the procedure; E was
   ~1% and has risen to ~9% since 2022).
3. We wrote down, from the Committee's own wording, what typically earns each
   grade — e.g. "welcomes … but requires further information" → **B**;
   "regrets … reiterates its recommendation" → **C**.

**The blind test (the check on ourselves).**

4. We picked four countries and, using **only the documents the Committee's
   Special Rapporteur had** (the Concluding Observations, the State's follow-up
   report, and NGO submissions), the AI graded each priority paragraph **blind**
   and **wrote the grades down before** looking at the Committee's real grades.
5. Result: **18 of 24 correct**, and **every one of the six misses was exactly
   one grade too strict** — the AI kept saying "C" where the Committee had said
   "B".

**What we learned and corrected.**

6. The main lesson: **"C" is narrower than "not fully implemented yet."** C is
   for no information, a bare restatement of the existing framework, a bill
   stalled for years, or measures that pre-date the recommendation. If the State
   took a **concrete, on-point step during the review period** — passed or
   introduced a law, set up an institution, launched a policy — then even if it
   is incomplete, that is **B**.
7. Secondary lessons: **A** is more reachable than we first assumed (one
   completed action can earn A for a "continue your efforts" recommendation,
   even without full outcome statistics); **E** must stay rare and specific
   (an explicit refusal or a new contrary law — not merely a bad situation on
   the ground); the Committee **grades each lettered sub-part separately** about
   two-thirds of the time; and where **no NGO submitted** anything, the
   Committee's grades tend to sit slightly higher because it has less with which
   to test the State's own account.
8. We rewrote the rule in section 4 accordingly and **re-ran all four UPR
   assessments**. Denmark, Namibia and Paraguay moved from mostly-C to mostly-B;
   the United States stayed mostly C and E, because its record for the period is
   genuine inaction plus measures (in 2025) that run against the recommendations.

The full working notes are in
`training/CCPR_followup_grading_calibration.md` and
`training/CCPR_followup_grading_corpus_analysis.md`; the blind-test grades and
the country-by-country comparison are recorded there.

---

## 6. Turning grades into a score

- Each grade is worth points: **E = 1, D = 2, C = 3, B = 4, A = 5**.
- A country's **score for a mechanism** is the average of those points across its
  graded items — a number between 1 and 5.
- The **"combined"** score (used for the default map view) is the average of a
  country's UPR and Human Rights Committee scores where both exist; for the other
  ~110 countries it is simply the Human Rights Committee score.
- The map shades from red (1) through yellow (3) to green (5).

---

## 7. The database, map and website

1. One script (`site/build.py`) reads the four UPR databases and the Human Rights
   Committee data and writes a single SQLite file (`site/assessments.db`) with a
   row for every graded recommendation, plus a set of JSON files.
2. The website (`site/public/`) is a plain static site: a world map coloured by
   the scores, a sortable country table, and one page per country showing every
   grade with its verbatim recommendation and the Committee's wording (or, for
   the four UPR countries, our reasoning and quotations).

---

## 8. Things to be careful about

- **UPR:** only 4 countries; our assessment, AI-produced; a first pass for
  expert review; depends on what the UN and NGO reports happened to mention.
- **Human Rights Committee:** the Committee grades only 2–4 *priority*
  recommendations per country, not the whole record — a low score means those
  specific recommendations were not carried out, not an overall rating. We show
  each country at one point in time (its most recent evaluation, 2014–2026).
- Topic titles for pre-2019 evaluations are ours, not the UN's.
- Grades were transcribed and parsed by script; we spot-checked but have not
  hand-verified every one of the ~500 Human Rights Committee grade rows.

---

## 9. How to check it

- Every source document we used is in the project.
- The scripts that do the extraction and scoring are in `scripts/` and `site/`;
  running `python site/build.py` rebuilds the database and site data from
  scratch.
- To audit one country: open its page, then open the cited UN document (its
  symbol is shown) and compare.
