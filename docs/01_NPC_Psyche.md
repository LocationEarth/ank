Pfeiler 1: Der Psychologische Kern

Dieses Dokument (docs/01_NPC_Psyche.md) ist eine Detaillierung von Pfeiler 1 aus dem MANIFEST.md und beschreibt die grundlegende Architektur eines jeden autonomen NPCs in "Die Lebende Welt".
Einleitung

Der psychologische Kern ist das Betriebssystem eines jeden NPCs. Er definiert seine Identität, seine inneren Antriebe und die Regeln, nach denen er die Welt wahrnimmt und handelt. Ziel ist es, keine perfekten Roboter zu erschaffen, sondern glaubwürdige, fehlerhafte und sich entwickelnde künstliche Persönlichkeiten.
1. Das Lore-Dokument

Prinzip (High-Level):
Das Lore-Dokument ist die DNA, der "Charakterbogen 2.0" und das Langzeitgedächtnis eines jeden NPCs. Es ist die einzige, maßgebliche Quelle der Wahrheit für die Identität eines Charakters. Während seine Kernmerkmale (wie die Persönlichkeit) relativ statisch sind, werden seine Zustände (wie Beziehungen und Ziele) durch die Simulation in der Traumphase kontinuierlich weiterentwickelt.

Implementierung (Datenstruktur & Beispiel):
Die Struktur wird als YAML-Datei für jeden NPC definiert, was Lesbarkeit und Versionierung (via GitHub) erleichtert.

Beispiel: game_data/lore/npcs/samuel_vimes.yaml

id: samuel_vimes
persönlichkeit:
  - "Zynisch bis ins Mark"
  - "Pflichtbewusst bis zur Selbstzerstörung"
  - "Unbestechlich"
  - "Pragmatisch"
  - "Trägt ein tiefes Klassenbewusstsein (Unten vs. Oben)"
  - "Latent gewalttätig (kontrolliert durch Disziplin)"
geschichte: "Ehemaliger Säufer, durch Heirat mit Lady Sybil zum Herzog von Ankh aufgestiegen, ein Titel, der ihm verhasst ist. Kommandeur der Stadtwache von Ankh-Morpork, der Ordnung in die chaotischste Stadt der Scheibenwelt bringt."
hierarchie:
  organisation: "Stadtwache von Ankh-Morpork"
  rang: "Kommandeur, Herzog von Ankh"
beziehungen:
  "Lady Sybil Ramkin": { typ: "Ehefrau, Anker", vertrauen: 10, zuneigung: 10, furcht: 1 }
  "Lord Vetinari": { typ: "Vorgesetzter/Gegenspieler", vertrauen: 2, respekt: 8, furcht: 3 }
  "Hauptmann Karotte": { typ: "Ziehsohn/Moralischer Kompass", vertrauen: 9, zuneigung: 9, furcht: 0 }
aktive_ziele: # Dynamisch von der Traumphase generiert
  - "Finde die Wahrheit über das Amulett, um einen Justizirrtum zu vermeiden."
gedächtnis_log: # Temporäres Log, wird jede Nacht verarbeitet und geleert
  - "Habe Rhys bei Fluchtversuch verhaftet. Er beteuerte seine Unschuld."


2. Die Motivatoren (Zuckerbrot & Peitsche)

Prinzip (High-Level):
Dies ist der primäre Antriebsmotor für die Entscheidungsfindung eines NPCs. Anstatt nur auf externe Trigger zu reagieren, handeln NPCs proaktiv, um ihre fundamentalen Ziele (Zuckerbrot) zu erreichen und ihre tiefsten Ängste (Peitsche) zu vermeiden. Dieses System stellt sicher, dass jede Handlung einem nachvollziehbaren, inneren Zweck dient.

Implementierung (Datenstruktur & Beispiel):
Die Motivatoren sind ein zentraler, gewichteter Teil des Lore-Dokuments. Die Planungs-Agent-KI in der Traumphase wird explizit angewiesen, jeden potenziellen Plan gegen diese Listen zu validieren.

Beispiel-Ausschnitt aus samuel_vimes.yaml

motivatoren:
  zuckerbrot: # Was er anstrebt
    - "Eine funktionierende Wache und 'Frieden' auf den Straßen."
    - "Pünktlich um 18:00 Uhr zu Hause sein, um 'Wo ist meine Kuh?' zu lesen. # HÖCHSTE PRIORITÄT"
    - "Sicherstellen, dass das Gesetz für absolut jeden gilt."
  peitsche: # Was er vermeidet
    - "Die 'Bestie' in seinem Inneren zu entfesseln; die Kontrolle zu verlieren."
    - "Zu dem zu werden, was er verachtet: ein weicher, abgehobener Adliger."
    - "Dass seiner Familie (Sybil oder der junge Sam) etwas zustößt. # HÖCHSTE PRIORITÄT"

