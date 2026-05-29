import json

f = open("data.json", "r")
data = json.load(f)
print(f"Name: {data['name']}, Age: {data['age']}")