import json
#buka file json
myFile = open ('d:\data.json', 'r')
#baca isi file json
dataJSON = myFile.read()
#baca data json
data = json.loads(dataJSON)

for x in data:
    print('nim:', x['nim'], 'nama:', x['nama'])