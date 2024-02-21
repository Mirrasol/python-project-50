from gendiff.reader import get_data, get_extension
from gendiff.parser import parse_data
from gendiff.diff_maker import make_diff_tree
from gendiff.formatter import apply_format


def generate_diff(file1_path, file2_path, formatter='stylish'):
    """Generate the difference between two files in a specified format."""
    data1, file1_format = get_data(file1_path), get_extension(file1_path)
    data2, file2_format = get_data(file2_path), get_extension(file2_path)
    dict1 = parse_data(data1, file1_format)
    dict2 = parse_data(data2, file2_format)
    diff = make_diff_tree(dict1, dict2)
    return apply_format(diff, formatter)
