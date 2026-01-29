---
title: "Temporal Confidence Decay: A Mathematical Framework for Historical Epistemic Humility"
date: 2024-09-22
category: epistemology
tags: [epistemology, historical-science, deep-time, confidence, philosophy-of-science]
source: substack
---

# Temporal Confidence Decay: A Mathematical Framework for Historical Epistemic Humility

## Abstract

This paper proposes a mathematical framework for quantifying epistemic confidence in claims about past events, introducing two key concepts: Temporal Confidence Decay (TCD) and the Occam Factor (OF). We argue that confidence in historical claims should decrease predictably with temporal distance and multiplicatively with each required assumption. Applying this framework to various historical claims reveals a significant mismatch between expressed certainty and justified confidence, particularly in the historical sciences. We demonstrate that many claims about deep time events approach zero confidence when proper temporal and assumption-based discounting is applied, suggesting a need for recalibration in how historical scientific claims are presented and evaluated. This work builds upon recent philosophical analyses of the historical sciences (Cleland 2002, 2011; Turner 2007, 2011) and probabilistic approaches to historical uncertainty (Lavan 2019; Lavan et al. 2021).

## 1. Introduction

The relationship between temporal distance and epistemic certainty has long been recognized informally—we are generally more confident about recent events than ancient ones. However, this recognition rarely translates into systematic adjustments in expressed confidence levels, particularly in scientific contexts (Cleland 2002; Frodeman 1995). This paper develops a quantitative framework for understanding how temporal distance and accumulated assumptions should affect our confidence in historical claims.

The motivation for this framework emerges from an observed paradox: while historians readily acknowledge uncertainty about events mere centuries ago (Tucker 2004), scientists often express near-certainty about events allegedly occurring millions or billions of years in the past (Turner 2007). This inconsistency suggests that different epistemological standards are being applied across domains, or that social and professional factors override proper epistemic calibration (Sepkoski 2019).

## 2. The Temporal Confidence Decay Model

### 2.1 Basic Framework

We propose that confidence in any historical claim should be modeled as:

**CF(t) = CF₀ × D(t) × OF**

Where:

- CF(t) = Confidence Factor at time t (ranging from 0 to 1)
- CF₀ = Initial confidence based on available evidence quality
- D(t) = Decay function accounting for temporal degradation
- OF = Occam Factor accounting for assumption accumulation

### 2.2 The Decay Function

The decay function D(t) represents how confidence degrades over time due to:

1. Physical degradation of evidence (Raab & Frodeman 2002)
2. Loss of contextual information (Tucker 2011)
3. Transmission errors in recorded information (Cleland 2011)
4. Interpretive drift as cultural contexts change (Gould 1987)

We consider three possible forms:

- Exponential: D(t) = e^(-λt)
- Power law: D(t) = 1/(1 + t)^α
- Logarithmic: D(t) = 1/log(k + t)

The exponential model appears most appropriate for general use, as it captures the compound nature of information loss over time, consistent with archaeological and geological evidence degradation patterns (Hamilton & Krus 2018).

### 2.3 The Occam Factor

Building on Occam's Razor, we introduce the Occam Factor as a quantifiable penalty for assumption accumulation:

**OF = A^(-n)**

Where:

- A = Average confidence in each assumption (0 < A < 1)
- n = Number of independent assumptions required

This formalization transforms Occam's Razor from a heuristic preference to a calculable confidence penalty.

## 3. Case Studies in Temporal Confidence

### 3.1 Julius Caesar (t ≈ 2,000 years)

For Caesar's existence, we have:

- Contemporary written accounts
- Physical artifacts (coins, inscriptions)
- Multiple independent sources
- Institutional continuity

Applying our framework:

- CF₀ ≈ 0.95 (strong initial evidence)
- λ ≈ 0.0001/year (slow decay for well-documented events)
- n ≈ 5 (few required assumptions)
- A ≈ 0.9

**CF(2000) = 0.95 × e^(-0.2) × 0.9^5 ≈ 0.47**

Even for one of history's best-documented figures, mathematical confidence drops below 50%.

### 3.2 Human Origins (t ≈ 300,000 - 7,000,000 years)

For human evolutionary origins:

- Fragmentary fossil evidence
- Geological dating methods
- Morphological comparisons
- Genetic inferences from living organisms

Required assumptions include:

- Radiometric dating accuracy over deep time
- Uniformitarian geological processes
- Morphological similarity indicates ancestry
- Genetic molecular clocks remain constant
- Fossilization is interpretable
- Present processes explain past events
- (many others)

Applying our framework:

- CF₀ ≈ 0.7 (fragmentary evidence)
- λ ≈ 0.0001/year
- n ≈ 30-50
- A ≈ 0.9

