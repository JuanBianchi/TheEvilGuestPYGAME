import json
from constantes import JSON_CONFIG_PATH

def open_configs() -> dict:
    with open(JSON_CONFIG_PATH, 'r', encoding='utf-8') as config:
        return json.load(config)