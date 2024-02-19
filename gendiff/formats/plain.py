def to_string(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, (dict, list)):
        return '[complex value]'
    elif value is None:
        return 'null'
    return str(value).lower()


def to_plain(diff, path=''):
    """Apply 'plain' format."""
    lines = []
    for item in diff:
        key = item.get('key')
        value = item.get('val')
        node_type = item.get('type')

        if node_type == 'nested':
            new_path = path + f'{key}.'
            children = item.get('children')
            lines.append(to_plain(children, new_path))
        elif node_type == 'changed':
            lines.append(f"Property '{path}{key}' was updated.\
 From {to_string(value[0])} to {to_string(value[1])}")
        elif node_type == 'deleted':
            lines.append(f"Property '{path}{key}'\
 was removed")
        elif node_type == 'added':
            lines.append(f"Property '{path}{key}' was added with\
 value: {to_string(value)}")
    result = '\n'.join(lines)
    return result
