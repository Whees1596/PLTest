import json


def load_config() -> dict:
    with open('config.json', 'r', encoding='utf-8') as file:
        return json.load(file)


CONFIG = load_config()
