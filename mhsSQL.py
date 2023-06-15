import mysql.connector as sql
import pandas as pd

mydb = sql.connect(host='localhost',
                   database='mysiakad',
                   user='root',
                   password='13312217And')
data = pd.read_sql('SELECT * FROM mhs', con=mydb)
def findMhs(data, nim):
    # mencari indeks data nim yang akan dicari
    i = 0
    status = False
    for x in data ['NIM']:
        if x == nim:
            index = i
            status = True
            break
        i += 1
    #jika indeks ditemukan, tampilkan data
    #berdasarkan indeks
    if status == True:
        print('NIM    :', data['NIM'][index])
        print('Nama   :', data['NAMA'][index])
        print('Alamat :', data['ALAMAT'][index])
        print('Tgl Lhr:', data['TGL LAHIR'][index])
    else:
        print('Data tidak ditemukan')

findMhs(data, 'M005')