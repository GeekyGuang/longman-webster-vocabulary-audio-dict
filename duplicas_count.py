import json

with open('duplica_dict.json') as f:
    dict = json.load(f)
print(len(dict))