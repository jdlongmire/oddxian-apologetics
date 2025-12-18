# Kinetic Energy Dissipation During Block Collisions

**Calculation Date:** November 20, 2025
**Purpose:** Quantify heat generation from kinetic energy dissipation when continental blocks collide
**Status:** Draft for integration into paper Section 4.4

---

## 1. Executive Summary

The reviewer correctly noted that the heat budget in Section 4.4 accounts for frictional work during sliding but omits kinetic energy dissipation when blocks decelerate and collide. This calculation shows:

1. **Kinetic energy per block:** $\sim 4 \times 10^{16}$ J (at v = 100 m/hr)
2. **Total for 10 major blocks:** $\sim 4 \times 10^{17}$ J
3. **As fraction of frictional budget:** **0.4%** (negligible)
4. **Conclusion:** KE dissipation is 2-3 orders of magnitude smaller than frictional dissipation and does not materially affect the heat budget

---

## 2. Block Parameters

### 2.1. Typical Continental Block

**Linear dimensions:**
- Length: $L \sim 1000$ km $= 10^6$ m
- Width: $W \sim 1000$ km $= 10^6$ m
- Thickness: $h \sim 30$ km $= 3 \times 10^4$ m (crustal thickness)

**Volume:**
$$V = L \times W \times h = (10^6)(10^6)(3 \times 10^4) = 3 \times 10^{16}~\text{m}^3$$

**Mass** (assuming crustal density $\rho = 2700$ kg/m³):
$$M = \rho V = (2700)(3 \times 10^{16}) = 8.1 \times 10^{19}~\text{kg}$$

**Round to:** $M \sim 10^{20}$ kg (order of magnitude for large continental fragment)

### 2.2. Velocity Range

From Section 4.1 of paper:
> "Velocities of tens to hundreds of meters per hour"

**Conservative estimate:** $v = 100$ m/hr

**Conversion to SI:**
$$v = \frac{100~\text{m}}{3600~\text{s}} = 0.028~\text{m/s}$$

**Upper bound:** $v = 500$ m/hr $= 0.139$ m/s

---

## 3. Kinetic Energy Calculation

### 3.1. Single Block

**Kinetic energy:**
$$KE = \frac{1}{2}Mv^2$$

**At v = 100 m/hr (0.028 m/s):**
$$KE = \frac{1}{2}(10^{20})(0.028)^2 = 3.9 \times 10^{16}~\text{J}$$

**At v = 500 m/hr (0.139 m/s):**
$$KE = \frac{1}{2}(10^{20})(0.139)^2 = 9.7 \times 10^{17}~\text{J}$$

### 3.2. Global Total (Multiple Blocks)

**Estimate of major blocks in motion:**
- Paper mentions "ten continental-scale blocks" (Section 4.4)
- Not all move at maximum velocity simultaneously
- Effective number at high velocity: ~5-10

**Conservative estimate (10 blocks at 100 m/hr):**
$$KE_{total} = 10 \times 3.9 \times 10^{16} = 3.9 \times 10^{17}~\text{J}$$

**Upper bound (10 blocks at 500 m/hr):**
$$KE_{total} = 10 \times 9.7 \times 10^{17} = 9.7 \times 10^{18}~\text{J}$$

---

## 4. Comparison to Frictional Dissipation Budget

### 4.1. Total Frictional Work (from Section 4.4)

Paper estimates:
$$W_{friction} \sim 10^{23}~\text{J}$$

### 4.2. Kinetic Energy as Fraction

**Conservative case:**
$$\frac{KE_{total}}{W_{friction}} = \frac{3.9 \times 10^{17}}{10^{23}} = 3.9 \times 10^{-6} = 0.0004 = 0.04\%$$

**Upper bound case:**
$$\frac{KE_{total}}{W_{friction}} = \frac{9.7 \times 10^{18}}{10^{23}} = 9.7 \times 10^{-5} = 0.0097 = 1\%$$

### 4.3. Interpretation

Kinetic energy dissipation is **2-3 orders of magnitude smaller** than frictional dissipation. Even in the upper bound scenario, it represents only ~1% of the total heat budget.

**Why is KE so small compared to friction?**

The frictional work is:
$$W = F \times d$$

where $F$ is frictional force and $d$ is distance traveled.

For a block moving 1000 km with effective friction force $F = \mu \sigma_{eff} A$:
- Even at reduced friction ($\mu = 0.01$) and low effective stress (1% of lithostatic)
- Force is still large ($F \sim 10^{16}$ N)
- Distance is large ($d = 10^6$ m)
- Work: $W \sim 10^{22}$ J

