import sys
import os
import json

def load_list(list_file = 'list.json'):
    """
    Load shopping list from JSON file. If the file does not exist, return an empty list.
    """
    if not os.path.exists(list_file):
        return []
    with open(list_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_list(items_list, list_file = 'list.json'):
    """
    Save shopping list in JSON file.
    """
    with open(list_file, 'w', encoding='utf=8') as f:
        json.dump(items_list, f, indent=2, ensure_ascii=False)

