def load_config(config_path):
    import json
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def format_response(response):
    return f"Response: {response}"