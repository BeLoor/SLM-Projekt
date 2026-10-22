# 0000 – Architekturentscheidungen als ADRs dokumentieren

- **Status:** akzeptiert
- **Datum:** 2026-10-21
- **Entscheider:** Team

## Kontext und Problemstellung

Architekturentscheidungen sollen nachvollziehbar sein, für das Team, den Betreuer und den Projektbericht.

## Entscheidung

Wir dokumentieren jede relevante Architekturentscheidung als ADR im Format [MADR](https://adr.github.io/madr/) unter `docs/architecture/adrs/`, fortlaufend nummeriert (`NNNN-titel.md`). Vorlage: [`template.md`](template.md).

### Konsequenzen

- Begründungen inkl. betrachteter Alternativen und Literatur sind versioniert und fließen direkt in den Bericht.
- ADRs werden nicht nachträglich umgeschrieben, sondern durch neue ADRs abgelöst.