**CF(2,000,000) = 0.7 × e^(-200) × 0.9^40 ≈ 10^(-89)**

The confidence mathematically approaches zero.

### 3.3 Universal Common Descent (t ≈ 3,500,000,000 years)

For the claim that all life descended from a common ancestor:

- No direct observation
- Inference from current genetic similarities
- Assumption of constant natural processes
- Extrapolation from micro to macro evolution

The assumption stack includes all previous assumptions plus:

- Abiogenesis occurred
- Early life forms would leave detectable traces
- Evolution can produce novel body plans
- Genetic similarities prove common descent rather than common design
- (dozens more)

**CF(3,500,000,000) ≈ 10^(-150,000)**

The number becomes so small as to be mathematically indistinguishable from zero, supporting what Turner (2007) calls the "epistemic asymmetry" between experimental and historical sciences.

## 4. The Confidence Mismatch Phenomenon

### 4.1 Observed Patterns

Applying our framework reveals a striking pattern: expressed confidence in historical claims often inversely correlates with what temporal analysis would predict. Claims about recent historical events are often presented with appropriate uncertainty, while claims about events in deep time are presented as established facts (Gould 1987; Trend 2002).

Examples of mismatched confidence:

- "We think Caesar probably crossed the Rubicon" (high justified confidence, modest expression)
- "Dinosaurs evolved into birds 150 million years ago" (near-zero justified confidence, certain expression)
- "All life shares a common ancestor" (infinitesimal justified confidence, textbook fact)

This phenomenon has been noted by philosophers of the historical sciences (Turner 2011; Jeffares 2010), but its implications have not been fully appreciated in scientific practice.

### 4.2 Potential Explanations

Several factors may contribute to this mismatch:

1. **Methodological blindness**: Scientists may not recognize the compounding effect of assumptions
2. **Social dynamics**: Professional incentives favor confidence over uncertainty
3. **Paradigm protection**: Established frameworks resist confidence downgrading
4. **Rhetorical strategies**: Certainty is more persuasive than acknowledged uncertainty
5. **Category confusion**: Conflating observable present patterns with historical reconstruction

## 5. Implications for Scientific Practice

### 5.1 Recalibrating Scientific Communication

If we accept that temporal confidence decay is real and quantifiable, several practices should change:

1. **Graduated certainty language**: Claims should use language reflecting calculated confidence
2. **Explicit assumption listing**: All historical claims should enumerate required assumptions
3. **Confidence intervals**: Deep time claims should include temporal uncertainty ranges
4. **Alternative explanation acknowledgment**: Low-confidence claims should present alternatives

### 5.2 Reforming Educational Materials

Textbooks and educational materials particularly need reform:

- Replace "Scientists know that..." with "Based on X assumptions, scientists infer..."
- Include temporal confidence calculations for major claims
- Distinguish clearly between observation and historical reconstruction
- Present competing explanations for low-confidence scenarios

### 5.3 Reevaluating Consensus Claims

The framework suggests that many consensus positions in historical sciences may rest on unjustifiably high confidence. Rather than abandoning these positions, we should:

1. Acknowledge their tentative nature
2. Continue using them as working hypotheses
3. Remain genuinely open to alternatives
4. Avoid using consensus as an epistemological trump card

## 6. Objections and Responses

### 6.1 "This Framework Undermines All Historical Knowledge"

**Response**: The framework doesn't eliminate historical knowledge but calibrates confidence appropriately. Recent, well-documented events retain reasonable confidence levels. Only claims about deep time with large assumption stacks approach zero confidence.

### 6.2 "Scientific Methods Compensate for Temporal Distance"

**Response**: While scientific methods are powerful, they cannot eliminate temporal uncertainty. Each method introduces its own assumptions, which compound rather than cancel uncertainty (Cleland 2002). Radiometric dating, for instance, assumes constant decay rates—an assumption that cannot be directly verified over the time scales involved (Frodeman 1995). As Bayliss (2015) demonstrates, even sophisticated Bayesian chronological models must acknowledge increasing uncertainty with temporal distance.

### 6.3 "Successful Predictions Validate Deep Time Theories"

**Response**: Predictive success validates present-day patterns and mechanisms, not historical reconstructions. A theory can successfully predict current observations while being wrong about historical origins (Turner 2007). Ptolemaic astronomy made successful predictions while being fundamentally incorrect about cosmic structure. As Sober (1988) argues, the epistemic asymmetry between observing present patterns and inferring past causes remains insurmountable.

## 7. The Epistemic Virtue of Calibrated Confidence

