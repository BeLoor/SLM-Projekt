# Local Heroes SLM

Domänenspezifisches Small Language Model (RAG-basiert) für Informationen zum Musikwettbewerb „Local Heroes“.
Wissenschaftliches Teamprojekt, OVGU Magdeburg, WiSe 2026/27.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
cp .env.example .env
```

Betrieb über Docker Compose: siehe [`deploy/`](deploy/).

## Struktur

| Ordner | Inhalt |
|---|---|
| `docs/` | Dokumentation: Architektur, ADRs, Daten, Evaluation, Betrieb |
| `src/local_heroes/` | Quellcode, geschnitten nach Pipeline-Stufen |
| `eval/` | Testfragenkatalog und Evaluationsskript |
| `configs/` | Konfiguration (Modell, Chunking, Prompts) |
| `deploy/` | Dockerfiles, docker-compose.yml |
| `data/` | Lokale Daten, **nicht im Git** |
| `notebooks/` | Exploration, kein Produktivcode |
| `tests/` | Unit- und Integrationstests |

Einstieg in die Doku: [`docs/README.md`](docs/README.md)
