# Illustrated Systematics: QA Log

## 2026-11-01: First asset ingestion (PR #10, branch feat/illustrated-systematics-program)

Ingested by thinx-muse at JD's direction from originals JD uploaded to the thinx-muse side chat on 2026-11-01. All five assets are revision 1, status graphic-draft. Nothing in this log is JD-approved or published; JD approval is still required for every asset.

### Assets ingested and verified

Each file below was downloaded back from the branch after commit through the GitHub API (Contents API, plus the Git Blobs API for the two files over the 1 MB Contents API limit), and its SHA-256 recomputed from the downloaded bytes. The recomputed hash matched the hash of JD's uploaded original in every case, so the committed files are byte-identical to the originals (no recompression).

| Volume ID | Asset | SHA-256 | Bytes | Size (px) |
|---|---|---|---|---|
| BWM-IS-03 | volumes/BWM-IS-03/plate.jpg | 83a5deed409894a1fa20a7b0f4d7ff047dcc96dec8c5bab463b2bd362cb5880d | 941779 | 1125x1231 |
| BWM-IS-02 | volumes/BWM-IS-02/plate.jpg | 2175dba462f30a2e47f170002f31117d4a6f6366d474c3a931bc2e10569033e6 | 1089086 | 1024x1536 |
| BWM-IS-00 | volumes/BWM-IS-00/plate-world-model.jpg | ab5e4f01d4907d7dddeb31453cee32dbbced2f15eab80b7ade972c40e162d5bd | 1156436 | 1024x1536 |
| BWM-IS-00 | volumes/BWM-IS-00/plate-architecture.jpg | cae6dcd06b08924622d00882d9938ea40b802fbea2ba1b0a89b81fed6c254aac | 422508 | 1125x633 |
| STYLE-GUIDE | style-guide.jpg | 7bdb9cbd7c52e6172de39dd700a1e977577372be9d615ae6a4ff45019456b8f5 | 894485 | 1024x1536 |

Transcriptions filed alongside the plates: volumes/BWM-IS-03/TRANSCRIPTION.md, volumes/BWM-IS-02/TRANSCRIPTION.md, volumes/BWM-IS-00/TRANSCRIPTION.md (the last covers the world-model plate; the architecture plate is summarized below and not transcribed panel by panel).

### Architecture plate (BWM-IS-00, plate-architecture.jpg): main sections

Landscape summary plate titled "The Biblical WorldModel: A Systematic Theology of Covenant and Communion". Sections: Foundational Commitments (Scripture normative; the triune God as source of truth, logic, and love; truth objective and coherent; world designed and ordered; humans moral agents; history purposeful, culminating in perfected communion); The Systematic Architecture, eight domains ST-1 God and Triune Purpose through ST-8 Judgment and Consummated Communion, framed by The Eternal Triune God above and The Covenantal Framework / Perfected Loving Communion below; Distinctive Contributions and Working Hypotheses, each typed (Direct Teaching, Good Consequence, or Theological Hypothesis); The Redemptive Arc (Eternal Purpose, Creation, Fall, Law, Christ, Restoration, Church, Consummation); Method and Rationale (hermeneutic, metaphysical, epistemic, telic); Intellectual Influences, exemplars not authorities (Aquinas, Calvin, Van Til, Plantinga, Godel, Lakatos). Footer: J.D. Longmire; Sola Scriptura; Methodological Designism; Covenant Theology; Triune God; Loving Communion; From Very Good to Perfected; Romans 8:28.

### Findings (open, for JD disposition or a revision 2)

