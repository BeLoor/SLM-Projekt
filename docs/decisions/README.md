# Architekturentscheidungen (ADRs)

In diesem Ordner halten wir die Architekturentscheidungen des Projekts als ADRs im MADR-Format fest. Warum wir ADRs verwenden, steht in [000](000-adrs-verwenden.md).

## Vorlage

Jedes ADR basiert auf der [Vorlage](adr-template.md). Sie ist eine leicht angepasste deutsche Übersetzung des MADR-Templates von https://adr.github.io/madr/ (10.11.2026).

## Namensschema

`NNN-titel-der-entscheidung.md`

* `NNN` ist eine dreistellige, fortlaufende Nummer
* Nummern werden nie wiederverwendet, auch nicht bei abgelehnten oder abgelösten ADRs
* der Titel wird kleingeschrieben und Wörter werden mit Bindestrichen getrennt

## Ein ADR schreiben

1. `adr-template.md` kopieren und nach dem Namensschema mit der nächsten freien Nummer benennen
2. Alle Platzhalter in `{}` ausfüllen. Optionale Abschnitte können entfernt werden.
3. `status: proposed` und das aktuelle Datum setzen
4. Aussagen mit Quellen belegen und die Quellen nummeriert unter "Quellen" angeben
5. Das ADR in den Index unten eintragen
6. Wenn alle `decision-makers` zugestimmt haben, den Status auf `accepted` setzen

## Ein ADR lesen

1. Zuerst den Status prüfen. Nur ADRs mit `accepted` sind gültig.
2. Bei `superseded by ADR-NNN` dem Verweis auf das neue ADR folgen
3. "Kontext und Problemstellung" und "Entscheidung" lesen
4. Für die Begründung im Detail "Vor- und Nachteile der Optionen" lesen

## Status-Lebenszyklus

| Status | Bedeutung |
| --- | --- |
| `proposed` | Die Entscheidung ist vorgeschlagen und noch nicht von allen abgestimmt. |
| `accepted` | Die Entscheidung ist angenommen und gilt. |
| `rejected` | Der Vorschlag wurde abgelehnt. |
| `deprecated` | Die Entscheidung gilt nicht mehr und wurde durch kein neues ADR ersetzt. |
| `superseded by ADR-NNN` | Die Entscheidung wurde durch das genannte ADR abgelöst. |

Ein ADR startet als `proposed` und wird danach `accepted` oder `rejected`. Ein angenommenes ADR kann später `deprecated` oder `superseded` werden.

## Nicht umschreiben, sondern ablösen

Ein angenommenes ADR wird inhaltlich nicht mehr verändert. Erlaubt sind nur Korrekturen von Tippfehlern und Links sowie die Änderung des Status.

Ändert sich eine Entscheidung, wird ein neues ADR geschrieben. Das alte ADR bekommt den Status `superseded by ADR-NNN` und bleibt erhalten. Das neue ADR verweist unter "Weitere Informationen" auf das alte. So bleibt nachvollziehbar, warum sich eine Entscheidung geändert hat.

## Index

| Nr. | Titel | Status | Datum |
| --- | --- | --- | --- |
| [000](000-adrs-verwenden.md) | Dokumentation für Architekturentscheidungen | proposed | 2026-11-10 |
| [001](001-rag-statt-fine-tuning.md) | RAG statt Fine-Tuning | in Arbeit | |
