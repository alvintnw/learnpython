# ==========================================
# 9. STRUKTUR DATA LANJUTAN (Tuple & Set)
# ==========================================
print("== 9. Tuple & Set ==")

# Tuple: Kumpulan data terurut yang bersifat immutable (tidak dapat diubah)
koordinat_jakarta = (-6.2088, 106.8456)
print(f"Koordinat Lokasi: {koordinat_jakarta}")
print(f"Latitude        : {koordinat_jakarta[0]}")
print(f"Longitude       : {koordinat_jakarta[1]}")

# Set: Kumpulan data tidak terurut yang otomatis menghapus duplikat
daftar_peserta = ["Andi", "Budi", "Citra", "Budi", "Andi", "Dewi"]
peserta_unik = set(daftar_peserta)

print(f"\nDaftar Awal  : {daftar_peserta}")
print(f"Peserta Unik : {peserta_unik}")

# Operasi himpunan pada Set
kelas_a = {"Andi", "Budi", "Citra"}
kelas_b = {"Citra", "Dewi", "Eka"}
print(f"Ikut kedua kelas (Irisan): {kelas_a.intersection(kelas_b)}")
