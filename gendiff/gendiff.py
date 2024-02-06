from gendiff.parser import get_data


def to_string(dct):
    result = '{\n'
    for k, v in dct.items():
        if v[0] == ' ':
            result += f' + {k}: {v[1]}\n'
        elif v[1] == ' ':
            result += f' - {k}: {v[0]}\n'
        elif v[0] == v[1]:
            result += f'   {k}: {v[0]}\n'
        else:
            result += f' - {k}: {v[0]}\n'
            result += f' + {k}: {v[1]}\n'
    return result + '}'


def to_plain(dct):
    for v in dct.values():
        if isinstance(v[0], bool):
            v[0] = str(v[0]).lower()
        elif isinstance(v[1], bool):
            v[1] = str(v[1]).lower()
        elif v[0] is None:
            v[0] = 'null'
        elif v[1] is None:
            v[1] = 'null'
    return dct


def generate_diff(file1_path, file2_path):
    dict1 = get_data(file1_path)
    dict2 = get_data(file2_path)
    dict3 = {}
    for k in sorted(dict1.keys() | dict2.keys()):
        if k in dict1 and k in dict2:
            dict3[k] = [dict1[k], dict2[k]]
        elif k in dict1 and k not in dict2:
            dict3[k] = [dict1[k], ' ']
        else:
            dict3[k] = [' ', dict2[k]]
    result = to_plain(dict3)
    return to_string(result)
