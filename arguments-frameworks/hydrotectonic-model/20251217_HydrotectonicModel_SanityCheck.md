# Sanity Check Report: Hydrotectonic Model v2.1

**Date**: 2025-12-17
**Document Checked**: `20251217-hydrotectonic-model-complete.md`
**Protocol Version**: SANITY_CHECK_PROTOCOL_SCIENTIFIC.md v1.0

---

## Summary

| Check | Status | Notes |
|-------|--------|-------|
| 1. Budget Closure | ⚠️ CONDITIONAL | Heat budget depends on undefended pore pressure assumption |
| 2. Physical Law Compliance | ⚠️ CONDITIONAL | Energy partitioning not quantified |
| 3. Assumption Audit | ❌ FAIL | Critical assumption (99% pore pressure) not defended |
| 4. Calculation Traceability | ⚠️ CONDITIONAL | Standard constants should be cited |
| 5. Literature Cross-Check | ⚠️ CONDITIONAL | Pore pressure/thin-film mechanism needs literature support |
| 6. Circularity Check | ✅ PASS | No circular reasoning detected |
| 7. Objection Engagement | ❌ FAIL | Strongest objections not addressed in document |
| 8. Falsifiability Check | ⚠️ CONDITIONAL | Some "predictions" are post hoc; novel ones need sharpening |
| 9. Professional Tone | ✅ PASS | Academic and measured |
| 10. Symmetrical Standards | ⚠️ CONDITIONAL | We have unsolved problems while criticizing consensus for same |

**Overall**: ❌ **FAIL** - Critical gaps identified before proceeding

---

## Detailed Results

### 1. Budget Closure

**Heat Budget:**
- INPUT: Gravitational PE = 10²⁵ J (10 blocks settling 1 km)
- OUTPUT (claimed): Frictional dissipation = 10²³ J (~1% of PE)
- GAP: Where does the other 99% go?

