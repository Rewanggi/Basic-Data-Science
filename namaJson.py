import json
jsonData = '{"nim": "K01", "nama": "Mr. X"}'
data = json.loads(jsonData)

print(data["nim"])
print(data["nama"])