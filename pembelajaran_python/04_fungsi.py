# ==========================================
# 4. FUNGSI
# ==========================================
print("== Fungsi ==")

# Fungsi dengan default parameter dan type hinting
def sapa(nama: str = "Pengunjung") -> str:
    """Fungsi untuk menyapa pengguna dengan nama opsional."""
    return f"Halo, {nama}! Selamat belajar Python."

def luas_persegi(sisi: float) -> float:
    """Fungsi untuk menghitung luas persegi."""
    return sisi * sisi

# Pemanggilan fungsi
print(sapa("Ani"))
print(sapa())  # Menggunakan nilai default "Pengunjung"
print(f"Luas persegi sisi 4: {luas_persegi(4)}")
