# ==========================================
# 10. LIST COMPREHENSION
# ==========================================
print("== 10. List Comprehension ==")

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mengkuadratkan semua angka dalam satu baris
kuadrat = [x ** 2 for x in angka]
print(f"Angka Awal : {angka}")
print(f"Kuadrat    : {kuadrat}")

# Menyaring hanya angka genap (Conditional List Comprehension)
angka_genap = [x for x in angka if x % 2 == 0]
print(f"Angka Genap: {angka_genap}")

# Mengubah huruf menjadi kapital untuk kata tertentu
bahasa = ["python", "java", "javascript", "php"]
bahasa_besar = [b.upper() for b in bahasa if len(b) > 3]
print(f"Bahasa (>3 huruf): {bahasa_besar}")