1. Style guide vs program documents, shirt rule conflict. The program README, panel script template, and the BWM-IS-03 panel script specify a fixed red shirt and dark jacket for the narrator. The Visual Series Style Guide (style-guide.jpg, ingested in this pass) instead specifies an 8-color rotating shirt palette (Red, Purple, Blue, Navy, Green, Burgundy, Slate, Charcoal), and the ingested plates follow the guide, not the fixed rule: BWM-IS-02 is red, the BWM-IS-00 world-model plate is purple, and BWM-IS-03 is blue in the header and green in panel 10. Recommendation: adopt the style guide as the governing visual document and amend the program documents to palette rotation.
2. No visible volume ID on any plate. The sourcing policy requires every graphic to visibly carry oddXian.com and its volume ID. None of the five ingested graphics carries a visible volume ID. Recorded in the manifest through the asset paths and this log; a visible ID would require a derivative footer or a policy amendment, which is JD's call.
3. oddXian.com pointer missing on three plates. BWM-IS-03 carries oddXian.com (bottom right). BWM-IS-02 and both BWM-IS-00 plates carry no visible oddXian.com pointer. The style guide itself carries none either, although it instructs "Include oddXian.com on each graphic". Manifest field oddxian_pointer_verified is therefore true only for BWM-IS-03 and false for the other four rows.
4. BWM-IS-02 panel 2 spelling defect: "ceeation" [sic] for "creation" in the speech bubble. Preserved as [sic] in the transcription. Requires art regeneration to fix; logged for revision 2.
5. BWM-IS-02 panel 2 quotation defect: the speech bubble places a paraphrase in quotation marks with no citation ("A covenant of love within the Godhead that grounds God's work in ceeation [sic] and redemption."). This conflicts with the sourcing policy rule distinguishing quotations from paraphrases. Logged for revision 2.
6. BWM-IS-02 panel 5 suggestion: the panel quotes Philippians 2:12 on working out salvation, in a panel about sovereignty and real human agency. Adding Philippians 2:13 (God who works in you) would carry the sovereignty half of the panel's own claim. Suggestion only, for JD.
7. BWM-IS-03 panel 4 doctrinal qualification needed. The panel quotes John 14:26 and applies the Helper's teaching and remembrance promise to God's people generally ("guiding His people, preserving the truth, and opening understanding"). The volume's own NARRATIVE.md warns against collapsing the original apostolic promises of John 14:26 and 16:13 into a blanket guarantee for subsequent interpreters. The plate and the narrative are in tension; the narrative qualification should govern, and the discrepancy is logged here rather than silently passed.
8. BWM-IS-03 aspect ratio off standard. At 1125x1231 the plate is not the series standard 1024x1536 (2:3 portrait) used by BWM-IS-02, the BWM-IS-00 world-model plate, and the style guide. It will not sit in a uniform grid or print layout with the others. Recommendation: keep the original as revision 1 and produce a padded or re-rendered 2:3 derivative if JD wants a uniform set.
9. Claim classification, world-model plate panel 3. The plate defines sin as closed self-interest on its face. The architecture plate classifies "Closed self-interest as the root of sin (all sin as disordered love of self)" as Good Consequence, not Direct Teaching. Any claim register or companion narrative for BWM-IS-00 must classify it as Good Consequence, so the series does not present its most distinctive claim at a higher warrant than its own architecture assigns it.
10. BWM-IS-01 duplicate home. BWM-IS-01 remains chat-draft in this path, but a Triune Foundation plate already exists on main under jd-teaching-infographics/ (filed 2026-10-31). Two homes for the same series will drift. Recommendation: pick one canonical home and make the other an index pointer.
11. BWM-IS-00 is a proposed ID. The frontispiece designation for the two overview plates is a recommendation recorded in this log, not yet ratified by JD. The 25-volume count in SERIES-INDEX.md is unchanged by it.
12. Legibility. Panel body text on all three 10-panel plates is small at phone-feed size. The transcriptions filed in this pass are the accessible text record; panel crops would be needed for video derivation.

### Disposition

All assets: graphic-draft (QA logged, not JD-approved). No asset is approved, published, or assigned a publication URL. PR #10 remains a draft.

## Addendum, 2026-11-01: BWM-IS-04 ingested; governance alignment under the handover

JD approved the BWM-IS-04 example plate in chat on 2026-11-01 and approved thinx-muse to act as Principal Assistant for this program. Doctrine and publication remain JD's approval alone, per OPERATING-AGREEMENT.md. Under that handover, the following were done on this branch:

1. BWM-IS-04 The Attributes and Glory of God, built end to end by thinx-muse (panel plan, generation at 1280x1920 from the series exemplars, proofread), is ingested at volumes/BWM-IS-04/plate.jpg (971374 bytes, sha256 532c6ae8f547a7139882424cfb892dcb35e864897ee3b830b15ca8a9680b15c1) with PANEL-SCRIPT.md (including per-panel claim classifications) and TRANSCRIPTION.md. Green shirt, per the style guide palette rotation and the guide's own 04 thumbnail. Status: graphic-draft; the example was approved, publication is not yet approved.
2. Repair disclosure. The raw generation carried four lettering defects: panel 1 reference rendered "Epheeronomy 6:4"; panel 7 bubble "sloow"; panel 5 caption "communin"; gibberish trailing the small per-panel ID lines. A model edit pass changed none of them. All four were repaired programmatically (programmatic text replacement over the defective words only) and verified by crop readback before ingestion. The repaired words sit in a slightly more condensed typeface than the surrounding generated lettering; this is visible on close inspection of panel 5. The ingested file is therefore a repaired derivative of the raw generation, recorded here rather than passed off as a clean generation.
3. Finding 1 (shirt rule) resolved by amendment. README.md and PANEL-SCRIPT-TEMPLATE.md now specify palette rotation per the Visual Series Style Guide, which is recorded as the governing visual document. The BWM-IS-03 panel script's red-shirt line is superseded by this amendment.
4. Finding 2 (visible volume ID) resolved by policy amendment. SOURCING-POLICY.md point 6 now provides: originals lacking the visible ID are never altered silently; the ID is recorded in the manifest, the gap is logged here, and the ID and pointer are carried on the published derivative. Graphics produced after 2026-11-01 must carry both in the original artwork (BWM-IS-04 does: footer oddXian.com | BWM-IS-04).
5. README.md stale statements corrected: 25 volumes (not 24), program status, and the ingestion status of volumes 01 to 04.
6. Still open for JD: ratification of the BWM-IS-00 frontispiece designation (finding 11); the IS-01 canonical-home decision (finding 10); revision 2 items for IS-02 (findings 4 to 6) and the IS-03 items (findings 7 and 8); a companion narrative for IS-04.

