import os
import json
import yaml


def get_extension(file_path):
    head, file_name = os.path.split(file_path)
    return file_name.split('.')[1]


def get_data(file):
    """Get data from the specified file."""
    extension = get_extension(file)
    if extension == 'json':
        with open(file, 'r') as file:
            return json.load(file)
    elif extension in ('yml', 'yaml'):
        with open(file, 'r') as file:
            return yaml.safe_load(file)
    return "Unsupported file format."
