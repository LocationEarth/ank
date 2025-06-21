# ANK: Eine Lebende Scheibenwelt

**Status:** Detailliertes Konzept | **Typ:** Nicht-kommerzielles Fan-Projekt | **Technologie:** KI-gestützte Simulation

## Vision

„ANK“ ist ein ambitioniertes, nicht-kommerzielles Fan-Projekt, das eine digitale Version von Ankh-Morpork erschafft – eine lebendige, atmende Stadt, die Terry Pratchetts Scheibenwelt in ihrer chaotischen, zynischen und magischen Pracht einfängt. Die Spielwelt ist keine statische Kulisse, sondern ein dynamisches Ökosystem, in dem NPCs wie Sam Vimes, Lord Vetinari oder Ponder Stibbons denken, lernen und ihre Realität hinterfragen. Spieler agieren als Katalysatoren, die Quests, Intrigen und sogar die fundamentale Natur der Welt beeinflussen, während eine verborgene Meta-Narrative die Grenzen zwischen Spieler, Charakter und Schöpfer verwischt. Das Ziel ist eine immersive Simulation, die Pratchetts Humor, Philosophie und narrative Kausalität (Narrativium) in einem interaktiven Rahmen vereint.

## Kernidee

Die Welt wird durch vier architektonische Pfeiler angetrieben, die zusammen eine Gesellschaft erschaffen, die aus autonomen Individuen, dynamischen Zyklen, sozialen Netzwerken und einer selbstreflexiven Meta-Erzählung besteht. Das Spiel ist in drei Phasen geplant, wobei Phase I (6-9 Monate) einen Prototyp („Fall der verdächtigen Pastete“) mit 10-15 NPCs (z. B. Stadtwache) liefert. Die Entwicklung nutzt fine-getunte LLMs (z. B. Mistral 7B, Gemini), Godot, Firebase und YAML, optimiert für eine Solo-Entwicklung.

---

### Die Vier Architektonischen Pfeiler im Überblick

#### 1. Der Psychologische Kern: Die Seele der NPCs
* **Was:** Jeder NPC hat eine psychologische „DNA“, definiert durch ein Lore-Dokument (Persönlichkeit, Geschichte, Beziehungen), Motivatoren (Ziele wie „Frieden auf den Straßen“, Ängste wie „die Bestie entfesseln“), eine Negative Bilanz (Log von Misserfolgen und Manipulationen) und ein Aktions-Gerüst (valide Aktionen).
* **Wie:** In der Traumphase analysiert ein LLM (z. B. ein fine-getuntes `vimes-7b`) Ereignisse, um neue Ziele zu generieren, während die Negative Bilanz Resilienz gegen Exploits schafft. Das Aktions-Gerüst verbindet KI-Intentionen mit Spielmechaniken.
* **Scheibenwelt-Treue:** Die NPCs spiegeln Pratchetts Charaktere wider (z. B. Vimes’ Zynismus, Karottes Idealismus) und unterstützen die L-Raum-Hypothese, indem sie Anomalien erkennen.
* **Warum:** Dies schafft glaubwürdige, fehlerhafte und sich entwickelnde Persönlichkeiten, die Ankh-Morpork lebendig machen.

#### 2. Die Kognitive Maschine: Der Herzschlag der Welt
* **Was:** Der Tag-Nacht-Zyklus strukturiert die Simulation in Tages-Phase (Aktion, Interaktion, Protokollierung) und Traumphase (Reflexion, Lernen, Planung). NPCs führen Tages-Skripte aus, während der "Chirurgische LLM" improvisiert, wenn Spieler Skripte stören.
* **Wie:** In der Tages-Phase protokollieren NPCs Ereignisse im `Gedächtnis_Log`. In der Traumphase analysiert ein LLM diese Ereignisse, generiert Erkenntnisse (z. B. „Spieler_X ist unzuverlässig“) und erstellt neue Tages-Skripte.
* **Scheibenwelt-Treue:** Der Zyklus simuliert Ankh-Morporks Chaos, wo Charaktere wie Vimes nachts ihre Fälle überdenken, und unterstützt Pratchetts Narrativium durch dynamische Evolution.
* **Warum:** Dies sorgt für eine persistente Welt, in der NPCs auf Spieleraktionen reagieren und sich verändern.

