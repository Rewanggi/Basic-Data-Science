import json

#buka file json
myFile = open('d:\data.json', 'r')
#baca isi file json
dataJSON =myFile.read()
#baca data json
data = json.loads(dataJSON)

print("NIM mhs ke-1:", data[0]['nim'])
print("Nama mhs ke-2:", data[1]['nama']) 