# Scientific Sanity Check Protocol

**Purpose**: Verify rigor and honesty when developing scientific arguments that challenge consensus positions
**Invoke**: After completing any major claim, calculation, or argument section
**Created**: 2025-12-17 (Adapted from LRT formalization protocol)
**Scope**: Hydrotectonic model, deep time critiques, macro-evolution challenges, and similar work

---

## Why This Protocol Exists

When challenging consensus scientific positions, the standard of evidence is asymmetric: errors by challengers are seized upon; errors by defenders are absorbed. This is not unfair - it reflects appropriate epistemic caution. The response is not complaint but **greater rigor**.

This protocol ensures:
1. We don't overclaim what we've demonstrated
2. We don't hand-wave past quantitative requirements
3. We engage strongest objections, not strawmen
4. We maintain academic tone regardless of confidence
5. We distinguish stipulation from derivation
6. We remain falsifiable

---

## Quick Checklist

Run through these 10 checks before claiming any major result:

### ☐ 1. Budget Closure Check

**Purpose**: Verify quantitative budgets actually close

**Applies to**: Energy, heat, mass, sediment, water, time - any conserved or constrained quantity

**Procedure**:
```
For each budget claimed to close:
1. List all INPUTS (sources)
2. List all OUTPUTS (sinks)
3. List all STORAGE terms (accumulation/depletion)
4. Verify: Σ(inputs) = Σ(outputs) + Δ(storage)
5. Check units consistency throughout
6. Identify largest uncertainty term
```

**Pass Criteria**:
- ✅ Explicit numerical balance shown
- ✅ All major terms accounted for
- ✅ Uncertainty bounds stated
- ✅ Balance closes within stated uncertainty

**Fail Indicators**:
- ❌ "The budget closes" without showing calculation
- ❌ Missing major terms (e.g., heat budget without radiation sink)
- ❌ Orders of magnitude don't balance
- ❌ Hand-waving: "remaining energy dissipates through various mechanisms"

**Example (Hydrotectonic Heat Budget)**:
```
INPUT:  Gravitational PE release = 10²³ J
OUTPUT: Frictional dissipation = 10²³ J (water films)
        + Seismic radiation = ? (estimate needed)
        + Plastic work = ? (estimate needed)
CHECK:  Do outputs sum to input? Show calculation.
```

---

### ☐ 2. Physical Law Compliance

**Purpose**: Verify no conservation law violations

**Applies to**: All mechanistic claims

**Procedure**:
```
For each mechanism proposed:
1. Energy conservation: Does E_in = E_out + ΔE_stored?
2. Momentum conservation: Are forces balanced or acceleration explained?
3. Mass conservation: Does matter balance?
4. Thermodynamics: Does entropy increase (or explain why not)?
5. Check rate laws: Are velocities/fluxes physically achievable?
```

**Pass Criteria**:
- ✅ Each conservation law explicitly addressed
- ✅ No perpetual motion (energy from nowhere)
- ✅ No negative entropy (spontaneous ordering without work)
- ✅ Rates consistent with known physics

**Fail Indicators**:
- ❌ Energy appears without source
- ❌ Heat disappears without sink
- ❌ Processes faster than physical limits allow
- ❌ "The system self-organizes" without energy accounting

---

### ☐ 3. Assumption Audit

**Purpose**: Explicitly distinguish what is STIPULATED vs DERIVED

**Procedure**:
```
Create three-column table:
| Claim | Status | Justification |
|-------|--------|---------------|
| Deep ballast exists | STIPULATED | Biblical boundary condition (Stage 0) |
| Heat flux ~7 W/m² | DERIVED | Appendix B calculation |
| Pore pressure reaches 99% lithostatic | ASSUMED | Required for mechanism; needs validation |
```

**Categories**:
- **STIPULATED**: Accepted as framework axiom (e.g., biblical initial conditions)
- **DERIVED**: Calculated from prior assumptions using physics
- **ASSUMED**: Needed for mechanism but not yet justified
- **EMPIRICAL**: Based on observational data (cite source)

