import json

with open("trademark_sample.json", encoding="utf-8") as f:
    data = json.load(f)

def get_trademarks():
    return data
