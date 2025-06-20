# extractor.py
import google.generativeai as genai
import json
import argparse
import pathlib
from typing import List, Dict, Set
from config import GEMINI_API_KEY

def load_prompt_template(file_path: pathlib.Path) -> str:
    """Lädt die Prompt-Vorlage aus einer Textdatei."""
    try:
        return file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"!! Fehler: Prompt-Datei nicht gefunden unter {file_path}")
        exit() # Beendet das Skript, wenn der Prompt fehlt

def get_characters_from_book(book_title: str, prompt_template: str, model) -> List[str]:
    """Sendet einen Prompt an die Gemini API, um die Charaktere aus einem Buch zu extrahieren."""
    print(f"Analysiere Roman: {book_title}...")
    prompt = prompt_template.format(book_title=book_title)
    
    try:
        response = model.generate_content(prompt)
        # Robuste Bereinigung der Antwort, um häufige LLM-Formatierungsfehler zu beheben
        cleaned_response = response.text.strip()
        if cleaned_response.startswith("```json"):
            cleaned_response = cleaned_response[7:]
        elif cleaned_response.startswith("```"):
            cleaned_response = cleaned_response[3:]
        
        if cleaned_response.endswith("```"):
            cleaned_response = cleaned_response[:-3]
        
        return json.loads(cleaned_response)
    except (json.JSONDecodeError, Exception) as e:
        print(f"!! Fehler bei der Analyse von '{book_title}': {e}")
        print(f"!! Erhaltene Antwort: {response.text}")
        return []

def main(args):
    """Hauptfunktion: Orchestriert den gesamten Extraktionsprozess."""
    # Konfiguriere API und Modell
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(args.model_name)

    # Lade Konfigurationsdateien
    prompt_template = load_prompt_template(args.prompt_file)
    try:
        with args.input_file.open('r', encoding='utf-8') as f:
            novel_list = json.load(f).get("novels", [])
            if not novel_list:
                raise ValueError("Die JSON-Datei enthält keinen 'novels'-Schlüssel oder die Liste ist leer.")
    except FileNotFoundError:
        print(f"!! Fehler: Eingabedatei '{args.input_file}' wurde nicht gefunden.")
        return
    except (json.JSONDecodeError, ValueError) as e:
        print(f"!! Fehler beim Lesen der Eingabedatei '{args.input_file}': {e}")
        return

    # Datenverarbeitung
    character_appearances: Dict[str, List[str]] = {}
    
    print("Starte den Literarischen Extraktor...")
    for book in novel_list:
        chars_in_book = get_characters_from_book(book, prompt_template, model)
        for char in chars_in_book:
            char_normalized = char.strip() # Normalisiere den Namen
            if char_normalized not in character_appearances:
                character_appearances[char_normalized] = []
            character_appearances[char_normalized].append(book)
        print(f"-> {len(chars_in_book)} Charaktere aus '{book}' verarbeitet.")
        print("-" * 30)

    # Finale Datenstruktur aufbereiten
    sorted_characters = sorted(character_appearances.keys())
    output_data = {
        "metadata": {
            "total_unique_characters": len(sorted_characters),
            "processed_novels": len(novel_list)
        },
        "character_master_list": sorted_characters,
        "appearances_by_character": character_appearances
    }

    # Sicherstellen, dass der output-Ordner existiert
    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Ergebnisse speichern
    print(f"Extraktion abgeschlossen. Speichere Manifest in {args.output_file}")
    with args.output_file.open('w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print("Prozess erfolgreich beendet.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrahiert Scheibenwelt-Charaktere aus Romanen via Gemini API.")
    parser.add_argument(
        "--input-file", 
        type=pathlib.Path, 
        default=pathlib.Path("input/novels.json"), 
        help="Pfad zur JSON-Datei mit der Romanliste."
    )
    parser.add_argument(
        "--prompt-file", 
        type=pathlib.Path, 
        default=pathlib.Path("prompts/extractor_prompt.txt"), 
        help="Pfad zur Textdatei mit der Prompt-Vorlage."
    )
    parser.add_argument(
        "--output-file", 
        type=pathlib.Path, 
        default=pathlib.Path("output/character_manifest.json"), 
        help="Pfad zur Ausgabe-JSON-Datei."
    )
    parser.add_argument(
        "--model-name", 
        type=str, 
        default="gemini-1.5-pro-latest", 
        help="Name des zu verwendenden Gemini-Modells."
    )
    
    args = parser.parse_args()
    main(args)