Disposition remains: no asset in this program is published; PR #10 remains a draft.

Human-Curated, AI-Enabled (HCAE)

## Addendum 2, 2026-11-01: JD approval, PR #10 merged, BWM-IS-05 ingested, IS-04 narrative

JD approved the outstanding gate list in chat on 2026-11-01. Actions taken on that approval:

1. PR #10 merged. Fresh gate before merging: head 6ff631d775ec30f80095e3e30e2dbf394dcf1b32 unchanged, mergeable true, state clean. Marked ready, merged; merge commit 883a4801fdded8df69c47688e9d26350a725ea24 verified equal to the main head on readback. Branch feat/illustrated-systematics-program deleted; ref verified 404. The program scaffold and the IS-00, IS-02, IS-03, and IS-04 assets are now on main, all still at graphic-draft status; nothing is published by the merge.
2. Finding 11 closed. The BWM-IS-00 frontispiece designation is ratified by JD; SERIES-INDEX.md updated to say so.
3. Finding 10 closed. Canonical home decided: this path (biblical-worldmodel/illustrated-systematics) is the series home; jd-teaching-infographics keeps its copies and now carries a pointer note in its README. Ingestion of the IS-01 plate into this path remains to be done.
4. BWM-IS-04 companion narrative drafted (volumes/BWM-IS-04/NARRATIVE.md), with claim register and panel-to-source map; the panel 7 cross sentence is registered as Good and Necessary Consequence, not as the Exodus 34:6 text. Draft, not yet JD-approved.
5. BWM-IS-05 Creation: Very Good built by thinx-muse and ingested in the follow-on PR: volumes/BWM-IS-05/plate.jpg (963068 bytes, 1280x1920, sha256 e9b32b75338c64570303b8a9e9d6751e311341b9a0f559fd8bf44ee98b022584), PANEL-SCRIPT.md with claim classifications (panel 9 and the Horizon line carry the two-states thesis as theological synthesis, MEDIUM, per the treatise Genesis 1:31 study), TRANSCRIPTION.md. Burgundy shirt per palette rotation.
6. IS-05 repair disclosure. Three lettering defects in the raw generation were repaired programmatically and verified by crop readback: panel 2 caption ("things" rendered for "that brings"; repaired across the line break as "that / brings reality into being."); panel 6 (a stray letter t at the start of caption line 3, splitting "It / t is", removed); panel 10 closing reference ("Cocossians 1:16" corrected to "Colossians 1:16"). Panel 1's word "else" was inspected at 6x magnification and is correctly lettered, tightly kerned; no repair. Two earlier patch attempts on intermediate local drafts mislocated the panel 6 letter and the panel 10 line and were discarded; the ingested file is the verified final. The ingested plate is a repaired derivative of the raw generation, recorded here.

Still JD's: publication of any volume; the IS-02 and IS-03 revision 2 items (findings 4 to 8); ingestion of IS-01 into this path.

Human-Curated, AI-Enabled (HCAE)

## Addendum 3, 2026-11-01: QA process adopted; BWM-IS-05 re-audited; BWM-IS-04 retro-audit

JD reported garbled text on BWM-IS-05 panel 1 and directed that a QA process be put in place. JD then clarified the panel 1 caption word "else" was tightly kerned rather than garbled. The magnified inspection his report triggered found the real defects:

