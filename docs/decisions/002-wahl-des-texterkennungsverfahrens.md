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

* Gut, weil {Argument}
* Schlecht, weil {Argument}

### Neu-OCR mit Tesseract inklusive Drehkorrektur

Alle Seiten werden als Bild gerendert (z. B. 300 dpi, Graustufen) und mit Tesseract (`-l deu`) neu erkannt. Vorher wird die Ausrichtung je Seite per Tesseract-OSD erkannt und korrigiert.

* Gut, weil {Argument}
* Schlecht, weil {Argument}

### OCR mit vorgeschalteter Layout-Erkennung

Ein Werkzeug zur Dokumentanalyse (z. B. Docling oder Surya) erkennt zuerst Spalten, Überschriften und Bildunterschriften. Danach wird jeder Bereich einzeln erkannt. Das kann auch beim Zerlegen der Seiten in einzelne Artikel helfen.

* Gut, weil {Argument}
* Schlecht, weil {Argument}

### Vision-Language-Modell liest die Seitenbilder

Ein multimodales Modell bekommt das Seitenbild und gibt den Text strukturiert aus, z. B. getrennt nach Artikeln. Mehrere Kandidaten für das Basismodell sind multimodal und kämen dafür in Frage.

* Gut, weil {Argument}
* Schlecht, weil {Argument}

### Cloud-OCR-Dienst

Die Seiten werden an einen kommerziellen Dienst zur Dokumentenerkennung geschickt (z. B. Google Document AI oder Azure AI Document Intelligence). Zu prüfen ist, ob das wegen des Urheberrechts an den Artikeln überhaupt zulässig ist.

* Gut, weil {Argument}
* Schlecht, weil {Argument}


## Weitere Informationen

{Hier können zusätzliche Belege für das Ergebnis der Entscheidung oder die Zustimmung des Teams dokumentiert werden. Außerdem kann festgehalten werden, wann und wie die Entscheidung umgesetzt werden soll und ob bzw. wann sie erneut geprüft werden soll. Auch Links zu anderen Entscheidungen und Ressourcen können hier stehen.}

### Quellen