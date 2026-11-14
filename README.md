# SISTEM PAKAR KLASIFIKASI KELAYAKAN PENERIMAAN BEASISWA

## 1. Nama dan NIM

- **Nama:** Suci Mustika Ramadhani
- **NIM:** F1D02510093
- **Mata Kuliah:** Kecerdasan Buatan

## 2. Topik dan Cara Menjalankan Program

### Topik

Sistem Pakar Klasifikasi Kelayakan Penerimaan Beasiswa.

Program ini dibuat untuk membantu menentukan rekomendasi awal kelayakan seorang mahasiswa dalam seleksi beasiswa berdasarkan beberapa kondisi, yaitu IPK, semester aktif, kelancaran pembayaran biaya kuliah, dan jumlah mata kuliah semester 2 yang telah lulus.

Sistem memberikan tiga kategori hasil, yaitu:

1. **Layak Beasiswa Penuh:** Mahasiswa memenuhi persyaratan akademik, administrasi keuangannya lancar, dan jumlah mata kuliah semester 2 yang lulus memenuhi syarat.
2. **Tidak Layak / Ditolak:** Mahasiswa memiliki kendala akademik (IPK di bawah 2.75) atau kendala keuangan (pembayaran biaya kuliah menunggak).
3. **Perlu Evaluasi Lanjutan:** Persyaratan belum seluruhnya terpenuhi, tetapi belum ditemukan alasan untuk menolak, sehingga perlu pemeriksaan lebih lanjut.

### Bahasa dan Versi

- Bahasa pemrograman: Python
- Versi: Python 3
- Format basis pengetahuan: JSON
- Metode inferensi: Forward Chaining

### File Program

- `main.py` : Berisi kode utama program dan proses Forward Chaining.
- `kb_beasiswa.json` : Berisi judul, pertanyaan, aturan IF-THEN, sumber pengetahuan, dan batas keberlakuan sistem.

### Cara Menjalankan Program

1. Pastikan Python 3 sudah terpasang di komputer.
2. Simpan file `main.py` dan `kb_beasiswa.json` dalam satu folder.
3. Buka folder tersebut menggunakan Visual Studio Code.
4. Buka terminal pada folder program.
5. Jalankan perintah berikut:

```bash
python main.py
```

Jika perintah tersebut tidak berhasil, gunakan:

```bash
py main.py
```

6. Setelah program berjalan, jawab pertanyaan yang diberikan.
7. Masukkan `y` untuk jawaban Ya dan `t` untuk jawaban Tidak.
8. Setelah semua pertanyaan dijawab, program akan menampilkan fakta awal, hasil rekomendasi, alasan, jejak Forward Chaining, sumber referensi, dan batas keberlakuan sistem.

## 3. Daftar Sumber dan Tabel Aturan

### A. Daftar Sumber

Sumber pengetahuan digunakan sebagai dasar dalam menyusun aturan pada sistem pakar. Sumber yang digunakan berasal dari dua jurnal ilmiah yang membahas klasifikasi kelayakan bantuan pendidikan atau beasiswa.

**Sumber 1 (S1)**

- Penulis: Ida Kumala Sari, Arief Hermawan, dan Donny Avianto
- Judul: Klasifikasi Kelayakan Bantuan Pendidikan Menggunakan Metode Decision Tree
- Terbitan: INSOLOGI: Jurnal Sains dan Teknologi, Vol. 5 No. 3, 2026

**Sumber 2 (S2)**

- Penulis: Komang Rosmiani, et al.
- Judul: Analisis Kelayakan Penerimaan Bantuan Pendidikan Beasiswa Luwu Timur Tahun 2025 Menggunakan Metode Random Forest
- Terbitan: Jurnal Dipakomti, Vol. 18 No. 1, 2026

### B. Tabel Aturan (Rule Base)

Basis pengetahuan pada sistem ini terdiri dari lima aturan IF-THEN yang digunakan untuk menghasilkan kesimpulan.

| Kode | Aturan IF-THEN | Mode | Sumber |
|---|---|---|---|
| R1 | IF ipk >= 3.00 AND semester aktif <= 8 THEN akademik memenuhi syarat | DAN | S2 |
| R2 | IF akademik memenuhi syarat AND pembayaran biaya kuliah lancar THEN administrasi keuangan lancar | DAN | S1 |
| R3 | IF administrasi keuangan lancar AND jumlah mata kuliah semester 2 yang lulus >= 5 THEN Rekomendasi: Layak Beasiswa Penuh | DAN | S1 |
| R4 | IF ipk < 2.75 OR pembayaran biaya kuliah menunggak THEN kendala evaluasi akademik atau keuangan | ATAU | S1 |
| R5 | IF kendala evaluasi akademik atau keuangan THEN Rekomendasi: Tidak Layak / Ditolak | DAN | S2 |

