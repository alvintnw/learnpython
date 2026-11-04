# ==========================================
# 5. STRUKTUR DATA (List & Dictionary)
# ==========================================
print("\n== 5. Struktur Data (List & Dictionary) ==")

# List: Kumpulan data terurut
hobi = ["Membaca", "Koding", "Berenang"]
hobi.append("Bersepeda")  # Menambah data baru

print(f"Daftar Hobi: {hobi}")
print("Daftar hobi satu per satu:")
for item in hobi:
    print(f"- {item}")

# Dictionary: Data berbasis pasangan Key-Value
profil_mahasiswa = {
    "nama": nama,
    "umur": umur,
    "ipk": 3.75,
    "mata_kuliah": ["Pemrograman Web", "Struktur Data"]
}

print(f"\nProfil Mahasiswa: {profil_mahasiswa['nama']}")
print(f"IPK: {profil_mahasiswa['ipk']}")
print(f"Matkul Pertama: {profil_mahasiswa['mata_kuliah'][0]}")
