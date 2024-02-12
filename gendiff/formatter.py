from gendiff.formats.stylish import to_stylish
from gendiff.formats.plain import to_plain


def to_format(diff, formatter='stylish'):
    if formatter == 'stylish':
        return to_stylish(diff)
    elif formatter == 'plain':
        return to_plain(diff)