### C. Keterangan Fakta

- `ipk >= 3.00` : IPK mahasiswa minimal 3.00.
- `semester aktif <= 8` : Semester aktif mahasiswa maksimal semester 8.
- `pembayaran biaya kuliah lancar` : Pembayaran biaya kuliah lancar dan tidak ada tunggakan.
- `pembayaran biaya kuliah menunggak` : Pembayaran biaya kuliah memiliki tunggakan.
- `jumlah mata kuliah semester 2 yang lulus >= 5` : Minimal 5 mata kuliah semester 2 telah lulus.
- `ipk < 2.75` : IPK mahasiswa di bawah 2.75.

### D. Keterangan Fakta Turunan (Kesimpulan Sementara)

- `akademik memenuhi syarat` : Hasil R1, persyaratan akademik terpenuhi.
- `administrasi keuangan lancar` : Hasil R2, akademik terpenuhi dan pembayaran lancar.
- `kendala evaluasi akademik atau keuangan` : Hasil R4, terdapat kendala akademik atau keuangan.

### E. Keterangan Sumber pada Aturan

- S1: Sari, Hermawan, dan Avianto (INSOLOGI, 2026).
- S2: Rosmiani, et al. (Jurnal Dipakomti, 2026).

## 4. Metode yang Dipilih dan Alasannya

Metode inferensi yang digunakan dalam sistem pakar ini adalah **Forward Chaining (FC)**.

Forward Chaining merupakan metode penalaran yang dimulai dari fakta atau kondisi awal yang diberikan oleh pengguna. Fakta tersebut kemudian dicocokkan dengan aturan yang tersedia sampai sistem mendapatkan kesimpulan.

Metode Forward Chaining dipilih karena sesuai dengan cara kerja program. Pengguna memberikan jawaban terlebih dahulu, kemudian sistem memproses jawaban tersebut untuk menentukan rekomendasi kelayakan beasiswa. Selain itu, aturan pada sistem ini bersifat berantai: hasil suatu aturan (misalnya `akademik memenuhi syarat`) menjadi syarat bagi aturan berikutnya, sehingga cocok diselesaikan dengan Forward Chaining.

### Langkah Kerja Forward Chaining

1. Pengguna menjawab pertanyaan yang diberikan oleh program.
2. Jawaban pengguna disimpan sebagai fakta awal.
3. Sistem mencocokkan fakta dengan aturan yang terdapat dalam file `kb_beasiswa.json`. Aturan bermode `dan` terpenuhi jika semua syaratnya ada, sedangkan aturan bermode `atau` terpenuhi jika salah satu syaratnya ada.
4. Jika kondisi suatu aturan terpenuhi, sistem menghasilkan fakta atau kesimpulan baru.
5. Fakta baru dapat digunakan untuk memenuhi aturan berikutnya.
6. Proses pencocokan diulang sampai tidak ada fakta baru yang dihasilkan.
7. Jika tidak ada rekomendasi yang dihasilkan, sistem memberikan rekomendasi **Perlu Evaluasi Lanjutan**.
8. Sistem menampilkan hasil akhir beserta alasan dan jejak aturan yang dipakai.

### Contoh Proses Forward Chaining

Misalnya pengguna memberikan fakta berikut:

- `ipk >= 3.00`
- `semester aktif <= 8`
- `pembayaran biaya kuliah lancar`
- `jumlah mata kuliah semester 2 yang lulus >= 5`

Proses penalarannya:

1. Fakta `ipk >= 3.00` dan `semester aktif <= 8` memenuhi aturan R1 sehingga menghasilkan `akademik memenuhi syarat`.
2. Fakta `akademik memenuhi syarat` dan `pembayaran biaya kuliah lancar` memenuhi aturan R2 sehingga menghasilkan `administrasi keuangan lancar`.
3. Fakta `administrasi keuangan lancar` dan `jumlah mata kuliah semester 2 yang lulus >= 5` memenuhi aturan R3.
4. Sistem menghasilkan kesimpulan `Rekomendasi: Layak Beasiswa Penuh`.

