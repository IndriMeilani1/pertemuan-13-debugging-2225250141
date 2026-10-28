
def baca_data(nama_file):
    nilai = []

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()

            if baris == "":
                continue

            try:
                angka = float(baris)
                nilai.append(angka)
            except ValueError:
                print("Data tidak valid, dilewati:", baris)

    return nilai


def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)


def nilai_tertinggi(nilai):
    return max(nilai)


def tulis_rekap(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI\n")
        file.write("Daftar nilai: " + str(data) + "\n")
        file.write("Jumlah nilai: " + str(sum(data)) + "\n")
        file.write("Rata-rata: " + str(hitung_rata_rata(data)) + "\n")
        file.write("Nilai tertinggi: " + str(nilai_tertinggi(data)) + "\n")


input_file = "nilai.txt"
output_file = "hasil_rekap.txt"

nilai = baca_data(input_file)

if len(nilai) > 0:
    tulis_rekap(output_file, nilai)
    print("Data berhasil dibaca.")
    print("Rata-rata:", hitung_rata_rata(nilai))
    print("Nilai tertinggi:", nilai_tertinggi(nilai))
    print("Hasil rekap disimpan di", output_file)
else:
    print("Tidak ada data nilai yang valid.")
