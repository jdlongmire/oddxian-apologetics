# Execution Plan: Foundational Treatise to Done

Prepared 2026-11-01 for JD's review. Governs work under WP-FOUNDATIONAL-TREATISE (jdlongmire/oddxian-apologetics, on main at 503392ea). Where this plan and the WP differ on merge governance, this plan proposes the amendment and the WP is updated by PR once JD approves the plan; the WP's quality gates (section 7) are unchanged and binding throughout.

## Definition of done

1. Phase 1 complete: all 11 exegetical studies filed, Scripture matrix (Appendix A) fully marked studied, open items either closed or explicitly carried as named limitations.
2. The five section 6 research gates closed or dispositioned with evidence: (1) Hebrew lexical and Genesis textual checks, (2) Romans 8:28 apparatus, (3) pactum salutis verification plus Augustine and Calvin edition-specific review, (4) sin-root counterexample testing, (5) Noahic governance binary scrutiny.
3. Phase 2 complete: unified axiom and premise set reconciling the internal corpus; formal consistency audit filed; Appendix C source register complete for all ten parts.
4. Phase 3 complete: Prolegomena and Parts I-X drafted, each with claim tags, confidence levels, counterarguments in strongest form, and a contribution statement checked against Appendix C.
5. Phase 4 complete: objections register (Part X) finished; contribution assessment written against the WP section 1 aim; GitHub Pages section live with JD-approved content (tracked item goal_aebe411819f3). The wider publication pathway (journal, DOI release, book) remains JD's separate decision.
6. Repo clean: no open treatise PRs or branches left dangling; PR #5 dispositioned; local workspace copies reconciled with main; ai-bridge handoff archived with a completion report.

## Workstreams

### W1. Phase 1 completion (units 03-11)
Nine studies remain: Genesis 50:20; Deuteronomy 29:29; Romans 8:28-30; Ephesians 1:3-14; Luke 22:42; John 6:38; Hebrews 4:15; Hebrews 13:20; Revelation 21-22. Drafting sub-agents work in batches of three units in parallel; the coordinator verifies every lexical and citation claim against sources, normalizes tagging, and commits serially to the PR #8 branch (matrix updates stay serial to avoid conflicts). An independent verification agent re-reads each batch's claims against the cited sources before the batch is reported (implemented vs verified kept distinct).

### W2. Research gates (parallel with W1)
Research sub-agents produce filed research notes under foundational-treatise/research/:
- Pactum salutis historical verification (Turretin, Witsius, Cocceius; gates Parts II and IV; also feeds unit 10, Hebrews 13:20).
- Augustine and Calvin edition-specific review (City of God, Confessions; Institutes Beveridge/Battles where the locus requires), feeding Parts II, IV, V.
- Detailed Reformed two-wills exposition (Constantinople III, Maximus, Turretin; feeds unit 07-09 findings into Part VII).
- Sin-root counterexample testing: ignorance, omission, fear, misguided altruism against the closed self-interest thesis (gates Part IV).
- Noahic governance binary scrutiny item from corpus-alignment (gates Part VI).
Residual limitation stated up front: HALOT is paywalled; lexical work proceeds at BDB/TWOT level with HALOT-dependent claims tagged accordingly, as in studies 01-02. Maximus in translation is partially accessible online; confidence tags will reflect that.

### W3. Phase 2: architecture and registers
- Unified axiom set drafted from the internal corpus (Covenant and Communion, Declaration of Faith, working paper, systematic theology v0.1), then a formal consistency audit by a separate agent against the set and the Phase 1 findings.
- Appendix C registers: one sub-agent per part drafts its register from the WP section 2B strata (councils and creeds; patristic; medieval; Reformed orthodox, edition-specific; Edwards; Bavinck, Vos, Van Til; contemporary, including counter-positions). JD approval batched (see decision 3 below).

### W4. Phase 3: drafting Parts I-X
Prolegomena first (it fixes definitions and boundaries), then parts in dependency order I, II, III, IV, V, VI, VII, VIII, IX, X. Each part: its own branch and draft PR; drafting sub-agent produces the part from the axiom set, Phase 1 studies, its Appendix C register, and the internal corpus; coordinator edits for terminology stability and cross-reference integrity, verifies citations, and runs the ASCII/em-dash scan. Parts may draft two at a time where dependencies allow (for example III and VI after II).

