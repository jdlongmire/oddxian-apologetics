# Illustrated Systematics: QA Log

## 2026-11-01: First asset ingestion (PR #10, branch feat/illustrated-systematics-program)

Ingested by thinx-muse at JD's direction from originals JD uploaded to the thinx-muse side chat on 2026-11-01. All five assets are revision 1, status graphic-draft. Nothing in this log is JD-approved or published; JD approval is still required for every asset.

### Assets ingested and verified

Each file below was downloaded back from the branch through the Contents API after commit, and its SHA-256 recomputed from the downloaded bytes. The recomputed hash matched the hash of JD's uploaded original in every case, so the committed files are byte-identical to the originals (no recompression).

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
