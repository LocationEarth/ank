Pfeiler 3: Die Soziale Simulation

Dieses Dokument (docs/03_Soziale_Dynamik.md) ist eine Detaillierung von Pfeiler 3 aus dem MANIFEST.md und beschreibt die Mechanismen, durch die aus autonomen Individuen eine vernetzte, reaktive und sich selbst organisierende Gesellschaft entsteht.
Einleitung

Dieser Pfeiler beschreibt das "Wir" der Spielwelt. Während die ersten beiden Pfeiler den einzelnen NPC als denkendes und lernendes Individuum definieren, legt dieser Pfeiler die Regeln und Systeme fest, die das soziale Gefüge, die öffentlichen Meinungen und die Machtdynamiken zwischen den NPCs steuern. Hier entstehen Reputation, Gerüchte und Politik aus den Interaktionen der Charaktere.
1. Die Soziale Bilanz (Die Währung der Gesellschaft)

Prinzip (High-Level):
Die Soziale Bilanz ist ein quantifizierbares Maß für den Stand und den Ruf eines Akteurs (NPC oder Spieler) innerhalb der Gemeinschaft. Sie ist der Motor für soziale Konsequenzen und bestimmt, wie Individuen von der Gemeinschaft wahrgenommen und behandelt werden. Es ist ein mehrdimensionales System für soziales Kapital, das über eine einfache "Reputationsleiste" hinausgeht.

Implementierung (Datenstruktur & Prozess):
Die Soziale Bilanz ist ein zentrales Objekt im Lore-Dokument. Sie wird in der Traumphase durch den Event-Prozessor basierend auf den protokollierten Ereignissen des Tages dynamisch aktualisiert.

Beispiel: Auszug aus der Lore von Kommandeur Mumm.
YAML

bilanz:
  reputation_allgemein: 75 # "Ein harter, aber gerechter Hund."
  glaubwuerdigkeit: 85 # Was er sagt, hat Gewicht.
  einfluss_wache: 95
  status: "Bekannter Realitäts-Manipulator" # Optional; nach Aufdeckung der "Kausalen Verführung"

beziehungen:
  # Die 'Soziale Bilanz' mit spezifischen Personen
  "Lord Vetinari": { typ: "Vorgesetzter/Gegenspieler", vertrauen: 2, respekt: 8, furcht: 9 }
  "Spieler_X": { typ: "Informant/Problemkind", vertrauen: 1, respekt: 3, furcht: 7 } # Vertrauen durch Manipulation zerstört

    Update-Mechanismus: Die Traumphase analysiert Ereignisse. IF Spieler erfüllt Quest für die Wache -> THEN Mumm.beziehungen.Spieler.respekt += 5. IF Spieler wird bei der Anwendung der "Kausalen Verführung" aufgedeckt -> THEN Mumm.beziehungen.Spieler.vertrauen = 0, Mumm.beziehungen.Spieler.furcht = 7, Spieler.bilanz.status = "Bekannter Realitäts-Manipulator".
    Auswirkung: Die Aktionen anderer NPCs werden direkt von diesen Werten beeinflusst. Ein Händler wird einem Spieler mit niedrigem Vertrauen keinen Kredit gewähren. Ein Wächter wird einem Spieler mit hohem Respekt eher eine heikle Information anvertrauen.

2. Der Soziale-Dynamik-Filter (Die ungeschriebenen Gesetze)

Prinzip (High-Level):
Dieses Modul übersetzt die harten Zahlen der Sozialen Bilanz in die weichen, subtilen Nuancen menschlicher Kommunikation. Es simuliert die soziale Etikette und stellt sicher, dass eine Interaktion nicht nur inhaltlich logisch, sondern auch formal und emotional dem sozialen Kontext entspricht. Es ist der Grund, warum ein Bittsteller demütig und ein Kommandeur befehlend klingt.

Implementierung (Prozess & Parameter):
Der Filter ist ein Service, der vom Konversations-Orchestrator vor jeder sichtbaren NPC-Interaktion aufgerufen wird.

    Der Filter analysiert die Hierarchie- und Beziehungs-Daten der beteiligten Akteure.
    Er gibt ein Set von "Konversations-Parametern" an den Skript-Interpreter oder den Generativen Dialog-Agent zurück.

Parameter-Beispiele:

    duration: [short, medium, long]
    formality: [casual, formal, strict]
    content_tags: [gossip, command, personal, business, plea]
    emotional_tone: [friendly, neutral, tense, hostile]

Beispiel: Der Rekrut Joric meldet sich bei Wächter Kael. Der Filter analysiert die massive Hierarchielücke und gibt zurück: [duration: short, formality: strict, content_tags: [report], emotional_tone: neutral]. Das Ergebnis ist ein kurzes, prägnantes, aufgabenorientiertes Gespräch.
3. Die Narrative Konsolidierung (Das kollektive Gedächtnis)

Prinzip (High-Level):
Dies ist der Mechanismus der Gesellschaft, um mit Ambiguität und Informationslücken umzugehen. Anstatt ein Mysterium für immer ungelöst zu lassen, bildet die Gemeinschaft durch einen Prozess aus Gerüchten, Angst und offiziellen Verlautbarungen eine neue, vereinfachte "Gemeinschafts-Wahrheit". Dieser Prozess heilt narrative Brüche in der Welt und kann zu emergenten sozialen Phänomenen wie Massenhysterie oder der Schaffung von Legenden führen.

Implementierung (Sub-Prozess der Traumphase):
Dieser rechenintensive Prozess wird seltener ausgelöst, typischerweise nach wichtigen, ungelösten Weltereignissen.

    Sammeln: Die KI sammelt alle Gedächtnis_Logs zum relevanten Thema von allen NPCs einer Region.
    Gewichten: Jede Aussage wird basierend auf der glaubwuerdigkeit und dem einfluss des Sprechers gewichtet.
    Synthetisieren: Die KI erhält den Auftrag, aus den gewichteten, oft widersprüchlichen Aussagen eine einzige, plausible und narrativ befriedigende "offizielle Geschichte" zu formen.
    Verankern: Diese neue "Gemeinschafts-Wahrheit" wird als fester Lore-Eintrag ("Was jeder weiß") in das Gedächtnis vieler NPCs geschrieben.

Beispiel: "Die Entstehung einer Hexenjagd". Einzelne, isolierte Berichte über seltsames Verhalten von NPCs (die durch "Kausale Verführung" manipuliert wurden) werden vom System gesammelt. Die Narrative Konsolidierung synthetisiert daraus die Gemeinschafts-Wahrheit: "Es gibt 'Gedanken-Diebe' unter uns! Sie stehlen den Willen der Bürger." Dies führt zu einer emergenten, paranoia-getriebenen Questreihe, in der die Gemeinschaft versucht, die Manipulatoren (die Spieler der Gilde) zu finden und zu bestrafen.
