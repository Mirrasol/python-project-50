import json


def to_json(diff):
    """Apply JSON format."""
    return json.dumps(diff, indent=4)
