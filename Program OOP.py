class Data:
    def __init__(self):
        self.__nama = ""
        self.__nilai = 0

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama):
        self.__nama = nama

    # Getter untuk nilai
    def get_nilai(self):
        return self.__nilai

    # Setter untuk nilai
    def set_nilai(self, nilai):
        if nilai.isdigit() and 0 <= int(nilai) <= 100:
            self.__nilai = int(nilai)
        else:
            print("Nilai harus berupa angka antara 0 dan 100.")

    # Method untuk menghapus data
    def hapus_data(self):
        self.__nama = ""
        self.__nilai = 0
        print("Data berhasil dihapus.")


# Fungsi utama untuk menu
def main():
    data = Data()
    while True:
        print("\n===== Program OOP =====")
        print("1. Mendeklarasikan Objek")
        print("2. Menampilkan Objek")
        print("3. Merubah Nilai Objek")
        print("4. Menghapus Objek")
        print("5. Keluar Dari Program")
        pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): ")

        if pilihan == "1":
            nama = input("Masukkan Nama: ")
            nilai = input("Masukkan Nilai: ")
            data.set_nama(nama)
            data.set_nilai(nilai)
            print("Data Berhasil Ditambahkan")

        elif pilihan == "2":
            if data.get_nama() and data.get_nilai() != 0:
                print("\nNama:", data.get_nama())
                print("Nilai:", data.get_nilai())
            else:
                print("Data kosong. Silakan tambahkan data terlebih dahulu.")

        elif pilihan == "3":
            nama = input("Masukkan Nama Baru: ")
            nilai = input("Masukkan Nilai Baru: ")
            data.set_nama(nama)
            data.set_nilai(nilai)
            print("Data Berhasil Diubah")

        elif pilihan == "4":
            data.hapus_data()

        elif pilihan == "5":
            print("Keluar dari program...")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1-5.")


if __name__ == "__main__":
    main()