**Model claims** (Appendix B.3):
- Seismic radiation
- Plastic deformation
- Residual PE (blocks don't fully settle)

**Problem**: These are listed but NOT QUANTIFIED. The entire heat argument depends on only 1% converting to friction, but this isn't demonstrated.

**Critic's Challenge**:
- Uses μ = 0.01 on FULL normal stress → 8×10²⁶ J → 600 W/m²
- Model uses μ = 0.01 on EFFECTIVE stress (1% of normal) → 10²³ J → 7 W/m²
- **Difference is 1000×** and hinges entirely on pore pressure assumption

**Status**: ⚠️ CONDITIONAL - Budget closes IF pore pressure assumption holds

---

### 2. Physical Law Compliance

| Law | Status | Notes |
|-----|--------|-------|
| Energy conservation | ⚠️ | 99% of PE unaccounted (claimed but not calculated) |
| Momentum | ✅ | Force balance in Appendix D |
| Thermodynamics | ⚠️ | Heat sink (Hypercanes) capacity = heat budget, but both depend on same assumption |
| Rate limits | ⚠️ | Terminal velocity "estimated" at 10-100 m/hr without derivation |

**Status**: ⚠️ CONDITIONAL - No violations, but gaps in quantification

---

### 3. Assumption Audit

| Claim | Status | Justification | Critical? |
|-------|--------|---------------|-----------|
| Deep ballast at creation | STIPULATED | Biblical boundary (Stage 0) | No - labeled |
| **Pore pressure 99% lithostatic** | **ASSUMED** | Required for mechanism | **YES - UNDEFENDED** |
| Friction coefficient μ = 0.01 | ASSUMED | "Reduced friction" | Yes - needs source |
| Water film ~10 m thick | ASSUMED | "Order of magnitude" | Yes - not derived |
| Heat flux ~7 W/m² | DERIVED | Appendix B | **Depends on pore pressure** |
| Seismic/plastic = 99% PE | ASSUMED | Listed, not calculated | Yes - gap |

**Critical Finding**: The 7 W/m² claim is marked DERIVED but depends entirely on the ASSUMED 99% pore pressure. This is the exact point the critic attacks.

**Status**: ❌ FAIL - Critical assumption not defended

---

### 4. Calculation Traceability

| Number | Source | Traceable? |
|--------|--------|-----------|
| ρ = 2700 kg/m³ | Standard | ⚠️ Should cite textbook |
| M_ocean = 1.4×10²¹ kg | Standard | ⚠️ Should cite |
| c_p = 4186 J/(kg·K) | Standard | ⚠️ Should cite |
| L_v = 2.26×10⁶ J/kg | Standard | ⚠️ Should cite |
| σ_n = ρgh = 400 MPa | Calculated | ✅ |
| Hypercane threshold | Emanuel 1995 | ✅ |
| Evap rate 100 mm/hr | Vardiman 2003 | ✅ |

**Status**: ⚠️ CONDITIONAL - Minor issue; add standard citations

---

### 5. Literature Cross-Check

| Claim | Literature | Status |
|-------|-----------|--------|
| Transition zone water (ringwoodite) | Pearson et al. 2014 | ✅ Confirmed |
| Cold slabs in tomography | van der Hilst et al. 1997 | ✅ Confirmed |
| Near-lithostatic pore pressure at scale | **NOT CITED** | ❌ **NEEDS SUPPORT** |
| Thin-film lubrication at crustal scale | **NOT CITED** | ❌ **NEEDS SUPPORT** |
| Subduction zone decollements | Moore & Saffer 2001; etc. | ✅ Cited as analogs |

**Critical Gap**: The core mechanism (pore pressure → friction collapse → thin-film sliding) lacks direct literature support. The analogs cited (overpressured basins, decollements) exist at much smaller scales.

**Needed**:
- Literature on pore pressure approaching lithostatic at crustal scale
- Lubrication theory for geological detachments
- Stability analysis for thin-film sliding under load

**Status**: ⚠️ CONDITIONAL - Core mechanism needs literature support

---

### 6. Circularity Check

| Type | Status | Notes |
|------|--------|-------|
| Logical | ✅ PASS | Premises don't assume conclusion |
| Definitional | ✅ PASS | Terms defined independently |
| Parametric | ⚠️ CAUTION | Pore pressure assumption is load-bearing |
| Evidential | ✅ PASS | No evidence filtering detected |

**Note on Parametric**: The model doesn't derive pore pressure from other quantities - it assumes it. This isn't circular, but it IS a critical assumption that the entire model depends on. If this assumption fails, everything downstream fails.

**Status**: ✅ PASS (no circularity, but critical assumption flagged)

---

### 7. Strongest Objection Engagement

**The Facebook challenges represent the strongest objections:**

| Objection | Addressed? | Location |
|-----------|-----------|----------|
| Energy budget (600 vs 7 W/m²) | ❌ NO | Not in document |
| Pore pressure self-defeating | ❌ NO | Not addressed |
| Missing equations (shear, lubrication, Reynolds, drainage) | ❌ NO | Not provided |
| Lakatosian degenerative status | ⚠️ PARTIAL | Section 1.0.3 (symmetrical critique) |

**Critic's specific demands not met**:
1. Shear-stress derivation - NOT PROVIDED
2. Lubrication-theory equations - NOT PROVIDED
3. Reynolds number analysis - NOT PROVIDED
4. Pore-pressure diffusion modeling - NOT PROVIDED
5. Drainage-rate calculations - NOT PROVIDED
6. Energy-budget closure showing where PE goes - NOT PROVIDED

**Status**: ❌ FAIL - Strongest objections not engaged

---

### 8. Falsifiability Check

| Prediction | Risky? | Falsification Criteria |
|------------|--------|----------------------|
| Structural unconformity (chaotic/coherent) | ⚠️ | Vague - what counts? |
| Detachment horizons at 10-50 km | ✅ | Clear |
| Megabreccia at basin boundaries | ✅ | Clear |
| Elevated ringwoodite water | ❌ | Already confirmed - post hoc |
| Cold slabs at depth | ❌ | Already observed - post hoc |

**Issue**: Several "predictions" are already confirmed (Pearson 2014, van der Hilst 1997). These are accommodations of existing data, not risky predictions. The genuinely novel predictions (structural unconformity, specific detachment signatures) need sharper specification.

**Status**: ⚠️ CONDITIONAL - Need to distinguish risky predictions from post hoc accommodations

---

### 9. Professional Tone

**Scan for prohibited language:**

| Found | Context | Issue? |
|-------|---------|--------|
| "solves the heat problem" | Title claim | ⚠️ Minor - could say "addresses" |
| "physically coherent" | Multiple | ✅ OK |
| "provides...framework" | Conclusions | ✅ OK |
| "demonstrates...not prohibited" | Conclusions | ✅ OK (hedged) |

**No major issues found.** Tone is academic and measured throughout.

**Status**: ✅ PASS

---

### 10. Symmetrical Standards

| Our Criticism of Consensus | Same Problem in Our Model? |
|---------------------------|---------------------------|
| "Unfalsifiable - absorbs anomalies" | ⚠️ We absorb deep slab anomaly via Stage 0 |
| "Unsolved problems" | ⚠️ We have unsolved pore pressure problem |
| "Post hoc auxiliary hypotheses" | ⚠️ Stage 0 is a major auxiliary hypothesis |
| "Relies on untestable assumptions" | ✅ Our stipulations are explicit |

**Assessment**: The document acknowledges competing research programmes (Section 1.0.2), which is good. However, we criticize the consensus for having unsolved problems while having a major unsolved problem ourselves (pore pressure maintenance). This asymmetry should be acknowledged.

**Status**: ⚠️ CONDITIONAL - Acknowledge our own gaps more explicitly

---

## Critical Issues Summary

### Must Address Before Claiming Model Complete:

1. **Pore Pressure Defense**
   - The entire model depends on σ'_eff → 0 via pore pressure
   - No calculation or literature support provided
   - This is the EXACT point the critic attacks
   - **Need**: Lubrication theory, stability analysis, drainage calculations

2. **Energy Partitioning**
   - Claims 99% of PE goes to seismic/plastic/residual
   - None of these quantified
   - **Need**: Show calculation for where the other 10²⁵ J goes

3. **Objection Engagement**
   - Document doesn't address the strongest objections
   - **Need**: Add section responding to energy budget and pore pressure challenges

4. **Literature Support for Core Mechanism**
   - Pore pressure and thin-film sliding at crustal scale not demonstrated
   - **Need**: Literature review on fault lubrication, pore pressure at depth

### May Proceed With Caveats:

5. Standard constant citations (minor)
6. Sharpen novel predictions (moderate)
7. Acknowledge our unsolved problems alongside consensus's (moderate)

---

## Recommendation

**❌ DO NOT claim model "solves" heat problem until:**

1. Pore pressure maintenance is defended with:
   - Literature on achievable pore pressures at depth
   - Stability analysis (can the regime self-sustain?)
   - Drainage rate calculations
   - Response to "self-defeating" objection

2. Energy partitioning is quantified:
   - Calculate seismic radiation fraction
   - Calculate plastic work fraction
   - Show sum of all outputs = input

3. Objections are engaged:
   - Add explicit response section to document
   - Address critic's specific equation demands

**Proceed With**: Research to fill these gaps, then revise document.

---

## Next Actions

1. Literature search: pore pressure at crustal depths, fault lubrication mechanisms
2. Develop explicit pore pressure stability analysis
3. Quantify energy partitioning (seismic + plastic + residual + friction = total PE)
4. Add objection-response section to document
5. Re-run sanity check after revisions

---

**Report Generated**: 2025-12-17
**Checked By**: Claude / JD Longmire collaboration
**Protocol**: SANITY_CHECK_PROTOCOL_SCIENTIFIC.md v1.0
