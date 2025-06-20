Pfeiler 2: Die Kognitive Maschine

Dieses Dokument (docs/02_Simulationszyklus.md) ist eine Detaillierung von Pfeiler 2 aus dem MANIFEST.md und beschreibt den Kernprozess, der die "Lebende Welt" antreibt und die Entwicklung der NPCs ermöglicht.
Einleitung

Die Kognitive Maschine ist der Herzschlag der Spielwelt. Sie ist kein statischer Zustand, sondern ein unaufhörlicher, zyklischer Prozess, der die Grundlage für alles Lernen, Planen und für jede emergente Entwicklung bildet. Das Kernprinzip ist die Trennung von unmittelbarer Erfahrung und tiefer Reflexion, abgebildet in einem konstanten Tag-Nacht-Zyklus. Der Zyklus lautet: Erfahrung -> Protokollierung -> Reflexion -> Planung -> Aktion.
1. Der Tag-Nacht-Zyklus (Das Metronom der Welt)

Prinzip (High-Level):
Der Tag-Nacht-Zyklus ist der fundamentale Rhythmus, nach dem die Welt operiert. Die Tages-Phase ist die Zeit der Aktion, der Interaktion und des Sammelns von Erfahrungen. Die Traumphase (Nacht) ist die Zeit der asynchronen, serverseitigen Verarbeitung, in der die gesammelten Erfahrungen zu Erkenntnissen, neuen Zielen und Plänen für den nächsten Tag "destilliert" werden. Diese Trennung ist entscheidend, um eine tiefe Simulation zu ermöglichen, ohne die Echtzeit-Performance des Spiels zu beeinträchtigen.

Implementierung (Technische Details):

    Der Zyklus ist serverseitig gesteuert. Eine "Tages-Phase" kann einer konfigurierbaren Echtzeit-Dauer entsprechen (z.B. 2-4 Stunden).
    Die "Traumphase" ist ein kurzer, intensiver Batch-Job, der nach Ende jeder Tages-Phase automatisch für alle NPCs ausgeführt wird (z.B. ein 5-10-minütiger Prozess).

2. Die Tages-Phase (Die Bühne der Erfahrung)

Prinzip (High-Level):
Die Tages-Phase ist die für den Spieler sicht- und erlebbare Ebene. Hier werden die Ergebnisse der nächtlichen Reflexion als konkretes Verhalten auf die "Bühne" gebracht. Alles, was in dieser Phase geschieht – jede Aktion des Spielers, jeder Dialog, jede beobachtete NPC-Interaktion – wird als unbewerteter "Roh-Datum" für die nächste Traumphase protokolliert.

Implementierung (Prozesse während des Tages):

    Ausführung der Tages-Skripte: Der Skript-Interpreter führt die in der letzten Traumphase generierten Verhaltens- und Dialogbäume für jeden NPC aus. Dies stellt das berechenbare Grundverhalten sicher.
    Die "Bühnen-Simulation": NPCs interagieren sichtbar miteinander, basierend auf ihren Skripten. Diese Interaktionen werden durch den Sozialen-Dynamik-Filter (aus Pfeiler 1) in Form und Dauer geprägt.
    Der "Chirurgische LLM": Der Generative Dialog-Agent wird vom Konversations-Orchestrator getriggert, wenn unvorhergesehene Spieleraktionen auftreten oder Schlüsselmomente eine freie Interaktion erfordern.
    Protokollierung im Gedächtnis_Log: Jedes signifikante Ereignis (z.B. "Spieler hat mich angelogen", "Habe Kael und Vetinari streiten sehen", "Konnte mein Ziel 'Verkaufe Pastete' nicht erfüllen") wird als einfacher Texteintrag im temporären Gedächtnis_Log des betreffenden NPCs gespeichert.

3. Die Traumphase (Der Interne Monolog)

Prinzip (High-Level):
Dies ist das Herzstück der Kognitiven Maschine. Hier findet das wahre "Denken" statt. Wir modellieren diesen Prozess als ein "Gespräch mit sich selbst", das jeder NPC führt. Die KI erhält den gesamten Kontext ihrer Lore und die Erlebnisse des Tages und wird durch einen strukturierten Prompt angewiesen, einen mehrstufigen Reflexionsprozess durchzuführen.

Implementierung (Die logischen Module im "Traum-Prompt"):
Die Traumphase ist ein einziger, großer API-Aufruf an ein leistungsstarkes LLM (z.B. Gemini 1.5 Pro). Der Prompt ist so strukturiert, dass er die KI anleitet, die folgenden logischen Schritte durchzuführen:

    Schritt A: Event-Prozessor (Retrospektion)
        Funktion: Liest den rohen Gedächtnis_Log des Tages und fasst ihn zu den wichtigsten, bedeutungsvollen Ereignissen zusammen. ("Ich wurde mehrmals beschuldigt, aber auch verteidigt. Mein Plan, Zeuge A zu befragen, ist gescheitert.")

    Schritt B: Kognitions-Kern (Synthese & Erkenntnis)
        Funktion: Dies ist die Umsetzung unserer "Carry-Lookahead Adder"-Analogie. Die KI wird angewiesen, die zusammengefassten Ereignisse nicht isoliert, sondern als Muster zu betrachten und mit ihrer Kern-Identität (Persönlichkeit, Motivatoren, Negative Bilanz) zu verbinden. Hier entstehen die "Aha-Erlebnisse".
        Beispiel-Logik: IF [Ereignis: "Wiederholte Beschuldigung"] AND [Persönlichkeit: "Zynisch"] AND [Negative Bilanz: "Wurde schon einmal fälschlich beschuldigt"] -> THEN [Erkenntnis: "Die ganze Stadt ist gegen mich, ich kann niemandem trauen."]

    Schritt C: Planungs-Agent (Prospektion)
        Funktion: Basierend auf der neuen Erkenntnis und den permanenten Motivatoren formuliert die KI neue, konkrete Aktive_Ziele für den nächsten Tag. Sie wählt dabei aus der Liste der Verfügbaren Aktionen, die ihr das Aktions-Gerüst vorgibt. Der Prompt enthält eine Anweisung zur Selbstkritik ("Passt dieser Plan zu einem 'feigen' Charakter?").

    Schritt D: Skript-Generator (Kompilierung)
        Funktion: Der finale Schritt im Prompt. Die KI wird angewiesen, die neuen Aktive_Ziele und den angepassten emotionalen Zustand in ein konkretes, ausführbares Tages-Skript zu übersetzen.
        Beispiel-Output (vereinfacht):

{
  "ziel_fuer_tag": "Finde heraus, wer die Gerüchte über mich verbreitet.",
  "aktionen": [
    {"zeit": "09:00", "aktion": "gehe_zu", "ziel": "Taverne"},
    {"zeit": "09:15", "aktion": "befrage_Wirt", "dialog_fokus": "geruechte"}
  ]
}

Dieser Zyklus stellt sicher, dass jeder NPC jeden Tag als eine leicht veränderte, von den Erfahrungen des Vortags geprägte Version seiner selbst erwacht.

