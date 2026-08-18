from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

class Risk(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass(frozen=True)
class CommandDecision:
    allowed: bool
    risk: Risk
    reason: str

SAFE_PREFIXES = (("git", "status"), ("git", "diff"), ("git", "log"), ("git", "show"), ("git", "branch"), ("pytest",), ("ruff",))
MEDIUM_PREFIXES = (("git", "checkout", "-b"), ("git", "add"), ("git", "commit"), ("git", "push"), ("npm", "install"), ("npm", "ci"), ("uv", "sync"))
HIGH_PREFIXES = (("git", "reset"), ("git", "clean"), ("git", "push", "--force"), ("gh", "pr", "merge"), ("supabase", "db", "reset"), ("supabase", "db", "push"), ("npm", "publish"))

def _starts_with(parts: list[str], prefix: tuple[str, ...]) -> bool:
    return tuple(parts[: len(prefix)]) == prefix

def decide_command(command: list[str]) -> CommandDecision:
    if not command:
        return CommandDecision(False, Risk.HIGH, "Empty command")
    if any(x in command for x in ("&&", "||", ";", "|", ">", ">>", "<")):
        return CommandDecision(False, Risk.HIGH, "Shell chaining/redirection is blocked")
    for prefix in HIGH_PREFIXES:
        if _starts_with(command, prefix):
            return CommandDecision(False, Risk.HIGH, f"High-risk command blocked: {' '.join(command)}")
    for prefix in MEDIUM_PREFIXES:
        if _starts_with(command, prefix):
            return CommandDecision(True, Risk.MEDIUM, "Allowed with approval")
    for prefix in SAFE_PREFIXES:
        if _starts_with(command, prefix):
            return CommandDecision(True, Risk.LOW, "Safe development command")
    return CommandDecision(False, Risk.HIGH, f"Command not on allowlist: {' '.join(command)}")
