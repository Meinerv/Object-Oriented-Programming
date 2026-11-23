import time
import random

class Pesanan:
    counter = 0

    def __init__(self, keranjang):
        self.keranjang = keranjang
        self.nomor_transaksi = self._buat_nomor_transaksi()
        self.status = "Menunggu Konfirmasi"

    def _buat_nomor_transaksi(self):
        Pesanan.counter += 1

        waktu = time.strftime("%Y%m%d%H%M")
        nomor_urut = f"{Pesanan.counter:03d}"
        return f"TRX-{waktu}-{nomor_urut}"

    def konfirmasi_pesanan(self):
        if not self.keranjang.daftar_item:
            print("Gagal konfirmasi: Keranjang kosong!")
            return False

        print("\n--- KONFIRMASI PESANAN ---")
        self.keranjang.tampilkan_keranjang()

        while True:
            konfirmasi = input(f"Apakah Anda yakin ingin memproses pesanan {self.nomor_transaksi}? (y/n): ").strip().lower()
            
            if konfirmasi == 'y':
                self.status = "Diproses"
                print(f"Pesanan {self.nomor_transaksi} berhasil dikonfirmasi dan sedang diproses!")
                return True
            
            elif konfirmasi == 'n':
                print("Konfirmasi pesanan dibatalkan.")
                return False
            
            else:
                print("Input tidak valid. Masukkan y atau n.")

    def cetak_struk(self):
        print("\n" + "="*35)
        print(f"{'STRUK PEMBELIAN SEBLAK':^35}")
        print("="*35)
        print(f"No. Transaksi : {self.nomor_transaksi}")
        print(f"Status        : {self.status}")
        print("-" * 35)
        
        for item in self.keranjang.daftar_item:
            if hasattr(item.produk, "level_pedas"):
                nama = f"{item.produk.nama} Lv.{item.produk.level_pedas}"
            else:
                nama = item.produk.nama
                
            nama = nama[:18]
            print(f"{nama:<18} x{item.jumlah:<3} Rp {item.hitung_subtotal():>8,}")
            
        print("-" * 35)
        print(f"{'TOTAL BAYAR':<23} Rp {self.keranjang.hitung_total():>8,}")
        print("="*35)