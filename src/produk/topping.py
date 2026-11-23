
from .produk import Produk
from pathlib import Path
import pandas as pd


class Topping(Produk):
    def __init__(self, kode, nama, harga_dasar, jenis_bahan):
        super().__init__(kode, nama, "Bahan Prasmanan", harga_dasar)
        self.jenis_bahan = jenis_bahan

    def hitung_harga(self):
        return self.harga_dasar

    def tampilkan_info(self):
        return (
            f"[{self.kode}] {self.nama} "
            f"({self.jenis_bahan}) - "
            f"Rp{self.hitung_harga():,.0f}"
        )


def load_topping():
    lokasi_file = Path(__file__).with_name("topping.csv")

    try:
        df = pd.read_csv(lokasi_file)

        kolom_wajib = {"kode", "nama", "harga_dasar", "jenis_bahan"}

        if not kolom_wajib.issubset(df.columns):
            raise ValueError("Kolom CSV topping tidak lengkap.")

        daftar_topping = []

        for _, row in df.iterrows():
            topping = Topping(
                str(row["kode"]),
                str(row["nama"]),
                int(row["harga_dasar"]),
                str(row["jenis_bahan"])
            )

            daftar_topping.append(topping)

        return daftar_topping

    except FileNotFoundError:
        print(f"File tidak ditemukan: {lokasi_file}")
        return []

    except pd.errors.EmptyDataError:
        print("File CSV topping kosong.")
        return []

    except (ValueError, KeyError, TypeError) as e:
        print(f"Terjadi kesalahan pada data topping: {e}")
        return []

    except pd.errors.ParserError as e:
        print(f"Format CSV topping tidak valid: {e}")
        return []


daftar_topping = load_topping()
