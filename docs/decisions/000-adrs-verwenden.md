---
status: accepted
date: 2026-11-12
decision-makers: BeLoor, Mytery676767
consulted: BeLoor, Mytery676767
informed: BeLoor, Mytery676767
---

# Dokumentation für Architekturentscheidungen

## Kontext und Problemstellung

Wir benötigen ein Werkzeug, um Architekturentscheidungen nachvollziehbar und strukturiert festzuhalten.

Wissen über Architekturentscheidungen geht verloren, wenn es nur implizit in der Architektur enthalten ist. Jansen und Bosch bezeichnen das als Knowledge Vaporization [1].

Wir nutzen das unter https://adr.github.io/madr/#full-template (10.11.2026) vorgestellte Template dafür und haben es für unsere Anforderungen angepasst und auf Deutsch übersetzt. Die Konfigurationen für Jekyll und "Just the Docs" wurden entfernt, da diese nicht benutzt werden.


## Entscheidungstreiber

* Notwendigkeit für nachvollziehbare Architekturentscheidungen
    * bei Einarbeitung in das Projekt kann verstanden werden, warum sich für eine konkrete Lösung entschieden wurde
    * Entscheidungen können zu einem späteren Zeitpunkt des Projekts nachvollzogen werden und müssen bei Bedarf begründet verändert werden
* Alternativen müssen abgewogen werden
* Entscheidungsprozesse dürfen nicht zu lange dauern

## Betrachtete Optionen

* ADR
    * Nygard-ADR
    * MADR (Markdown ADR)
    * Y-Statement
    * Tyree/Akerman-Template
* Wiki-Seiten (Confluence, Notion)
* Pull Requests / Commit-Messages
* Decision Log

## Entscheidung

Gewählte Option: "ADR im MADR-Format", weil es als einziges der betrachteten Formate Alternativen explizit abwägt und dabei keinen hohen Dokumentationsaufwand verursacht. Gleichzeitig ist das Format nicht zu ausführlich, um einen zu großen Overhead und Unübersichtlichkeit zu vermeiden.

Das Nygard-Format hat keinen eigenen Abschnitt für Alternativen [2]. Das Y-Statement sieht in seiner veröffentlichten Form keinen Teil für verworfene Alternativen vor [3]. Das Tyree/Akerman-Template verursacht einen hohen Dokumentationsaufwand [4]. Wiki-Seiten, Commit-Messages und ein Decision Log geben ohne zusätzliches Template keine Struktur für die Abwägung von Alternativen vor.


### Konsequenzen

* Gut, weil Entscheidungen mit ihrer Begründung als eigenständige Dokumente vorliegen. Das verringert nach Jansen und Bosch den Verlust von Architekturwissen [1].
* Gut, weil neue Teammitglieder die Motivation früherer Entscheidungen nachlesen können. Ohne diese Motivation bleibt nach Nygard nur, eine Entscheidung blind zu akzeptieren oder blind rückgängig zu machen [2].
* Gut, weil die MADRs als Markdown-Dateien im Repository liegen und zusammen mit dem Code versioniert werden [2, 5].
* Schlecht, weil das Ausfüllen eines MADR mehr Zeit kostet als ein ADR im Nygard-Format [4].
* Schlecht, weil ADRs nur einen Nutzen haben, wenn sie dauerhaft gepflegt werden. In etwa der Hälfte der von Buchgeher et al. untersuchten GitHub-Repositories mit ADRs gibt es nur ein bis fünf ADRs [6].


### Bestätigung

Alle Entscheidungen sind in einem eigenständigen MADR festgehalten. Das gewählte Template wird in jedem MADR benutzt.


## Vor- und Nachteile der Optionen

### Nygard-ADR

Von Michael Nygard 2011 vorgeschlagenes Format mit den Abschnitten Titel, Kontext, Entscheidung, Status und Konsequenzen [2].

* Gut, weil das Format kurz ist. Nygard sieht ein bis zwei Seiten pro ADR vor [2].
* Gut, weil es in der Praxis am weitesten verbreitet ist. In den meisten von Buchgeher et al. untersuchten Repositories wird das Nygard-Template verwendet [6].
* Gut, weil Studierende es in einem kontrollierten Experiment signifikant besser bewertet haben als MADR. Sie beschrieben es als schneller und einfacher auszufüllen [4].
* Schlecht, weil es keinen eigenen Abschnitt für betrachtete Alternativen und deren Abwägung gibt [2].

### MADR (Markdown ADR)

Von Kopp, Armbruster und Zimmermann entwickeltes Template in Markdown [7]. Neben Kontext, Entscheidung und Konsequenzen enthält es Abschnitte für Entscheidungstreiber, betrachtete Optionen und deren Vor- und Nachteile [8].

* Gut, weil Alternativen und deren Vor- und Nachteile explizit festgehalten werden [8].
* Gut, weil es in einer Feature-Analyse von fünf ADR-Templates die höchste Gesamtbewertung erhalten hat. Die Bewertung wurde von den Autoren der Studie selbst vorgenommen [4].
* Gut, weil Teilnehmende einer Studie angaben, dass MADR die Gründe für eine Entscheidung klarer erklärt [4].
* Gut, weil optionale Abschnitte weggelassen werden können und es eine minimale Variante des Templates gibt [5].
* Schlecht, weil das Ausfüllen mehr Zeit kostet als beim Nygard-Format [4].

### Y-Statement

Von Zdun, Capilla, Tran und Zimmermann beschriebenes Format, das eine Entscheidung in einem einzigen Satz festhält [3]. Der Satz nennt Kontext, Anliegen, gewählte Option, angestrebte Qualität und akzeptierten Nachteil [3].

