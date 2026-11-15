---
status: proposed
date: 2026-11-12
decision-makers: BeLoor, Mytery676767
consulted: BeLoor, Mytery676767
informed: BeLoor, Mytery676767
---
# RAG statt Fine-Tuning

## Kontext und Problemstellung

Sollte das Fachwissen mittels eines RAG (Retrieval-Augmented Generation) Modells oder einem feingetunten Modell umgesetzt werden? Also soll das SLM mithilfe einer hintergelegten Datenbank die Informationen ausgeben oder auf zusätzliche Informationen trainiert werden?

## Entscheidungstreiber

* Neue Artikel (Informationen) erscheinen mehrmals wöchentlic
* Antworten sollen auf Quellen verweisen
* Das Modell soll auf einer RTX 4080 SUPER betrieben werden können

## Betrachtete Optionen

* RAG
* Finetuning
* Hybrides Model aus RAG und Finetuning

## Entscheidung

Gewählte Option: RAG, weil viele Daten nur einmalig oder sehr selten vorhanden sind. Das heißt, dass diese für das Training nicht gut geeignet sind. Auch können so Fakten direkt rezitiert werden, was die Fehleranfälligkeit senkt [1,2]. Zusätzlich kann das Modell dadurch die entsprechenden Zeitungsartikel direkt referenzieren und neues Wissen aufnehmen, ohne neu trainiert werden zu müssen. Ein hybrides Modell wird nicht benötigt, da die benötigte Funktionalität (siehe Problemverständnis) bereits vollständig vom RAG-Modell abgedeckt wird.

### Konsequenzen

* Gut, weil neues Wissen in der benötigten Frequenz ohne großen Mehraufwand in die Datenbank eingepflegt werden kann [3]
* Gut, weil die Fehler-/Halluzinationswahrscheinlichkeit gesenkt wird [1,2]
* Gut, weil sich auf Quellen direkt bezogen werden kann
* Schlecht, weil eine Vektordatenbank konzeptioniert, angelegt und gepflegt werden muss [3]
* Schlecht, weil ein Algorithmus zum Retrieval entwickelt werden muss [2]

### Bestätigung

Antworten auf Fragen werden mit Verweis auf die katalogisierten Daten generiert. Die Menge an Halluzinationen sollte nicht höher als 5 % sein.  

## Vor- und Nachteile der Optionen

### Finetuning

Durch ein zusätzliches Training auf den Zieldaten wird das Modell in Bezug auf die gewünschten Daten ergänzt.

* Gut, weil keine zusätzliche Struktur geschaffen werden muss, um die Zusatzdaten zu speichern und abzurufen
* Gut, weil das Lösen von zusätzlichen Aufgaben antrainiert werden kann [2]
* Schlecht, weil das Modell jedes Mal, wenn neue Daten eingeführt werden, neu trainiert werden muss.
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

Ein Model, das die Elemente von RAG und Hybrid vereinigt

* Gut, weil Stärken von RAG und Finetuning verbunden werden
* Schlecht, weil jeweiliger Mehraufwand bestehen bleibt

## Weitere Informationen

Sollte sich die Anforderungsliste ändern, muss die Wahl der grundlegenden Modellart neu evaluiert werden.


### Quellen

1. Heydar Soudani, Evangelos Kanoulas, and Faegheh Hasibi. 2024. Fine Tuning vs. Retrieval Augmented Generation for Less Popular Knowledge. In Proceedings of the 2024 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region (SIGIR-AP 2024). Association for Computing Machinery, New York, NY, USA, 12–22. https://doi.org/10.1145/3673791.3698415

2. Oded Ovadia, Menachem Brief, Moshik Mishaeli, and Oren Elisha. 2024. Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 237–250, Miami, Florida, USA. Association for Computational Linguistics. 10.18653/v1/2024.emnlp-main.15 https://doi.org/10.48550/arXiv.2312.05934

3. Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang and Haofen Wang (2023). Retrieval-Augmented Generation for Large Language Models: A Survey. arXiv e-prints (arXiv:2312.10997). https://doi.org/10.48550/arXiv.2312.10997

4. Y. Luo, Z. Yang, F. Meng, Y. Li, J. Zhou and Y. Zhang, "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-Tuning," in IEEE Transactions on Audio, Speech and Language Processing, vol. 33, pp. 3776-3786, 2025, doi: 10.1109/TASLPRO.2025.3606231.

5. Lewis, P. et al. 2021. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. arXiv. Available at: https://doi.org/10.48550/arXiv.2005.11401.
