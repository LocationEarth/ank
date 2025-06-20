Pfeiler 2: Die Kognitive Maschine

Dieses Dokument (docs/02_Simulationszyklus.md) ist eine Detaillierung von Pfeiler 2 aus dem MANIFEST.md und beschreibt den Kernprozess, der die "Lebende Welt" antreibt und die fortlaufende Evolution der NPCs ermöglicht.
Einleitung

Die Kognitive Maschine ist der Motor der Welt, ihr unaufhörlicher Herzschlag. Sie ist ein zyklischer Prozess, der sicherstellt, dass Charaktere nicht statisch sind, sondern auf Erfahrungen reagieren, lernen und ihre zukünftigen Handlungen anpassen. Das Fundament dieses Prozesses ist der Tag-Nacht-Zyklus, der die Phasen der direkten Aktion von denen der tiefen, internen Reflexion trennt. Der ununterbrochene Kreislauf lautet: Erfahrung → Protokollierung → Reflexion → Planung → Aktion.
1. Der Tag-Nacht-Zyklus (Das Metronom der Welt)

Prinzip (High-Level):
Der Tag-Nacht-Zyklus ist der fundamentale Taktgeber, der die Simulation strukturiert. Diese Trennung ist eine entscheidende architektonische Entscheidung, um zwei Ziele zu erreichen:

    Performance: Rechenintensive, tiefe Simulationen (Traumphase) werden von der Echtzeit-Interaktion entkoppelt, um ein flüssiges Spielerlebnis zu gewährleisten.
    Glaubwürdigkeit: Es simuliert ein menschliches Muster. Wesen erleben Dinge tagsüber und verarbeiten, konsolidieren und lernen daraus im Schlaf (oder in Ruhephasen).

Implementierung (Technische Details):

    Der Zyklus wird serverseitig gesteuert. Eine Tages-Phase kann einer konfigurierbaren Echtzeit-Dauer entsprechen (z.B. 2-4 Stunden). Im Prototypen wird diese zur Beschleunigung auf ca. 10 Minuten gesetzt.
    Die Traumphase ist ein kurzer, serverseitiger Batch-Job, der unmittelbar nach dem Ende einer Tages-Phase für alle aktiven NPCs ausgeführt wird.

2. Die Tages-Phase (Die Bühne der Erfahrung)

Prinzip (High-Level):
Die Tages-Phase ist die "performative" Ebene der Simulation. Hier werden die Ergebnisse der nächtlichen Reflexion als konkretes NPC-Verhalten für den Spieler sichtbar. Jede signifikante Aktion und Interaktion in dieser Phase wird als unbewerteter Roh-Datum für die nächste Traumphase protokolliert. Es ist die Phase des Handelns und des Sammelns von Sinneseindrücken.

Implementierung (Prozesse während des Tages):

    Ausführung der Tages-Skripte: Der Skript-Interpreter führt die im Voraus generierten Verhaltens- und Dialogbäume aus. Dies bildet das Grundverhalten der NPCs für den jeweiligen Tag.
    Der "Chirurgische LLM": Der Generative Dialog-Agent wird vom Konversations-Orchestrator als Fallback getriggert, wenn eine geplante Aktion durch Spieler-Intervention ungültig wird oder ein Schlüsselmoment der Erzählung maximale Interaktionsfreiheit erfordert.
    Protokollierung im Gedächtnis_Log: Jedes relevante Ereignis wird als einfacher, faktischer Eintrag im temporären Gedächtnis_Log des NPCs gespeichert. Beispiele: "Spieler hat mich angelogen.", "Mein Ziel 'Befrage Zeuge A' ist gescheitert, da Zeuge A im Gefängnis ist.", "Habe eine 'Kausale Verführung' durch Spieler_X gespürt."

3. Die Traumphase (Der Interne Monolog)

Prinzip (High-Level):
Dies ist das Herz der Kognitiven Maschine, wo das eigentliche Lernen und die Evolution stattfinden. Als "Gespräch mit sich selbst" modelliert, erhält die KI (z.B. Gemini 1.5 Pro) einen umfassenden Prompt mit ihrer gesamten Lore und den Ereignissen des Tages. Sie wird angewiesen, einen mehrstufigen Reflexionsprozess durchzuführen, um zu neuen Einsichten und Plänen zu gelangen.

Implementierung (Die logischen Schritte im "Traum-Prompt"):
Die KI wird angewiesen, die folgenden Schritte sequenziell abzuarbeiten:

    Schritt A: Prüfung auf Manipulation
        Der Kognitions-Kern prüft als Erstes das Feld implantierte_ziele (aus Pfeiler 1). Existiert ein solches Ziel, wird es mit absoluter Priorität behandelt. Basierend auf der Mentalen Resistenz des NPCs kann dieser Versuch jedoch als [Verletzung der Autonomie] in der Negativen Bilanz vermerkt werden, was zu Misstrauen und Gegenmaßnahmen führt.

    Schritt B: Event-Prozessor (Retrospektion)
        Fasst den Gedächtnis_Log zu den wichtigsten Ereignissen des Tages zusammen. Dies reduziert das "Rauschen" und identifiziert die relevanten Datenpunkte für die weitere Analyse.

    Schritt C: Kognitions-Kern (Synthese & Erkenntnis)
        Dies ist die "Carry-Lookahead Adder"-Logik. Die KI wird angewiesen, die zusammengefassten Ereignisse als Muster zu betrachten und sie mit ihrer Kern-Identität (Persönlichkeit, Motivatoren, Negative Bilanz) zu verbinden. Sie antizipiert Konsequenzen und generiert eine zentrale "Erkenntnis" des Tages.

    Schritt D: Planungs-Agent (Prospektion)
        Basierend auf der Erkenntnis (oder einem implantierten_ziel) formuliert die KI neue, proaktive Aktive_Ziele für den nächsten Tag.
        Entscheidend: Sie wählt diese Ziele aus der dynamisch generierten Liste des Aktions-Gerüsts (aus Pfeiler 1) aus, um die mechanische Machbarkeit zu garantieren.
        Der Prompt enthält eine Anweisung zur Selbstkritik, um die Plausibilität des Plans zu prüfen ("Passt dieser Plan zu einem 'zynischen' Charakter?").

    Schritt E: Skript-Generator (Kompilierung)
        Der finale Schritt. Die KI übersetzt die abstrakten Aktive_Ziele und den neuen emotionalen Zustand in ein konkretes, ausführbares Tages-Skript im JSON/YAML-Format. Dieses Skript enthält Verhaltensweisen, Bewegungsrouten und verzweigte Dialogbäume für den nächsten Tag.

Dieser Zyklus sorgt dafür, dass die Welt niemals statisch ist. Jeder Sonnenaufgang bringt NPCs hervor, die durch die Erfahrungen des Vortags subtil, aber bedeutungsvoll verändert wurden.
