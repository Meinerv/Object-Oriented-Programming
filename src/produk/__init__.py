from .produk import Produk
from .menu_seblak import MenuSeblak, daftar_seblak
from .topping import Topping, daftar_topping

def tampilkan_katalog(daftar_produk):
    print("KATALOG SEBLAK & PRASMANAN")
    print("\n[MENU SIAP PESAN]")
    for p in daftar_produk:
        if isinstance(p, MenuSeblak):
            print(p.tampilkan_info())
            
    print("\n[TOPPING]")
    for p in daftar_produk:
        if isinstance(p, Topping):
            print(p.tampilkan_info())