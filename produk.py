class Produk:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def tampilkan_produk(self):
        print("Nama Produk :", self.nama)
        print("Harga       :", self.harga)
        print("Jumlah Beli :", self.jumlah)

    def total_produk(self):
        return self.harga * self.jumlah

    def hitung_diskon(self, total):
        if total > 5000:
            return total * 5 / 100
        else:
            return 0