1. What JD saw. Panel 1 caption, "else": correctly lettered (e-l-s-e all present) but kerned so tightly it does not read cleanly at delivery size. Re-lettered under the new process's reading-scale rule. JD's underlying judgment stands: the plate had not been adequately proofed.
2. The systematic defect. The generator rendered "Genesis" as "Genessis" (doubled s) in five of the seven Genesis references on the plate: panels 1, 4, 6, 7, and 8. Panels 2 and 5 rendered it correctly. All five were repaired programmatically (pixel-measured ink boxes, height-matched re-lettering) and verified by 5x crop readback. "Genesis" spelling is now a standing checklist item in QA-PROCESS.md.
3. Process adopted. QA-PROCESS.md is filed with this program: an element checklist for every plate (header elements, per-panel title, bubble, reference, every caption line, closing checklist, footer), each element read from a magnified crop against the panel script, letter by letter for names and references; pass/fail judged at reading scale; a second pass after any repair, neighbors included; repairs disclosed; no ingestion without a completed checklist recorded here.
4. BWM-IS-05 retro-audit result. Every element on the plate has now been read from magnified crops against PANEL-SCRIPT.md: header (title, subtitle, framing box, book stack, VOL. 05), panels 1 to 9 (title, bubble, reference, all caption lines), panel 10 (six checklist lines, closing verse, Colossians 1:16 as repaired), footer. After the repairs in addendum 2 and this addendum, all elements PASS. Final plate: 959210 bytes, 1280x1920, sha256 dfbf9fe757633952b58c79040a19ed2187203260f8fa75ad160945afc6b381e9 (supersedes the addendum 2 hash).
5. BWM-IS-04 retro-audit result. Every element read from magnified crops against its panel script: header (title, subtitle, framing box, book stack), panels 1 to 10 including all references and caption lines, footer. All elements PASS, including the four repairs disclosed in the first QA log (Deuteronomy, slow, communion, per-panel ID lines). One observation recorded without repair: panel 5's reference renders the numeral in "1 John 4:8" as a plain stroke that can be misread as a capital I out of context; in context it is unambiguous, and the transcription records the correct reference. Flagged for JD if he wants it re-lettered in a future revision.

Human-Curated, AI-Enabled (HCAE)

## Addendum 4, 2026-11-01: full-series audit under QA-PROCESS; publication derivatives; Pages site

At JD's direction the remaining supplied plates were audited under QA-PROCESS.md before any publication use, and the series was published to the GitHub Pages site (docs/illustrated-systematics/) on his approval given in the side chat the same day.

1. BWM-IS-01 (The Triune Foundation of Our Faith). Every element read from magnified crops: header, panels 1 to 10 (all bubbles, references, captions, scene signs in panel 3), closing checklist and verse (Matthew 22:37-39). PASS, no repairs. References verified letter by letter, including Genesis 1:26 (correct) and Ephesians 1:4-5. The plate is now ingested into volumes/BWM-IS-01/ from jd-teaching-infographics with a full transcription.
2. BWM-IS-02 (The Eternal Decree and Covenant). Every element read: header, panels 1 to 10, closing verse (Ephesians 1:4-5). One lettering defect confirmed: panel 2 bubble "ceeation" for "creation". The panel 9 caption's "righteousness." was inspected at 2.5x and is a true period with a minor print artifact; no repair. Editorial note stands from the first QA log: the panel 2 bubble is a summary statement in quotation marks with no citation; the Pages page for this volume labels it as a summary statement, and any wording change is JD's editorial call. Publication derivative (docs/illustrated-systematics/images/is-02.jpg): "ceeation" repaired to "creation" (verified by 4x crop readback) and a footer band added carrying oddXian.com and BWM-IS-02. The original plate in volumes/ is unaltered.
3. BWM-IS-03 (The Bible). Every element read: header (including the framing statement), panels 1 to 10, in-panel checklist in panel 8, closing verse. PASS, no lettering repairs. The plate carries oddXian.com in its closing panel; the volume ID rides the publication derivative, which also pads the plate to the 2:3 standard (1125x1688, navy bands) as is-03.jpg. The known doctrinal note stands: panel 4's caption applies John 14:26's promise generally; the qualification belongs to the companion narrative, which is JD's to rule on.
4. BWM-IS-00 (frontispiece overview and architecture plates). Every element read: overview header and panels 1 to 10 with closing checklist (Romans 11:36); architecture plate ST-1 to ST-8 boxes, foundational commitments, contributions table with its claim classifications, influences, and footer. PASS, no repairs. Publication derivatives add only the footer band with oddXian.com and BWM-IS-00. The overview panel 3 thesis (sin is closed self-interest) is carried on its Pages page with its architecture-plate classification, Good Consequence.
5. Publication. docs/illustrated-systematics/ now serves the series index and one page per volume (IS-00 through IS-05) with the plate, the panel-by-panel text, and companion narratives where they exist; the docs home page links the series. Statuses in the manifest and series index are updated to published for these volumes on JD's approval of 2026-11-01. The standing flow from here: volumes are produced on the weekly schedule, presented to JD for review, and published only on his approval; the same plates and narratives feed the narrated-video edition (TikTok and YouTube).

Human-Curated, AI-Enabled (HCAE)
