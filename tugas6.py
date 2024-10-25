def pilih_makanan():
    makan_pedas = input("Makan pedas? (y/t): ")

    if makan_pedas == 'y':
        berkuah = input("Berkuah? (y/t): ")
        if berkuah == 'y':
            makanan = "Seblak"
        else:
            makanan = "Indomie"
    else:
        manis = input("Manis? (y/t): ")
        if manis == 'y':
            makanan = "Buah"
        else:
            makanan = "Bala-bala"

    print(f"Makanan = {makanan}")

pilih_makanan()