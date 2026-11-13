# ==========================================
# 7. ERROR HANDLING (Try - Except - Else - Finally)
# ==========================================
print("\n== 7. Penanganan Error (Try/Except) ==")

try:
    angka_pembilang = 10
    angka_penyebut = 2  # Ubah ke 0 untuk menguji penanganan error
    hasil = angka_pembilang / angka_penyebut
except ZeroDivisionError:
    print("Peringatan: Tidak bisa membagi angka dengan nol!")
except ValueError:
    print("Peringatan: Input harus berupa angka!")
else:
    # Dieksekusi HANYA jika blok try berhasil tanpa error
    print(f"Perhitungan berhasil! Hasil: {hasil}")
finally:
    # Selalu dieksekusi dalam kondisi apa pun
    print("Proses pengecekan error selesai.")
