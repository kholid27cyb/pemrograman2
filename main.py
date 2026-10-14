from produk import Produk

data_produk = []

jumlah_produk = int(input("Masukkan jumlah produk: "))

for i in range(jumlah_produk):
    print("\nProduk ke-", i + 1)

    nama = input("Nama produk : ")
    harga = int(input("Harga produk : "))
    jumlah = int(input("Jumlah beli : "))

    produk = Produk(nama, harga, jumlah)
    data_produk.append(produk)

print("\n=== HASIL PEMBELIAN ===")

total_semua = 0

for produk in data_produk:
    produk.tampilkan_produk()

    total = produk.total_produk()
    print("Total Produk:", total)
    print()

    total_semua += total

diskon = data_produk[0].hitung_diskon(total_semua)

total_bayar = total_semua - diskon

print("Total Pembelian :", total_semua)
print("Diskon 5%       :", diskon)
print("Total Bayar     :", total_bayar)