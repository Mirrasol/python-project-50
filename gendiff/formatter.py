from gendiff.formats.stylish import to_stylish


def to_format(diff, formatter='stylish'):
    if formatter == 'stylish':
        return to_stylish(diff)
