"""Static safety and syntax checks for the committed notebook."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

NOTEBOOK = Path("source/Emotion_Sentiment_Analysis_tool.ipynb")
SECRET_PATTERNS = {
    "private key": r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY",
    "AWS access key": r"AKIA[0-9A-Z]{16}",
    "GitHub token": r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})",
    "OpenAI key": r"sk-[A-Za-z0-9_-]{20,}",
    "Google API key": r"AIza[0-9A-Za-z_-]{30,}",
    "Slack token": r"xox[baprs]-[A-Za-z0-9-]{10,}",
    "Kaggle token": r"KGAT_[A-Za-z0-9_-]{20,}",
}


def main() -> int:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    failures: list[str] = []

    for index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue

        if cell.get("execution_count") is not None:
            failures.append(f"cell {index}: execution_count is not cleared")
        if cell.get("outputs"):
            failures.append(f"cell {index}: outputs are not cleared")

        source = "".join(cell.get("source", []))
        python_source = "\n".join(
            line
            for line in source.splitlines()
            if not line.lstrip().startswith(("!", "%"))
        )
        try:
            ast.parse(python_source)
        except SyntaxError as exc:
            failures.append(f"cell {index}: invalid Python syntax: {exc}")

    serialized = json.dumps(notebook, ensure_ascii=False)
    for label, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, serialized):
            failures.append(f"high-confidence secret pattern detected: {label}")

    if failures:
        print("\n".join(f"ERROR: {failure}" for failure in failures))
        return 1

    print(
        f"OK: {NOTEBOOK} has valid Python syntax, no outputs, "
        "and no high-confidence secret patterns"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
