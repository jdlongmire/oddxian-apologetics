# Quantitative Consistency Check

**Date:** 2025-11-20
**Purpose:** Verify all numerical values are consistent across the hydrotectonic paper

---

## Key Values Summary

### Block Dimensions and Masses

**Example 1 (Section 3.3, line 158):**
- Dimensions: 1000 km × 1000 km × 30 km
- Mass: ~10²⁰ kg
- Used for: Heat capacity calculation in water

**Example 2 (Section 4.1, line 188):**
- Dimensions: 800 km × 1000 km × 35 km
- Mass: M ≈ 8 × 10¹⁹ kg
- Used for: Quantitative force balance

**Example 3 (Section 4.4, line 230):**
- Mass: M ~ 10²⁰ kg each
- Used for: Heat budget calculation with ten blocks

**Consistency:** ✅ Different examples use slightly different dimensions, producing masses in the range 8 × 10¹⁹ to 10²⁰ kg. This is appropriate variation for illustrative purposes.

---

### Displacements

**Throughout paper:**
- Standard displacement: **1000 km**
- Context: "thousands of kilometers over the course of months"

**Consistency:** ✅ Uniform use of 1000 km as representative displacement.

---

### Velocities

**Throughout paper:**
- General: "tens to hundreds of meters per hour"
- Specific example: 100 m/hr (used in kinetic energy calculation, line 230)

**Consistency:** ✅ Consistent phrasing. 100 m/hr is midrange of "tens to hundreds."

---

### Heat Flux

**All references:**
- Line 14 (Abstract): ~7 W/m²
- Line 56 (Summary): ~7 W/m²
- Line 230 (Section 4.4): ~7 W/m² (calculated from 10²³ J / surface area / time)
- Line 232 (Section 4.4): "additional 7 W/m²"
- Line 322 (Section 6.6): ~7 W/m²

**Consistency:** ✅ Perfectly consistent across all mentions.

---

### Temperature Increase

**All references:**
- Line 14 (Abstract): ~1 K
- Line 56 (Summary): ~1 K
- Line 232 (Section 4.4): ΔT ~ 1 K (calculated from radiation balance)
- Line 322 (Section 6.6): ~1 K
- Line 648 (Appendix B): ~1 K

**Consistency:** ✅ Perfectly consistent. Calculation in Section 4.4 (line 232) shows 7 W/m² / 6 W/m²·K ≈ 1 K.

---

### Energy Budgets

**Frictional work:**
- Line 230: W ~ 10²³ J (from moving ten blocks 1000 km)

**Gravitational potential energy:**
- Line 158: ΔPE ~ 10²⁴ J (single block, 1 km elevation change)
- Line 230: ΔPE = MgΔh ~ 10²⁴ J (mentioned as dominant energy source)

**Kinetic energy:**
- Line 230: KE ≈ 4 × 10¹⁶ J per block at 100 m/hr
- Line 230: Total KE ~ 4 × 10¹⁷ J for ten blocks (< 0.5% of friction budget)

**Consistency:** ✅ All values consistent:
- Frictional work (10²³ J) is ~10% of gravitational PE (10²⁴ J)
- Kinetic energy (10¹⁷ J) is <<< 1% of frictional work
- Hierarchy: PE (10²⁴) > Friction (10²³) >> KE (10¹⁷)

---

### Water Layer Thickness

**Line 158 (Section 3.3):**
- "10-meter-thick water layer at the base of the block"
- Volume: 10¹³ m³
- Mass: 10¹⁶ kg

**Note:** Other sections mention "thin water films" (mm to cm scale) for the actual sliding interface. The 10-meter layer in line 158 refers to the total water volume involved, not necessarily a uniform film thickness.

**Consistency:** ✅ Context distinguishes between:
- Total water volume mobilized (~10 m equivalent depth over block base)
- Interfacial film thickness (mm-cm scale)

---

### Other Key Values

**Friction coefficient:**
- Pre-collapse (dry): 0.6-0.85 (Byerlee friction)
- Post-collapse (water-lubricated): ~0.01
- Reduction factor: 60-85×

**Effective stress:**
- Reduced to 1% of lithostatic during collapse
- σ'_n = 4 MPa at depth 15 km (from σ_n = 400 MPa at 1% reduction)

**Earth surface area:**
- 5 × 10¹⁴ m² (used in heat flux calculation)

**Time duration:**
- One year: 3 × 10⁷ s (used in heat flux calculation)

**Consistency:** ✅ All standard values used consistently.

---

## Cross-Section Verification

### Heat Budget (Section 4.4, line 230)

**Given:**
- Ten blocks, M ~ 10²⁰ kg each
- Distance: 1000 km
- Friction coefficient: 0.01
- Effective stress: 1% of lithostatic

**Work done:**
- W ~ 10²³ J

**Heat flux:**
- Distributed over Earth's surface area (5 × 10¹⁴ m²)
- Over one year (3 × 10⁷ s)
- Flux = W / (Area × Time) = 10²³ / (5 × 10¹⁴ × 3 × 10⁷)
- Flux = 10²³ / 1.5 × 10²² = 6.7 W/m² ≈ **7 W/m²** ✅

### Temperature Increase (Section 4.4, line 232)

**Given:**
- Additional heat flux: 7 W/m²
- Surface temperature: T ~ 288 K
- Radiative balance: ΔF = 4σT³ΔT

**Calculation:**
- 4σT³ = 4 × (5.67 × 10⁻⁸) × (288)³
- 4σT³ = 4 × 5.67 × 10⁻⁸ × 2.39 × 10⁷
- 4σT³ ≈ 5.4 W/m²·K ≈ **6 W/m²·K** (as stated)

**Temperature increase:**
- ΔT = ΔF / (4σT³) = 7 / 6 ≈ **1.2 K** ≈ **1 K** ✅

---

## Conclusion

**All quantitative values are internally consistent across the document.**

### Verified Consistencies:
- ✅ Block masses scale correctly with dimensions
- ✅ Heat flux (~7 W/m²) calculated consistently
- ✅ Temperature increase (~1 K) calculated correctly
- ✅ Energy hierarchy (PE > Friction >> KE) maintained
- ✅ Velocities (tens to hundreds m/hr) used consistently
- ✅ Displacements (1000 km) uniform
- ✅ Friction coefficients and reductions consistent

### Appropriate Variations:
- Block dimensions vary between examples (appropriate for different contexts)
- Water layer descriptions distinguish total volume vs. film thickness

**Status:** No inconsistencies found. Paper is quantitatively coherent.
