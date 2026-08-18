from __future__ import annotations

import os

from google.adk.models.lite_llm import LiteLlm

NVIDIA_BASE_URL = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
NVIDIA_MODEL = os.getenv("NVIDIA_MODEL", "z-ai/glm-5.2")


def build_model():
    provider = os.getenv("DOUGHNUT_AI_PROVIDER", "nvidia").strip().lower()
    if provider == "nvidia":
        api_key = os.getenv("NVIDIA_API_KEY")
        if not api_key:
            raise RuntimeError("NVIDIA_API_KEY is required when DOUGHNUT_AI_PROVIDER=nvidia")
        return LiteLlm(model=f"openai/{NVIDIA_MODEL}", api_base=NVIDIA_BASE_URL, api_key=api_key)
    if provider == "gemini":
        return os.getenv("DOUGHNUT_AGENT_MODEL", "gemini-2.5-flash")
    raise ValueError(f"Unsupported DOUGHNUT_AI_PROVIDER: {provider}")
