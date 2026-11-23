
from .produk import Produk
from pathlib import Path
import pandas as pd


class MenuSeblak(Produk):
    def __init__(self, kode, nama, harga_dasar, level_pedas=0):
        super().__init__(kode, nama, "Menu Utama", harga_dasar)
        self.level_pedas = level_pedas

    def hitung_harga(self):
        return self.harga_dasar

    def tampilkan_info(self):
        return (
            f"[{self.kode}] {self.nama} "
            f"(Level {self.level_pedas}) - "
            f"Rp{self.hitung_harga():,.0f}"
        )


def load_menu_seblak():
    lokasi_file = Path(__file__).with_name("menu_seblak.csv")

    try:
        df = pd.read_csv(lokasi_file)

        kolom_wajib = {"kode", "nama", "harga_dasar", "level_pedas"}

        if not kolom_wajib.issubset(df.columns):
            raise ValueError("Kolom CSV menu seblak tidak lengkap.")

        daftar_seblak = []

        for _, row in df.iterrows():
            menu = MenuSeblak(
                str(row["kode"]),
                str(row["nama"]),
                int(row["harga_dasar"]),
                int(row["level_pedas"])
            )

            daftar_seblak.append(menu)

        return daftar_seblak

    except FileNotFoundError:
        print(f"File tidak ditemukan: {lokasi_file}")
        return []

    except pd.errors.EmptyDataError:
        print("File CSV menu seblak kosong.")
        return []

    except (ValueError, KeyError, TypeError) as e:
        print(f"Terjadi kesalahan pada data menu seblak: {e}")
        return []

    except pd.errors.ParserError as e:
        print(f"Format CSV menu seblak tidak valid: {e}")
        return []


daftar_seblak = load_menu_seblak()
