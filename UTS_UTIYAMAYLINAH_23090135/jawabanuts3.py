def hitung_total_harga(daftar_harga):
    total = sum(daftar_harga)
    return total

def main():
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    daftar_harga = []

    for i in range(jumlah_barang):
        harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
        daftar_harga.append(harga)

    total_harga = hitung_total_harga(daftar_harga)
    print(f"\nTotal harga belanjaan dari {jumlah_barang} barang adalah Rp {total_harga}")

if __name__ == "__main__":
    main()
