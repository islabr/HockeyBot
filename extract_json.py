import json

def json_extract(json_data, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(json_data, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(json_data, dict):
            for k, val in json_data.items():
                if isinstance(val, (dict, list)):
                    extract(val, arr, key)
                elif k == key:
                    arr.append(val)
        elif isinstance(json_data, list):
            for item in json_data:
                extract(item, arr, key)
        return arr

    values = extract(json_data, arr, key)
    return values