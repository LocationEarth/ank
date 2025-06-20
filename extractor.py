# extractor.py
import google.generativeai as genai
import json
from typing import List, Dict, Set
from config import GEMINI_API_KEY

# Konfiguration des Gemini-Modells
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest') # Ein leistungsstarkes Modell für Analyse

# --- Konstanten ---
# Eine verkürzte, chronologische Liste für diesen Test. Kann beliebig erweitert werden.
NOVEL_LIST: List[str] = [
    "Wachen! Wachen! (Guards! Guards!)",
    "Helle Barden (Men at Arms)",
    "Hohle Worte (Feet of Clay)",
    "Klonk! (Thud!)"
]

# Der Prompt, der die KI anleitet.
EXTRACTOR_PROMPT_TEMPLATE: str = (
    "Du bist ein Experte für Terry Pratchetts Scheibenwelt mit enzyklopädischem Wissen. "
    "Analysiere den Roman '{book_title}'. Deine Aufgabe ist es, eine Liste der Haupt- und "
    "wichtigsten wiederkehrenden Nebencharaktere zu extrahieren, die in diesem spezifischen Roman "
    "eine signifikante, handlungstragende Rolle spielen. "
    "Gib das Ergebnis ausschließlich als valides JSON-Array von Strings aus, z.B. [\"Charakter A\", \"Charakter B\"]."
)

def get_characters_from_book(book_title: str) -> List[str]:
    """
    Sendet einen Prompt an die Gemini API, um die Charaktere aus einem Buch zu extrahieren.
    """
    print(f"Analysiere Roman: {book_title}...")
    prompt = EXTRACTOR_PROMPT_TEMPLATE.format(book_title=book_title)
    
    try:
        response = model.generate_content(prompt)
        # Bereinigen der Antwort, um sicherzustellen, dass es valides JSON ist
        cleaned_response = response.text.strip().replace("`", "")
        if cleaned_response.startswith("json"):
             cleaned_response = cleaned_response[4:].strip()

        characters = json.loads(cleaned_response)
        print(f"-> Gefundene Charaktere: {', '.join(characters)}")
        return characters
    except (json.JSONDecodeError, Exception) as e:
        print(f"!! Fehler bei der Analyse von '{book_title}': {e}")
        return []

def main():
    """
    Hauptfunktion: Iteriert durch die Buchliste, sammelt Charaktere und speichert das Ergebnis.
    """
    # Ein Dictionary, um zu speichern, in welchen Büchern ein Charakter vorkommt.
    character_appearances: Dict[str, List[str]] = {}
    # Ein Set für die schnelle, de-duplizierte Sammlung aller Charakternamen.
    all_unique_characters: Set[str] = set()

    print("Starte den Literarischen Extraktor...")
    for book in NOVEL_LIST:
        chars_in_book = get_characters_from_book(book)
        all_unique_characters.update(chars_in_book)
        
        for char in chars_in_book:
            if char not in character_appearances:
                character_appearances[char] = []
            character_appearances[char].append(book)
        print("-" * 20)

    # Sortieren für eine saubere Ausgabe
    sorted_characters = sorted(list(all_unique_characters))
    
    # Erstellen der finalen Datenstruktur
    output_data = {
        "total_unique_characters": len(sorted_characters),
        "character_master_list": sorted_characters,
        "appearances_by_character": character_appearances
    }

    # Speichern der Ergebnisse in einer JSON-Datei
    output_path = "output/character_manifest.json"
    print(f"Extraktion abgeschlossen. Speichere {len(sorted_characters)} einzigartige Charaktere in {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print("Prozess beendet.")

if __name__ == "__main__":
    main()