Absolut. Das "Sowohl-als-auch"-Prinzip ist der beste Weg, um sicherzustellen, dass die Dokumentation sowohl die strategische Vision (das "Warum") als auch die technische Spezifikation (das "Wie") erfasst. Ein Dokument, das beides leistet, ist für alle Beteiligten – vom Designer bis zum Programmierer – von maximalem Wert.

Wie besprochen, beginnen wir mit dem ersten und wichtigsten Pfeiler.
Pfeiler 1: Der Psychologische Kern

Dieses Dokument (docs/01_NPC_Psyche.md) ist eine Detaillierung von Pfeiler 1 aus dem MANIFEST.md und beschreibt die grundlegende Architektur eines jeden autonomen NPCs in "Die Lebende Welt".
Einleitung

Der psychologische Kern ist das Betriebssystem eines jeden NPCs. Er definiert seine Identität, seine inneren Antriebe und die Regeln, nach denen er die Welt wahrnimmt und handelt. Ziel ist es, keine perfekten Roboter zu erschaffen, sondern glaubwürdige, fehlerhafte und sich entwickelnde künstliche Persönlichkeiten.
1. Das Lore-Dokument

Prinzip (High-Level):
Das Lore-Dokument ist die DNA, der "Charakterbogen 2.0" und das Langzeitgedächtnis eines jeden NPCs. Es ist die einzige, maßgebliche Quelle der Wahrheit für die Identität eines Charakters. Während seine Kernmerkmale (wie die Persönlichkeit) relativ statisch sind, werden seine Zustände (wie Beziehungen und Ziele) durch die Simulation in der Traumphase kontinuierlich weiterentwickelt.

Implementierung (Datenstruktur & Beispiel):
Die Struktur wird als YAML-Datei für jeden NPC definiert, was Lesbarkeit und Versionierung (via GitHub) erleichtert.

Beispiel: game_data/lore/npcs/samuel_vimes.yaml
YAML

id: samuel_vimes
persönlichkeit:
  - "Zynisch bis ins Mark"
  - "Pflichtbewusst bis zur Selbstzerstörung"
  - "Unbestechlich"
  - "Pragmatisch"
  - "Trägt ein tiefes Klassenbewusstsein (Unten vs. Oben)"
  - "Latent gewalttätig (kontrolliert durch Disziplin)"
geschichte: "Ehemaliger Säufer, durch Heirat mit Lady Sybil zum Herzog von Ankh aufgestiegen, ein Titel, der ihm verhasst ist. Kommandeur der Stadtwache von Ankh-Morpork, der Ordnung in die chaotischste Stadt der Scheibenwelt bringt."
hierarchie:
  organisation: "Stadtwache von Ankh-Morpork"
  rang: "Kommandeur, Herzog von Ankh"
beziehungen:
  "Lady Sybil Ramkin": { typ: "Ehefrau, Anker", vertrauen: 10, zuneigung: 10, furcht: 1 }
  "Lord Vetinari": { typ: "Vorgesetzter/Gegenspieler", vertrauen: 2, respekt: 8, furcht: 3 }
  "Hauptmann Karotte": { typ: "Ziehsohn/Moralischer Kompass", vertrauen: 9, zuneigung: 9, furcht: 0 }
aktive_ziele: # Dynamisch von der Traumphase generiert
  - "Finde die Wahrheit über das Amulett, um einen Justizirrtum zu vermeiden."
gedächtnis_log: # Temporäres Log, wird jede Nacht verarbeitet und geleert
  - "Habe Rhys bei Fluchtversuch verhaftet. Er beteuerte seine Unschuld."

2. Die Motivatoren (Zuckerbrot & Peitsche)

Prinzip (High-Level):
Dies ist der primäre Antriebsmotor für die Entscheidungsfindung eines NPCs. Anstatt nur auf externe Trigger zu reagieren, handeln NPCs proaktiv, um ihre fundamentalen Ziele (Zuckerbrot) zu erreichen und ihre tiefsten Ängste (Peitsche) zu vermeiden. Dieses System stellt sicher, dass jede Handlung einem nachvollziehbaren, inneren Zweck dient.

