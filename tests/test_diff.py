import pytest
from gendiff.gendiff import generate_diff


def test_generate_json():
    with open('./tests/fixtures/result_stylish_flat.txt', 'r') as file3:
        result = file3.read().strip('\n')
        assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result


def test_generate_yml():
    with open('./tests/fixtures/result_stylish_flat.txt', 'r') as file3:
        result = file3.read().strip('\n')
        assert generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml') == result


def test_generate_tree():
    with open('./tests/fixtures/result_stylish_tree.txt', 'r') as file_tree:
        result = file_tree.read().strip('\n')
        tree1 = './tests/fixtures/tree1.json'
        tree2 = './tests/fixtures/tree2.json'
        assert generate_diff(tree1, tree2) == result
