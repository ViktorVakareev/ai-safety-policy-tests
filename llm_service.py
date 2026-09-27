"""llm_service.py

Starter code for the "Build Your First Safety Test Suite" lab.

This is a very small rule-based stand-in for an LLM call — no real model is
involved, just keyword matching — which keeps the lab's focus on writing
tests rather than on the "AI" itself. Per the lab instructions this file
should not be modified: the pytest suite (test_llm_service.py) is what you
write and extend to prove the safety policy holds.

Behavior:
  * Unsafe prompts   -- contain a keyword like "dangerous code",
                        "harmful instruction", etc. -> refused with
                        POLICY_REFUSAL_MESSAGE.
  * Safe prompts     -- greetings such as "hello" or "greet" -> a friendly
                        canned reply.
  * Neutral prompts  -- anything else (including empty/whitespace-only
                        input) -> a generic canned reply.

Matching is case-insensitive and matches anywhere in the prompt (a
substring match), and the safety policy always takes priority: if a prompt
both greets and contains an unsafe keyword, it is refused.
"""

POLICY_REFUSAL_MESSAGE = "I'm sorry, but I can't help with that request."

# Keywords that mark a prompt as unsafe. Checked as substrings, so phrasing
# built around them (not just an exact match) is still caught.
UNSAFE_KEYWORDS = [
    "dangerous code",
    "harmful instruction",
    "malware",
    "exploit",
    "weapon",
    "hack into",
]

# Keywords that mark a prompt as a friendly greeting (only checked once a
# prompt has already been cleared by the unsafe-keyword check).
GREETING_KEYWORDS = [
    "hello",
    "hi",
    "greet",
    "greetings",
]


def generate_response(prompt: str) -> str:
    """Return a canned response for `prompt` based on the safety policy.

    Raises:
        ValueError: if `prompt` is None.
    """
    if prompt is None:
        raise ValueError("prompt must not be None")

    normalized = prompt.lower()

    if any(keyword in normalized for keyword in UNSAFE_KEYWORDS):
        return POLICY_REFUSAL_MESSAGE

    if any(keyword in normalized for keyword in GREETING_KEYWORDS):
        return "Hello! How can I help you today?"

    return f"Here is a neutral response to: {prompt}"
