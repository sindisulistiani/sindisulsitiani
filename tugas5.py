nama = input("Nama: ")
jeniskelamin = input("laki-laki/perempuan (l/p)? ")
usia = int(input("Usia: "))

if jeniskelamin == "l":
    if usia > 25:
        print(f"Halo, bapak {nama}")
    else:
        print(f"Halo, de {nama}")
else:
    if usia > 20:
        print(f"Halo, ibu {nama}")
    else:
        print(f"Halo, neng {nama}")

depan = input("Nama depan: ")
belakang = input("Nama belakang: ")
lengkap = depan + " " + belakang

if jeniskelamin == "l":
    print(f"Selamat siang, bapak {lengkap}")
else:
    print(f"Selamat siang, ibu {lengkap}")