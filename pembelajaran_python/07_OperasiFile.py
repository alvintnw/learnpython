# ==========================================
# 7. OPERASI FILE (File I/O)
# ==========================================
print("\n== 8. Penulisan dan Pembacaan File ==")

# Inisialisasi variabel lokal agar file bisa dijalankan secara mandiri
nama = "Budi"
nilai = 78
nama_file = "catatan_belajar.txt"

# Menulis ke file (Menggunakan context manager 'with' untuk otomatis menutup file)
try:
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("Catatan Modul Pembelajaran Python\n")
        file.write(f"Siswa: {nama}\n")
        file.write(f"Nilai Akhir: {nilai}\n")

    print(f"Berhasil menyimpan catatan ke '{nama_file}'.")

    # Membaca file
    print(f"\nIsi dari file '{nama_file}':")
    with open(nama_file, "r", encoding="utf-8") as file:
        isi_file = file.read()
        print(isi_file)

except IOError as e:
    print(f"Terjadi kesalahan saat memproses file: {e}")
