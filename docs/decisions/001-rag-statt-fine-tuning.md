---
status: proposed
date: 2026-11-12
decision-makers: BeLoor, Mytery676767
consulted: BeLoor, Mytery676767
informed: BeLoor, Mytery676767
---
# Grundlegende SLM Struktur

## Kontext und Problemstellung

Sollte das Fachwissen mittels eines RAG (Retrievel Augmented Generation) Models oder einem finegetuneten Models umgesetztewerden. Also soll 
das SLM mithilfe einer hintergelegten Datenbank die Informationen ausgeben oder auf zusätzliche Informationen trainiert werden?

## Entscheidungstreiber

* Grundlegende Entscheidung zur Planung sowie Umsetzung des Projektes
* Alle entscheidungsmöglichkeiten haben weitere Implikationen auf performance sowie ablauf des Projektes

## Betrachtete Optionen

* RAG
* Finetuning

## Entscheidung

Gewählte Option: RAG, weil viele Daten nur einmalig oder sehr selten vorhanden sind. Das heißt dass diese für training nicht gut geeignet sind. Auch können so Fakten direkt rezietiert werden, was die Fehleranfälligkeit senkt [1,2]. Zusätzlich kann dass Model dadurch die entsprechenden Zeitungsartikel dierekt referenzieren und neues Wissen aufnehmen ohne neu trainiert werden zu müssen.

### Konsequenzen

* Gut, weil neues Wissen kann ohne zusätzliches Training in den Wissenspool des SLM aufgenommen werden [3]
* Gut, weil die Fehler-/ (Halluzinations) wahrscheilichkeit gesenkt wird [1,2]
* Gut, weil sich auf Quellen direkt bezogen werden kann 
* Schlecht, weil eine unterliegende Datenbank angelegt und gepflegt werden muss [3]
* Schlecht, weil ein Algorithmus zum Datenbankabruf entwickelt werden muss [2]

### Bestätigung

Es existiert eine Datenbank, in der relevante Informationen kategorieseiert und gespeichert sind. Das SLM bezieht sich auf diese Datenbank und refferenziert diese. 

## Vor- und Nachteile der Optionen

### Finetuning

Durch ein Zusätzliches Training auf den Zieldaten wird das Model in Bezug auf die gewünschten Daten ergänzt 

* Gut, weil keine Zusätzliche Struktur geschaffen werden muss um die Zusatzdaten zu speichern und abzurufen
* Schlecht, weil das Model jedes mal wenn neue Daten eingeführt werden neu trainiert werden muss.

### RAG

Das Model greift auf eine unterliegende Datenbank zu um Informationen zu beziehen. 

* Gut, weil neues Wissen kann ohne zusätzliches Training in den Wissenspool des SLM aufgenommen werden [3]
* Gut, weil die Fehler-/ (Halluzinations) wahrscheilichkeit gesenkt wird [1,2]
* Gut, weil sich auf Quellen direkt bezogen werden kann 
* Schlecht, weil eine unterliegende Datenbank angelegt und gepflegt werden muss [3]
* Schlecht, weil ein Algorithmus zum Datenbankabruf entwickelt werden muss [2]


### Quellen

1. Heydar Soudani, Evangelos Kanoulas, and Faegheh Hasibi. 2024. Fine Tuning vs. Retrieval Augmented Generation for Less Popular Knowledge. In Proceedings of the 2024 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region (SIGIR-AP 2024). Association for Computing Machinery, New York, NY, USA, 12–22. https://doi.org/10.1145/3673791.3698415

2. Oded Ovadia, Menachem Brief, Moshik Mishaeli, and Oren Elisha. 2024. Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 237–250, Miami, Florida, USA. Association for Computational Linguistics. 10.18653/v1/2024.emnlp-main.15

3. Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., et al. (2023). Retrieval-Augmented Generation for Large Language Models: A Survey. arXiv e-prints (arXiv:2312.10997). https://doi.org/10.48550/arXiv.2312.10997