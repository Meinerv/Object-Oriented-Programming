class ItemPesanan:
    def __init__(self, produk, jumlah=1):
        self.produk = produk
        self.jumlah = jumlah

    def hitung_subtotal(self):
        return self.produk.hitung_harga() * self.jumlah

    def __str__(self):
        return f"{self.produk.nama} x{self.jumlah} - Rp {self.hitung_subtotal():,}"