# ModelMatch

> Evidence-based LLM model selection for your specific use case.

## What is this?

A Python framework that helps engineers pick the right LLM for their use case. 
Most "AI vs AI" comparisons are anecdotal. ModelMatch generates custom test sets, 
runs candidate models, and produces statistically rigorous recommendations.

## Status

🚧 Active development — building in public.

**Currently working:**
- Unified provider wrapper (call any LLM with one function)
- Local model support via Ollama

**Coming next:**
- Multi-provider support (Groq, Gemini, Together AI)
- Use case analyzer agent
- Test set generator
- Multi-judge evaluator with bias mitigation
- Statistical analysis & recommendation reports

## Quick Look

```python
from modelmatch.providers import call_model

response = call_model(
    model_name="ollama/llama3.2:3b",
    prompt="Explain LLMs in one sentence"
)
```

## Tech

- Python 3.11 · Poetry · LiteLLM · Ollama

## License

M