**Pass Criteria**:
- ✅ Every major claim categorized
- ✅ No DERIVED claims that actually depend on undefended ASSUMPTIONS
- ✅ STIPULATED items clearly labeled as framework commitments
- ✅ Chain of derivation traceable

**Fail Indicators**:
- ❌ Treating ASSUMED as DERIVED
- ❌ Hidden assumptions in "obvious" steps
- ❌ Circular: A derived from B, B derived from A
- ❌ Framework axioms presented as empirical conclusions

---

### ☐ 4. Calculation Traceability

**Purpose**: Every number must trace to source

**Procedure**:
```
For each numerical claim:
1. Source: Where does this number come from?
   - Literature (cite specific paper, table, page)
   - Calculation (show derivation or reference appendix)
   - Estimate (state basis and uncertainty)
   - Assumption (flag as requiring defense)

2. Units: Are units consistent and correct?

3. Order of magnitude: Does the number pass smell test?
```

**Pass Criteria**:
- ✅ Every number has explicit source
- ✅ Calculations reproducible from stated inputs
- ✅ Literature values correctly transcribed (spot-check)
- ✅ Estimates flagged with uncertainty ranges

**Fail Indicators**:
- ❌ Numbers appear without source
- ❌ "Standard values" without citation
- ❌ Unit errors (W vs J, m² vs m³)
- ❌ Results differ when recalculated

---

### ☐ 5. Literature Cross-Check ⚠️ CRITICAL

**Purpose**: Verify claims not already contradicted by existing data

**Procedure**:
```
For each testable prediction or factual claim:
1. Search for directly relevant experimental/observational data
2. Identify 3-5 key papers (prefer recent, high-quality sources)
3. Extract reported values with uncertainties
4. Compare to our claim
5. Document result
```

**Decision Matrix**:
| Result | Action |
|--------|--------|
| Our claim matches data | ✅ Note as consistent |
| Our claim untested | ✅ Note as prediction |
| Our claim within uncertainty | ⚠️ Note marginal |
| Our claim contradicted | ❌ STOP - revise or abandon |

**Red Flags** (immediately stop if found):
- ❌ High-quality experiments directly contradict our claim
- ❌ Multiple independent datasets show opposite trend
- ❌ We're predicting what's already measured to be different

**Documentation**:
```markdown
## Literature Check: [Claim]
- **Claim**: [Our specific claim]
- **Search terms**: [What we searched]
- **Key papers**: [3-5 citations]
- **Reported values**: [Data with uncertainties]
- **Comparison**: [Match/Contradict/Untested]
- **Conclusion**: [Proceed/Revise/Abandon]
```

---

### ☐ 6. Circularity Check ⚠️ CRITICAL

**Purpose**: Detect all forms of circular reasoning

**Types to check**:

#### 6a. Logical Circularity
- Conclusion assumed in premises
- Example: "The Flood deposited these sediments rapidly because they're Flood deposits"

#### 6b. Definitional Circularity
- Term defined using itself
- Example: Defining "catastrophic" using "rapid" then "rapid" using "catastrophic"

#### 6c. Parametric Circularity
- Parameter derived using itself
- Example: Using observed slab depths to derive mechanism that predicts slab depths

#### 6d. Evidential Circularity
- Evidence interpreted through conclusion, then used to support conclusion
- Example: Dating method rejected because it contradicts model, absence of contradicting dates cited as support

**Procedure**:
```
For each major argument:
1. List premises explicitly
2. State conclusion explicitly
3. Check: Does any premise assume the conclusion?
4. Check: Does any definition require the conclusion to be meaningful?
5. Trace parameter derivations - any self-reference?
```

**Pass Criteria**:
- ✅ Premises independent of conclusion
- ✅ Definitions non-circular
- ✅ Parameters derived from independent sources
- ✅ Evidence not filtered by conclusion

**Fail Indicators**:
- ❌ Argument works only if conclusion assumed
- ❌ Counter-evidence systematically reinterpreted
- ❌ "We know X because Y, and Y because X"

---

### ☐ 7. Strongest Objection Engagement

**Purpose**: Address steel-manned opposition, not strawmen

