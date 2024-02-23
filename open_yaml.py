import yaml


def read_yaml_file(file_path="keys/secrets.yaml"):
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        secrets = yaml_data["secrets"]
        key = eval(secrets["key"].encode('utf-8'))
        nonce = eval(secrets["nonce"].encode('utf-8'))
        tag = eval(secrets["tag"].encode('utf-8'))
        length = int(secrets["length"])
    return key, nonce, tag, length
