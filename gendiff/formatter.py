from gendiff.formats.stylish import to_stylish
from gendiff.formats.plain import to_plain
from gendiff.formats.json import to_json


def apply_format(diff, formatter='stylish'):
    if formatter == 'stylish':
        return to_stylish(diff)
    elif formatter == 'plain':
        return to_plain(diff)
    elif formatter == 'json':
        return to_json(diff)
