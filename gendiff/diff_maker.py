def make_diff_tree(dict1, dict2):
    """Calculate the inner diff-structure."""
    diff = []
    for key in sorted(dict1.keys() | dict2.keys()):
        if key not in dict2.keys():
            diff.append({'status': 'deleted', 'key': key, 'val': dict1[key]})
        elif key not in dict1.keys():
            diff.append({'status': 'added', 'key': key, 'val': dict2[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff.append({
                'status': 'nested',
                'key': key,
                'children': make_diff_tree(dict1[key], dict2[key]),
            })
        elif dict1[key] == dict2[key]:
            diff.append({'status': 'unchanged', 'key': key, 'val': dict1[key]})
        elif dict1[key] != dict2[key]:
            diff.append({
                'status': 'changed',
                'key': key,
                'val': [dict1[key], dict2[key]],
            })
    return diff
