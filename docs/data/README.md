# Datenbasis

## Quellen

## Aufbereitung
OCR → Bereinigung → Metadaten → Chunking

## Korpus-Schema (JSONL)

| Feld | Typ | Beschreibung |
|---|---|---|
| `id` | string | eindeutige ID |
| `text` | string | Artikeltext bzw. Chunk |
| `quelle` | string | Zeitung |
| `datum` | string | Erscheinungsdatum (ISO 8601) |
| `seite` | string | Seite(n) |