Metode ini tidak menggunakan rumus perhitungan numerik karena proses penalarannya dilakukan dengan mencocokkan fakta terhadap aturan IF-THEN.

## 5. Empat Kasus Uji dan Screenshot

Pengujian dilakukan untuk mengetahui apakah sistem dapat memberikan kesimpulan sesuai dengan fakta dan aturan yang telah dibuat. Pengujian mencakup tiga kategori hasil rekomendasi (Layak Beasiswa Penuh, Tidak Layak / Ditolak, dan Perlu Evaluasi Lanjutan), serta satu pengujian tambahan ketika seluruh pertanyaan dijawab Tidak.

### Kasus 1

**Kondisi yang dimasukkan:**

| Pertanyaan | Jawaban |
|---|---|
| Apakah IPK Anda minimal 3.00? | Ya |
| Apakah semester aktif Anda maksimal semester 8? | Ya |
| Apakah pembayaran biaya kuliah Anda lancar dan tidak memiliki tunggakan? | Ya |
| Apakah minimal 5 mata kuliah semester 2 Anda telah lulus? | Ya |
| Apakah IPK Anda di bawah 2.75? | Tidak |

**Fakta awal yang terbentuk:** `ipk >= 3.00`, `semester aktif <= 8`, `pembayaran biaya kuliah lancar`, dan `jumlah mata kuliah semester 2 yang lulus >= 5`.

**Hasil:** Rekomendasi: Layak Beasiswa Penuh.

**Alasan:** Persyaratan akademik terpenuhi, administrasi keuangan lancar, dan jumlah mata kuliah semester 2 yang lulus memenuhi syarat. Kondisi tersebut memenuhi aturan R1, R2, dan R3.

**Screenshot hasil pengujian:**

<img width="979" height="858" alt="Kasus1" src="https://github.com/user-attachments/assets/2daf67fa-9da4-4180-bd37-ed5b8a3135dc" />

**Keluaran program (teks):**

```
Fakta Awal:
- ipk >= 3.00
- jumlah mata kuliah semester 2 yang lulus >= 5
- pembayaran biaya kuliah lancar
- semester aktif <= 8

Hasil Rekomendasi:
-> Rekomendasi: Layak Beasiswa Penuh

Alasan:
- Persyaratan akademik telah terpenuhi.
- Administrasi keuangan dinyatakan lancar.
- Jumlah mata kuliah yang disetujui memenuhi syarat.
```

### Kasus 2

**Kondisi yang dimasukkan:**

| Pertanyaan | Jawaban |
|---|---|
| Apakah IPK Anda minimal 3.00? | Tidak |
| Apakah semester aktif Anda maksimal semester 8? | Tidak |
| Apakah pembayaran biaya kuliah Anda lancar dan tidak memiliki tunggakan? | Ya |
| Apakah minimal 5 mata kuliah semester 2 Anda telah lulus? | Tidak |
| Apakah IPK Anda di bawah 2.75? | Ya |

**Fakta awal yang terbentuk:** `ipk < 2.75` dan `pembayaran biaya kuliah lancar`.

**Hasil:** Rekomendasi: Tidak Layak / Ditolak.

**Alasan:** IPK berada di bawah 2.75 sehingga terdapat kendala akademik, meskipun pembayaran biaya kuliah lancar. Aturan R4 bermode ATAU, jadi satu syarat saja sudah cukup. Kondisi tersebut memenuhi aturan R4 dan R5.

**Screenshot hasil pengujian:**

<img width="998" height="822" alt="Kasus2" src="https://github.com/user-attachments/assets/5437db44-1db1-44b0-92e5-fcf1259bf46a" />

**Keluaran program (teks):**

```
Fakta Awal:
- ipk < 2.75
- pembayaran biaya kuliah lancar

Hasil Rekomendasi:
-> Rekomendasi: Tidak Layak / Ditolak

Alasan:
- Terdapat kendala akademik atau keuangan.
- Persyaratan kelayakan belum terpenuhi.
- Diperlukan perbaikan sesuai ketentuan beasiswa.
```

### Kasus 3

**Kondisi yang dimasukkan:**

| Pertanyaan | Jawaban |
|---|---|
| Apakah IPK Anda minimal 3.00? | Tidak |
| Apakah semester aktif Anda maksimal semester 8? | Tidak |
| Apakah pembayaran biaya kuliah Anda lancar dan tidak memiliki tunggakan? | Tidak |
| Apakah minimal 5 mata kuliah semester 2 Anda telah lulus? | Tidak |
| Apakah IPK Anda di bawah 2.75? | Tidak |

