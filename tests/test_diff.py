import pytest
from gendiff.gendiff import generate_diff


def read_expected(expected_path):
    with open(expected_path, 'r') as file:
        result = file.read().strip('\n')
        return result


@pytest.mark.parametrize('file1_path, file2_path, expected, formatter',
                         [
                             ('tests/fixtures/tree1.json', 'tests/fixtures/tree2.json', 'tests/fixtures/result_stylish.txt', 'stylish'),
                             ('tests/fixtures/tree1.yml', 'tests/fixtures/tree2.yml', 'tests/fixtures/result_stylish.txt', 'stylish'),
                             ('tests/fixtures/tree1.yml', 'tests/fixtures/tree2.yml', 'tests/fixtures/result_plain.txt', 'plain'),
                             ('tests/fixtures/tree1.json', 'tests/fixtures/tree2.json', 'tests/fixtures/result_json.json', 'json'),
                         ])
def test_generate_diff(file1_path, file2_path, expected, formatter):
    result = read_expected(expected)
    assert generate_diff(file1_path, file2_path, formatter) == result
