nama = input("Nama: ")
jeniskelamin = input("Laki-laki/perempuan (l/p)? ")
usia = int(input("Usia: "))

if jeniskelamin == "l":
    if usia > 25:
        print("Halo, bapak", nama)
    else:
        print("Halo, de", nama)
else:
    if usia > 20:
        print("Halo, ibu", nama)
    else:
        print("Halo, neng", nama)

depan = input("Masukkan nama depan: ")
belakang = input("Masukkan nama belakang: ")
lengkap = depan + " " + belakang

if jeniskelamin == "l":
    print("Selamat siang, bapak", lengkap)
else:
    print("Selamat siang, ibu", lengkap)