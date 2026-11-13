# ==========================================
# 6. MANIPULASI STRING
# ==========================================
print("\n== 6. Manipulasi String ==")
kalimat = "  Belajar Python Sangat Seru  "

print(f"Teks Asli        : '{kalimat}'")
print(f"Huruf Besar Semua: {kalimat.upper()}")
print(f"Huruf Kecil Semua: {kalimat.lower()}")
print(f"Hapus Spasi Luar : '{kalimat.strip()}'")
print(f"Ganti Kata       : {kalimat.replace('Seru', 'Menyenangkan')}")

# Pemisahan kata (Split tanpa argumen otomatis menangani spasi ganda/berlebih)
kata_list = kalimat.split()
print(f"Daftar Kata      : {kata_list}")
print(f"Jumlah Kata      : {len(kata_list)}")
