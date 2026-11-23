from transaksi.pesanan import Pesanan
from produk.menu_seblak import MenuSeblak
from produk.topping import Topping

class LayananPenjualan:
    def __init__(self, daftar_produk, gudang):
        self.daftar_produk = daftar_produk
        self.gudang = gudang
        self.daftar_pesanan = []

    def tampilkan_katalog(self):
        print("\n----- Katalog Menu Seblak -----")
        menu_ditemukan = False

        for produk in self.daftar_produk:
            if isinstance(produk, MenuSeblak):
                print(produk.tampilkan_info())
                menu_ditemukan = True

        if not menu_ditemukan:
            print("<!> Menu seblak belum tersedia.")

        print("\n----- Katalog Topping Seblak -----")
        topping_ditemukan = False

        for produk in self.daftar_produk:
            if isinstance(produk, Topping):
                print(produk.tampilkan_info())
                topping_ditemukan = True

        if not topping_ditemukan:
            print("<!> Topping belum tersedia.")

        print()

    def cari_produk(self, kode):
        for produk in self.daftar_produk:
            if kode == produk.kode:
                return produk
        return None

    def proses_pesanan(self, keranjang):
        if not keranjang.daftar_item:
            print("<!> Keranjang masih kosong.")
            return False

        kebutuhan = {}

        for item in keranjang.daftar_item:
            kode = item.produk.kode
            kebutuhan[kode] = kebutuhan.get(kode, 0) + item.jumlah

        for kode, jumlah in kebutuhan.items():
            if not self.gudang.cek_stok(kode, jumlah):
                print(f"<!> Stok produk {kode} tidak mencukupi")
                return False

        pesanan = Pesanan(keranjang)

        if not pesanan.konfirmasi_pesanan():
            return False

        for kode, jumlah in kebutuhan.items():
            self.gudang.kurangi_stok(kode, jumlah)

        data_pesanan = {
            "nomor": pesanan.nomor_transaksi,
            "items": list(keranjang.daftar_item),
            "total": keranjang.hitung_total(),
            "status": pesanan.status
        }

        self.daftar_pesanan.append(data_pesanan)

        pesanan.cetak_struk()

        return True
        
    def tampilkan_pesanan(self):
        print(f"\n----- Daftar Pesanan -----")
        if not self.daftar_pesanan:
            print("<!> Belum ada pesanan masuk.")
            return

        for pesanan in self.daftar_pesanan:
            print(f"\nNomor: {pesanan['nomor']}")
            print(f"Status: {pesanan['status']}")
            print("Detail pesanan:")
            for item in pesanan["items"]:
                print(f"- {item.produk.nama} x{item.jumlah}")
            print(f"Total: Rp{pesanan['total']:,}")
        print("-----------------------------")

    def jalankan_cli(self):
        from transaksi.keranjang import Keranjang
        keranjang = Keranjang()

        while True:
            print(f"\n----- Seblak Online -----")
            print(f"1. Lihat Katalog")
            print(f"2. Tambah produk ke keranjang")
            print(f"3. Lihat keranjang")
            print(f"4. Konfirmasi pesanan")
            print(f"5. Lihat pesanan masuk")
            print(f"6. Lihat stok")
            print(f"0. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.tampilkan_katalog()

            elif pilihan == "2":
                self.tampilkan_katalog()
                kode = input("Masukkan kode produk: ")
                produk = self.cari_produk(kode)

                if produk is None:
                    print("<!> Produk tidak ditemukan.")
                    continue

                try:
                    jumlah = int(input("Masukkan jumlah: "))
                    if jumlah <= 0:
                        print("<!> Jumlah harus lebih dari 0")
                        continue

                    keranjang.tambah_item(produk, jumlah)
                    print("Produk berhasil ditambahkan.")

                except ValueError as error:
                    print(f"<!> Input tidak valid: {error}")

            elif pilihan == "3":
                if not keranjang.daftar_item:
                    print("<!> Keranjang masih kosong.")
                else:
                    print(f"\n----- Keranjang -----")
                    for item in keranjang.daftar_item:
                        print(
                            f"{item.produk.nama} | {item.jumlah} x "
                            f"{item.produk.hitung_harga():,} = Rp{item.hitung_subtotal():,}" 
                        )
                    print(f"Total: Rp{keranjang.hitung_total():,}")

            elif pilihan == "4":
                berhasil = self.proses_pesanan(keranjang)
                if berhasil:
                    keranjang = Keranjang()

            elif pilihan == "5":
                self.tampilkan_pesanan()

            elif pilihan == "6":
                self.gudang.lihat_stok()

            elif pilihan == "0":
                print("Terima kasih!")
                break

            else:
                print("<!> Pilihan tidak tersedia")