
from produk import daftar_seblak, daftar_topping
from inventori.gudang import Gudang
from layanan.layanan_penjualan import LayananPenjualan

katalog_hari_ini = daftar_seblak + daftar_topping

gudang = Gudang()

for produk in katalog_hari_ini:
    gudang.tambah_stok(produk.kode, 20)

layanan = LayananPenjualan(katalog_hari_ini, gudang)
layanan.jalankan_cli()
