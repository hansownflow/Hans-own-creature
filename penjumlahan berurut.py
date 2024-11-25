def input_angka(n, current=1, total=0):
   
    if current > n:
        return total
    
    
    try:
        angka = float(input(f"Masukkan angka ke-{current}: "))
       
        return input_angka(n, current + 1, total + angka)
    except ValueError:
        print("Mohon masukkan angka yang valid!")
        return input_angka(n, current, total)

try:
    jumlah = int(input("Masukkan Jumlah: "))
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0!")
    else:
        hasil = input_angka(jumlah)
        print(f"Hasil penjumlahan berurut: {hasil}")
except ValueError:
    print("Mohon masukkan angka yang valid!")