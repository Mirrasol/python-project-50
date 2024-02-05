import pytest
from gendiff.gendiff import generate_diff


def test_generate():
    with open('./tests/fixtures/result_json.txt', 'r') as file3:
        result = file3.read().strip('\n')
        assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result
