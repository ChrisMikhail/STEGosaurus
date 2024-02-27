import yaml


def read_yaml_file(file_path="keys/secrets.yaml"):
    """Reads a yaml file and returns the secrets"""
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        secrets = yaml_data["secrets"]
        key = secrets["key"]
        nonce = secrets["nonce"]
        tag = secrets["tag"]
        length = secrets["length"]
    return key, nonce, tag, length
