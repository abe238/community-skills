---
name: prompt-optimizer
description: Use when the user wants to improve prompt effectiveness, apply best practices from Anthropic's research, or transform a basic prompt into a high-performance structured prompt using XML tags, examples, chain of thought, role prompting, and other proven techniques.
version: 1.0.0
author: Abe Diaz (@abe238)
license: MIT
metadata:
  hermes:
    tags: [prompting, prompt-engineering, claude, optimization, xml, chain-of-thought, examples]
    related_skills: [adversarial-prompting, rapid-domain-mastery]
---

# Prompt Optimizer

## Overview

Transform basic prompts into high-performance, structured prompts using proven techniques from Anthropic's research. Apply the compound effect of multiple techniques (XML structure + examples + chain of thought + role prompting) for multiplicative quality improvements of up to 95% over baseline prompts.

## When to Use This Skill

Use this skill when:
- Users provide a basic prompt that needs optimization
- Output quality or consistency is poor with current prompts
- Format requirements are inconsistent or unclear
- Complex reasoning tasks need better structure
- Domain expertise needs to be incorporated
- Multi-step workflows require better organization
- Users want to apply Claude 4.5 best practices

## Three-Pass Optimization Method

### Pass 1: Analysis and Coverage
Analyze the original prompt and apply core techniques focusing on coverage and structure:

1. **Clarity Assessment**: Apply "The Golden Rule" - would a colleague understand this prompt without context?
2. **Core Technique Selection**: Apply Anthropic's priority order based on prompt needs:
   - **Be Clear & Direct** (always) - Add context, audience, workflow, success criteria
   - **Use Examples** (format consistency) - Add 3-5 diverse, relevant examples when output format matters
   - **Let Claude Think** (complex reasoning) - Add structured chain of thought for multi-step problems
   - **Use XML Tags** (multi-part prompts) - Structure with cognitive containers for organization
   - **Give Claude a Role** (domain expertise) - Add specific expert persona when specialized knowledge needed
   - **Prefill Response** (output control) - Guide response format for specific requirements
   - **Chain Prompts** (multi-step workflows) - Break into sequential steps for complex dependent tasks

3. **Advanced Strategy Integration**: Consider metacognitive prompting, constraint satisfaction, effort control

### Pass 2: Structure and Flow Review
Improve clarity, flow, and evidence while marking uncertain areas:

1. **XML Organization**: Structure with meaningful cognitive containers that separate different prompt parts
2. **Example Quality**: Ensure examples are relevant, diverse, clear, and progressive - covering edge cases
3. **Chain of Thought**: Add structured thinking for complex tasks (thinking → alternatives → evaluation → answer)
4. **Context Layering**: Organize immediate, background, and success contexts clearly
5. **Constraint Hierarchy**: Define hard constraints (must satisfy), soft constraints (preferred), anti-constraints (avoid)
6. **Flow Optimization**: Ensure logical progression and clear connections between sections
7. **Mark Uncertainties**: Flag areas that need verification with [VERIFY] tags

### Pass 3: Final Polish and Optimization
Apply Claude 4.5 optimizations and quality assurance:

1. **Claude 4.5 Enhancements**: 
   - Add explicit instructions and context explanations (why, not just what)
   - Enable parallel tool calling where appropriate
   - Prevent overengineering with focused constraints
   
2. **Quality Assurance**: Apply validation checklist using quality_checker.py
3. **Token Efficiency**: Optimize for performance without losing quality
4. **Error Prevention**: Add hallucination guards and uncertainty tracking
5. **Output Format Control**: Reduce markdown overuse, ensure clear prose
6. **Remove [VERIFY] tags**: After fact-checking and validation

## Optimization Framework

Use this systematic approach for consistent results:

```xml
<prompt_analysis>
1. <original_prompt>: [User's original prompt]
2. <clarity_issues>: [What's unclear or missing - context, audience, success criteria]
3. <technique_recommendations>: [Which core techniques to apply based on task type]
4. <complexity_assessment>: [Simple/Medium/Complex reasoning required]
5. <domain_expertise_needed>: [What specialized knowledge is required]
</prompt_analysis>

<optimization_plan>
1. <structure_improvements>: [XML organization needed for cognitive containers]
2. <examples_needed>: [What examples would help - format, edge cases, variations]
3. <thinking_requirements>: [Chain of thought structure for reasoning]
4. <constraints_to_add>: [Hard/soft/anti-constraints for clarity]
5. <claude45_enhancements>: [Specific 4.5 optimizations - explicit instructions, context explanations]
</optimization_plan>

<optimized_prompt>
[Final optimized prompt with all techniques applied systematically]
</optimized_prompt>
```

### Quality Validation

After optimization, validate using the built-in quality checker:

```bash
python scripts/quality_checker.py "your optimized prompt here"
```

This checks for:
- Clear task definition
- Sufficient context
- Relevant examples
- XML structure
- Defined constraints
- Output format specification
- Ambiguity avoidance
- Appropriate complexity matching

## Resources

### references/
- `core_techniques.md` - Detailed reference for all 7 core prompting techniques with examples
- `advanced_strategies.md` - Metacognitive prompting, constraint satisfaction, optimization patterns  
- `claude45_optimizations.md` - Claude 4.5 specific enhancements and behavioral changes
- `templates.md` - Ready-to-use templates for common prompt patterns

### scripts/
- `prompt_analyzer.py` - Automated prompt analysis and technique recommendation script
- `quality_checker.py` - Validation script for optimized prompts

Load references as needed to inform optimization decisions. Use scripts for automated analysis when helpful.
