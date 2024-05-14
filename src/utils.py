import yaml

def load_settings():
    with open("config/settings.yaml", 'r') as file:
        return yaml.safe_load(file)
