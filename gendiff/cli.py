import argparse


def parse_arguments():
    """Parse user arguments from the console."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        choices=['json', 'plain', 'stylish'],
        default='stylish',
        help='set format of output'
    )
    return parser.parse_args()
