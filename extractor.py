# extractor.py
import google.generativeai as genai
import json
import argparse
import pathlib
from typing import List, Dict, Set
from config import GEMINI_API_KEY

# --- Globale Konfiguration ---
# Es ist eine bewährte Methode, die API global zu konfigurieren, 
# sobald die Bibliothek importiert wird.
try:
    genai.configure(api_key=GEMINI_API_KEY)
except AttributeError:
    print("!! Fehler: Stellen Sie sicher, dass die 'google-generativeai'-Bibliothek aktuell ist.")
    print("!! Führen Sie aus: pip install --upgrade google-generativeai")
    exit()

def load_prompt_template(file_path: pathlib.Path) -> str:
    """Lädt die Prompt-Vorlage aus einer Textdatei."""
    try:
        return file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"!! Fehler: Prompt-Datei nicht gefunden unter {file_path}")
        exit()

def load_novel_list(file_path: pathlib.Path) -> List[str]:
    """Lädt die Romanliste aus einer JSON-Datei."""
    try:
        with file_path.open('r', encoding='utf-8') as f:
            data = json.load(f)
            novel_list = data.get("novels", [])
            if not novel_list:
                raise ValueError("Die JSON-Datei enthält keinen 'novels'-Schlüssel oder die Liste ist leer.")
            return novel_list
    except FileNotFoundError:
        print(f"!! Fehler: Eingabedatei '{file_path}' wurde nicht gefunden.")
        exit()
    except (json.JSONDecodeError, ValueError) as e:
        print(f"!! Fehler beim Lesen der Eingabedatei '{file_path}': {e}")
        exit()

def get_characters_from_book(book_title: str, prompt_template: str, model) -> List[str]:
    """Sendet einen Prompt an die Gemini API, um die Charaktere aus einem Buch zu extrahieren."""
    print(f"Analysiere Roman: {book_title}...")
    prompt = prompt_template.format(book_title=book_title)
    
    try:
        response = model.generate_content(prompt)
        cleaned_response = response.text.strip()
        # Robuste Bereinigung für JSON, das in Markdown-Blöcken eingeschlossen ist
        if cleaned_response.startswith("```json"):
            cleaned_response = cleaned_response[7:].strip()
            if cleaned_response.endswith("```"):
                cleaned_response = cleaned_response[:-3].strip()
        
        return json.loads(cleaned_response)
    except (json.JSONDecodeError, Exception) as e:
        print(f"!! Fehler bei der Analyse von '{book_title}': {e}")
        print(f"!! Erhaltene Antwort (Auszug): {response.text[:200]}")
        return []

def save_output_to_json(data: Dict, file_path: pathlib.Path):
    """Speichert die Ausgabedaten in einer JSON-Datei."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Prozess erfolgreich beendet. Manifest gespeichert in {file_path}")
    except IOError as e:
        print(f"!! Fehler beim Speichern der Ausgabedatei: {e}")

def main(args):
    """Hauptfunktion: Orchestriert den gesamten Extraktionsprozess."""
    print("Initialisiere Gemini-Modell...")
    model = genai.GenerativeModel(args.model_name)

    print("Lade Konfigurationsdateien...")
    prompt_template = load_prompt_template(args.prompt_file)
    novel_list = load_novel_list(args.input_file)

    character_appearances: Dict[str, List[str]] = {}
    
    print("Starte den Literarischen Extraktor...")
    for book in novel_list:
        chars_in_book = get_characters_from_book(book, prompt_template, model)
        for char in chars_in_book:
            char_normalized = char.strip()
            if char_normalized: # Ignoriere leere Strings
                if char_normalized not in character_appearances:
                    character_appearances[char_normalized] = []
                character_appearances[char_normalized].append(book)
        print(f"-> {len(chars_in_book)} Charaktere aus '{book}' verarbeitet.")
        print("-" * 30)

    sorted_characters = sorted(character_appearances.keys())
    output_data = {
        "metadata": {
            "total_unique_characters": len(sorted_characters),
            "processed_novels": len(novel_list),
            "model_used": args.model_name
        },
        "character_master_list": sorted_characters,
        "appearances_by_character": character_appearances
    }

    save_output_to_json(output_data, args.output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrahiert Scheibenwelt-Charaktere aus Romanen via Gemini API.")
    # Argumente bleiben dieselben wie zuvor
    parser.add_argument("--input-file", type=pathlib.Path, default=pathlib.Path("input/novels.json"))
    parser.add_argument("--prompt-file", type=pathlib.Path, default=pathlib.Path("prompts/extractor_prompt.txt"))
    parser.add_argument("--output-file", type=pathlib.Path, default=pathlib.Path("output/character_manifest.json"))
    parser.add_argument("--model-name", type=str, default="gemini-1.5-pro-latest")
    
    args = parser.parse_args()
    main(args)