Whereas kinetic energy scales with $v^2$, and the velocities are geologically fast but mechanically slow (cm/s range).

**Conclusion:** The low velocities mean kinetic energy is negligible compared to work done over large distances.

---

## 5. Where Does Kinetic Energy Go?

### 5.1. Collision Dynamics

When blocks collide, kinetic energy dissipates through:

1. **Elastic deformation and seismic radiation** (~5-10%)
   - Generates earthquakes
   - Energy propagates as seismic waves
   - Most dissipates far from collision zone

2. **Plastic deformation (mountain building)** (~40-60%)
   - Crustal thickening
   - Converts KE → gravitational PE
   - Work done lifting rock against gravity
   - Not directly converted to heat

3. **Frictional heating at collision interface** (~30-50%)
   - Fault slip at plate boundary
   - This IS converted to heat
   - But already included in frictional dissipation budget

### 5.2. Heat Generation from Collisions

Only the frictional component directly produces heat. Assuming 40% of KE goes to frictional heating:

**Conservative case:**
$$Q_{collision} = 0.4 \times 3.9 \times 10^{17} = 1.6 \times 10^{17}~\text{J}$$

**Upper bound:**
$$Q_{collision} = 0.4 \times 9.7 \times 10^{18} = 3.9 \times 10^{18}~\text{J}$$

**As fraction of total heat budget:**
- Conservative: $\frac{1.6 \times 10^{17}}{10^{23}} = 0.00016 = 0.016\%$
- Upper bound: $\frac{3.9 \times 10^{18}}{10^{23}} = 0.0039 = 0.4\%$

**Conclusion:** Heat from collision-related friction is **negligible** compared to the heat from continuous sliding friction over thousands of kilometers.

---

## 6. Gravitational Potential Energy: The Dominant Source

### 6.1. The Reviewer's Implied Concern

A more significant energy budget question is: what drives block motion? The paper correctly identifies gravitational potential energy (PE) as a major source:

> "...dissipating 10²⁴ J in mantle rock...even if all the gravitational potential energy of the block (mass ~10²⁰ kg, elevation change ~1 km, ΔPE ~ 10²⁴ J)..." (Section 3.3)

This suggests that **gravitational PE release** during block motion and settling is on the order of $10^{24}$ J, **ten times larger** than the frictional budget estimate of $10^{23}$ J.

### 6.2. Where Does Gravitational PE Go?

When blocks move from elevated positions to lower elevations (or basins subside):

$$\Delta PE = Mg\Delta h$$

For block settling by $\Delta h = 1$ km average:
$$\Delta PE = (10^{20})(10)(10^3) = 10^{24}~\text{J}$$

This energy is partitioned among:
1. **Frictional dissipation** (heat) - as blocks slide
2. **Seismic radiation** (elastic waves)
3. **Plastic work** (deformation, fracturing)
4. **Kinetic energy** (block motion)
5. **Residual PE** (not fully dissipated; blocks reach new equilibrium)

### 6.3. Is the $10^{23}$ J Estimate Too Low?

**Paper's estimate (Section 4.4):**
$$W = N \cdot F \cdot D = (10)(\text{friction force})(10^6~\text{m}) \approx 10^{23}~\text{J}$$

**Gravitational PE available:**
$$\Delta PE \sim 10^{24}~\text{J}$$

