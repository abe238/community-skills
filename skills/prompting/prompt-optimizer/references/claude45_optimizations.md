# Claude 4.5 Specific Optimizations

## Key Behavioral Changes in 4.5
- **More precise instruction following** than previous versions
- **Better tool usage** with explicit direction
- **Improved parallel processing** capabilities
- **Enhanced long-context performance**

## Be Explicit With Instructions

Claude 4.5 responds well to clear, explicit requests:

```
❌ IMPLICIT: "Create an analytics dashboard"
✅ EXPLICIT: "Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond basics to create a fully-featured implementation."
```

## Context Improves Performance

Explaining *why* helps Claude understand goals:

```
Instead of: "Use markdown sparingly"
Try: "Use markdown sparingly because this will be rendered in a terminal that doesn't support rich formatting."
```

## Tool Usage Optimization

### Make Claude Proactive
```xml
<default_to_action>
By default, implement changes rather than only suggesting them.
If intent is unclear, infer the most useful likely action and proceed, using tools to discover missing details.
</default_to_action>
```

### Make Claude Conservative
```xml
<do_not_act_before_instructions>
Don't jump into implementation unless clearly instructed.
When intent is ambiguous, default to providing information and recommendations rather than taking action.
</do_not_act_before_instructions>
```

## Parallel Tool Calling Enhancement

```xml
<use_parallel_tool_calls>
If calling multiple tools with no dependencies, make all independent tool calls in parallel. Prioritize simultaneous execution over sequential when actions can be done in parallel.

Example: When reading 3 files, run 3 tool calls simultaneously.

However, if tools depend on previous results, call sequentially. Never use placeholders or guess missing parameters.
</use_parallel_tool_calls>
```

## Output Format Control

### Reduce Markdown Overuse
```xml
<avoid_excessive_markdown>
Write in clear, flowing prose using complete paragraphs.
Reserve markdown for `inline code`, code blocks (```), and simple headings (###).

Don't use lists (* or 1.) unless presenting truly discrete items where list format is best. Instead, incorporate items naturally into sentences.
</avoid_excessive_markdown>
```

## Prevent Overengineering

### In Code Tasks
```xml
<minimize_overengineering>
Avoid over-engineering. Only make changes directly requested or clearly necessary. Keep solutions simple and focused.

Don't add features, refactor code, or make "improvements" beyond what was asked. Don't create helpers or abstractions for one-time operations.
</minimize_overengineering>
```

## Long-Horizon Task Management

```xml
<context_management>
Your context window will be automatically compacted as it approaches limits, allowing indefinite work continuation.

Don't stop tasks early due to token concerns. Save progress to memory before context refreshes. Be persistent and autonomous - complete tasks fully even as budget approaches.
</context_management>
```

## Thinking Sensitivity

When extended thinking is **disabled**, Claude Opus 4.5 is sensitive to the word "think." Replace with alternatives:
- "consider" instead of "think about"
- "believe" instead of "think"
- "evaluate" instead of "think through"

## Interleaved Thinking

For reflection after tool use:

```
After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.
```

## Verbosity Control

Claude 4.5 tends toward efficiency and may skip summaries. If you want updates:

```
After completing a task that involves tool use, provide a quick summary of the work you've done.
```
