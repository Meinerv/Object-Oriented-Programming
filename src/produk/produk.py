from abc import ABC, abstractmethod

class Produk(ABC):
    def __init__(self, kode, nama, kategori, harga_dasar):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.harga_dasar = harga_dasar

    @abstractmethod
    def hitung_harga(self):
        pass

    @abstractmethod
    def tampilkan_info(self):
        pass