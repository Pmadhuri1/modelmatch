"""
modelmatch.providers
====================
A thin wrapper around LiteLLM so the rest of ModelMatch
doesn't have to know about provider-specific quirks.

Every other module in ModelMatch will use call_model() to talk to LLMs.
This is the ONLY place we should write provider-specific logic.
"""

from litellm import completion


def call_model(model_name: str, prompt: str) -> str:
    """
    Send a prompt to any LLM and return its text response.

    Args:
        model_name: Which model to use, in LiteLLM format.
                    Examples:
                      - "ollama/llama3.2:3b"            (local, free)
                      - "groq/llama-3.1-8b-instant"    (Groq free tier)
                      - "gpt-4o-mini"                  (OpenAI, paid)
        prompt: The text instruction to send to the model.

    Returns:
        The model's text response as a string.
    """
    # Local Ollama needs an explicit api_base; cloud providers don't.
    api_base = "http://localhost:11434" if model_name.startswith("ollama/") else None

    response = completion(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        api_base=api_base,
    )

    return response["choices"][0]["message"]["content"]


# ---- Quick test when you run this file directly ----
if __name__ == "__main__":
    print("Testing ModelMatch provider wrapper...")
    print("=" * 60)

    answer = call_model(
        model_name="ollama/llama3.2:3b",
        prompt="In one short sentence, explain what an LLM is."
    )

    print(f"Model response:\n{answer}\n")
    print("=" * 60)
    print("✅ Provider wrapper works!")