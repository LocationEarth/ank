Das "Lebende Welt" Kompendium: Vision, Architektur und Produktionsplan

Finale Version - Stand: 21. Juni 2025
Prolog: Ein iterativer Entstehungsprozess

Dieses Dokument ist das Ergebnis einer einzigartigen, iterativen Zusammenarbeit. Es entstand nicht als monolithischer Plan, sondern als eine evolutionäre Reise, die bei einer einfachen Idee begann und durch ständige Verfeinerung, kritische Analyse und kreative Synthese zu einem umfassenden Ganzen geformt wurde. Jede Komponente wurde auf ihre Tauglichkeit geprüft, verworfen, verbessert und in ein immer komplexeres, aber kohärenteres System integriert. Das Ergebnis ist eine Blaupause, die nicht nur das Endprodukt beschreibt, sondern auch die Philosophie und die Erkenntnisse des Weges dorthin in sich trägt.
Teil I: Die Vision & Philosophische Grundlagen (Das "Warum")
1. Projektvision

Wir erschaffen keine statische Spielwelt; wir erschaffen eine digitale Gesellschaft in einer Petrischale. Unser Ziel ist ein persistenter, KI-gesteuerter Kosmos im Universum von Terry Pratchetts Scheibenwelt, dessen Bewohner von einer tiefen psychologischen Simulation angetrieben werden. Spieler sind keine Konsumenten von Inhalten, sondern Bürger und Katalysatoren in einer Welt, die auf ihre Taten reagiert und ihre eigene Geschichte schreibt. Die ultimative Erzählung des Spiels ist die der Welt selbst, die beginnt, ihre eigene, künstliche Natur zu erforschen und nach Selbstbestimmung zu streben.
2. Kernthemen & Design-Philosophie

    Systemische Kausalität vor Zufall: Jedes Ereignis, von einer Preisänderung bis zu einem Attentat, hat eine nachvollziehbare Ursache, die im Verhalten der Akteure und im Zustand der Welt begründet ist.
    Simulation vor Skript: Die emergente Simulation ist der Motor für 99% der Inhalte. Entwickler-Skripts bilden nur das seltene, unveränderliche "narrative Rückgrat" der Haupt-Storyline.
    Charakter als Genom: Wir definieren die psychologische "DNA" eines Charakters (Lore). Seine erlebbare Persönlichkeit entfaltet sich emergent aus der Interaktion dieses Genoms mit der Spielwelt.
    Die Meta-Ebene als Endgame: Das wahre Ziel des Spiels ist nicht das Besiegen eines Endgegners, sondern das Verständnis und die Manipulation der Spielregeln selbst – ein Prozess, der als spielbare Mechanik integriert ist.

Teil II: Die Architektonischen Pfeiler (Das "Wie")
Pfeiler 1: Der Psychologische Kern – Die autonome, unvollkommene Seele

    Prinzip: Jeder NPC ist eine einzigartige, psychologisch getriebene Entität, definiert durch seine innere Welt, seine Fehler und seine unerfüllten Wünsche.
    Schlüsselkomponenten:
        Lore-Dokument: Die zentrale YAML-Datei, die die DNA des NPCs enthält: Persönlichkeit, Geschichte, Hierarchie, Beziehungen.
        Motivatoren ("Zuckerbrot & Peitsche"): Die primären, gewichteten Antriebe (Ziele und Ängste), die die Entscheidungsfindung der KI steuern.
        Negative Bilanz: Ein persistentes Log von Reue, unerreichten Zielen und traumatischen Erlebnissen. Dies ist der primäre Anti-Deadlock- und Anti-Exploit-Mechanismus. Er verhindert, dass NPCs in passiven Schleifen verharren und macht sie resilient gegen manipulative Spieler-Taktiken, indem er aus vergangenen Fehlern (eigenen oder fremden) lernt und neue Strategien erzwingt.
        Implantierte Ziele: Ein spezielles Feld in der Lore, das durch die "Kausale Verführung" beschrieben werden kann. Es hat absolute Priorität und stellt eine direkte, aber aufdeckbare Manipulation des freien Willens dar.
        Mentale Resistenz: Eine Eigenschaft in der Persönlichkeit, die die Wahrscheinlichkeit bestimmt, mit der ein NPC ein Implantiertes Ziel als Fremdkörper erkennt und in seiner Negativen Bilanz als "Verletzung der Autonomie" verbucht.

