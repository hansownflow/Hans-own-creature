print("=====SELAMAT DATANG DI KEBUN BINATANG TRISAKTI=====")

running_total = 0
while True:
    # Input Umur
    umur = input("masukkan umur : ")
    if umur == "":
        pembayaran = float(input("masukkan jumlah uang : "))
        kembalian = pembayaran - running_total
        print(f"Running kembalian: ${kembalian:.2f}")
        print("=====TERIMAKASIH=====")
        break
    umur = int(umur)
    if umur <= 2:
        harga = 0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14
        print(f"Harga $ {harga}")
    elif umur >= 65:
        harga = 18
        print(f"Harga $ {harga}")
    else:
        harga = 23
        print(f"Harga $ {harga}")
    
    # Add to running total and display
    running_total += harga
    print(f"Running total : ${running_total:.2f}")