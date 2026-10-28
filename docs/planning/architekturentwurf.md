# Erster Architekturentwurf

Diese Datei hält einen ersten Architekturentwurf fest und schafft eine erste Struktur und Übersicht. 
Es ist noch keine verbindliche Architektur und dient der ersten Planung. 
Evaluation und Betrieb sind nicht Teil dieses Entwurfs.

## Annahmen
Es wird versucht, auf detaillierte Entscheidungen zu verzichten. Erste Annahmen werden hier festgehalten und sind noch nicht wissenschaftlich recherchiert oder belegt und müssen noch tiefer analysiert und belegt werden.

- RAG statt Fine-Tuning: wird aktuell angenommen 
    - das Modell muss beim Hinzufügen von neuen Dokumenten nicht neu trainiert werden
    - das Modell kann seine Aussagen mit den direkten Zeitungsabschnitten belegen (Quelle, Datum und Seite zu jedem Textabschnitt müssen dafür mitgespeichert werden)
    - eine "Corporate-Voice" bzw. immer gleichartige Tonart und strikte Ausgabeformate sind nicht notwendig
    - längere Prompts durch eingefügte Textabschnitte sind bei der erwarteten Nutzung akzeptabel, solange sie in den Grafikspeicher passen
    - Fine-Tuning ist schlechter zum Beibringen neuen Faktenwissens und eher dazu, Stil und Format anzupassen
- Die grundlegende Infrastruktur
    - Erste Idee ist eine light-weight Linux-Distribution mit Docker-Containern für die unterschiedlichen Komponenten des Projekts

## Daten-Pipeline

### Rohdaten
Zeitungsseiten als PDF-Dateien (eingescannt durch Dirk)

### Texterkennung
Erkennt maschinenlesbaren Text aus den PDF-Dateien und zerlegt ihn in einzelne Artikel.

### Aufbereitung / Indexierung
Für RAG müssen die Texte in Abschnitte zerlegt (Chunking), mit Metadaten versehen und als Embeddings indexiert werden.

### Wissensbasis
Speichert Textabschnitte mit Metadaten und Embeddings, damit das Retrieval inhaltlich passende Abschnitte findet.

Die Frage ist, welche Datenbank hier genau genommen wird.

---

## Interaktion mit dem Modell

### Oberfläche für das Sprachmodell
Eine simple Oberfläche für die Interaktion mit dem System als Alternative zur direkten API-Anfrage.

### API / Orchestrierung
Die Anfrage muss angenommen und vorverarbeitet werden.
Das Retrieval wird aufgerufen.
Mit dem Ergebnis und dem ursprünglichen Prompt wird der Prompt für das Sprachmodell gebaut.
Das Modell muss aufgerufen werden und die Antwort (optional samt Quelle) wird zurückgegeben.

### Retrieval aus der Wissensbasis
Es müssen entsprechende relevante Abschnitte retrieved werden, damit sie durch die Orchestrierung zusammen mit der Anfrage an das Modell übergeben werden können.

### Das eigentliche Sprachmodell
Das eigentliche generative Sprachmodell. Hier ist zu entscheiden, welches und welche Größe. Wie ist das Sprachmodell ansprechbar?

---