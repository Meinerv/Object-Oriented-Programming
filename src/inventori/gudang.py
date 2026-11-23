
class Gudang:
    
    def __init__(self):
        self.stok = {}

    def tambah_stok(self, kode, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah stok harus lebih dari 0")

        if kode in self.stok:
            self.stok[kode] += jumlah
        else:
            self.stok[kode] = jumlah

    def cek_stok(self, kode, jumlah):
        if jumlah <= 0:
            return False

        return self.stok.get(kode, 0) >= jumlah

    def kurangi_stok(self, kode, jumlah):
        if kode not in self.stok:
            raise KeyError(f"<!> Kode produk {kode} tidak ditemukan di gudang.")

        if not isinstance(jumlah, int):
            raise TypeError("<!> Jumlah pengurangan harus berupa integer.")

        if jumlah <= 0:
            raise ValueError("<!> Jumlah pengurangan harus lebih dari 0.")

        if not self.cek_stok(kode, jumlah):
            raise ValueError(f"<!> Stok {kode} tidak mencukupi.")

        self.stok[kode] -= jumlah

    def lihat_stok(self):
        print("\n ----- Data Stok -----")

        if not self.stok:
            print("<!> Belum ada data stok.")
            return

        for kode, jumlah in self.stok.items():
            print(f"Kode: {kode} | Stok: {jumlah}")

        print("------------------------")

