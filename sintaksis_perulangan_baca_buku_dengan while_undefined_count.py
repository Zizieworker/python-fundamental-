"""
program perulangan membaca buku dengan while sampai paham studi kasus nyata
"""

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu')
total_jumlah_baca = 0


jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan di pahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')


while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")

    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Baca ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah di baca dan di pahami")

     #print(f'Jumlah buku yang sudah dibaca dan di pahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
        print('"Bu, semua buku sudah dibaca dan pahami')
    else:
        print(f'"Bu, tidak semua buku bisa di pahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku')