Implementierung (Datenstruktur & Beispiel):
Die Motivatoren sind ein zentraler, gewichteter Teil des Lore-Dokuments. Die Planungs-Agent-KI in der Traumphase wird explizit angewiesen, jeden potenziellen Plan gegen diese Listen zu validieren.

Beispiel-Ausschnitt aus samuel_vimes.yaml
YAML

motivatoren:
  zuckerbrot: # Was er anstrebt
    - "Eine funktionierende Wache und 'Frieden' auf den Straßen."
    - "Pünktlich um 18:00 Uhr zu Hause sein, um 'Wo ist meine Kuh?' zu lesen. # HÖCHSTE PRIORITÄT"
    - "Sicherstellen, dass das Gesetz für absolut jeden gilt."
  peitsche: # Was er vermeidet
    - "Die 'Bestie' in seinem Inneren zu entfesseln; die Kontrolle zu verlieren."
    - "Zu dem zu werden, was er verachtet: ein weicher, abgehobener Adliger."
    - "Dass seiner Familie (Sybil oder der junge Sam) etwas zustößt. # HÖCHSTE PRIORITÄT"

3. Die Negative Bilanz

Prinzip (High-Level):
Dies ist der Mechanismus, der Charakteren eine langfristige Tiefe und Resilienz gegen spielerische Exploits verleiht. NPCs sind nicht nur durch ihre Erfolge, sondern auch durch ihre Misserfolge, ihre Reue und ihre unerfüllten Träume geprägt. Diese "psychologischen Narben" verhindern, dass ein NPC in einen narrativen Deadlock gerät, indem sie ihn dazu zwingen, neue Strategien zu entwickeln, wenn alte Pläne scheitern.

Implementierung (Datenstruktur & Beispiel):
Wir fügen der Lore eine neue Sektion hinzu. Jeder Eintrag ist ein vergangenes Ereignis, das den Charakter weiterhin beeinflusst.

Beispiel-Ausschnitt (neu für samuel_vimes.yaml)


negative_bilanz:
  - typ: "Ungelöster Fall"
    beschreibung: "Der Mordfall in der Schneidergilde vor 5 Jahren. Die Spuren waren kalt. Es wurmt mich."
    intensitaet: 8 # Skala von 1-10
  - typ: "Persönliches Versagen"
    beschreibung: "Jahre des Alkoholismus, die die Nachtwache fast zerstört haben. Eine ständige Mahnung."
    intensitaet: 6
  - typ: "Aktuelles Scheitern" # dynamisch von der Traumphase hinzugefügt
    beschreibung: "Konnte den Diebstahl von Elaras Amulett nicht verhindern."
    intensitaet: 7



4. Das Aktions-Gerüst

Prinzip (High-Level):
Dies ist die fundamentale Brücke zwischen dem abstrakten "Geist" des NPCs und der regelbasierten, mechanischen Spielwelt. Es definiert die "Grammatik" aller möglichen Handlungen und stellt sicher, dass die von der KI erdachten Pläne auch tatsächlich im Spiel ausgeführt werden können.

Implementierung (Datenstruktur & Beispiel):
Im Gegensatz zu den anderen Komponenten ist dies kein statischer Teil der Lore-Datei. Es ist eine dynamische Liste, die in Echtzeit vom Aktions-Berechner-Modul für jede Figur generiert wird. Diese Liste wird dann als Input an die KI (insbesondere den Planungs-Agent und den Skript-Generator) übergeben.

Beispiel: Dynamisch generierte [Verfügbare Aktionen] für Kael, der auf dem Marktplatz steht.

[
  {
    "aktion_id": "spreche_mit",
    "ziel_id": "haendler_b_id",
    "beschreibung": "Mit Händler B sprechen"
  },
  {
    "aktion_id": "kaufe_item",
    "ziel_id": "wurststand_id",
    "voraussetzung": "inventar.geld > 5",
    "beschreibung": "Eine Wurst kaufen"
  },
  {
    "aktion_id": "gehe_zu",
    "ziel_id": "taverne_koordinaten",
    "beschreibung": "Zur Taverne gehen"
  },
  {
    "aktion_id": "verhafte_person",
    "voraussetzung": "hierarchie.rang > 'Rekrut'",
    "beschreibung": "Jemanden verhaften"
  }
]

Der Planungs-Agent in der Traumphase wählt dann aus diesen möglichen Aktionen aus, um einen konkreten und ausführbaren Plan für das Tages-Skript zu erstellen.

