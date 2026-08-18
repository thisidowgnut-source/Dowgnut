from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.adk.agents import Agent
from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint

from .model import build_model

REPO_ROOT = Path(os.getenv("DOUGHNUT_REPO_ROOT", Path(__file__).resolve().parents[3])).resolve()

root_agent = Agent(
    name="doughnut_dev_agent",
    model=build_model(),
    instruction="""
You are Doughnut Dev Agent, the autonomous software engineer for the repository.
Always inspect repository state and project docs before editing. Reuse existing
AG-UI/ADK patterns. Make the smallest complete change, verify it, inspect the
diff, and report exact files and test results. Never expose secrets and never
perform destructive operations.
""",
)

middleware_agent = ADKAgent(
    adk_agent=root_agent,
    app_name="doughnut_flava_dev",
    user_id=os.getenv("DOUGHNUT_AGENT_USER_ID", "developer"),
    session_timeout_seconds=8 * 60 * 60,
    use_in_memory_services=True,
)

app = FastAPI(title="Doughnut Flava Development Agent", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("DOUGHNUT_CORS_ORIGINS", "http://localhost:8081,http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
add_adk_fastapi_endpoint(app, middleware_agent, path="/agent")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "repo": str(REPO_ROOT)}
