from pathlib import Path
import json
import os

PATHS_JSON_FILENAME = 'paths.json'

def find_file_pathlib(filename, search_path):
    for file in Path(search_path).rglob(filename):
        return str(file)
    return None

def check_json():
    if not os.path.exists(PATHS_JSON_FILENAME):
        with open(PATHS_JSON_FILENAME, 'w', encoding='utf8') as f:
            json.dump({},f)
    return

def file_add(filename, path='C:/'):
    if os.path.exists(PATHS_JSON_FILENAME):
        with open(PATHS_JSON_FILENAME, 'r', encoding='utf8') as f:
            try:
                paths = json.load(f)
            except Exception:
                paths = {}

    paths.update({f'{filename}': f'{find_file_pathlib(filename, path)}'})
    
    with open(PATHS_JSON_FILENAME, 'w', encoding='utf8') as file:
        json.dump(paths, file, ensure_ascii=False, indent=4)
    return 



