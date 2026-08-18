from __future__ import annotations

import subprocess
from pathlib import Path

from .policy import decide_command


class RepoTools:
    def __init__(self, root: Path):
        self.root = root.resolve()

    def _path(self, relative: str) -> Path:
        target = (self.root / relative).resolve()
        if target != self.root and self.root not in target.parents:
            raise ValueError("Path escapes repository root")
        return target

    def repo_status(self) -> dict:
        return self._run(["git", "status", "--short", "--branch"])

    def read_file(self, relative: str) -> dict:
        path = self._path(relative)
        if not path.is_file():
            return {"ok": False, "error": "File not found"}
        return {"ok": True, "path": relative, "content": path.read_text(encoding="utf-8")}

    def search(self, pattern: str, glob: str = "*") -> dict:
        results = []
        for path in self.root.rglob(glob):
            if not path.is_file() or ".git" in path.parts or "node_modules" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for i, line in enumerate(text.splitlines(), 1):
                if pattern.lower() in line.lower():
                    results.append(f"{path.relative_to(self.root)}:{i}:{line[:240]}")
                    if len(results) >= 100:
                        return {"ok": True, "matches": results}
        return {"ok": True, "matches": results}

    def write_file(self, relative: str, content: str) -> dict:
        path = self._path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return {"ok": True, "path": relative}

    def run_command(self, command: list[str], approve_medium: bool = False) -> dict:
        decision = decide_command(command)
        if not decision.allowed or (decision.risk.value == "medium" and not approve_medium):
            return {"ok": False, "blocked": True, "risk": decision.risk.value, "reason": decision.reason}
        return self._run(command)

    def git_diff(self) -> dict:
        return self._run(["git", "diff", "--"])

    def run_quality_gate(self) -> dict:
        checks = [["pytest", "-q"], ["ruff", "check", "agent/src", "agent/tests"]]
        results = [self._run(cmd) for cmd in checks]
        return {"ok": all(r["returncode"] == 0 for r in results), "checks": results}

    def _run(self, command: list[str]) -> dict:
        p = subprocess.run(command, cwd=self.root, capture_output=True, text=True, timeout=120)
        return {"command": command, "returncode": p.returncode, "stdout": p.stdout[-12000:], "stderr": p.stderr[-12000:]}
