import pytest
import json
from gendiff.gendiff import generate_diff


def test_generate_flat_json():
    with open('./tests/fixtures/result_stylish_flat.txt', 'r') as file_json:
        result = file_json.read().strip('\n')
        assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result


def test_generate_flat_yml():
    with open('./tests/fixtures/result_stylish_flat.txt', 'r') as file_yml:
        result = file_yml.read().strip('\n')
        assert generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml') == result


def test_generate_tree():
    with open('./tests/fixtures/result_stylish_tree.txt', 'r') as file_tree:
        result = file_tree.read().strip('\n')
        tree1 = './tests/fixtures/tree1.json'
        tree2 = './tests/fixtures/tree2.json'
        assert generate_diff(tree1, tree2) == result


def test_generate_plain():
    with open('./tests/fixtures/result_plain.txt', 'r') as file_plain:
        result = file_plain.read().strip('\n')
        tree1 = './tests/fixtures/tree1.yml'
        tree2 = './tests/fixtures/tree2.yml'
        assert generate_diff(tree1, tree2, 'plain') == result


def test_generate_json():
    with open('./tests/fixtures/result_json.json', 'r') as file_json:
        result = file_json.read().strip('\n')
        tree1 = './tests/fixtures/tree1.json'
        tree2 = './tests/fixtures/tree2.json'
        subject = generate_diff(tree1, tree2, 'json')
        assert subject == result
