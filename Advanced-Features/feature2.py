# pprint
# use to formatted pretty print
import pprint
import json

with open("data.json", "r") as f:
    data = json.load(f)
    pprint.pprint(data)
