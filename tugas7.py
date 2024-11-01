nama_depan = ["Pendekar", "Kesatria", "Pengembara", "Dewi", "Manusia", "Jawara", "Ki/Nyai", "Empu", "Siluman", "Robot"]
nama_tengah = ["Jempol", "Sarung", "Kera", "Langit", "Iblis", "Micin", "Laut", "Naga", "Keris", "Gayung", "Beton", "Kolor"]  # sesuai bulan Januari-Desember
nama_belakang = ["Perkasa", "Durjana", "Kekinian", "Ternodai", "Panca Pesona", "Melarat", "Dari Utara", "Tujuh Rupa", "Keramat", "Elektronik"]

tanggal_lahir = int(input("Angka terakhir tanggal lahirmu? "))
bulan_lahir = int(input("Bulan lahirmu? "))
nomor_hp = int(input("Angka terakhir nomor HP mu? "))

depan = nama_depan[tanggal_lahir % 10]
tengah = nama_tengah[(bulan_lahir - 1) % 12]  # Sesuai bulan (1=Januari, 12=Desember)
belakang = nama_belakang[nomor_hp % 10]

print("WWWuuuuuzzzz....!!!")
print(f"Namamu adalah {depan} {tengah} {belakang}")