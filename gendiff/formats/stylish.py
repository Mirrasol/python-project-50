INDENT = 4


def make_start_indent(depth, spaces_count):
    return ' ' * (depth * spaces_count - 2)


def make_end_indent(depth, spaces_count):
    return ' ' * ((depth - 1) * spaces_count)


def to_string(value, depth=1, spaces_count=INDENT):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        current_indent = ' ' * spaces_count * depth
        end_indent = make_end_indent(depth, spaces_count)
        result = '{\n'
        for k, v in value.items():
            result += f'{current_indent}{k}:\
 {to_string(v, depth + 1, spaces_count)}\n'
        result += f'{end_indent}}}'
        return result
    return str(value)


def to_stylish(diff, depth=1):
    """Apply 'stylish' format."""
    lines = []
    start_indent = make_start_indent(depth, INDENT)
    end_indent = make_end_indent(depth, INDENT)
    for item in diff:
        key = item.get('key')
        value = item.get('val')
        status = item.get('status')

        if status == 'nested':
            children = item.get('children')
            lines.append(
                f'{start_indent}  {key}: {to_stylish(children, depth + 1)}'
            )
        elif status == 'changed':
            lines.append(f'{start_indent}- {key}:\
 {to_string(value[0], depth + 1, INDENT)}')
            lines.append(f'{start_indent}+ {key}:\
 {to_string(value[1], depth + 1, INDENT)}')
        elif status == 'deleted':
            lines.append(
                f'{start_indent}- {key}: {to_string(value, depth + 1, INDENT)}'
            )
        elif status == 'added':
            lines.append(
                f'{start_indent}+ {key}: {to_string(value, depth + 1, INDENT)}'
            )
        elif status == 'unchanged':
            lines.append(
                f'{start_indent}  {key}: {to_string(value, depth + 1, INDENT)}'
            )
    result = '\n'.join(lines)
    return '{\n' + result + f'\n{end_indent}' + '}'
