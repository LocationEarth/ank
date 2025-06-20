Pfeiler 3: Die Soziale Simulation

Dieses Dokument (docs/03_Soziale_Dynamik.md) ist eine Detaillierung von Pfeiler 3 aus dem MANIFEST.md und beschreibt die Mechanismen, durch die aus autonomen Individuen eine vernetzte, reaktive und sich selbst organisierende Gesellschaft entsteht.
Einleitung

Während Pfeiler 1 und 2 den einzelnen NPC als denkendes und lernendes Individuum definieren, beschreibt dieser Pfeiler das "Wir" der Spielwelt. Er legt die Regeln und Systeme fest, die das soziale Gefüge, die öffentlichen Meinungen und die Machtdynamiken zwischen den NPCs steuern. Dies ist die Ebene, auf der Politik, Gerüchte und Reputation entstehen.
1. Die Soziale Bilanz (Die Währung der Gesellschaft)

Prinzip (High-Level):
Die Soziale Bilanz ist ein quantifizierbares Maß für den Stand und den Ruf eines NPCs innerhalb seiner Gemeinschaft. Sie geht über einen einfachen "Reputations-Score" hinaus und erfasst multiple Facetten wie Vertrauen, Respekt, Furcht und Glaubwürdigkeit. Diese Bilanz ist die primäre Datenquelle, die ein NPC-Gehirn heranzieht, um zu entscheiden, wie es einen anderen NPC oder den Spieler behandeln soll. Sie ist die Währung, mit der sozialer Einfluss gehandelt wird.

Implementierung (Datenstruktur & Prozess):
Die Soziale Bilanz ist ein zentrales Objekt im Lore-Dokument eines jeden NPCs. Sie wird in der Traumphase durch den Event-Prozessor basierend auf den Ereignissen des Tages dynamisch aktualisiert.

Beispiel: Auszug aus der Lore von Kommandeur Mumm.
YAML

bilanz:
  reputation_allgemein: 75 # "Ein harter, aber gerechter Hund."
  glaubwuerdigkeit: 85 # Was er sagt, hat Gewicht.
  einfluss_wache: 95 # Sein Wort ist Gesetz in der Wache.
  einfluss_adel: 20 # Wird von den Adligen verachtet, aber gefürchtet.

beziehungen:
  # Die 'Soziale Bilanz' mit spezifischen Personen
  "Lord Vetinari": { typ: "Vorgesetzter/Gegenspieler", vertrauen: 2, respekt: 8, furcht: 3 }
  "Hauptmann Karotte": { typ: "Ziehsohn", vertrauen: 9, zuneigung: 9, furcht: 0 }

    Update-Mechanismus: IF Mumm löst einen wichtigen Fall -> THEN Mumm.bilanz.reputation_allgemein += 5. IF Spieler belügt Mumm und wird entlarvt -> THEN Mumm.beziehungen.Spieler.vertrauen -= 10.
    Auswirkung: Andere NPCs nutzen diese Werte. Ein Händler, dessen Vertrauen-Wert gegenüber dem Spieler auf 1/10 gesunken ist, wird ihm im Dialog automatisch höhere Preise anbieten oder bestimmte Waren gar nicht erst zeigen.

2. Der Soziale-Dynamik-Filter (Die ungeschriebenen Gesetze)

Prinzip (High-Level):
Dieses Modul übersetzt die harten Zahlen der Sozialen Bilanz in die weichen, subtilen Nuancen menschlicher Kommunikation. Es simuliert die soziale Etikette und stellt sicher, dass eine Interaktion nicht nur inhaltlich, sondern auch formal dem sozialen Kontext entspricht. Es ist der Grund, warum ein Rekrut anders mit seinem Hauptmann spricht als mit seinem besten Freund in der Taverne.

Implementierung (Prozess & Parameter):
Der Filter ist ein Service, der vom Konversations-Orchestrator vor jeder sichtbaren NPC-NPC-Interaktion ("Bühnen-Simulation") aufgerufen wird.

    Der Filter erhält die IDs der beiden interagierenden NPCs.
    Er analysiert deren Hierarchie- und Beziehungs-Daten aus der Lore.
    Er gibt ein Set von "Konversations-Parametern" zurück, die den Stil des Gesprächs vorgeben.

Parameter-Beispiele:

    duration: [short, medium, long]
    formality: [casual, formal, strict]
    content_tags: [gossip, command, personal, business, plea]
    emotional_tone: [friendly, neutral, tense, hostile]

Beispiel: Der junge Rekrut Joric (Rang: Rekrut) meldet sich bei Kael (Rang: Wächter). Der Filter gibt zurück: [duration: short, formality: strict, content_tags: [report, command], emotional_tone: neutral]. Das Ergebnis ist der kurze, knappe Dialog, den wir bereits entworfen haben.
3. Die Narrative Konsolidierung (Das kollektive Gedächtnis)

Prinzip (High-Level):
Dies ist der fortschrittlichste soziale Mechanismus. Er simuliert, wie eine Gesellschaft mit Ambiguität, ungelösten Rätseln und "losen Enden" umgeht. Anstatt ein Mysterium für immer ungelöst zu lassen, bildet die Gemeinschaft durch einen Prozess aus Gerüchten, offiziellen Verlautbarungen und kollektivem Wunschdenken eine neue, vereinfachte "Gemeinschafts-Wahrheit", auch wenn diese faktisch falsch sein mag.

Implementierung (Sub-Prozess der Traumphase):
Dies ist ein spezieller, seltener Prozess, der ausgelöst wird, wenn ein wichtiges Weltereignis über mehrere Tage ungelöst bleibt.

    Sammeln: Die KI sammelt alle Gedächtnis_Logs der relevanten NPCs zum Thema (z.B. "Das gestohlene Amulett").
    Gewichten: Jede Aussage wird basierend auf der Hierarchie und der bilanz.glaubwuerdigkeit des Sprechers gewichtet. Vetinaris Wort wiegt mehr als das von Nobby Nobbs.
    Synthetisieren: Die KI erhält den Auftrag, aus diesen gewichteten, oft widersprüchlichen Aussagen eine einzige, plausible und "befriedigende" Geschichte zu formen.
    Verankern: Diese neue "Gemeinschafts-Wahrheit" wird als fester Lore-Eintrag in das Gedächtnis von vielen NPCs (insbesondere denen ohne direkte Beteiligung) geschrieben.

Beispiel: Die widersprüchlichen Fakten zum Amulett-Diebstahl ("Rhys ist verhaftet", "Amulett ist immer noch weg", "Ich habe gehört, er hatte Komplizen") werden zur Gemeinschafts-Wahrheit: "Der Fremde Rhys hat das Amulett gestohlen und es an seine Bande weitergegeben, bevor Kommandeur Mumm ihn schnappen konnte." Dieses Narrativ löst alle Widersprüche auf und schließt den Fall für die Öffentlichkeit ab, wodurch die soziale Ordnung wiederhergestellt wird.
