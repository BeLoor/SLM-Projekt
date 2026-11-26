---
status: proposed
date: 2026-11-26
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
* Neu-OCR mit Tesseract und anschließender Layout-Erkennung
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

Die Tabelle bewertet die Optionen anhand der Entscheidungstreiber. Bewertet ist nur, was sich ohne Test mit den eigenen Daten beurteilen lässt.

Legende:

* ✓ erfüllt
* (✓) grundsätzlich erfüllt, die Qualität muss der Test zeigen
* ✗ nicht erfüllt
* X! nicht erfüllt bei einem Muss-Kriterium (K.-o.)
* ? erst mit Test oder weiterer Klärung beurteilbar
* n. b. nicht bewertet, weil die Option bereits ausgeschieden ist

| Entscheidungstreiber                            | Textlayer | Tesseract | Layout + OCR | Tesseract + Layout | VLM           | Cloud      |
| ----------------------------------------------- | --------- | --------- | ------------ | ------------------ | ------------- | ---------- |
| Muss: Lesereihenfolge bei mehreren Spalten      | X! (a)    | ? (b) [1] | (✓) [2]      | (✓) [2]            | n. b.         | n. b.      |
| Muss: Text nicht inhaltlich verändern           | n. b.     | ✓ [8]     | ✓ [8]        | ✓ [8]              | X! (k) [8, 9] | n. b.      |
| Muss: Urheberrecht und sensible Daten           | n. b.     | ✓ (h)     | ✓ (h) [2]    | ✓ (h) [2]          | ✓ (h)         | X! (i) [7] |
| Muss: gedrehte Seiten                           | n. b.     | ✓ [1]     | ? (c)        | ✓ [1]              | n. b.         | n. b.      |
| Muss: Faxseiten mit niedriger Auflösung         | n. b.     | ? (d) [1] | ?            | ? (d) [1]          | n. b.         | n. b.      |
| Muss: Bildunterschriften getrennt vom Fließtext | n. b.     | ?         | (✓) [3]      | (✓) [3]            | n. b.         | n. b.      |
| Muss: frei verfügbar und nutzbar                | n. b.     | ✓ [4]     | ✓ (e) [2]    | ✓ [2, 4]           | n. b.         | ? (f) [5]  |
| Muss: in die Pipeline einbindbar                | n. b.     | ✓ [4]     | ✓ [2]        | ✓ (g) [6]          | n. b.         | n. b.      |
| Muss: vertretbare Verarbeitungszeit             | n. b.     | ? (j)     | ? (j)        | ? (j)              | n. b.         | n. b.      |
| Soll: geringer Wartungsaufwand                  | n. b.     | ? (l)     | ? (l)        | ? (l)              | n. b.         | n. b.      |
| Soll: Seitenzahl, Artikelgrenzen und Quelle     | n. b.     | ?         | (✓) (m) [3]  | (✓) (m) [3]        | n. b.         | n. b.      |

Anmerkungen:

* (a) Siehe Kontext: Der vorhandene Textlayer vermischt die Spalten und zerfällt in Zeichensalat.
* (b) Tesseract erwartet standardmäßig eine Textseite. Mehrspaltige Layouts behandelt die Dokumentation nicht gesondert [1].
* (c) In den ersten Versuchen im Team hat Docling quer liegende Seiten schlecht verarbeitet. Das muss der Test bestätigen.
* (d) Tesseract arbeitet laut Dokumentation am besten mit mindestens 300 dpi [1]. Faxseiten liegen meist darunter. Ob Hochskalieren reicht, muss der Test zeigen.
* (e) Gilt für Docling (MIT-Lizenz [2]). Die Lizenz von Surya wurde nicht geprüft.
* (f) Der Dienst ist kostenpflichtig. Bei Azure sind z. B. nur 500 Seiten pro Monat kostenlos [5].
* (g) Docling kann Tesseract direkt als OCR-Engine nutzen [6].
* (h) Die Verarbeitung läuft lokal. Die Daten verlassen die eigene Infrastruktur nicht.
* (i) Die Scans enthalten urheberrechtlich geschützte Artikel und personenbezogene Daten, z. B. Namen und Telefonnummern. Beim Cloud-Dienst gehen sie an einen Drittanbieter. Das erfordert einen Auftragsverarbeitungsvertrag [7] und eine Klärung mit den Rechteinhabern. Beides liegt nicht vor.
* (j) Muss im Test gemessen werden.
* (k) Allgemeine VLMs schreiben unsicher erkannte Wörter oft in eine plausible Form um, statt sie wörtlich zu übernehmen [8]. Auf verschlechterten Vorlagen neigen sie zudem zu erfundenen Inhalten [9]. Solche Fehler sind im Ergebnis nicht als Fehler erkennbar. OCR-spezialisierte VLMs sind laut [8] deutlich weniger betroffen. Sie gehören nicht zu den betrachteten Optionen.
* (l) Lässt sich erst im Betrieb beurteilen.
* (m) Das Layout-Modell erkennt unter anderem Überschriften sowie Kopf- und Fußzeilen der Seite [3]. Das hilft bei Artikelgrenzen und Quelle. Ob das bei Zeitungsseiten reicht, muss der Test zeigen.

Über ein Muss-Kriterium scheiden damit aus: "Vorhandenen PDF-Textlayer nutzen", "Vision-Language-Modell liest die Seitenbilder" und "Cloud-OCR-Dienst". Zwischen den übrigen drei Optionen entscheidet der Test mit den eigenen Daten.

