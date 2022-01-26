daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich"]
print('Tampilkan variabel daftar buku')
print(daftar_buku)

print('\nProses semua dengan for in ')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar buku pada index tertentu ')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in  range ')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ['bethony', -5566, 'Basara 123',4555, 4.566]
print('\nTampilkan dengan for in  range dengan tipe data yang berbeda  ')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai seperti di awal ')
daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich"]
daftar_buku.append('giyu tamioka')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print(' \nClear list ')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pada data list pada python')
daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich","Journey of alex fegurson "]
daftar_buku[0] = 'Big Thinking'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil element ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nBuku yang di ambil tadi')
print(buku)

print('\nPerintah Pop saja')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop (-1)')
daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich","Journey of alex fegurson "]
daftar_buku.pop(-3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
