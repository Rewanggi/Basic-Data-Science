from urllib.request import urlopen
import json

#buka URL
response = urlopen('https://jsonplaceholder.typicode.com/users')
#baca data stream dari URL
data = response.read()
#baca data JSON
y=json.loads(data)
#baca data pada key 'nama' dan address -> city' setiap entitas
for data in y:
    print(data['name'], '-', data['address']['city'], '-',data['address']['zipcode'])