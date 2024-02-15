from gendiff.parser import get_data
from gendiff.diff_maker import make_diff_tree
from gendiff.formatter import apply_format


def generate_diff(file1_path, file2_path, formatter='stylish'):
    """Calculate the difference between two files in a preferred format."""
    dict1 = get_data(file1_path)
    dict2 = get_data(file2_path)
    diff = make_diff_tree(dict1, dict2)
    return apply_format(diff, formatter)
