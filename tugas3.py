depan = input("Nama Depan: ")

belakang = input("Nama Belakang: ")

jeniskelamin = input("Laki-laki/perempuan (l/p)? ")

print("Nama Lengkap:", depan, belakang)
print("Jenis Kelamin:", "Laki-laki" if jeniskelamin.lower() == 'l' else "Perempuan" if jeniskelamin.lower() == 'p' else "Tidak diketahui")