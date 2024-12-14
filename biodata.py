def write_biodata():
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    email = input("Email: ")
    dosen_wali = input("Dosen Wali: ")

    with open("Biodata.txt", "w") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Umur: {umur}\n") 
        file.write(f"Alamat: {alamat}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Dosen Wali: {dosen_wali}\n")

    print("File Biodata.txt telah dibuat.")

def read_biodata():
    try:
        with open("Biodata.txt", "r") as file:
            contents = file.read()
            print("Isi File Biodata.txt:")
            print(contents)
    except FileNotFoundError:
        print("File Biodata.txt tidak ditemukan.")
