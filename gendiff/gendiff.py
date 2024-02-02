import json


def get_data(file):
    with open(file) as file:
        return json.load(file)


def to_format(dct):
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


def generate_diff(file1_path, file2_path):
    dict1 = get_data(file1_path)
    dict2 = get_data(file2_path)
    dict3 = {}
    for k in sorted(dict1.keys()|dict2.keys()):
        if k in dict1 and k in dict2:
            dict3[k] = [dict1[k], dict2[k]]
        elif k in dict1 and k not in dict2:
            dict3[k] = [dict1[k], ' ']
        else:
            dict3[k] = [' ', dict2[k]]
    for v in dict3.values():
        if v[0] is False:
            v[0] = 'false'
        if v[0] is True:
            v[0] = 'true'
        if v[1] is False:
            v[1] = 'false'
        if v[1] is True:
            v[1] = 'true'
    return to_format(dict3)
