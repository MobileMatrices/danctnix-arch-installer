image_config = {
    "ui": 'barebone',
    "device": 'pinephone',
    "arch": "aarch64",
    "hostname": "danctnix",
    "storage": "undefined"
}

def update_config(key, value):
    image_config[key] = value

def get_config():
    return image_config