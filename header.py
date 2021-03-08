import json

HEADER = {}

with open('./header.json') as json_file:
    HEADER = json.load(json_file)