import json
import yaml


def get_data(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as file:
            return json.load(file)
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path) as file:
            return yaml.safe_load(file)
