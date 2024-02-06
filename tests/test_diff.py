import pytest
from gendiff.gendiff import generate_diff


def test_generate_json():
    with open('./tests/fixtures/result_plain.txt', 'r') as file3:
        result = file3.read().strip('\n')
        assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result


def test_generate_yml():
    with open('./tests/fixtures/result_plain.txt', 'r') as file3:
        result = file3.read().strip('\n')
        assert generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml') == result
