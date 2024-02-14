def to_string(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, (dict, list)):
        return '[complex value]'
    elif value is None:
        return 'null'
    return str(value).lower()


def to_plain(diff, path=''):
    lines = []
    for item in diff:
        key = item.get('key')
        value = item.get('val')
        status = item.get('status')

        if status == 'nested':
            new_path = path + f'{key}.'
            children = item.get('children')
            lines.append(to_plain(children, new_path))
        elif status == 'changed':
            lines.append(f"Property '{path}{key}' was updated.\
 From {to_string(value[0])} to {to_string(value[1])}")
        elif status == 'deleted':
            lines.append(f"Property '{path}{key}'\
 was removed")
        elif status == 'added':
            lines.append(f"Property '{path}{key}' was added with\
 value: {to_string(value)}")
    result = '\n'.join(lines)
    return result
