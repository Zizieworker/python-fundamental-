"""
program perulangan membaca buku dengan while sampai paham studi kasus nyata
"""

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu')
jumlah_baca = 0


jumlah_paham = 0
print(f'Jumlah buku yang sudah dibaca dan di pahami {jumlah_paham}')


while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9:
        print(f"Buku ke {jumlah_paham + 1} belum paham")

    else:
        jumlah_paham = jumlah_paham + 1
        print(f"Baca ke {jumlah_paham} sudah di baca dan di pahami")

     #print(f'Jumlah buku yang sudah dibaca dan di pahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
    if jumlah_paham == jumlah_buku:
        print('"Bu, semua buku sudah dibaca dan pahami')
    else:
        print(f'"Bu, tidak semua buku bisa di pahami {jumlah_paham} buku')


