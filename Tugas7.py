print("=== RUMAH SAKIT ANA ===")
print("DAFTAR PENYAKIT PASIEN")

print("1. Bronkitis")
print("2. Cacar Air")
print("3. Diare Akut")
print("4. Sinusitis")
print("5. Campak")
print("6. Infeksi Saluran Kemih")
print("7. Gagal Ginjal")
print("8. Radang Usus Buntu")
print("9. Hepatitis")
print("10. Meningitis")

nama = input("Masukkan nama pasien: ")
usia = int(input("Masukkan usia pasien: "))
pilihan = int(input("Pilih penyakit (1-10): "))
lama = int(input("Lama opname (hari): "))

if pilihan == 1:
    penyakit = "Bronkitis"
elif pilihan == 2:
        penyakit = "Cacar Air"
        elif pilihan == 3:
            penyakit = "Diare Akut"
            elif pilihan == 4:
                penyakit = "Sinusitis"
                elif pilihan == 5:
                    penyakit = "Campak"
                    elif pilihan == 6:
                        penyakit = "Infeksi Saluran Kemih"
                        elif pilihan == 7:
                            penyakit = "Gagal Ginjal"
                            elif pilihan == 8:
                                penyakit = "Radang Usus Buntu"
                                elif pilihan == 9:
                                    penyakit = "Hepatitis"
                                    elif pilihan == 10:
                                        penyakit = "Meningitis"
                                        else:
                                            penyakit = ""

                                            if pilihan >= 1 and pilihan <= 10:
                                                print("\n=== DATA PASIEN ===")
                                                    print("Nama pasien:", nama)
                                                        print("Usia pasien:", usia, "tahun")
                                                            print("Penyakit:", penyakit)
                                                                print("Lama opname:", lama, "hari")

                                                                    if lama > 7:
                                                                            print("Status: Opname lama")
                                                                                elif lama >= 1:
                                                                                        print("Status: Opname normal")
                                                                                            else:
                                                                                                    print("Status: Data opname tidak valid")
                                                                                                    else:
                                                                                                        print("Pilihan penyakit tidak tersedia")