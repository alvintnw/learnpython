# ==========================================
# 3. PERULANGAN (Loops)
# ==========================================
print("== Perulangan for ==")
for angka in range(1, 6):
    print(f"Angka ke-{angka}")

print("\n== Perulangan while ==")
hitung = 1
while hitung <= 3:
    print(f"Perulangan while: {hitung}")
    hitung += 1

print("\n== Kontrol Perulangan (Break & Continue) ==")
print("Contoh 'continue' (melewati angka 3):")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"Nilai: {i}")

print("\nContoh 'break' (berhenti saat angka 4):")
for i in range(1, 6):
    if i == 4:
        break
    print(f"Nilai: {i}")
