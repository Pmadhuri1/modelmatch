# Learning Log

## Day 1 — May 14, 2026

### What I shipped
- Local LLM (Llama 3.2 via Ollama) running on M1 Mac
- ModelMatch v0.1: provider wrapper that calls any LLM with one function
- Public GitHub repo: github.com/Pmadhuri1/modelmatch

### Errors I solved (interview gold)
1. **Bash vs zsh PATH confusion** — Different shells read different config files. Fixed by configuring `.zshrc` and setting VS Code to use zsh.

2. **Python version range conflict** — pyproject.toml had `<4.0`, LiteLLM needs `<3.14`. Tightened the range.

3. **Critical Mac storage (only 9 GB free)** — Cleared Homebrew caches, app caches, and Python caches. Freed enough space to continue.

4. **Wrong folder for Poetry** — Was in `~/projects/`, needed to be in `~/projects/modelmatch/`. Lesson: always run Poetry from the folder containing pyproject.toml.

5. **Ollama not running** — Started Ollama service, set to auto-start with `brew services start ollama`.

6. **Git SSH auth denied** — Switched from SSH to HTTPS remote, push succeeded silently.

### Concepts learned
- Shells (bash, zsh) and config files
- PATH environment variable
- Virtual environments (Poetry)
- Python type hints
- LiteLLM as universal LLM adapter
- Local LLM serving (Ollama)
- `.gitignore` security
- Git remote URLs (SSH vs HTTPS)

### Day 2 plan
- Sign up for free API tiers (Groq, Gemini, Together AI)
- Securely manage keys via .env + python-dotenv
- Call 4 different models with same code
- First pytest unit test
- LinkedIn announcement