#### 3. Die Soziale Simulation: Das Gefüge der Gesellschaft
* **Was:** Die Soziale Bilanz (Reputation, Glaubwürdigkeit) definiert den sozialen Stand. Der Soziale-Dynamik-Filter passt Interaktionen an Etikette an. Die Narrative Konsolidierung formt Gerüchte zu einer „Gemeinschafts-Wahrheit“.
* **Wie:** Die Soziale Bilanz wird in der Traumphase aktualisiert. Der Filter generiert Konversations-Parameter (z. B. „formal“, „angespannt“). Die Konsolidierung synthetisiert eine kollektive Geschichte aus den Logs aller NPCs.
* **Scheibenwelt-Treue:** Dies bildet Ankh-Morporks Hierarchien, Gildenkonflikte und Gerüchtekultur nach.
* **Warum:** Es schafft eine vernetzte, reaktive Gesellschaft, die emergente Geschichten erzeugt.

#### 4. Die Meta-Narrative: Die verborgene Wahrheit
* **Was:** Die L-Raum-Hypothese lässt NPCs erkennen, dass sie in einer Geschichte leben. Die Gilde der Narrativen Ingenieure manipuliert die Realität mit „Quantenameisen“. Die Wilfred-Schnittstelle ermöglicht subtile Spielleiter-Eingriffe.
* **Wie:** Anomalien (z. B. Spieler-Respawns) lösen in der Traumphase die Erkenntnis aus. Spieler werden über Quests in die Gilde eingeführt. Spielleiter injizieren `[GM_EVENT]`-Ereignisse.
* **Scheibenwelt-Treue:** Greift Pratchetts L-Raum und Narrativium auf und spiegelt seinen skurrilen, konzeptuellen Humor wider.
* **Warum:** Dies verwandelt die Welt in einen Akteur, der Spieler in eine einzigartige, existenzielle Erzählung einbindet.

---

### Das Aktionsgitter: Die Brücke zwischen KI und Mechanik
* **Was:** Das Aktionsgitter verbindet die abstrakten Intentionen der KI (z. B. „Druck erhöhen“) mit konkreten, mechanischen Aktionen (z. B. „drohen_mit_verhaftung“), um Kohärenz zu gewährleisten.
* **Wie:** Der `Konversations-Orchestrator` bildet die KI-Intention auf eine valide, im Spiel ausführbare Aktion ab, basierend auf Persönlichkeit und Kontext. Die resultierenden Dialoge und Handlungen sind somit immer im Rahmen der Spielregeln.
* **Warum:** Es verhindert leere Versprechungen der KI und schafft eine nahtlose, glaubwürdige Immersion, bei der Gedanke und Tat des NPCs immer übereinstimmen.

---

### Technologie-Stack (Geplant)
* **Kern-Engine:** Godot
* **Simulations-Logik & Werkzeuge:** Python 3.9+
* **KI-Modelle:**
    * **Konzeption & Daten-Extraktion:** Gemini & Grok
    * **In-Game Simulation (Lokal):** Fine-getunte Mistral 7B-Derivate
* **Datenhaltung:** YAML & JSON für die Entwicklung (versioniert in Git), Migration zu Firestore/SQLite für die Live-Anwendung.
* **Infrastruktur:** GitHub (Repo, Actions), Google Cloud (Traumphasen-Verarbeitung), Vercel (Tools/Frontend-Hosting).

### Projektstatus
Dieses Projekt befindet sich in einer weit fortgeschrittenen **Konzeptions- und Architekturphase**. Alle Kernsäulen und -mechaniken sind definiert. Der nächste Schritt ist die Umsetzung von **Phase I des Entwicklungsplans**: die Erstellung eines spielbaren "Vertical Slice"-Prototypen.

### Beitragen & Lizenz
Dieses Projekt wird aktuell als Solo-Unterfangen entwickelt. Zukünftige Kollaborationsmöglichkeiten werden hier bekannt gegeben.

Der für dieses Projekt entwickelte Code und die Architektur stehen unter der **MIT-Lizenz**. Das geistige Eigentum der Scheibenwelt, ihrer Charaktere, Orte und Konzepte gehört ausschließlich dem Nachlass von Sir Terry Pratchett und seinen Lizenznehmern. Dieses Projekt ist eine **nicht-kommerzielle Hommage** und verfolgt keinerlei finanzielle Interessen.
