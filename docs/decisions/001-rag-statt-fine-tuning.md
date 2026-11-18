---
status: accepted
date: 2026-11-18
decision-makers: BeLoor, Mystery676767
consulted: BeLoor, Mystery676767
informed: BeLoor, Mystery676767
---
# RAG statt Fine-Tuning

## Kontext und Problemstellung

Sollte das Fachwissen mittels eines RAG (Retrieval-Augmented Generation) Modells oder eines feingetunten Modells umgesetzt werden? Also soll das SLM mithilfe einer hintergelegten Datenbank die Informationen ausgeben oder auf zusätzliche Informationen trainiert werden?

## Entscheidungstreiber

* Die Artikel werden nach und nach von Dirk eingescannt und bereitgestellt, und nach neuen Wettbewerben kommen weitere hinzu
* Antworten sollen auf Quellen verweisen
* Das Modell soll auf einer RTX 4080 SUPER betrieben werden können

## Betrachtete Optionen

* RAG
* Fine-Tuning
* Hybrides Modell aus RAG und Fine-Tuning

## Entscheidung

Gewählte Option: RAG, weil viele Daten nur einmalig oder sehr selten vorhanden sind. Das heißt, dass diese für das Training nicht gut geeignet sind. Auch können so Fakten direkt rezitiert werden, was die Fehleranfälligkeit senkt [1,2]. Zusätzlich kann das Modell dadurch die entsprechenden Zeitungsartikel direkt referenzieren und neues Wissen aufnehmen, ohne neu trainiert werden zu müssen. Ein hybrides Modell wird nicht benötigt, da die benötigte Funktionalität (siehe [Problemverständnis](../planning/problemverstaendnis.md)) bereits vollständig vom RAG-Modell abgedeckt wird.

### Konsequenzen

* Gut, weil neues Wissen in der benötigten Frequenz ohne großen Mehraufwand in die Datenbank eingepflegt werden kann [3]
* Gut, weil die Fehler-/Halluzinationswahrscheinlichkeit gesenkt wird [1,2]
* Gut, weil sich auf Quellen direkt bezogen werden kann
* Schlecht, weil eine Vektordatenbank konzeptioniert, angelegt und gepflegt werden muss [3]
* Schlecht, weil ein Algorithmus zum Retrieval entwickelt werden muss [2]

### Bestätigung

Antworten auf Fragen werden mit Verweis auf die katalogisierten Daten generiert. Die Menge an Halluzinationen sollte nicht höher als 5 % sein.

## Vor- und Nachteile der Optionen

### Fine-Tuning

Durch ein zusätzliches Training auf den Zieldaten wird das Modell in Bezug auf die gewünschten Daten ergänzt.

* Gut, weil keine zusätzliche Struktur geschaffen werden muss, um die Zusatzdaten zu speichern und abzurufen
* Gut, weil das Lösen von zusätzlichen Aufgaben antrainiert werden kann [2]
* Schlecht, weil das Modell jedes Mal, wenn neue Daten eingeführt werden, neu trainiert werden muss
* Schlecht, weil beim Training von neuem Wissen altes Wissen verloren gehen kann [4]
* Schlecht, weil jede Trainingsiteration viel Rechenaufwand kostet

### RAG

Das Modell greift auf eine unterliegende Vektordatenbank zu, um Informationen zu beziehen.

* Gut, weil neues Wissen ohne zusätzliches Training in den Wissenspool des SLM aufgenommen werden kann [3]
* Gut, weil die Fehler-/Halluzinationswahrscheinlichkeit gesenkt wird [1,2]
* Gut, weil sich auf Quellen direkt bezogen werden kann
* Schlecht, weil eine unterliegende Vektordatenbank angelegt und gepflegt werden muss [3]
* Schlecht, weil ein zusätzlicher Retrieval-Algorithmus existieren muss [2]

### Hybridmodell

Ein Modell, das die Elemente von RAG und Fine-Tuning vereinigt.

* Gut, weil Stärken von RAG und Fine-Tuning verbunden werden
* Schlecht, weil jeweiliger Mehraufwand bestehen bleibt

## Weitere Informationen

Sollte sich die Anforderungsliste ändern, muss die Wahl der grundlegenden Modellart neu evaluiert werden.

### Quellen

1. Soudani, H.; Kanoulas, E.; Hasibi, F. (2024): Fine Tuning vs. Retrieval Augmented Generation for Less Popular Knowledge. In: Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region (SIGIR-AP 2024), S. 12-22. DOI: 10.1145/3673791.3698415
2. Ovadia, O.; Brief, M.; Mishaeli, M.; Elisha, O. (2024): Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs. In: Conference on Empirical Methods in Natural Language Processing (EMNLP 2024), S. 237-250. DOI: 10.18653/v1/2024.emnlp-main.15
3. Gao, Y.; Xiong, Y.; Gao, X.; Jia, K.; Pan, J.; Bi, Y.; Dai, Y.; Sun, J.; Wang, M.; Wang, H. (2023): Retrieval-Augmented Generation for Large Language Models: A Survey. arXiv-Preprint. DOI: 10.48550/arXiv.2312.10997
4. Luo, Y.; Yang, Z.; Meng, F.; Li, Y.; Zhou, J.; Zhang, Y. (2025): An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-Tuning. IEEE Transactions on Audio, Speech and Language Processing 33, S. 3776-3786. DOI: 10.1109/TASLPRO.2025.3606231
5. Lewis, P.; Perez, E.; Piktus, A.; Petroni, F.; Karpukhin, V.; Goyal, N.; Küttler, H.; Lewis, M.; Yih, W.; Rocktäschel, T.; Riedel, S.; Kiela, D. (2021): Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. arXiv-Preprint. DOI: 10.48550/arXiv.2005.11401
