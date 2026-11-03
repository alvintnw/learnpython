# ==========================================
# 6. MANIPULASI STRING
# ==========================================
print("\n== 6. Manipulasi String ==")
kalimat = "  Belajar Python Sangat Seru  "

print(f"Teks Asli        : '{kalimat}'")
print(f"Huruf Besar Semua: {kalimat.upper()}")
print(f"Hapus Spasi Luar : '{kalimat.strip()}'")
print(f"Ganti Kata       : {kalimat.replace('Seru', 'Menyenangkan')}")

# Pemisahan kata (Split)
kata_list = kalimat.strip().split(" ")
print(f"Jumlah Kata      : {len(kata_list)}")
