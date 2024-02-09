from gendiff.parser import get_data


def generate_diff(file1_path, file2_path):
    dict1 = get_data(file1_path)
    dict2 = get_data(file2_path)
    diff = make_diff_tree(dict1, dict2)
    return diff


def make_diff_tree(dict1, dict2):
    diff = []
    for key in sorted(dict1.keys() | dict2.keys()):
        if key not in dict2.keys():
            diff.append({'status': 'deleted', 'key': key, 'val': dict1[key]})
        elif key not in dict1.keys():
            diff.append({'status': 'added', 'key': key, 'val': dict2[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff.append({'status': 'nested', 'key': key, 'children': make_diff_tree(dict1[key], dict2[key])})
        elif dict1[key] == dict2[key]:
            diff.append({'status': 'unchanged', 'key': key, 'val': dict1[key]})
        elif dict1[key] != dict2[key]:
            diff.append({'status': 'deleted', 'key': key, 'val': dict1[key]})
            diff.append({'status': 'added', 'key': key, 'val': dict2[key]})
    return diff