* Gut, weil der Dokumentationsaufwand sehr gering ist [3].
* Gut, weil Architekten laut den Autoren schlanke Dokumentation großen Templates vorziehen [3].
* Schlecht, weil in der veröffentlichten Form kein Teil für verworfene Alternativen vorgesehen ist [3].
* Schlecht, weil die Autoren selbst für wichtige Entscheidungen ausführlichere Templates empfehlen [3].

### Tyree/Akerman-Template

Von Tyree und Akerman 2005 in IEEE Software veröffentlichtes Template mit 14 Feldern, darunter Issue, Assumptions, Constraints, Positions, Argument und Implications [9].

* Gut, weil Annahmen, Randbedingungen, Alternativen und Begründung ausführlich festgehalten werden [9].
* Schlecht, weil 14 Felder pro Entscheidung ausgefüllt werden müssen [9].
* Schlecht, weil das Template in einer Feature-Analyse wegen seines hohen Dokumentationsaufwands schlechter abgeschnitten hat als MADR, Nygard-ADR und Y-Statement [4].

### Wiki-Seiten (Confluence, Notion)

Entscheidungen werden auf Seiten in einem Wiki außerhalb des Repositorys dokumentiert.

* Gut, weil Confluence eine eigene Vorlage für Entscheidungen anbietet [10].
* Schlecht, weil die Dokumentation nicht zusammen mit dem Code versioniert wird. Nygard und MADR sehen die Ablage im Repository vor [2, 5].
* Schlecht, weil Dokumentation häufig veraltet, wenn sie nicht im selben Schritt wie der Code angepasst wird [11].

### Pull Requests / Commit-Messages

Die Begründung einer Entscheidung wird in der Beschreibung eines Pull Requests oder in der Commit-Message festgehalten.

* Gut, weil kein zusätzliches Dokument entsteht und die Begründung direkt an der Änderung hängt.
* Schlecht, weil die Begründung oft fehlt. Bei rund 44 % der von Tian et al. untersuchten Commit-Messages fehlt die Information, was oder warum etwas geändert wurde [12].
* Schlecht, weil Links von Commits auf Issues oder Pull Requests veralten können und die Information dann verloren geht [12].
* Schlecht, weil es keinen festen Ort für betrachtete Alternativen gibt und eine Entscheidung über viele Commits verteilt sein kann.

### Decision Log

Alle Entscheidungen werden fortlaufend in einem einzigen Dokument festgehalten, zum Beispiel in einer Tabelle.

* Gut, weil alle Entscheidungen auf einen Blick sichtbar sind.
* Neutral, weil auch die Sammlung aller ADRs eines Projekts einen Decision Log bildet [13]. Ein Decision Log schließt ADRs also nicht aus.
* Schlecht, weil große Dokumente nach Nygard schlechter aktuell gehalten werden als kleine modulare Dokumente [2].
* Schlecht, weil ohne festes Template pro Eintrag nicht sichergestellt ist, dass Alternativen abgewogen werden.


## Weitere Informationen

Die Entscheidung wird erneut geprüft, wenn der Aufwand für das Schreiben der MADRs den Projektfortschritt spürbar bremst.

### Quellen

1. Jansen, A.; Bosch, J. (2005): Software Architecture as a Set of Architectural Design Decisions. In: 5th Working IEEE/IFIP Conference on Software Architecture (WICSA 2005), S. 109-120. DOI: 10.1109/WICSA.2005.61
2. Nygard, M. (2011): Documenting Architecture Decisions. https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions (10.11.2026)
3. Zdun, U.; Capilla, R.; Tran, H.; Zimmermann, O. (2013): Sustainable Architectural Design Decisions. IEEE Software 30(6), S. 46-53. DOI: 10.1109/MS.2013.97
4. Nogueira, F.; Silva, N.; Conte, T. (2026): One Size Fits All? An Empirical Comparison of ADR Templates regarding Comprehension, Usability, and Ease of Adoption. In: EASE 2026. Preprint: https://arxiv.org/abs/2604.27333 (10.11.2026)
5. MADR. Markdown Architectural Decision Records. https://adr.github.io/madr/ (10.11.2026)
6. Buchgeher, G.; Schöberl, S.; Geist, V.; Dorninger, B.; Haindl, P.; Weinreich, R. (2023): Using Architecture Decision Records in Open Source Projects. An MSR Study on GitHub. IEEE Access 11, S. 63725-63740. DOI: 10.1109/ACCESS.2023.3287654
7. Kopp, O.; Armbruster, A.; Zimmermann, O. (2018): Markdown Architectural Decision Records: Format and Tool Support. In: 10th Central European Workshop on Services and their Composition (ZEUS 2018). CEUR Workshop Proceedings.
8. Zimmermann, O. (2022): The Markdown ADR (MADR) Template Explained and Distilled. https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html (10.11.2026)
9. Tyree, J.; Akerman, A. (2005): Architecture Decisions: Demystifying Architecture. IEEE Software 22(2), S. 19-27. DOI: 10.1109/MS.2005.27
10. Atlassian: Decision Template. https://www.atlassian.com/software/confluence/templates/decision (10.11.2026)
11. Tan, W. S.; Wagner, M.; Treude, C. (2023): Detecting Outdated Code Element References in Software Repository Documentation. Empirical Software Engineering. DOI: 10.1007/s10664-023-10397-6
12. Tian, Y.; Zhang, Y.; Stol, K.-J.; Jiang, L.; Liu, H. (2022): What Makes a Good Commit Message? In: 44th International Conference on Software Engineering (ICSE 2022), S. 2389-2401. DOI: 10.1145/3510003.3510205
13. ADR GitHub Organization: Architectural Decision Records. https://adr.github.io/ (10.11.2026)