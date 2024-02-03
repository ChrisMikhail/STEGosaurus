import yaml


def read_yaml_file(file_path="secrets.yaml"):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data
