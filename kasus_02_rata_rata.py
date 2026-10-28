
def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)


nilai = [80, 60, 90, 70]

print("Daftar nilai:", nilai)
print("Jumlah nilai:", sum(nilai))
print("Banyak data:", len(nilai))
print("Rata-rata:", hitung_rata_rata(nilai))
