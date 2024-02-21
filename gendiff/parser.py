import json
import yaml


def parse_data(data, format):
    """Parse data in a specified format."""
    if format == 'json':
        return json.loads(data)
    elif format in ('yml', 'yaml'):
        return yaml.safe_load(data)
