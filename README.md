# Pertemuan 13 - Debugging dan Testing
Nama: Indri Meilani
NIM: 2225250141
Kelas: 3A

## Kasus
Program kasus_03_file_nilai.py merupakan program Python yang digunakan untuk membaca data nilai dari file nilai.txt, kemudian menghitung jumlah nilai, rata-rata, dan nilai tertinggi. Setelah itu, hasil perhitungan disimpan ke dalam file hasil_rekap.txt. Program ini diuji untuk memastikan data dari file teks dapat dibaca dan diolah dengan benar.

## Test Case
Pengujian dilakukan menggunakan beberapa kondisi, yaitu ID TC01 dengan input file nilai.txt yang berisi angka 80, 60, 90, dan 70, dengan hasil yang diharapkan program dapat membaca semua nilai dan menghitung rata-rata 75 serta nilai tertinggi 90. ID TC02 menggunakan file yang berisi baris kosong, dengan hasil yang diharapkan baris kosong dapat dilewati tanpa menyebabkan program mengalami error. ID TC03 menggunakan file yang berisi data tidak valid, misalnya tulisan yang bukan angka, dengan hasil yang diharapkan program memberikan pesan bahwa data tidak valid dan tetap bisa membaca angka yang benar. Pada pengujian awal, TC01 dapat mengalami kesalahan apabila format isi file tidak sesuai dengan proses konversi float(baris), sedangkan TC02 dan TC03 belum dapat ditangani dengan baik karena belum terdapat validasi data. Oleh karena itu, pengujian awal dinyatakan belum berhasil sepenuhnya.

## Bug Report
Kesalahan ditemukan pada bagian fungsi baca_data(), tepatnya pada perintah nilai.append(float(baris)). Gejala yang terjadi adalah program tidak dapat membaca data jika isi file memiliki format yang tidak sesuai dengan angka, sehingga muncul error ValueError. Penyebabnya adalah program langsung mengubah setiap baris menjadi tipe data float tanpa memeriksa apakah isi baris tersebut benar-benar angka. Perbaikannya dilakukan dengan menambahkan try-except untuk menangani data yang tidak valid, menggunakan strip() untuk menghapus spasi atau karakter baris baru, serta menambahkan kondisi untuk melewati baris kosong.

## Retest
Setelah codingan diperbaiki, pengujian dilakukan kembali menggunakan data yang sama. Pada TC01, data 80, 60, 90, dan 70 berhasil dibaca dengan rata-rata 75 dan nilai tertinggi 90. Pada TC02, baris kosong berhasil dilewati tanpa menyebabkan error. Pada TC03, data yang bukan angka berhasil dideteksi dan dilewati dengan menampilkan pesan bahwa data tidak valid. Hasil perhitungan juga berhasil disimpan ke dalam file hasil_rekap.txt. Dengan demikian, program sudah berjalan lebih baik setelah dilakukan perbaikan.

## Cara Menjalankan
python3 praktik/praktik_4_debugging.py

## Refleksi
Teknik debugging yang paling membantu menurut saya adalah menggunakan teknik try-except dan melakukan pengujian dengan beberapa test case. Teknik ini membantu mengetahui bagian program yang mengalami kesalahan, terutama ketika membaca data dari file teks yang formatnya berbeda-beda. Dengan mencoba beberapa kondisi input, saya juga bisa mengetahui apakah program hanya berjalan pada data tertentu atau sudah bisa menangani berbagai kondisi. Dari kegiatan ini, saya belajar bahwa sebelum mengolah data, kita perlu memastikan data yang dimasukkan sudah sesuai dengan format yang dibutuhkan program.
