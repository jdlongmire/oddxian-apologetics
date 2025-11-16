# Multi-LLM Expert Consultation System for Christian Apologetics

## Overview

The Multi-LLM system provides parallel consultation across multiple AI experts (Grok, ChatGPT, Gemini) for Christian apologetics development, specializing in argument refinement, peer review, biblical scholarship, and philosophical analysis.

**Architecture Note**: This system supplements Claude Code (your primary development assistant) by providing additional expert perspectives when needed. Claude Code handles direct development work, while the multi-LLM team offers diverse opinions for complex apologetics challenges.

## Status: ✅ FULLY OPERATIONAL (Phase 1 Enhanced)

**All 3 APIs Working:**
- ✅ Grok (Grok-3 model)
- ✅ ChatGPT (GPT-4 model)
- ✅ Gemini (Gemini-2.0-flash-exp model)

**Core Features:**
- ✅ Parallel consultation (async requests)
- ✅ Response synthesis with recommendation extraction
- ✅ Comprehensive test suite
- ✅ Session logging

**Phase 1 Enhancements:**
- ✅ SQLite caching with query fingerprinting (SHA256)
- ✅ Smart TTL by query type (1-30 days)
- ✅ Exponential backoff retry logic (3 attempts)
- ✅ Multi-dimensional quality scoring (5 dimensions)
- ✅ Automatic query type detection
- ✅ Response ranking by quality
- ✅ Specialized consultation methods

## Quick Start

### 1. Configuration

```bash
# Copy template and add your API keys
cp api_config_template.json api_config.json
# Edit api_config.json with your keys (NEVER commit this file!)
```

### 2. Validate API Health

Quick health check (recommended before each session):

```bash
cd multi_llm
python3 health_check.py
```

Expected output:
```
======================================================================
API HEALTH CHECK
======================================================================

Overall Status: [OK] HEALTHY
Healthy APIs: 3/3

API Status:
  [OK] GROK: 0.47s
  [OK] CHATGPT: 0.51s
  [OK] GEMINI: 0.34s
======================================================================

[SUCCESS] All APIs operational and ready for use
```

**Exit Codes**:
- `0`: All APIs healthy
- `1`: Degraded (some APIs unavailable)
- `2`: Unhealthy (no APIs available)

### 3. Use for Apologetics Consultation

```python
import asyncio
from enhanced_llm_bridge import EnhancedMultiLLMBridge, QueryType

async def main():
    bridge = EnhancedMultiLLMBridge()

    # Option 1: Argument development
    result = await bridge.consult_argument(
        argument="Fine-tuning of physical constants points to design",
        objections=["Multiverse theory", "Anthropic principle"],
        context="Cosmological argument for God's existence"
    )

    # Option 2: Biblical/theological consultation
    result = await bridge.consult_theology(
        question="How does Romans 5:12 relate to the problem of death before the Fall?",
        context="Young Earth Creationism vs Old Earth perspectives"
    )

    # Option 3: Peer review of apologetics content
    result = await bridge.consult_peer_review(
        section="Your article content here...",
        focus_area="logical consistency and biblical fidelity"
    )

    # Option 4: General consultation with auto-detection
    result = await bridge.consult_all_experts(
        "What are the strongest responses to the problem of evil?",
        query_type=QueryType.GENERAL  # Auto-detected if omitted
    )

    # Results include quality scores and rankings
    print(f"Best response from: {result['best_response']['source']}")
    print(f"Quality score: {result['best_response']['quality']:.2f}/1.0")

    # Cache stats
    stats = bridge.get_cache_stats()
    print(f"Cache: {stats['hit_rate']:.1%} hit rate")

asyncio.run(main())
```

## Apologetics-Specific Features

### Query Types for Apologetics

The system automatically detects and optimizes for:

- **ARGUMENT_DEVELOPMENT**: Refining philosophical/theological arguments
- **BIBLICAL_ANALYSIS**: Scripture interpretation and theology
- **PEER_REVIEW**: Content review for logical/biblical soundness
- **OBJECTION_RESPONSE**: Addressing skeptical challenges
- **GENERAL**: General apologetics questions

### Quality Scoring for Apologetics

Responses automatically scored across 5 dimensions:

1. **Biblical Accuracy** (30% weight): Scripture citations, theological soundness
2. **Logical Rigor** (25%): Argument validity, avoiding fallacies
3. **Practical Applicability** (20%): Usability in actual apologetics contexts
4. **Scholarly Depth** (15%): Historical/philosophical grounding
5. **Clarity** (10%): Clear communication for target audience

```python
result = await bridge.consult_argument(argument, objections)

# Access quality scores
for response in result['responses']:
    scores = response['quality_scores']
    print(f"{response['source']}: {scores.overall:.2f}/1.0")
    print(f"  Biblical accuracy: {scores.biblical_accuracy:.2f}")
    print(f"  Logical rigor: {scores.logical_rigor:.2f}")
    print(f"  Practical applicability: {scores.practicality:.2f}")

# Best response automatically identified
best = result['best_response']
print(f"Recommended: {best['source']} ({best['quality']:.2f}/1.0)")
```

