import json

name = input("ismingizni kiriting: ")
age = input("yoshingizni kiriting: ")

data = {"name": name, "age": age}

f = open("data.json", "w")
json.dump(data, f)