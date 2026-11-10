print("=== APOTEK ANA ===")
print("DAFTAR OBAT APOTEK")

print("1. Oralit")
print("2. Plester Luka")
print("3. Kasa Steril")
print("4. Betadine")
print("5. Losion Calamine")
print("6. Saline Hidung")
print("7. Tablet Hisap")
print("8. Minyak Kayu Putih")
print("9. Salep Antiseptik")
print("10. Paracetamol")

pilihan = int(input("Pilih obat (1-10): "))
jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))

stok = 0
harga = 0
nama_obat = ""
found = True

if pilihan == 1:
    nama_obat = "Oralit"
    stok, harga = 50, 10000
elif pilihan == 2:
    nama_obat = "Plester Luka"
    stok, harga = 30, 5000
elif pilihan == 3:
    nama_obat = "Kasa Steril"
    stok, harga = 25, 10000
elif pilihan == 4:
    nama_obat = "Betadine"
    stok, harga = 20, 10000
elif pilihan == 5:
    nama_obat = "Losion Calamine"
    stok, harga = 15, 25000
elif pilihan == 6:
    nama_obat = "Saline Hidung"
    stok, harga = 20, 20000
elif pilihan == 7:
    nama_obat = "Tablet Hisap"
    stok, harga = 40, 10000
elif pilihan == 8:
    nama_obat = "Minyak Kayu Putih"
    stok, harga = 35, 18000
elif pilihan == 9:
    nama_obat = "Salep Antiseptik"
    stok, harga = 18, 15000
elif pilihan == 10:
    nama_obat = "Paracetamol"
    stok, harga = 50, 10000
else:
    found = False
    print("Pilihan obat tidak tersedia.")

if found:
    print(f"\nInformasi Obat: {nama_obat}")
    print(f"Stok tersedia: {stok} unit")
    print(f"Harga per unit: Rp{harga}")

if jumlah_beli > stok:
    print("Status: Transaksi Gagal. Stok tidak mencukupi!")
elif jumlah_beli <= 0:
    print("Status: Jumlah pembelian tidak valid") 
else:
    total_harga = jumlah_beli * harga
    print("Status: Transaksi Berhasil.")
    print(f"Total Biaya: Rp{total_harga}")

if total_harga >= 100000:
    print("Bonus: Mendapatkan vitamin gratis!")