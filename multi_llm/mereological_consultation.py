"""
Multi-LLM Consultation: Mereological Irreducibility for Intentional Properties
Session 001 - Demonstratio Potissima refinement
"""

import asyncio
import sys
import json
from pathlib import Path
from datetime import datetime

# Add parent directory to path to import enhanced_llm_bridge
sys.path.append(str(Path(__file__).parent))

from enhanced_llm_bridge import EnhancedMultiLLMBridge, QueryType

async def consult_on_mereological_irreducibility():
    """
    Consult all three LLMs on developing a robust defense of mereological
    irreducibility for intentional properties specifically.
    """

    # Initialize the bridge
    bridge = EnhancedMultiLLMBridge()

    # Define the consultation prompt
    consultation_prompt = """
## CONTEXT: Demonstratio Potissima - Critical Premise Defense

We are refining a formal deductive argument for classical theism called the Demonstratio Potissima.
Multi-LLM analysis has identified **mereological irreducibility for intentional properties** as the
load-bearing premise requiring robust defense.

## THE PREMISE TO DEFEND:

**Mereological Irreducibility Principle:** A whole cannot possess properties that are not present
in at least some of its parts. Specifically, **intentional properties** (aboutness, representation,
directedness toward unrealized ends) cannot emerge from purely non-intentional components.

## THE CHALLENGE:

Critics argue that emergence studies show higher-level properties can arise from lower-level ones:
- **Water's liquidity** emerges from H₂O molecules that aren't themselves liquid
- **Temperature** emerges from molecular motion without individual molecules having temperature
- **Consciousness/intentionality** might work similarly - emerging from non-intentional physical processes

The objector claims: "The entire field of emergence studies argues against mereological irreducibility.
Why can't intentionality emerge from non-intentional parts just like liquidity emerges from non-liquid molecules?"

## YOUR TASK:

Develop a philosophically rigorous defense showing why **intentionality specifically** cannot emerge
from the non-intentional, even though other properties (like liquidity) can emerge from lower-level components.

Please address:

1. **Category Distinction:** What makes intentionality fundamentally different from emergent properties like liquidity or temperature? Why is this a categorical difference, not just a difference of degree?

2. **Weak vs. Strong Emergence:** Explain the difference between:
   - **Weak emergence** (reducible, like liquidity = molecules moving in patterns)
   - **Strong emergence** (genuinely novel, irreducible)
   - Why intentionality falls in the latter category

3. **The "Aboutness" Problem:** How do we show that **representation** (directedness toward unrealized future states, holding abstract goals) cannot arise from particles moving deterministically according to physical laws?

4. **Direct Response to Liquidity Objection:** Precisely why is the liquidity analogy disanalogous? What feature does intentionality have that liquidity lacks?

5. **Anticipated Counter-Arguments:** What are the strongest objections to this defense, and how should they be addressed?

6. **Philosophical Support:** Which philosophers have developed the strongest arguments for this position? Which frameworks support it?

## DESIRED OUTPUT:

A clear, rigorous philosophical argument that:
- Distinguishes intentionality from uncontroversial emergence cases
- Shows why non-representing parts cannot generate representation
- Addresses the liquidity objection directly
- Anticipates and defuses strongest counter-arguments
- Raises confidence in mereological irreducibility from ~40% to 70-80%

Please provide your most rigorous philosophical analysis.
"""

    print("\n" + "="*80)
    print("MULTI-LLM CONSULTATION: Mereological Irreducibility Defense")
    print("="*80)
    print("\nQuerying Grok, ChatGPT, and Gemini...")
    print("\nThis may take 30-60 seconds...\n")

    # Run the consultation (using THEORY_QUESTION type for philosophical analysis)
    results = await bridge.consult_all_experts(
        prompt=consultation_prompt,
        query_type=QueryType.THEORY_QUESTION,
        use_cache=False  # Don't cache this specific consultation
    )

    # Display results
    bridge.print_results_with_scores(results)

    # Save detailed results to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = Path(__file__).parent.parent / "sessions" / f"session-001-mereological-consultation-{timestamp}.json"

    # Extract successful responses and calculate averages
    successful_responses = [r for r in results['responses'] if r.get('success')]
    avg_quality = sum(r.get('quality_score', 0) for r in successful_responses) / len(successful_responses) if successful_responses else 0

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': timestamp,
            'prompt': consultation_prompt,
            'query_type': results.get('query_type'),
            'responses': results['responses'],
            'quality_scores': results.get('quality_scores', {}),
            'best_response': results.get('best_response'),
            'analysis': {
                'total_responses': len(results['responses']),
                'successful_responses': len(successful_responses),
                'avg_quality_score': avg_quality
            }
        }, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*80}")
    print(f"Detailed results saved to: {output_file.name}")
    print(f"Average quality score: {avg_quality:.2f}")
    print(f"Best response: {results.get('best_response', {}).get('source', 'N/A')}")
    print(f"{'='*80}\n")

    return results

if __name__ == "__main__":
    asyncio.run(consult_on_mereological_irreducibility())