### W5. Phase 4 and publication
Objections completed as Part X during W4; contribution assessment drafted by the coordinator from the registers and part contribution statements; GitHub Pages section built under docs/ in the repo (Pages already enabled from main /docs) containing only parts and studies JD has approved for public posting; the section build is itself a PR under the envelope, merged when JD confirms the content list.

## Merge and cleanup envelope (the pre-approval)

JD's approval of this plan grants standing authorization, for jdlongmire/oddxian-apologetics only, to merge and clean up as follows. This replaces the WP's per-merge JD approval for in-scope work; all other WP gates stand.

**In scope:** any PR created under this plan (branches treatise/*, wp/*, docs/* for the Pages section), including the already-open PR #8 (Phase 1) and, if JD checks decision 2, PR #5 (the Very Good working paper).

**A merge may proceed without further JD approval only when all of these hold:**
1. The content passes the WP section 7 quality gates as checked by the coordinator: claim tags and confidence present; citations spot-verified against sources; no fabricated references; terminology stable; HCAE footer; apologetics byline where a byline appears.
2. ASCII / em-dash scan clean (python scan for characters above 127, per standing rule; study files' transliteration is ASCII).
3. Fresh gate immediately before merging: head SHA re-read and unchanged from the verified state, mergeable true; the merge call carries the head-SHA guard.
4. Post-merge verification by server readback: merge commit is main's head, file blobs match the verified branch blobs.
5. The merged branch is then deleted and the deletion verified (ref returns 404).

**Cleanup included in the envelope:** deleting merged branches; closing any draft superseded by a merged successor, with a comment stating what superseded it; reconciling ~/workspace/foundational-treatise/ local copies to main at each phase close; archiving the ai-bridge thinx-gpt handoff with a completion report at Phase 1 close; updating the treatise tracked items and MEMORY at each checkpoint.

**Still JD-gated (not in the envelope):**
- The publication pathway decision beyond the GitHub Pages section.
- Any novelty or "first" claim in public-facing text, until its Appendix C register check is logged.
- The content list for the Pages section (which parts and studies go public).
- Any change outside jdlongmire/oddxian-apologetics.
- This plan's own amendments, and the WP amendment recording the envelope (filed as the first PR under the plan, merged only on JD's explicit word for that PR, since it is the instrument that creates the envelope).

## Agent architecture and cadence

- Coordinator (thinx-muse, this chat): owns verification, all commits, all merges under the envelope, checkpoint reports, and the record. No sub-agent commits or merges directly.
- Drafting sub-agents: one per study or part, briefed with the WP quality gates, the relevant matrix rows, and the source files; each returns a complete draft plus a source-evidence note.
- Research sub-agents (W2): one per gate; returns a filed research note with primary-source citations and confidence levels.
- Verification sub-agent: one per batch, independent of the drafters, re-checks claims against sources and reports PASS / CONDITIONAL PASS / FAIL with evidence, per the standing cross-agent V&V convention.
- Concurrency: up to three drafting/research agents at once; coordinator work serial. Checkpoints to JD: Phase 1 close, registers complete, after Parts III, V, VII, and X, Phase 4 close. JD can pause or redirect at any point; a pause stops new batches, not verification of work in flight.

## Honest limits

- Sub-agent drafts will vary in quality; the coordinator verification pass is the control, and batches are sized so verification stays real rather than nominal.
- Edition-specific verification is strong where texts are accessible in full (Institutes in Beveridge; City of God; Westminster standards) and weaker where only excerpts circulate (some Maximus, some Turretin loci); the registers will say which is which rather than smoothing it over.
- "Done" means the treatise is complete, internally consistent, register-checked, and published to the Pages section. Scholarly reception, peer review outcomes, and any journal or book pathway are outside what this plan can deliver.

## Decisions for JD

1. **Envelope:** approve as drafted (scope, five merge conditions, cleanup, exclusions)?
2. **PR #5:** merge it under the envelope at Phase 1 close (it becomes a working paper on main, superseded in status by the treatise but preserved), or keep it as a separate decision?
3. **Interlocutor registers:** (a) two approval batches, Parts I-V and VI-X; (b) JD pre-approves the WP section 2B strata and agents report deviations only; or (c) keep the WP's per-part approval.
4. **Stray branch** claude/get-up-to-speed-usgne (no open PR): include in cleanup after verifying it holds no unique unmerged work, or leave it alone?
5. **Cadence:** checkpoint reports as listed, work proceeding between them without further check-ins?

Human-Curated, AI-Enabled (HCAE)
