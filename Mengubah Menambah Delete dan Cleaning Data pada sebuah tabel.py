import pandas as pd
nameFile = 'd:\mhs.csv'
data = pd.read_csv(nameFile, sep=";")

#merubah Item ('NIM') sebagai Index, untuk mengaktifkan ganti nilai "inplace" menjadi True
data.set_index('NIM', inplace=False)

#Menambah Usia
ListUsia = [40,40,14,13,17,40,40,14,13,17]
#data['USIA'] = ListUsia

#Menghapus Kolom index, untuk mengaktifkan ganti nilai "inplace" menjadi True
data.drop([0,1], axis = 0, inplace = False)

#Menghapus Kolom, untuk mengaktifkan ganti nilai "inplace" menjadi True
data.drop(['NIM','NAMA'], axis = 1, inplace = False)

#Merubah nama Kolom, untuk mengaktifkan ganti nilai "inplace" menjadi True
data.rename(columns = {"NAMA": "Name",
                      "ALAMAT": "Adrress"}, inplace = False)

#Merubah nama Index, untuk mengaktifkan ganti nilai "inplace" menjadi True
data.rename(index = {0 : "mhs1",
                     1 : "mhs2"}, inplace = False)

#Filter Kolom, tidak bisa menggunakan inplace = True/False, untuk mengaktifkan hapus lambang pagar (#) di samping "data"
#data = data.filter(items=['NIM', 'NAMA']), tidak bisa menggunakan inplace = True/False

#Mengurutkan/Sort daftar item ( NIM, NAMA, TGL LAHIR, ALAMAT, USIA), fungsi ascending bisa dirubah True dan False, fungsi inplace bisa dirubah True/False
data.sort_values("NAMA", axis=0, ascending=False, inplace=False)

#Mengubah Nilai yang tidak ada di dalam list Item, contoh tinggi (Nan) dimanipulasi sehingga mempunyai nilai
data.fillna(data['TINGGI'].mean(), inplace = False)

#Menghapus nilai yang hilang/tidak terdaftar, how='any'/'all'.
data.dropna (axis=0, how = 'any', inplace = False)

#melakukan iterasi terhadap kolom menjadi baris.
#for i, baris in data.iterrows():
     #print('indeks:', i,
          #'nim:', baris['NIM'],
          #'nama:', baris['NAMA'],
          #'alamat:', baris['TINGGI'])
          
          
#mencari data dengan kriteria tertentuy          
#data= data[data['TINGGI']>=168]
          
#mencari data sesuai kriteria tertentu         
#data= data[data[input()]==input()]
data
print(data)