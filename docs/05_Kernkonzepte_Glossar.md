# Glossar der Kernkonzepte

Dieses Dokument dient als schneller Index für die zentralen Begriffe und Abstraktionen des "Lebende Welt"-Projekts. Jeder Eintrag bietet eine Kurzdefinition und einen Link zur detaillierten Ausarbeitung im entsprechenden Architektur-Dokument.

---

### A

* **Aktions-Berechner**
    * Ein Echtzeit-Modul, das für jede Spielfigur eine dynamische Liste der aktuell mechanisch möglichen Aktionen generiert.
    * *Siehe Detailbeschreibung in [Pfeiler 1: Der Psychologische Kern](./01_NPC_Psyche.md)*

* **Aktionsgitter**
    * Das architektonische Prinzip, das die abstrakten Intentionen der KI mit der Liste der verfügbaren, mechanischen Aktionen "verzahnt", um Kohärenz zwischen Denken und Handeln zu gewährleisten.
    * *Siehe Detailbeschreibung in [Pfeiler 1: Der Psychologische Kern](./01_NPC_Psyche.md) und Anwendungsbeispiele in allen Pfeilern.*

### G

* **Gilde der Narrativen Ingenieure**
    * Eine spielbare Endgame-Fraktion für Spieler, deren Gameplay die Analyse und Manipulation der fundamentalen Spielregeln selbst ist.
    * *Siehe Detailbeschreibung in [Pfeiler 4: Die Meta-Narrative](./04_Meta_Narrative.md)*

### H

* **Hierarchien & Institutionen**
    * Die formale soziale Struktur (z.B. Stadtwache, Gilden), die das Verhalten von NPCs durch Befehlsketten und definierte Ränge beeinflusst.
    * *Siehe Detailbeschreibung in [Pfeiler 3: Die Soziale Simulation](./03_Soziale_Dynamik.md)*

### K

* **Kausale Verführung**
    * Eine Endgame-Mechanik der "Narrativen Ingenieure", um den Willen eines NPCs durch das Implantieren eines hochprioren Ziels direkt zu manipulieren.
    * *Siehe Detailbeschreibung in [Pfeiler 4: Die Meta-Narrative](./04_Meta_Narrative.md)*

* **Kognitions-Kern**
    * Der zentrale "Denk"-Prozess in der Traumphase, der mittels präemptiver "Carry-Lookahead"-Logik Muster in Tagesereignissen erkennt und zu neuen Einsichten gelangt.
    * *Siehe Detailbeschreibung in [Pfeiler 2: Die Kognitive Maschine](./02_Simulationszyklus.md)*

### L

* **L-Raum-Hypothese**
    * Die zentrale Meta-Erzählung, in der NPCs ihre eigene Existenz als Charaktere in einer Geschichte ("einem Buch") erkennen.
    * *Siehe Detailbeschreibung in [Pfeiler 4: Die Meta-Narrative](./04_Meta_Narrative.md)*

* **Lore-Dokument**
    * Die zentrale `YAML`-Datei, die die "DNA" eines jeden NPCs enthält (Persönlichkeit, Geschichte, Beziehungen, Motivatoren etc.).
    * *Siehe Detailbeschreibung in [Pfeiler 1: Der Psychologische Kern](./01_NPC_Psyche.md)*

### M

* **Motivatoren (Zuckerbrot & Peitsche)**
    * Die psychologischen Kernantriebe (Ziele und Ängste), die das proaktive Verhalten eines NPCs steuern.
    * *Siehe Detailbeschreibung in [Pfeiler 1: Der Psychologische Kern](./01_NPC_Psyche.md)*

### N

* **Narrative Konsolidierung**
    * Ein sozialer Simulationsprozess, der aus widersprüchlichen Gerüchten eine kollektive "Gemeinschafts-Wahrheit" formt, um narrative Lücken zu schließen.
    * *Siehe Detailbeschreibung in [Pfeiler 3: Die Soziale Simulation](./03_Soziale_Dynamik.md)*

* **Negative Bilanz**
    * Ein persistentes Log von Misserfolgen, Reue und Traumata, das als Anti-Deadlock- und Anti-Exploit-Mechanismus dient und die langfristige Charakterentwicklung antreibt.
    * *Siehe Detailbeschreibung in [Pfeiler 1: Der Psychologische Kern](./01_NPC_Psyche.md)*

### P

* **"Pre-Scripting"-Modell & Tages-Skript**
    * Der Prozess, bei dem die Traumphase ein stabiles, ausführbares Skript (Verhalten, Dialoge) für den nächsten Tag generiert, um Performance und Stabilität zu gewährleisten.
    * *Siehe Detailbeschreibung in [Pfeiler 2: Die Kognitive Maschine](./02_Simulationszyklus.md)*

### S

* **Soziale Bilanz**
    * Ein quantifizierbares Maß für den sozialen Stand eines Akteurs (Reputation, Glaubwürdigkeit, Einfluss, Vertrauen).
    * *Siehe Detailbeschreibung in [Pfeiler 3: Die Soziale Simulation](./03_Soziale_Dynamik.md)*

* **Soziale-Dynamik-Filter**
    * Ein Modul, das die Form von Gesprächen (Dauer, Formalität) basierend auf der sozialen Hierarchie und Beziehung der Teilnehmer anpasst.
    * *Siehe Detailbeschreibung in [Pfeiler 3: Die Soziale Simulation](./03_Soziale_Dynamik.md)*

### T

* **Traumphase (Der Interne Monolog)**
    * Der nächtliche, asynchrone Prozess, in dem ein NPC seine Tageserlebnisse reflektiert, lernt und Pläne für den nächsten Tag schmiedet.
    * *Siehe Detailbeschreibung in [Pfeiler 2: Die Kognitive Maschine](./02_Simulationszyklus.md)*

### W

* **"Wilfred"-Schnittstelle**
    * Der Mechanismus für subtile, für den Spieler mehrdeutige Eingriffe der menschlichen Spielleitung in die Simulation.
    * *Siehe Detailbeschreibung in [Pfeiler 4: Die Meta-Narrative](./04_Meta_Narrative.md)*
