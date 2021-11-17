import json

config = {}

def save():
    global config
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)
def load():
    global config
    with open('config.json', 'r') as file:
        config = json.load(file)

def reload(id, value):
    global config
    load()
    config[id] = value
    save()
load()