## Common Use Cases

### 1. Developing Arguments

```python
result = await bridge.consult_argument(
    argument="The resurrection of Jesus is best explained by actual resurrection",
    objections=[
        "Hallucination hypothesis",
        "Legend development theory",
        "Conspiracy theory"
    ],
    context="Historical evidence for Christianity"
)
```

### 2. Biblical/Theological Questions

```python
result = await bridge.consult_theology(
    question="Does Genesis require a literal six-day creation?",
    context="Examining Hebrew yom and framework hypothesis"
)
```

### 3. Responding to Objections

```python
result = await bridge.consult_objection_response(
    objection="The God of the Old Testament is morally problematic",
    topic="Divine command theory and progressive revelation",
    audience="philosophical skeptics"
)
```

### 4. Content Review

```python
result = await bridge.consult_peer_review(
    section="""
    Your article or argument text here...
    Multiple paragraphs...
    """,
    focus_area="Check for logical fallacies and biblical accuracy"
)
```

### 5. Research Questions

```python
result = await bridge.consult_all_experts(
    "What are the strongest cosmological arguments currently in the literature?",
    query_type=QueryType.GENERAL
)
```

## Caching & Performance

### Smart Caching by Query Type

- **Arguments**: 14 days (arguments evolve slowly)
- **Biblical questions**: 30 days (foundational theology stable)
- **Peer review**: 1 day (context-dependent)
- **Objection responses**: 7 days (cultural context shifts)
- **General**: 7 days (default)

### Cache Management

```python
# Check cache statistics
stats = bridge.get_cache_stats()
print(f"Total entries: {stats['total_entries']}")
print(f"Hit rate: {stats['hit_rate']:.1%}")
print(f"Arguments cached: {stats['by_type']['argument']}")

# Clear cache if needed
bridge.clear_cache()  # Nuclear option
bridge.clear_old_entries(days=30)  # Surgical option
```

## File Structure

```
multi_llm/
├── README.md                      # This file (apologetics-adapted)
├── api_config_template.json       # Template for API keys
├── api_config.json               # Your keys (gitignored!)
├── enhanced_llm_bridge.py        # Enhanced bridge with quality scoring
├── claude_llm_bridge.py          # Legacy bridge (still functional)
├── health_check.py               # API health check script
├── test_enhanced_bridge.py       # Comprehensive test suite
├── test_suite.py                 # Legacy test suite
├── llm_cache.db                  # SQLite cache (gitignored)
└── consultation/                 # Consultation logs (gitignored)
    ├── consultation_log_*.json   # Historical logs
    └── *.md                      # Expert responses and summaries
```

## Integration with oddXian Apologetics Workflow

### When to Use Multi-LLM

- Complex philosophical arguments requiring multiple perspectives
- Biblical interpretation where scholarly consensus varies
- Peer review before publishing to oddxian.com
- Responding to sophisticated objections
- Researching historical/scholarly consensus

### When to Use Claude Code Directly

- File editing and repository operations
- Article writing and revision
- Build management and organization
- Session continuity and context retention

## Troubleshooting

### API Failures

**Grok failing:**
1. Verify API key: `xai-[your-key]`
2. Check https://api.x.ai is accessible
3. Check rate limits

**ChatGPT failing:**
1. Verify API key: `sk-proj-[your-key]`
2. Check OpenAI service status
3. Verify sufficient credits

**Gemini failing:**
1. Verify API key format
2. Check Google AI service status

### Getting Better Results

1. **Be specific**: "Respond to the problem of evil in the context of free will theodicy"
2. **Provide context**: Include relevant scripture, philosophical frameworks
3. **Specify audience**: "For philosophical skeptics" vs "For church group"
4. **Ask for sources**: Request citations to validate claims

## Security Notes

⚠️ **NEVER commit `api_config.json`** - Contains API keys!

- Template: `api_config_template.json` (committed)
- Your keys: `api_config.json` (gitignored)
- Logs: `consultation_log_*.json` (gitignored)
- Cache: `llm_cache.db` (gitignored)

## Performance

- **Parallel requests**: ~2-5 seconds for all 3 experts
- **Cache hits**: Instant (< 0.1 seconds)
- **Success rate**: 100% when all APIs configured correctly
- **Synthesis quality**: Excellent with multiple expert perspectives

## Future Enhancements

**Completed in Phase 1**:
- ✅ Caching - SQLite with query fingerprinting
- ✅ Retry logic - Exponential backoff (3 attempts)
- ✅ Response ranking - Multi-dimensional quality scoring

**Planned for Apologetics Adaptation**:
1. **Apologetics-specific prompts** - Trained on oddXian style and approach
2. **Scripture validation** - Auto-check biblical citations
3. **Logical fallacy detection** - Automatic identification of reasoning errors
4. **Citation extraction** - Pull scholarly references automatically
5. **Argument templates** - Pre-built consultation patterns for common tasks

---

**Maintainer**: James (JD) Longmire
**ORCID**: 0009-0009-1383-7698
**Last Updated**: 2025-11-16
**Version**: Apologetics Adaptation (Phase 1)
**Status**: Production-ready for apologetics development

---
