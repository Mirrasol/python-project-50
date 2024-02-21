import os


def get_file_format(file_path):
    head, file_name = os.path.split(file_path)
    return file_name.split('.')[1]


def get_data(file_path):
    """Get data from the specified file."""
    with open(file_path, 'r') as file:
        result = file.read().strip('\n')
        return result