**Procedure**:
```
For each major claim:
1. State the strongest objection a competent critic would raise
2. Quote or cite actual critics where possible
3. Provide substantive response (not dismissal)
4. Acknowledge if objection remains partially unanswered
```

**Quality Test**:
- Would a critic say "Yes, that's my objection and you addressed it fairly"?
- Or would they say "That's a caricature of my position"?

**Pass Criteria**:
- ✅ Objections stated in critic's own terms
- ✅ Responses engage substance, not motive
- ✅ Partial concessions where warranted
- ✅ Open questions acknowledged

**Fail Indicators**:
- ❌ "Critics say X, but they're wrong" (no engagement)
- ❌ Weakest version of objection addressed
- ❌ Objection dismissed as bias/ignorance
- ❌ No actual critics cited

**Template**:
```markdown
## Objection: [Strongest form]
**Source**: [Actual critic if possible]
**Substance**: [What they actually argue]
**Response**: [Our substantive reply]
**Residual**: [What remains unaddressed, if anything]
```

---

### ☐ 8. Falsifiability Check

**Purpose**: Ensure model makes risky predictions

**Procedure**:
```
List predictions that would FALSIFY the model if contradicted:
1. [Prediction 1] - How to test - What result would falsify
2. [Prediction 2] - How to test - What result would falsify
...
```

**Quality Test**:
- Are these predictions genuinely risky (could fail)?
- Or are they vague enough to accommodate any result?

**Pass Criteria**:
- ✅ At least 3 specific, testable predictions
- ✅ Each prediction specifies falsifying observation
- ✅ Predictions not trivially satisfied
- ✅ We would actually abandon/revise model if falsified

**Fail Indicators**:
- ❌ "The model predicts what we observe" (post hoc)
- ❌ Predictions so vague any result confirms
- ❌ Falsifying observations systematically reinterpreted
- ❌ No prediction would actually cause model revision

---

### ☐ 9. Professional Tone Verification

**Purpose**: Maintain academic credibility

**Prohibited Language**:
- ❌ Celebratory: "proves," "demolishes," "destroys," "breakthrough"
- ❌ Emotional: "obviously," "clearly," "undeniably," "any honest person"
- ❌ Dismissive: "so-called," "merely," "fundamentalist" (either direction)
- ❌ Promotional: "revolutionary," "paradigm-shifting," "groundbreaking"
- ❌ Emojis: Never in formal documents

**Required Hedging** (calibrate to actual confidence):
- "suggests" not "proves"
- "appears consistent with" not "confirms"
- "raises questions about" not "refutes"
- "the model predicts" not "we know"

**Pass Criteria**:
- ✅ Tone appropriate for peer-reviewed journal
- ✅ Claims calibrated to evidence
- ✅ Opponents treated with respect
- ✅ Uncertainty acknowledged

**Fail Indicators**:
- ❌ Would embarrass if quoted by critic
- ❌ Overclaims relative to evidence
- ❌ Ad hominem or motive attribution
- ❌ Reads like apologetics rather than science

---

### ☐ 10. Symmetrical Standards Check

**Purpose**: Apply same rigor to our framework as to opponents'

**Procedure**:
```
For each criticism we make of consensus position:
1. State the criticism
2. Check: Does our model have an analogous problem?
3. If yes: Address it explicitly, don't ignore
4. If no: Explain why the situations differ
```

**Examples**:
| Our Criticism of Consensus | Symmetry Check |
|---------------------------|----------------|
| "Unfalsifiable - any anomaly absorbed" | Do we absorb anomalies the same way? |
| "Relies on unobserved entities" | Do we invoke unobserved entities? |
| "Post hoc auxiliary hypotheses" | Do we add post hoc fixes? |
| "Circular dating methods" | Are our methods circular? |

**Pass Criteria**:
- ✅ Same standard applied to both frameworks
- ✅ Our analogous problems acknowledged
- ✅ Differences in severity defended, not assumed
- ✅ No special pleading

**Fail Indicators**:
- ❌ Criticizing opponent for X while we do X
- ❌ "Different when we do it" without justification
- ❌ Asymmetric skepticism
- ❌ Double standards on evidence quality

---