**Implication:** If only 10% of gravitational PE converts to frictional heat, the estimate is correct. The remaining 90% goes to:
- Seismic energy (radiated away, minimal local heating)
- Plastic deformation (stored as strain energy or new surface area)
- Residual PE (blocks don't fully settle in 1 year)

**Sensitivity check:** Even if 50% of gravitational PE → heat, total dissipation is $5 \times 10^{23}$ J, still well within the bounds showing modest surface heating (~1-2 K based on steam calculation).

### 6.4. Recommendation

The paper should clarify:
1. Kinetic energy is negligible (~0.4% of heat budget)
2. Gravitational PE is the dominant **energy source** for block motion
3. Frictional dissipation budget ($10^{23}$ J) represents 10-50% of available gravitational PE
4. Even if larger fraction converts to heat, the water-mediated dissipation mechanism keeps temperature rise modest

---

## 7. Summary and Integration Points

### 7.1. Key Results

| Component | Energy (J) | % of Friction Budget | Significance |
|-----------|-----------|---------------------|--------------|
| **Frictional work** | $10^{23}$ | 100% (baseline) | Dominant heat source |
| **Kinetic energy (total)** | $4 \times 10^{17}$ (conservative) | 0.4% | Negligible |
| | $10^{19}$ (upper bound) | 10% | Still minor |
| **KE → heat (collisions)** | $1.6 \times 10^{17}$ | 0.16% | Negligible |
| **Gravitational PE available** | $10^{24}$ | 1000% | Primary energy source |

### 7.2. Clarifications Needed in Paper

**Current statement (Section 4.4):**
> "For order-of-magnitude estimation: moving ten continental-scale blocks (M ~ 10²⁰ kg each) an average of 1000 km with friction coefficient 0.01..."

**Recommended addition:**

> "This estimate accounts for frictional work during sliding. Additional heat from kinetic energy dissipation when blocks decelerate is negligible: for blocks moving at 100 m/hr, kinetic energy is $KE = \frac{1}{2}Mv^2 \approx 4 \times 10^{16}$ J per block, giving total kinetic dissipation of $\sim 4 \times 10^{17}$ J for ten blocks—less than 0.5% of the frictional budget. The dominant energy source is gravitational potential energy as blocks settle into lower elevations, releasing $\Delta PE = Mg\Delta h \sim 10^{24}$ J. The frictional dissipation estimate ($10^{23}$ J) represents approximately 10% of this available gravitational energy, with the remainder partitioned among seismic radiation, plastic deformation, and residual potential energy in the post-collapse configuration."

### 7.3. Does This Change the Heat Budget Conclusion?

**No.** Even accounting for:
- Kinetic energy dissipation (negligible)
- Higher gravitational PE conversion to heat (factor of 5× increase possible)

The key result remains: **dissipation in water at shallow depths produces temperature increases of ~1-2 K**, far below the catastrophic hundreds of Kelvin in mantle-shear models.

**Why robust?**
The advantage of the hydraulic model is not the total energy involved but **where and how it dissipates**:
- Water heat capacity 4× higher than rock
- Dissipation at shallow depths → efficient cooling
- Distributed over large areas and volumes
- Phase changes absorb energy (vaporization)

Whether total energy is $10^{23}$ J or $5 \times 10^{23}$ J, dissipating it in water still avoids thermal catastrophe.

---

## 8. References

**Collision mechanics and energy partitioning:**
- Melosh, H.J., 1989. *Impact Cratering: A Geologic Process*. Oxford: Oxford University Press. (Chapter 3: Energy partitioning in impacts - analogous to crustal block collisions)

- Kanamori, H. and Brodsky, E.E., 2004. The physics of earthquakes. *Reports on Progress in Physics*, 67(8), pp.1429-1496. (Seismic efficiency: fraction of strain energy released as seismic waves vs. heat)

**Mountain building energetics:**
- England, P. and Molnar, P., 1990. Surface uplift, uplift of rocks, and exhumation of rocks. *Geology*, 18(12), pp.1173-1177. (Energetics of crustal thickening)

---

## 9. Recommended Text for Paper

### Option A: Brief Addition to Section 4.4

Insert after the sentence ending "...average flux of ~7 W/m²":

> "This calculation includes frictional work during sliding but omits kinetic energy dissipation when blocks collide. However, this omission is justified: for a continental block with mass $M \sim 10^{20}$ kg moving at $v = 100$ m/hr $(\approx 0.03$ m/s), kinetic energy is $KE = \frac{1}{2}Mv^2 \approx 4 \times 10^{16}$ J. For ten major blocks, total kinetic energy is $\sim 4 \times 10^{17}$ J, less than 0.5% of the frictional dissipation budget. Even if all of this kinetic energy converted to heat during collisions (an upper bound; much goes to seismic radiation and plastic deformation), it would not materially affect the heat flux estimate."

### Option B: Footnote

Add footnote to "For order-of-magnitude estimation" sentence:

> "The kinetic energy of moving blocks is negligible compared to frictional dissipation: $KE = \frac{1}{2}Mv^2 \approx 4 \times 10^{16}$ J per block at $v = 100$ m/hr, giving $\sim 4 \times 10^{17}$ J total (<0.5% of frictional work). Gravitational potential energy release ($\Delta PE = Mg\Delta h \sim 10^{24}$ J as blocks settle) is the dominant energy source; the frictional estimate represents ~10% conversion of available gravitational energy."

---

**Calculation Status:** Complete
**Recommendation:** **Option A** (brief addition to Section 4.4)
**Impact:** Addresses reviewer's legitimate concern, shows it's negligible, maintains focus on main argument
**Next Step:** User review, then integrate into paper alongside steam calculation
