"""Führt den Testfragenkatalog gegen die API aus.

Erwartetes Format pro Zeile in questions.jsonl:
{"id": "q001", "frage": "...", "soll_antwort": "...", "quelle": "..."}
"""
import argparse
import json
from pathlib import Path


def load_questions(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, default=Path(__file__).with_name("questions.jsonl"))
    parser.add_argument("--api", default="http://localhost:8000/ask")
    args = parser.parse_args()

    questions = load_questions(args.questions)
    print(f"{len(questions)} Fragen geladen")
    # TODO: Fragen an args.api senden, Antworten und Quellen bewerten, Ergebnis speichern


if __name__ == "__main__":
    main()
