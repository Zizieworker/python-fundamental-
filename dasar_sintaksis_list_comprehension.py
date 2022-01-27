print('\nPerintah Del Comphersion ')
daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich","Journey of alex fegurson "]
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList Comprehension yang pertama ')
daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich","Journey of alex fegurson "]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList Comprehension dengan Comprehension Start')
daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich","Journey of alex fegurson "]
del daftar_buku[0:-1] #Start :  End
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

#Comprehension Step
print('\nList Comprehension dengan Comprehension Start')
daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich","Journey of alex fegurson "]
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ["Atomic habit", "Cashflow Kuandran","Think And Grow rich","The Journey of alex fegurson "]
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])


# membuat list baru dengan comprehension ganil
print('\nMembuat list baru dengan comprehension ganjil ')
daftar_buku = ["1. Atomic habit", "2. Cashflow Kuandran","3. Think And Grow rich","4. The Journey of alex fegurson "]
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# membuat list baru dengan comprehension genap
print('\nMembuat list baru dengan comprehension genap ')
daftar_buku = ["1. Atomic habit", "2. Cashflow Kuandran","3. Think And Grow rich","4. The Journey of alex fegurson "]
daftar_buku_baru = daftar_buku[1::2] #START STOP END
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# membuat list baru dengan comprehension buang ujung
print('\nMembuat list baru dengan comprehension : Buang Ujung ')
daftar_buku = ["1. Atomic habit", "2. Cashflow Kuandran","3. Think And Grow rich","4. The Journey of alex fegurson "]
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# membuat list baru dengan comprehension ganil
print('\nMembuat list baru dengan comprehension ganjil ')
daftar_buku = ["1. Atomic habit", "2. Cashflow Kuandran","3. Think And Grow rich","4. The Journey of alex fegurson "]
print (daftar_buku[0::2])


