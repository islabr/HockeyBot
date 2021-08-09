def json_extract(json_data, key):
    """Recursively fetch values from nested JSON."""
    data = []

    def extract(json_data, data, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(json_data, dict):
            for index, value in json_data.items():
                if isinstance(value, (dict, list)):
                    extract(value, data, key)
                elif index == key:
                    data.append(value)
        elif isinstance(json_data, list):
            for item in json_data:
                extract(item, data, key)
        return data

    values = extract(json_data, data, key)
    return values