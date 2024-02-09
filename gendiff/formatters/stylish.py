import itertools

INDENT = 4


def make_start_indent(depth):
    return ' ' * (depth * INDENT - 2)


def make_end_indent(depth):
    return ' ' * ((depth - 1) * INDENT)


def to_string(current_value, spaces=INDENT):
    def walk(elem, depth):
        if isinstance(elem, bool):
            return str(elem).lower()
        elif elem is None:
            return 'null'
        elif isinstance(elem, dict):
            deep_indent_size = depth + spaces
            deep_indent = ' ' * deep_indent_size
            current_indent = ' ' * depth
            lines = []
            for k, v in elem.items():
                lines.append(f'{deep_indent}{k}: {walk(v, deep_indent_size)}')
            result = itertools.chain('{', lines, [current_indent + '}'])
            return '\n'.join(result)
        return str(elem)
    return walk(current_value, INDENT)


def to_stylish(diff, depth=1):
    lines = []
    start_indent = make_start_indent(depth)
    end_indent = make_end_indent(depth)
    for item in diff:
        key = item.get('key')
        value = item.get('val')
        status = item.get('status')

        if status == 'nested':
            children = item.get('children')
            lines.append(
                f'{start_indent}  {key}: {to_stylish(children, depth + 1)}'
            )
        elif status == 'deleted':
            lines.append(
                f'{start_indent}- {key}: {to_string(value, depth * INDENT)}'
            )
        elif status == 'added':
            lines.append(
                f'{start_indent}+ {key}: {to_string(value, depth * INDENT)}'
            )
        elif status == 'unchanged':
            lines.append(
                f'{start_indent}  {key}: {to_string(value, depth * INDENT)}'
            )
    result = '\n'.join(lines)
    return '{\n' + result + f'\n{end_indent}' + '}'