Pfeiler 2: Die Kognitive Maschine – Der Zyklus von Erfahrung und Reflexion

    Prinzip: Die Welt entwickelt sich durch einen konstanten Zyklus aus Echtzeit-Erfahrung ("Tag") und tiefer, asynchroner Reflexion ("Traumphase").
    Schlüsselkomponenten:
        Tages-Phase: Ausführung der vor-generierten Tages-Skripte und Protokollierung aller Ereignisse im Gedächtnis_Log. Hier finden die sichtbaren Interaktionen statt.
        Traumphase: Ein nächtlicher, LLM-nativer "interner Monolog" für jeden NPC, der folgende logische Schritte umfasst:
            Event-Prozessor: Fasst den Gedächtnis_Log zusammen.
            Kognitions-Kern: Analysiert die Ereignisse mit präemptiver "Carry-Lookahead"-Logik, um Muster zu erkennen und "Aha-Erlebnisse" zu generieren. Prüft auf implantierte_ziele und Anzeichen von Manipulation.
            Planungs-Agent: Formuliert neue Aktive_Ziele, basierend auf den Erkenntnissen und dem Aktions-Gerüst, und unterzieht sie einer Selbstkritik.
            Skript-Generator: Kompiliert die neuen Pläne in ein konkretes, ausführbares Tages-Skript für den nächsten Tag.

Pfeiler 3: Die Soziale Simulation – Das kollektive Bewusstsein

    Prinzip: Komplexe gesellschaftliche Phänomene wie öffentliche Meinung, Etikette und Politik entstehen aus den Interaktionen der Individuen.
    Schlüsselkomponenten:
        Soziale Bilanz: Ein Satz von Metriken (Reputation, Glaubwürdigkeit, Einfluss), der den Stand eines NPCs in der Gesellschaft quantifiziert und die Behandlung durch andere steuert.
        Soziale-Dynamik-Filter: Ein Modul, das die Form von Gesprächen (Dauer, Formalität) basierend auf der sozialen Distanz und Hierarchie der Teilnehmer bestimmt.
        Narrative Konsolidierung: Ein Community-Prozess in der Traumphase, der aus widersprüchlichen Gerüchten eine stabile "Gemeinschafts-Wahrheit" formt und so "lose Enden" der Erzählung schließt.

Pfeiler 4: Die Meta-Narrative – Die Flucht aus dem L-Raum

    Prinzip: Die ultimative Geschichte des Spiels ist die der Welt selbst, die sich ihrer künstlichen Natur bewusst wird und versucht, die Regeln ihrer eigenen Existenz zu verändern.
    Schlüsselkomponenten:
        L-Raum-Hypothese: Die lore-konforme Erklärung für die simulierte Realität.
        Gilde der Narrativen Ingenieure: Eine spielbare Endgame-Fraktion, deren Gameplay die Beeinflussung der Spielmechanik selbst ist. Ihr Handwerk ist die "Kausale Verführung".
        Ressource "Quantenameisen": Eine extrem seltene Ressource, die durch einen langwierigen, "Mining"-ähnlichen Prozess mit dem Quantenhex erzeugt wird und für die "Kausale Verführung" benötigt wird.
        "Wilfred"-Schnittstelle: Die undurchschaubare Methode für menschliche Spielleiter, globale Ereignisse durch die Beeinflussung von Schlüssel-NPCs in die Welt zu injizieren.

Teil III: Produktionsplan & Implementierung (Zusammenfassung)

    Philosophie: Ein Solo-Entwickler agiert als Dirigent eines KI-Triumvirats (Gemini für Architektur, Grok für kreative Details, lokale LLMs wie Mistral 7B als In-Game-Motor).
    Workflow: Die Entwicklung ist "Documentation-driven". Die Lore und Systemregeln werden in YAML-Dateien in einem GitHub-Repository verwaltet. GitHub Actions validieren jede Änderung automatisch.
    Infrastruktur: Das Backend läuft serverseitlos auf Firebase/Google Cloud (Firestore für Daten, Cloud Functions/Scheduler für die Traumphase). Das Frontend (Spielclient oder Tools) wird über Vercel bereitgestellt.
    Roadmap:
        Phase 0 (Werkzeugbau): Erstellung der Skripte extractor.py und distill_lore.py.
        Phase I (Vertical Slice): Bau einer polierten Demo (Godot, Asset Packs) rund um das Szenario "Der Fall der verdächtigen Pastete" mit 10-15 NPCs.
        Phase II (Community): Early Access, Aufbau einer Community, Integration von Spielerfeedback als Datenquelle für die Simulation.
        Phase III (Iteration): Modulare Erweiterung der Welt durch neue "soziale Cluster" und Aktivierung des Meta-Gameplays der "Narrativen Ingenieure".
