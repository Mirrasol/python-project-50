import argparse
import json
import yaml


def parse():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output'
    )
    return parser.parse_args()


def get_data(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as file:
            return json.load(file)
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path) as file:
            return yaml.load(file, Loader=yaml.FullLoader)
