sisi = int(input('Masukan Panjang Yang Di Inginkan = '))
mulai = 1
spasi = int(sisi/2)

# SEGITIGA ATAS

while True:

    if mulai%2 == 1:
        print(' ' * spasi , '*' * mulai)
        mulai += 1
        spasi -= 1
        continue

    elif mulai >= sisi:
        break
    mulai += 1


 # SEGITIGA BAWAH
spasi = 1
mulai -= 1
while True:
    if mulai%2 == 1:
        print(' ' * spasi , '*' * mulai)
        mulai -= 1
        spasi += 1
        continue

    elif mulai <= 1:
        break
    mulai -= 1