Die folgenden Abschnitte beschreiben die Optionen und nennen nur Punkte, die nicht schon in der Tabelle stehen.

### Vorhandenen PDF-Textlayer nutzen

Der Text wird direkt aus dem Textlayer gelesen, der beim Scannen erzeugt wurde. Kein zusätzlicher Verarbeitungsschritt.

* Gut, weil kein zusätzlicher maschineller Ressourcenaufwand entsteht
* Schlecht, weil Indizierung und Drehen der Seiten manuell erfolgen müssen

### Neu-OCR mit Tesseract inklusive Drehkorrektur

Alle Seiten werden als Bild gerendert (z. B. 300 dpi, Graustufen) und mit Tesseract (`-l deu`) neu erkannt. Vorher wird die Ausrichtung je Seite per Tesseract-OSD erkannt und korrigiert.

* Gut, weil die Überarbeitung der Daten automatisiert werden kann
* Gut, weil die Quote richtig erkannter Wörter hoch ist
* Schlecht, weil alle PDF-Dateien zuerst in PNG-Dateien umgewandelt werden müssen

### OCR mit vorgeschalteter Layout-Erkennung

Ein Werkzeug zur Dokumentanalyse (z. B. Docling oder Surya) erkennt zuerst Spalten, Überschriften und Bildunterschriften. Danach wird jeder Bereich einzeln erkannt. Das kann auch beim Zerlegen der Seiten in einzelne Artikel helfen.

* Gut, weil die Informationen direkt im Markdown-Format gespeichert werden
* Schlecht, weil das Werkzeug mit besonderen Schriftarten nicht gut umgehen kann

### Neu-OCR mit Tesseract und anschließender Layout-Erkennung

Die Option kombiniert die Stärken von Tesseract und einem Werkzeug zur Dokumentanalyse. Das PDF wird zuerst mit Tesseract neu erkannt und danach in ein verarbeitbares Markdown-Dokument überführt.

* Gut, weil die Vorteile der Neu-OCR und der Layout-Erkennung verbunden werden
* Schlecht, weil die Arbeitsschritte beider Methoden nötig sind

### Vision-Language-Modell liest die Seitenbilder

Ein multimodales Modell bekommt das Seitenbild und gibt den Text strukturiert aus, z. B. getrennt nach Artikeln. Mehrere Kandidaten für das Basismodell sind multimodal und kämen dafür in Frage.

* Gut, weil keine Vorverarbeitung nötig ist
* Gut, weil die Aufgabe durch Prompts gezielt gesteuert werden kann
* Schlecht, weil der Rechenaufwand hoch ist
* Schlecht, weil die Bildauflösung begrenzt ist

### Cloud-OCR-Dienst

Die Seiten werden an einen kommerziellen Dienst zur Dokumentenerkennung geschickt (z. B. Google Document AI oder Azure AI Document Intelligence).

* Gut, weil der Rechenaufwand nicht bei uns anfällt


## Weitere Informationen

Treten nach der Umsetzung größere Probleme mit dem gewählten Verfahren auf, wird diese Entscheidung durch ein neues ADR abgelöst (siehe [ADR 000](000-adrs-verwenden.md)).

### Quellen

1. Tesseract OCR (o. J.): Improving the quality of the output. Online-Dokumentation. URL: https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html (Abruf: 26.11.2026)
2. Livathinos, N.; Auer, C.; Lysak, M.; Nassar, A.; Dolfi, M.; Vagenas, P.; Berrospi, C.; Omenetti, M.; Dinkla, K.; Kim, Y.; Gupta, S.; Teixeira de Lima, R.; Weber, V.; Morin, L.; Meijer, I.; Kuropiatnyk, V.; Staar, P. W. J. (2025): Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion. In: AAAI 25 Workshop on Open-Source AI for Mainstream Use. arXiv-Preprint. DOI: 10.48550/arXiv.2501.17887
3. Pfitzmann, B.; Auer, C.; Dolfi, M.; Nassar, A. S.; Staar, P. W. J. (2022): DocLayNet: A Large Human-Annotated Dataset for Document-Layout Analysis. In: Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2022). DOI: 10.1145/3534678.3539043
4. Tesseract OCR (o. J.): tesseract. GitHub-Repository, Lizenz Apache 2.0. URL: https://github.com/tesseract-ocr/tesseract (Abruf: 26.11.2026)
5. Microsoft (o. J.): Azure AI Document Intelligence pricing. URL: https://azure.microsoft.com/pricing/details/ai-document-intelligence/ (Abruf: 26.11.2026)
6. Docling Project (o. J.): Pipeline options. Online-Dokumentation. URL: https://docling-project.github.io/docling/reference/pipeline_options/ (Abruf: 26.11.2026)
7. Europäisches Parlament; Rat der Europäischen Union (2016): Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung), Art. 28. In: Amtsblatt der Europäischen Union L 119, S. 1-88
8. Lee, G. G.; Ak, K. E.; Mohta, J.; Xu, Y.; Dimitriadis, D. (2026): Do VLMs Read or Rewrite? On Transcription Faithfulness in Vision-Language Models. arXiv-Preprint. DOI: 10.48550/arXiv.2607.21617
9. He, Z.; Zhang, C.; Wu, Z.; Chen, Z.; Zhan, Y.; Li, Y.; Zhang, Z.; Wang, X.; Qiu, M. (2025): Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models. In: Advances in Neural Information Processing Systems 38 (NeurIPS 2025). DOI: 10.48550/arXiv.2506.20168
