"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

dika = 400000
# TODO: Silakan buat kode Anda di bawah ini.

threshold_diskon = 500000

is_dapat_diskon = dico > threshold_diskon

print("dapat diskon:", is_dapat_diskon)

if is_dapat_diskon:
    diskon = 10/100 * dico
else: 
    diskon = 0

print("diskon:", diskon)

total_harga = int(dico - diskon)

print("total harga:", total_harga)