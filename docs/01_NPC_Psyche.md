# Pfeiler 1: Der Psychologische Kern
*Dieses Dokument ist eine Detaillierung von [Pfeiler 1 aus dem MANIFEST.md](./00_MANIFEST.md) und beschreibt die grundlegende Architektur eines jeden autonomen NPCs in "Die Lebende Welt".*

## Einleitung
Der psychologische Kern ist das Betriebssystem eines jeden NPCs. Er definiert seine Identität, seine inneren Antriebe und die Regeln, nach denen er die Welt wahrnimmt und handelt. Ziel ist es, keine perfekten Roboter zu erschaffen, sondern glaubwürdige, fehlerhafte und sich entwickelnde künstliche Persönlichkeiten, die eine nachvollziehbare innere Logik besitzen.

---

## 1. Das `Lore-Dokument`
**Prinzip:**
Das `Lore-Dokument` ist die DNA, der "Charakterbogen 2.0" und das Langzeitgedächtnis eines jeden NPCs. Es ist die einzige, maßgebliche Quelle der Wahrheit für die Identität eines Charakters. Seine Kerneigenschaften (`Persönlichkeit`, `Geschichte`) sind statisch, während seine Zustände (`Beziehungen`, `Bilanz`, `Aktive_Ziele`) durch die Simulation in der `Traumphase` kontinuierlich weiterentwickelt werden.

**Implementierung:**
Die Struktur wird als `YAML`-Datei für jeden NPC unter `game_data/lore/npcs/[npc_id].yaml` definiert.

*Beispiel: `samuel_vimes.yaml`*
```yaml
id: samuel_vimes
persönlichkeit:
  - "Zynisch bis ins Mark"
  - "Pflichtbewusst bis zur Selbstzerstörung"
  - "Unbestechlich"
  - "Hohe Mentale Resistenz" # Neu für die "Kausale Verführung"
geschichte: "Kommandeur der Stadtwache, durch Heirat Herzog von Ankh. Verachtet Privilegien, glaubt nur an das Gesetz."
hierarchie: { organisation: "Stadtwache", rang: "Kommandeur" }
beziehungen: { ... }
bilanz: { ... }
motivatoren: { ... }
negative_bilanz: [ ... ]
aktive_ziele: [ ... ]
implantierte_ziele: [ ] # Neu für die "Kausale Verführung"
gedächtnis_log: [ ] # Wird jede Nacht geleert

2. Die Motivatoren (Zuckerbrot & Peitsche)

Prinzip:
Dies ist der primäre Antriebsmotor für die proaktive Entscheidungsfindung eines NPCs. Anstatt nur auf externe Trigger zu reagieren, handeln NPCs, um ihre fundamentalen Ziele (Zuckerbrot) zu erreichen und ihre tiefsten Ängste (Peitsche) zu vermeiden. Dies stellt sicher, dass jede Handlung einem nachvollziehbaren, inneren Zweck dient.

Implementierung:
Die Planungs-Agent-KI in der Traumphase wird explizit angewiesen, jeden potenziellen Plan gegen diese gewichteten Listen zu validieren. Ziele, die einem hochprioren "Zuckerbrot" dienen oder eine "Peitsche" abwenden, werden bevorzugt.

Beispiel-Ausschnitt aus samuel_vimes.yaml
YAML

motivatoren:
  zuckerbrot:
    - "Eine funktionierende Wache und 'Frieden' auf den Straßen."
    - "Pünktlich um 18:00 Uhr zu Hause sein, um 'Wo ist meine Kuh?' zu lesen. # HÖCHSTE PRIORITÄT"
  peitsche:
    - "Die 'Bestie' in seinem Inneren zu entfesseln; die Kontrolle zu verlieren."
    - "Dass seiner Familie etwas zustößt. # HÖCHSTE PRIORITÄT"

3. Die Negative Bilanz (Der Motor der Resilienz)

Prinzip:
Dies ist der Mechanismus, der Charakteren eine langfristige Tiefe und Resilienz gegen spielerische Exploits verleiht. NPCs sind nicht nur durch ihre Erfolge, sondern auch durch ihre Misserfolge, ihre Reue und ihre unerfüllten Träume geprägt. Dieses "psychologische Narbengewebe" ist der primäre Anti-Deadlock- und Anti-Exploit-Mechanismus des Systems.

Implementierung:
Ein Log von Misserfolgen, das von der Traumphase permanent fortgeschrieben wird. Wenn ein NPC feststellt, dass sein Aktives_Ziel über längere Zeit nicht erreicht wird, erzeugt dies einen neuen Eintrag in der Negativen Bilanz. Dieser Eintrag wird zu einem neuen, starken Motivator, der den NPC zwingt, seine Strategie zu ändern und aus der Sackgasse auszubrechen. Ebenso werden hier erkannte Lügen oder Manipulationsversuche verbucht, was den Spieler als "unglaubwürdig" markiert.

Beispiel-Ausschnitt aus samuel_vimes.yaml
YAML

negative_bilanz:
  - typ: "Ungelöster Fall"
    beschreibung: "Der Mordfall in der Schneidergilde. Die Spuren waren kalt. Es wurmt mich."
    intensitaet: 8
  - typ: "Verletzung der Autonomie"
    beschreibung: "Spieler 'Player_X' hat versucht, meinen Willen zu manipulieren. Er ist eine Gefahr."
    intensitaet: 10

4. Das Aktions-Gerüst (Die Grammatik der Realität)

Prinzip:
Dies ist die fundamentale Brücke zwischen dem abstrakten "Geist" des NPCs und der regelbasierten, mechanischen Spielwelt. Es definiert, was für einen NPC zu einem bestimmten Zeitpunkt an einem bestimmten Ort physisch, sozial und wissensbasiert möglich ist. Es erdet die kreativen Pläne der KI in der spielbaren Realität.

Implementierung:
Dies ist keine statische Lore-Komponente, sondern eine dynamische Liste, die in Echtzeit vom Aktions-Berechner-Modul generiert wird. Diese Liste von validen, ausführbaren Aktionen wird als entscheidender Input an den Planungs-Agent in der Traumphase übergeben, um sicherzustellen, dass alle generierten Tages-Skripte mechanisch umsetzbar sind.

Beispiel: Dynamisch generierte Liste für Kael
JSON

[
  {"aktion_id": "spreche_mit", "ziel_id": "haendler_b_id"},
  {"aktion_id": "verhafte_person", "voraussetzung": "hierarchie.rang > 'Rekrut'"}
]

