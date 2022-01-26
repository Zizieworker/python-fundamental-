"""
program perulangan membaca buku dengan while sampai paham studi kasus nyata
"""

book_count = 10
print('Ibu berkata, "Baca semua bukumu')
read_count = 0


understood_count = 0
print(f'Jumlah buku yang sudah dibaca dan di pahami {understood_count}')


while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum paham")

    else:
        understood_count = understood_count + 1
        print(f"Baca ke {understood_count} sudah di baca dan di pahami")
S
     #print(f'Jumlah buku yang sudah dibaca dan di pahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
    if understood_count == book_count:
        print('"Bu, semua buku sudah dibaca dan pahami')
    else:
        print(f'"Bu, tidak semua buku bisa di pahami {understood_count} buku')

        # book_count ="mama"
        # print(book_count)



