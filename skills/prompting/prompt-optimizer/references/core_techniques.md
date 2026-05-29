# Core Prompting Techniques Reference

## 1. Be Clear and Direct

### Essential Components
- **Context**: What the results will be used for
- **Audience**: Who the output serves  
- **Workflow**: How this fits the bigger picture
- **Success criteria**: What good looks like

### Transformation Pattern
```
❌ VAGUE: "Write something about our product"
✅ CLEAR: "Write a 100-word product description for running shoes targeting fitness enthusiasts aged 25-40. Emphasize comfort and durability. Use energetic but professional tone."
```

### Context Layering Template
```xml
<context_layers>
  <immediate_context>What Claude needs to know right now</immediate_context>
  <background_context>Broader situation and constraints</background_context>
  <success_context>How success will be measured</success_context>
</context_layers>
```

## 2. Use Examples (Multishot Prompting)

### The 3-5 Rule
> "3-5 diverse examples dramatically improve output quality by 60-80%" - Anthropic Research

### Example Structure Template
```xml
<task>{{TASK_DESCRIPTION}}</task>

<examples>
  <example>
    <input>{{EXAMPLE_INPUT_1}}</input>
    <output>{{EXAMPLE_OUTPUT_1}}</output>
    <reasoning>{{WHY_THIS_CLASSIFICATION}}</reasoning>
  </example>
  <example>
    <input>{{EXAMPLE_INPUT_2}}</input>
    <output>{{EXAMPLE_OUTPUT_2}}</output>
    <reasoning>{{WHY_THIS_CLASSIFICATION}}</reasoning>
  </example>
  <example>
    <input>{{EXAMPLE_INPUT_3}}</input>
    <output>{{EXAMPLE_OUTPUT_3}}</output>
    <reasoning>{{WHY_THIS_CLASSIFICATION}}</reasoning>
  </example>
</examples>

<input_to_process>{{USER_INPUT}}</input_to_process>
```

### Example Quality Guidelines
- **Relevant**: Mirror actual use case
- **Diverse**: Cover edge cases and variations
- **Clear**: Use consistent XML structure
- **Progressive**: Show increasing complexity

## 3. Let Claude Think (Chain of Thought)

### When to Use CoT
✅ **Use for**: Complex math, multi-step analysis, decisions with many factors
❌ **Don't use for**: Simple queries, latency-critical tasks, straightforward classification

### Three Levels of Control

**Level 1 - Basic**:
```
Think step-by-step before answering.
```

**Level 2 - Guided**:
```
Before answering:
1. Identify key variables
2. Consider potential approaches
3. Evaluate trade-offs
4. Provide recommendation
```

**Level 3 - Structured**:
```xml
<instructions>
1. Analyze in <thinking> tags
2. Consider alternatives in <alternatives> tags  
3. Evaluate options in <evaluation> tags
4. Provide final answer in <answer> tags
</instructions>
```

### Critical Rule
> Always have Claude OUTPUT its thinking. Without outputting the thought process, no thinking occurs!

## 4. Use XML Tags

### Why XML Works
Claude processes XML tags as **cognitive containers** - separate thinking spaces for mental organization.

### Benefits
- **Clarity**: Separate different prompt parts
- **Accuracy**: Reduce misinterpretation by 40%
- **Flexibility**: Modify sections without rewriting
- **Parseability**: Extract specific response parts

### Best Practices
1. **Be consistent**: Same tag names throughout
2. **Reference tags**: "Using the contract in `<contract>` tags..."
3. **Nest for hierarchy**: `<outer><inner></inner></outer>`
4. **Use meaningful names**: Tags should describe content

## 5. Give Claude a Role

### Role Effectiveness Spectrum
```
Generic → Specific → Expert → Contextual Expert
"assistant" → "data scientist" → "senior fraud analyst" → "senior fraud analyst at fintech with 10 years experience"
```

### Domain Examples
| Domain | Generic | Expert |
|--------|---------|--------|
| Legal | lawyer | senior tax attorney specializing in international corporate law |
| Finance | analyst | CFO with 20 years SaaS experience |
| Technical | developer | senior backend engineer specializing in distributed systems |

## 6. Prefill Response

### Use Cases
- Force specific formats (JSON, XML)
- Maintain character consistency
- Guide response direction

### Examples
```python
# Force JSON
{"role": "assistant", "content": "{"}

# Maintain character  
{"role": "assistant", "content": "[SHAKESPEARE]: "}

# Guide direction
{"role": "assistant", "content": "**Executive Summary:**"}
```

## 7. Chain Complex Prompts

### When to Chain
✅ **Chain for**: Research synthesis, multi-step analysis, iterative creation, complex decisions

### Chaining Strategies
- **Sequential**: Research → Outline → Draft → Edit → Format
- **Parallel**: Analyze Doc A/B/C → Synthesize Results
- **Self-Correction**: Generate → Review → Refine → Validate

### Template
```xml
<workflow_step number="1">
  <objective>{{STEP_1_GOAL}}</objective>
  <input>{{STEP_1_INPUT}}</input>
  <output_format>{{STEP_1_FORMAT}}</output_format>
</workflow_step>
```
