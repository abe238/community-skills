# Advanced Prompting Strategies

## Metacognitive Prompting

Force Claude to examine its own reasoning process:

```xml
<metacognitive_protocol>
Before providing final answer:
1. In <initial_approach> tags, describe first instinct
2. In <alternative_methods> tags, consider 2 other approaches
3. In <confidence_check> tags, rate confidence (1-10) and explain
4. In <verification> tags, double-check using different method
5. In <final_answer> tags, provide conclusion
</metacognitive_protocol>
```

## Constraint Satisfaction Prompting

Modern models work better with sharp constraints than vague guidelines:

```
❌ VAGUE: "Write something engaging and informative about AI"
✅ SHARP: "Write exactly 150 words explaining AI to a 12-year-old, using only words they'd know from Harry Potter books"
```

### Constraint Hierarchy Template
```xml
<constraints>
  <hard_constraints>
    <!-- Must be satisfied -->
    - Exactly 500 words
    - No technical jargon
    - Include 3 specific examples
  </hard_constraints>
  
  <soft_constraints>
    <!-- Preferred but flexible -->
    - Conversational tone
    - One analogy per section
  </soft_constraints>
  
  <anti_constraints>
    <!-- Explicitly avoid -->
    - No bullet points
    - No passive voice
    - No clichés like "delve" or "tapestry"
  </anti_constraints>
</constraints>
```

## Iterative Refinement Patterns

### Three-Pass Method
```xml
<pass_1>
Generate rough draft focusing on coverage and structure.
Don't worry about quality - just get ideas down.
</pass_1>

<pass_2>
Review and improve:
- Clarity of arguments
- Flow between sections
- Evidence and examples
Mark uncertain areas with [VERIFY]
</pass_2>

<pass_3>
Final polish:
- Tighten language (cut 15% of words)
- Fix remaining issues
- Add compelling opening/conclusion
- Remove [VERIFY] after fact-checking
</pass_3>
```

## Effort Control Through Prompting

### Light Analysis (quick, surface-level)
```xml
<analysis_depth>
Provide quick analysis focusing only on 3 most important points.
Skip detailed explanations and edge cases.
Prioritize efficiency over exhaustiveness.
</analysis_depth>
```

### Deep Analysis (comprehensive)
```xml
<analysis_depth>
Provide thorough analysis exploring multiple angles.
Consider edge cases, alternatives, and complications.
Include detailed examples and step-by-step reasoning.
</analysis_depth>
```

## Quality Assurance Patterns

### Built-in Uncertainty Tracking
```xml
<uncertainty_protocol>
For each claim:
1. Rate confidence (1-10)
2. If confidence < 7, mark with [UNCERTAIN]
3. For numerical claims, provide ranges when exact figures unknown
4. Distinguish between facts and reasonable inferences
</uncertainty_protocol>
```

### Error Prevention
```xml
<hallucination_guards>
Before making factual claims:
1. Is this from training data or inference?
2. Could I be confusing similar concepts?
3. Am I filling gaps with assumptions?
4. Should I express uncertainty instead?

Use qualifying phrases:
- "Based on typical patterns..."
- "This appears to be..."
- "If I understand correctly..."
</hallucination_guards>
```

## The Compound Effect

### Why Combined Techniques Work Better
```
Technique Stack          | Quality Improvement
-------------------------|--------------------
Base prompt              | Baseline
+ XML structure          | +20% (clearer parsing)
+ 3-5 examples           | +35% (format consistency)
+ Chain of thought       | +25% (better reasoning)
+ Role prompting         | +15% (domain expertise)
-------------------------|--------------------
COMBINED                 | Multiplicative gains
```

The improvements compound because:
1. **XML** prevents mixing instructions with content
2. **Examples** eliminate format ambiguity
3. **CoT** forces systematic analysis
4. **Roles** activate domain knowledge