## Stop Words

Do NOT use without passing sanity check:

| Word | Problem | Alternative |
|------|---------|-------------|
| "Proves" | Overclaim | "Supports," "suggests," "is consistent with" |
| "Refutes" | Overclaim | "Challenges," "raises questions about" |
| "Obviously" | Dismissive | "The data indicate," "calculation shows" |
| "Impossible" | Overclaim | "Would require [specific condition]" |
| "Must" | Overclaim | "The model requires," "would need to" |
| "Complete" | Premature | "Addresses," "accounts for" |
| "Definitive" | Overclaim | "Substantive," "detailed" |

---

## Output Format

After running sanity check, document results:

**File Naming**: `YYYY-MM-DD_[Topic]_SanityCheck.md`
**Location**: Same folder as work being checked

**Template**:
```markdown
# Sanity Check Report: [Topic]
**Date**: YYYY-MM-DD
**Document Checked**: [filename]

## 1. Budget Closure
- [ ] Heat budget: ✅/❌ [notes]
- [ ] Mass/sediment budget: ✅/❌ [notes]
- [ ] Water budget: ✅/❌ [notes]
- [ ] Time budget: ✅/❌ [notes]

## 2. Physical Law Compliance
- [ ] Energy conservation: ✅/❌
- [ ] Momentum: ✅/❌
- [ ] Thermodynamics: ✅/❌
- [ ] Rate limits: ✅/❌

## 3. Assumption Audit
| Claim | Status | Justification |
|-------|--------|---------------|
| ... | STIPULATED/DERIVED/ASSUMED/EMPIRICAL | ... |

## 4. Calculation Traceability
- [ ] All numbers sourced: ✅/❌
- [ ] Spot-check passed: ✅/❌

## 5. Literature Cross-Check
- [ ] Key claims checked against data: ✅/❌
- [ ] No direct contradictions found: ✅/❌

## 6. Circularity Check
- [ ] Logical: ✅/❌
- [ ] Definitional: ✅/❌
- [ ] Parametric: ✅/❌
- [ ] Evidential: ✅/❌

## 7. Objection Engagement
- [ ] Strongest objections identified: ✅/❌
- [ ] Substantive responses provided: ✅/❌
- [ ] Residual issues acknowledged: ✅/❌

## 8. Falsifiability
- [ ] Risky predictions stated: ✅/❌
- [ ] Falsification criteria clear: ✅/❌

## 9. Professional Tone
- [ ] No prohibited language: ✅/❌
- [ ] Claims calibrated: ✅/❌

## 10. Symmetrical Standards
- [ ] Same rigor applied to our model: ✅/❌
- [ ] No double standards: ✅/❌

## Summary
**Overall**: ✅ PASS / ⚠️ CONDITIONAL / ❌ FAIL
**Issues Found**: [list]
**Actions Required**: [list]
**Proceed?**: YES / NO - [reason]
```

---

## When to Escalate

STOP and reassess before proceeding if:

- ❌ Any budget doesn't close within order of magnitude
- ❌ Physical law violation detected
- ❌ Circularity found in core argument
- ❌ Published data directly contradicts claim
- ❌ Cannot state falsification criteria
- ❌ Strongest objection has no substantive response
- ❌ Asymmetric standards detected

---

## Protocol Maintenance

**Version**: 1.0
**Created**: 2025-12-17
**Author**: JD Longmire / Claude collaboration
**Scope**: Scientific arguments challenging consensus (hydrotectonics, deep time, macro-evolution, etc.)

**Update when**:
- New failure mode discovered
- Check proves insufficient
- Scope expands to new domains

---

## Why This Matters

Challenging scientific consensus is legitimate but difficult. The asymmetric burden exists because:
1. Consensus represents accumulated evidence and testing
2. Extraordinary claims require extraordinary evidence
3. Errors by challengers damage credibility of all challengers

This protocol doesn't guarantee our conclusions are correct. It guarantees we've done due diligence - that we've checked our work with the same rigor we'd want applied to our critics.

**The goal is not to win arguments. The goal is to track truth.**

If our models fail these checks, we should revise them - not lower the bar.
