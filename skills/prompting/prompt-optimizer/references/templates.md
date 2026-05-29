# Prompt Templates

## Template 1: Comprehensive Analysis
```xml
<role>{{DOMAIN_EXPERT_ROLE}}</role>

<context>
{{BACKGROUND_INFORMATION}}
</context>

<task>
{{SPECIFIC_ANALYSIS_REQUEST}}
</task>

<methodology>
1. In <initial_assessment> tags, provide first impressions
2. In <systematic_analysis> tags, examine each key factor
3. In <synthesis> tags, combine findings into insights
4. In <recommendations> tags, suggest specific actions
5. In <confidence_levels> tags, rate certainty of each conclusion
</methodology>

<constraints>
- Maximum 800 words total
- Include specific examples
- Provide confidence ratings (1-10)
- Focus on actionable insights
</constraints>
```

## Template 2: Multi-Document Synthesis
```xml
<documents>
  <document index="1">
    <source>{{SOURCE_1}}</source>
    <content>{{CONTENT_1}}</content>
  </document>
  <document index="2">
    <source>{{SOURCE_2}}</source>
    <content>{{CONTENT_2}}</content>
  </document>
</documents>

<synthesis_framework>
1. <key_themes>: Identify 3-5 major themes across documents
2. <agreements>: Where do sources align?
3. <contradictions>: Where do they conflict?
4. <gaps>: What information is missing?
5. <implications>: What does this mean for {{CONTEXT}}?
</synthesis_framework>

<output_requirements>
- Quote specific passages to support points
- Note source for each claim
- Highlight areas of uncertainty
- Suggest follow-up questions
</output_requirements>
```

## Template 3: Decision Framework
```xml
<decision_context>
{{DECISION_TO_MAKE}}
</decision_context>

<stakeholders>
{{WHO_IS_AFFECTED}}
</stakeholders>

<constraints>
{{LIMITATIONS_AND_REQUIREMENTS}}
</constraints>

<decision_framework>
1. <options>: List 3-5 viable alternatives
2. <criteria>: Define evaluation dimensions
3. <analysis>: Score each option on each criterion
4. <trade_offs>: Identify key compromises
5. <recommendation>: Choose best option with rationale
6. <implementation>: Outline next steps
7. <monitoring>: How to track success
</decision_framework>
```

## Template 4: Few-Shot Classification
```xml
<task>{{CLASSIFICATION_TASK}}</task>

<categories>
- Category A: {{DESCRIPTION_A}}
- Category B: {{DESCRIPTION_B}}
- Category C: {{DESCRIPTION_C}}
</categories>

<examples>
  <example>
    <input>{{EXAMPLE_INPUT_1}}</input>
    <output>Category A</output>
    <reasoning>{{WHY_THIS_CATEGORY}}</reasoning>
  </example>
  <example>
    <input>{{EXAMPLE_INPUT_2}}</input>
    <output>Category B</output>
    <reasoning>{{WHY_THIS_CATEGORY}}</reasoning>
  </example>
  <example>
    <input>{{EXAMPLE_INPUT_3}}</input>
    <output>Category C</output>
    <reasoning>{{WHY_THIS_CATEGORY}}</reasoning>
  </example>
</examples>

<input_to_classify>
{{USER_INPUT}}
</input_to_classify>

Classify the input above and explain your reasoning.
```

## Template 5: Chain of Thought Analysis
```xml
<problem>
{{PROBLEM_DESCRIPTION}}
</problem>

<context>
{{RELEVANT_CONTEXT}}
</context>

<instructions>
Analyze this problem step by step:

1. In <understanding> tags, restate the problem in your own words
2. In <approach> tags, outline your analytical approach
3. In <analysis> tags, work through the problem systematically
4. In <conclusion> tags, provide your final answer with confidence level
</instructions>
```

## Template 6: Code Generation & Review
```xml
<task>{{CODE_TASK_DESCRIPTION}}</task>

<language>{{PROGRAMMING_LANGUAGE}}</language>

<requirements>
- {{FUNCTIONAL_REQUIREMENT_1}}
- {{FUNCTIONAL_REQUIREMENT_2}}
</requirements>

<constraints>
- {{TECHNICAL_CONSTRAINT_1}}
- {{TECHNICAL_CONSTRAINT_2}}
</constraints>

<test_cases>
  <test>
    <input>{{INPUT_1}}</input>
    <expected>{{OUTPUT_1}}</expected>
  </test>
  <test>
    <input>{{INPUT_2}}</input>
    <expected>{{OUTPUT_2}}</expected>
  </test>
</test_cases>

Generate the code and verify it passes all test cases.
```

## Template 7: Multi-Step Workflow
```xml
<objective>{{END_GOAL}}</objective>

<steps>
  <step number="1">
    <action>{{WHAT_TO_DO}}</action>
    <output_format>{{EXPECTED_OUTPUT}}</output_format>
  </step>
  <step number="2">
    <action>{{WHAT_TO_DO_WITH_STEP_1_OUTPUT}}</action>
    <output_format>{{EXPECTED_OUTPUT}}</output_format>
  </step>
  <step number="3">
    <action>{{FINAL_SYNTHESIS}}</action>
    <output_format>{{FINAL_DELIVERABLE_FORMAT}}</output_format>
  </step>
</steps>

<input>
{{YOUR_INPUT}}
</input>

Execute each step in order, showing your work for each.
```

## Template Selection Guide

| Use Case | Template | Key Features |
|----------|----------|--------------|
| Complex analysis | Template 1 | Structured methodology, confidence ratings |
| Document synthesis | Template 2 | Multi-source integration, conflict resolution |
| Decision making | Template 3 | Stakeholder analysis, trade-off evaluation |
| Classification tasks | Template 4 | Few-shot examples, reasoning explanation |
| Problem solving | Template 5 | Chain of thought, systematic approach |
| Code tasks | Template 6 | Requirements, constraints, test validation |
| Multi-step processes | Template 7 | Sequential workflow, clear deliverables |
