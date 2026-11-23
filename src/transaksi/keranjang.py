from .item_pesanan import ItemPesanan

class Keranjang:
    def __init__(self):
        self.daftar_item = []

    def tambah_item(self, produk, jumlah=1):
        if produk is None:
            raise ValueError("<!> Produk tidak valid.")

        if not isinstance(jumlah, int):
            raise TypeError("<!> Jumlah harus berupa integer.")

        if jumlah <= 0:
            raise ValueError("<!> Jumlah produk harus lebih dari 0.")

        for item in self.daftar_item:
            if item.produk.kode == produk.kode:
                item.jumlah += jumlah
                return
        
        item_baru = ItemPesanan(produk, jumlah)
        self.daftar_item.append(item_baru)

    def atur_jumlah(self, kode, jumlah_baru):
        for item in self.daftar_item:
            if item.produk.kode == kode:
                if jumlah_baru <= 0:
                    self.daftar_item.remove(item)
                else:
                    item.jumlah = jumlah_baru
                return
        print(f"<!> Kode {kode} tidak ditemukan di keranjang.")

    def hitung_total(self):
        return sum(item.hitung_subtotal() for item in self.daftar_item)

    def tampilkan_keranjang(self):
        print("\n----- Isi Keranjang -----")
        
        if not self.daftar_item:
            print("<!> Keranjang masih kosong.")
            return

        for item in self.daftar_item:
            print(f"- {item}")
        print(f"Total Sementara: Rp {self.hitung_total():,}")
        print("---------------------------")