Properly calibrated confidence represents an epistemic virtue often lacking in contemporary discourse about historical sciences. The tendency to overstate certainty about deep time events may stem from various motivations—defending against anti-scientific ideologies, maintaining professional authority, or simple habituation to conventional expressions—but it ultimately undermines scientific credibility.

Consider the rhetorical difference between:

- "Evolution is an established fact"
- "Based on current evidence and numerous assumptions, the theory of common descent represents our best working hypothesis, though mathematical analysis suggests we should hold it with appropriate uncertainty given the temporal distances involved"

The latter statement is more epistemically responsible while remaining scientifically substantive.

## 8. Conclusion

The Temporal Confidence Decay framework provides a mathematical tool for calibrating confidence in historical claims. When applied consistently, it reveals that many claims about deep time events command confidence levels approaching zero, despite being presented as established facts. This mismatch between expressed and justified confidence represents a significant epistemological problem in the historical sciences (Cleland 2002; Turner 2007).

The solution is not to abandon investigation of the deep past but to acknowledge the severe epistemic limitations temporal distance imposes (Currie 2018). By incorporating temporal confidence decay and the Occam Factor into our evaluation of historical claims, we can achieve greater intellectual honesty about what we can and cannot know about the distant past (Tucker 2004).

The framework suggests that phrases like "established fact" should be reserved for directly observable phenomena and recent, well-documented events. Claims about deep time should be presented as tentative inferences requiring numerous assumptions, with confidence levels that reflect their temporal distance and assumption stack (Lavan et al. 2021).

This recalibration would strengthen rather than weaken scientific credibility by demonstrating appropriate epistemic humility (Allchin 2011). It would also open space for genuine consideration of alternative explanations for observations currently interpreted through single dominant paradigms. In an era where trust in scientific institutions faces challenges, such intellectual honesty about the limitations of historical reconstruction could paradoxically strengthen public confidence in science's directly observable claims.

## References

Allchin, D. (2011). Evaluating knowledge of the nature of (whole) science. *Science Education*, 95(3), 518-542.

Bayliss, A. (2015). Quality in Bayesian chronological models in archaeology. *World Archaeology*, 47(4), 677-700.

Cleland, C. E. (2002). Methodological and epistemic differences between historical science and experimental science. *Philosophy of Science*, 69(3), 474-496.

Cleland, C. E. (2011). Prediction and explanation in historical natural science. *British Journal for the Philosophy of Science*, 62(3), 551-582.

Currie, A. (2018). *Rock, Bone, and Ruin: An Optimist's Guide to the Historical Sciences*. Cambridge: MIT Press.

Frodeman, R. (1995). Geological reasoning: Geology as an interpretive and historical science. *Geological Society of America Bulletin*, 107(8), 960-968.

Gould, S. J. (1987). *Time's Arrow, Time's Cycle: Myth and Metaphor in the Discovery of Geological Time*. Cambridge: Harvard University Press.

Hamilton, W. D., & Krus, A. M. (2018). The myths and realities of Bayesian chronological modeling revealed. *American Antiquity*, 83(2), 187-203.

Jeffares, B. (2010). Guessing the future of the past. *Biology & Philosophy*, 25(1), 125-142.

Lavan, M. (2019). Epistemic uncertainty, subjective probability, and ancient history. *The Journal of Interdisciplinary History*, 50(1), 91-111.

Lavan, M., Jew, D., & Danon, B. (Eds.). (2021). *The Uncertain Past: Probability in Ancient History*. Cambridge: Cambridge University Press.

Raab, L. M., & Frodeman, R. (2002). What is it like to be a geologist? A phenomenology of geology and its epistemological implications. *Philosophy & Geography*, 5(1), 69-81.

Sepkoski, D. (2019). The unfinished synthesis? Paleontology and evolutionary biology in the 20th century. *Journal of the History of Biology*, 52(4), 687-703.

Sober, E. (1988). *Reconstructing the Past: Parsimony, Evolution, and Inference*. Cambridge: MIT Press.

Tucker, A. (2004). *Our Knowledge of the Past: A Philosophy of Historiography*. Cambridge: Cambridge University Press.

Tucker, A. (2011). Historical science, over- and underdetermined: A study of Darwin's inference of origins. *The British Journal for the Philosophy of Science*, 62(4), 805-829.

Turner, D. (2007). *Making Prehistory: Historical Science and the Scientific Realism Debate*. Cambridge: Cambridge University Press.

Turner, D. (2011). *Paleontology: A Philosophical Introduction*. Cambridge: Cambridge University Press.

Van den Brink, G., de Ridder, J., & van Woudenberg, R. (2017). The epistemic status of evolutionary theory. *Theology and Science*, 15(4), 454-472.
