def create_file(file_name):
    """Fungsi untuk membuat file baru"""
    try:
        with open(file_name, "w") as file:
            print(f"File {file_name} berhasil dibuat.")
    except:
        print(f"Terjadi kesalahan saat membuat file {file_name}.")

def read_file(file_name):
    """Fungsi untuk membaca isi file"""
    try:
        with open(file_name, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except:
        print(f"Terjadi kesalahan saat membaca file {file_name}.")

def append_file(file_name, data):
    """Fungsi untuk menambahkan data ke dalam file"""
    try:
        with open(file_name, "a") as file:
            file.write(data + "\n")
            print(f"Data berhasil ditambahkan ke dalam file {file_name}.")
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except:
        print(f"Terjadi kesalahan saat menambahkan data ke dalam file {file_name}.")

def main():
    """Fungsi utama program"""
    while True:
        print("\n==== Program File Handling ====")
        print("1. Membuat dan Menulis File")
        print("2. Membaca File")
        print("3. Menambahkan Teks Pada File")
        print("4. Keluar Dari Program")

        choice = input("Masukkan pilihan Anda (1/2/3/4): ")

        if choice == "1":
            file_name = input("Masukkan nama file: ")
            create_file(file_name)
        elif choice == "2":
            file_name = input("Masukkan nama file: ")
            read_file(file_name)
        elif choice == "3":
            file_name = input("Masukkan nama file: ")
            data = input("Masukkan data yang akan ditambahkan: ")
            append_file(file_name, data)
        elif choice == "4":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()