**Fakta awal yang terbentuk:** `pembayaran biaya kuliah menunggak`.

**Hasil:** Rekomendasi: Tidak Layak / Ditolak.

**Alasan:** Seluruh pertanyaan dijawab Tidak, sehingga pertanyaan nomor 3 menghasilkan fakta `pembayaran biaya kuliah menunggak`. Fakta ini memenuhi aturan R4 (kendala keuangan) dan dilanjutkan ke aturan R5.

**Screenshot hasil pengujian:**

<img width="1016" height="800" alt="Kasus3" src="https://github.com/user-attachments/assets/f6240ae2-e416-4704-8800-e50bc5315244" />


**Keluaran program (teks):**

```
Fakta Awal:
- pembayaran biaya kuliah menunggak

Hasil Rekomendasi:
-> Rekomendasi: Tidak Layak / Ditolak

Alasan:
- Terdapat kendala akademik atau keuangan.
- Persyaratan kelayakan belum terpenuhi.
- Diperlukan perbaikan sesuai ketentuan beasiswa.
```

### Kasus 4

**Kondisi yang dimasukkan:**

| Pertanyaan | Jawaban |
|---|---|
| Apakah IPK Anda minimal 3.00? | Ya |
| Apakah semester aktif Anda maksimal semester 8? | Ya |
| Apakah pembayaran biaya kuliah Anda lancar dan tidak memiliki tunggakan? | Ya |
| Apakah minimal 5 mata kuliah semester 2 Anda telah lulus? | Tidak |
| Apakah IPK Anda di bawah 2.75? | Tidak |

**Fakta awal yang terbentuk:** `ipk >= 3.00`, `semester aktif <= 8`, dan `pembayaran biaya kuliah lancar`.

**Hasil:** Rekomendasi: Perlu Evaluasi Lanjutan.

**Alasan:** Persyaratan akademik terpenuhi dan administrasi keuangan lancar (aturan R1 dan R2), tetapi jumlah mata kuliah semester 2 yang lulus belum memenuhi syarat sehingga R3 tidak terpenuhi. Di sisi lain, tidak ada kendala yang membuat R4 dan R5 terpenuhi. Karena belum ada rekomendasi yang dihasilkan, program memberikan rekomendasi evaluasi lanjutan.

**Screenshot hasil pengujian:**

<img width="1027" height="836" alt="Kasus4" src="https://github.com/user-attachments/assets/50ea6299-2fde-4794-9f36-8bc983069241" />


**Keluaran program (teks):**

```
Fakta Awal:
- ipk >= 3.00
- pembayaran biaya kuliah lancar
- semester aktif <= 8

Hasil Rekomendasi:
-> Rekomendasi: Perlu Evaluasi Lanjutan

Alasan:
- Belum seluruh persyaratan beasiswa terpenuhi.
- Belum ditemukan alasan untuk keputusan penolakan.
- Diperlukan pemeriksaan dan evaluasi lebih lanjut.
```

## 6. Batas Keberlakuan Sistem

Sistem pakar ini menggunakan pengetahuan yang disusun berdasarkan parameter akademik dan administratif dari studi literatur pengelolaan beasiswa perguruan tinggi, yaitu jurnal Sari dkk. (2026) dan Rosmiani dkk. (2026). Sistem hanya dapat memberikan hasil berdasarkan fakta dan aturan yang telah dimasukkan ke dalam basis pengetahuan, sehingga parameter di luar IPK, semester aktif, pembayaran biaya kuliah, dan jumlah mata kuliah semester 2 yang lulus tidak dipertimbangkan. Hasil yang diberikan berupa rekomendasi awal seleksi, bukan keputusan mutlak kelulusan beasiswa.

## 7. Penggunaan Alat Bantu AI

Dalam proses pembuatan tugas ini, AI digunakan sebagai alat bantu untuk memahami konsep sistem pakar, menyusun aturan IF-THEN, membantu pembuatan kode program Python, serta menyusun dokumentasi README.

Hasil yang diberikan oleh AI kemudian diperiksa dan disesuaikan kembali agar sesuai dengan kebutuhan tugas. Program dan aturan yang digunakan juga dipelajari kembali agar dapat dipahami dan dijalankan dengan baik.
