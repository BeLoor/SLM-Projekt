---
status: proposed
date: 2026-11-24
decision-makers: BeLoor, Mystery676767
consulted: BeLoor, Mystery676767
informed: BeLoor, Mystery676767
---
# Wahl des Texterkennungsverfahrens

## Kontext und Problemstellung

Die Rohdaten sind eingescannte Zeitungsseiten als PDF (siehe [Architekturentwurf](../planning/architekturentwurf.md)). Für das RAG aus [ADR 001](001-rag-statt-fine-tuning.md) wird daraus maschinenlesbarer Text benötigt.

Die gescannten PDFs enthalten bereits einen Textlayer. Bei mehrspaltigem Zeitungslayout ist dieser aber weitgehend unbrauchbar, weil Spalten vermischt werden und Zeilen in Zeichensalat zerfallen. Außerdem ist ein Teil der Seiten um 90 Grad gedreht. Weitere Schwierigkeiten sind gefaxte Seiten mit geringer Auflösung und Bildunterschriften, die mitten im Fließtext landen.

Mit welchem Verfahren wird der Text aus den Scans gewonnen?


## Entscheidungstreiber

* Die Texterkennung muss:
    * die richtige Lesereihenfolge bei mehreren Spalten erkennen
    * Text von gedrehten Seiten verarbeiten können (oder die Seite vorher drehen)
    * Faxseiten mit niedriger Auflösung verarbeiten können
    * Bildunterschriften getrennt vom Fließtext verarbeiten
    * frei verfügbar und nutzbar sein
    * in die Pipeline für das nachträgliche Einfügen von neuen Artikeln eingebunden werden können
    * das Urheberrecht nicht verletzen und die Daten sensibel behandeln
    * die Texte in vertretbarer Zeit verarbeiten
    * den Text der Vorlage wiedergeben und ihn nicht inhaltlich verändern
* Die Texterkennung sollte:
    * mit geringem Wartungsaufwand zuverlässig genutzt werden können
    * Seitenzahl, Artikelgrenzen und Quelle für eine gute Struktur im RAG angeben

## Betrachtete Optionen

* Vorhandenen PDF-Textlayer nutzen
* Neu-OCR mit Tesseract inklusive Drehkorrektur
* OCR mit vorgeschalteter Layout-Erkennung
* Vision-Language-Modell liest die Seitenbilder
* Cloud-OCR-Dienst

## Entscheidung

Gewählte Option: "{Titel von Option 1}", weil {Begründung, z. B. einzige Option, die ein K.-o.-Kriterium erfüllt | die die Einflussgröße {Einflussgröße} auflöst | … | am besten abschneidet (siehe unten)}.


### Konsequenzen

* Gut, weil {positive Konsequenz, z. B. Verbesserung einer oder mehrerer gewünschter Qualitäten, …}
* Schlecht, weil {negative Konsequenz, z. B. Beeinträchtigung einer oder mehrerer gewünschter Qualitäten, …}
* … <!-- die Anzahl der Konsequenzen kann variieren -->


### Bestätigung

{Beschreiben, wie die Umsetzung des ADR bzw. die Einhaltung des ADR bestätigt werden kann oder wird. Entsprechen das gewählte Design und seine Umsetzung der Entscheidung? Dabei kann z. B. ein Design- oder Code-Review oder ein Test mit einer Bibliothek wie ArchUnit helfen. Dieses Element ist zwar als optional eingestuft, ist aber in vielen ADRs enthalten.}


## Vor- und Nachteile der Optionen

### Vorhandenen PDF-Textlayer nutzen

Der Text wird direkt aus dem Textlayer gelesen, der beim Scannen erzeugt wurde. Kein zusätzlicher Verarbeitungsschritt.

* Gut, weil kein zusätzlicher maschineller Ressourcenaufwand
* Schlecht, weil große Teile des Textes sind nicht auslesbar
* Schlecht, weil Indizierung und Drehen von Seiten muss manuell erfolgen

### Neu-OCR mit Tesseract inklusive Drehkorrektur

Alle Seiten werden als Bild gerendert (z. B. 300 dpi, Graustufen) und mit Tesseract (`-l deu`) neu erkannt. Vorher wird die Ausrichtung je Seite per Tesseract-OSD erkannt und korrigiert.

* Gut, weil Überarbeiten der Daten kann automatisiert werden.
* Gut, weil hohe Quote an richtig erkannten Worten.
* Schlecht, weil alle PDF-Files noch einmal in PNG-Dateien umgewandelt werden müssen.
* Schlecht, weil PNG-Dateien auf Ausrichtung geprüft werden müssen.

### OCR mit vorgeschalteter Layout-Erkennung

Ein Werkzeug zur Dokumentanalyse (z. B. Docling oder Surya) erkennt zuerst Spalten, Überschriften und Bildunterschriften. Danach wird jeder Bereich einzeln erkannt. Das kann auch beim Zerlegen der Seiten in einzelne Artikel helfen.

* Gut, weil Informationen direkt im MD-Format gespeichert werden.
* Schlecht, weil kann quer liegende Seiten schlecht verarbeiten
* Schlecht, weil kann mit besonderen Schriftarten nicht gut umgehen.

### NeuOCR mit vorgeschalteter Layout-Erkennung
Durch die Kombination der Stärken von Tesseract und einem weiteren Werkzeug zur Dokumentenanalyse wird das PDF mit Tesseract neu eingescannt und dann weiter in ein verarbeitbares MD-Dokument überführt.

* Gut, weil Vorteile von neu OCR und OCR verbunden werden
* Schlecht, weil die Arbeitsschritte beider Methoden nötig sind


### Vision-Language-Modell liest die Seitenbilder

Ein multimodales Modell bekommt das Seitenbild und gibt den Text strukturiert aus, z. B. getrennt nach Artikeln. Mehrere Kandidaten für das Basismodell sind multimodal und kämen dafür in Frage.

* Gut, weil automatische Korrektur von kleinen Fehlern
* Gut, weil keine Vorverarbeitung nötig ist
* Gut, weil Aufgabenlösung durch Prompts gezielt gesteuert werden kann
* Schlecht, weil hoher Rechenaufwand
* Schlecht, weil Haluzinmationsgefahr
* Schlecht, weil begrenzte Auflösung 

### Cloud-OCR-Dienst

Die Seiten werden an einen kommerziellen Dienst zur Dokumentenerkennung geschickt (z. B. Google Document AI oder Azure AI Document Intelligence). 

* Gut, weil vorteile von VLM
* Gut, weil rechenaufwandt nicht bei uns
* Schlecht, weil kosten können anfallen
* Schlecht, weil kann haluzinieren
* Schlecht, weil begrenzte Auflösung


## Weitere Informationen

Sollten nachträglich größere Probleme mit der gewählten Methode auftreten, kann diese noch naträglich geändert werden. 

### Quellen