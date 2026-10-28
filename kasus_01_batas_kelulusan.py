
def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


nilai = int(input("Masukkan nilai: "))

print("Nilai:", nilai)
print("Status:", status(nilai))
