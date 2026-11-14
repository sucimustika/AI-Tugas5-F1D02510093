
import json

# Membaca aturan dari file JSON
with open("kb_beasiswa.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Tampilan awal program
print("=" * 55)
print("       SISTEM PAKAR KLASIFIKASI KELAYAKAN")
print("                PENERIMAAN BEASISWA")
print("=" * 55)

print("\nJawablah pertanyaan berikut dengan:")
print("y = Ya")
print("t = Tidak")

# Menyimpan fakta pengguna
fakta = set()

# Proses tanya jawab
print("\n" + "-" * 55)
print("                 PERTANYAAN")
print("-" * 55)

for nomor, pertanyaan in enumerate(data["pertanyaan"], start=1):

    while True:
        jawaban = input(
            f"\n{nomor}. {pertanyaan['teks']} (y/t): "
        ).lower().strip()

        if jawaban == "y":
            if "fakta_ya" in pertanyaan:
                fakta.add(pertanyaan["fakta_ya"])
            break

        elif jawaban == "t":
            if "fakta_tidak" in pertanyaan:
                fakta.add(pertanyaan["fakta_tidak"])
            break

        else:
            print("Jawaban tidak valid! Masukkan y atau t.")

# Menyimpan fakta awal
fakta_awal = set(fakta)

# Proses Forward Chaining
aturan_dipakai = []
aturan_sudah_dijalankan = set()

while True:

    ada_fakta_baru = False

    for aturan in data["aturan"]:

        if aturan["id"] in aturan_sudah_dijalankan:
            continue

        syarat = aturan["jika"]

        # Memeriksa kondisi AND dan OR
        if aturan["mode"] == "dan":
            cocok = all(item in fakta for item in syarat)

        elif aturan["mode"] == "atau":
            cocok = any(item in fakta for item in syarat)

        else:
            cocok = False

        # Jika aturan terpenuhi
        if cocok:

            hasil = aturan["maka"]

            aturan_sudah_dijalankan.add(aturan["id"])
            aturan_dipakai.append(aturan)

            if hasil not in fakta:
                fakta.add(hasil)
                ada_fakta_baru = True

    # Berhenti jika tidak ada fakta baru
    if not ada_fakta_baru:
        break

# Menentukan rekomendasi
rekomendasi = [
    item for item in fakta
    if item.startswith("Rekomendasi:")
]

# Jika belum ada rekomendasi, berikan evaluasi lanjutan
if not rekomendasi:
    hasil_evaluasi = "Rekomendasi: Perlu Evaluasi Lanjutan"
    fakta.add(hasil_evaluasi)
    rekomendasi.append(hasil_evaluasi)

# Menampilkan hasil akhir
print("\n")
print("=" * 55)
print("             HASIL KELAYAKAN BEASISWA")
print("=" * 55)

print("\nFakta Awal:")

if fakta_awal:
    for item in sorted(fakta_awal):
        print("-", item)
else:
    print("- Tidak ada fakta yang bernilai ya.")

# Menampilkan rekomendasi
print("\nHasil Rekomendasi:")

for hasil in rekomendasi:
    print("->", hasil)

# Menampilkan alasan berdasarkan hasil
print("\nAlasan:")

if "Rekomendasi: Layak Beasiswa Penuh" in rekomendasi:

    print("- Persyaratan akademik telah terpenuhi.")
    print("- Administrasi keuangan dinyatakan lancar.")
    print("- Jumlah mata kuliah yang disetujui memenuhi syarat.")

elif "Rekomendasi: Tidak Layak / Ditolak" in rekomendasi:

    print("- Terdapat kendala akademik atau keuangan.")
    print("- Persyaratan kelayakan belum terpenuhi.")
    print("- Diperlukan perbaikan sesuai ketentuan beasiswa.")

else:

    print("- Belum seluruh persyaratan beasiswa terpenuhi.")
    print("- Belum ditemukan alasan untuk keputusan penolakan.")
    print("- Diperlukan pemeriksaan dan evaluasi lebih lanjut.")

# Menampilkan jejak Forward Chaining
print("\n" + "-" * 55)
print("             JEJAK FORWARD CHAINING")
print("-" * 55)

if aturan_dipakai:

    for aturan in aturan_dipakai:

        print("\nAturan:", aturan["id"])
        print("Mode:", aturan["mode"].upper())
        print("Syarat:", ", ".join(aturan["jika"]))
        print("Kesimpulan:", aturan["maka"])
        print("Sumber:", aturan["sumber"])

else:
    print("Tidak ada aturan yang terpenuhi.")

# Menampilkan sumber referensi
print("\n" + "-" * 55)
print("               SUMBER REFERENSI")
print("-" * 55)

for kode, sumber in data["sumber"].items():
    print(f"\n{kode}: {sumber}")

# Menampilkan batas keberlakuan
print("\n" + "-" * 55)
print("          BATAS KEBERLAKUAN SISTEM")
print("-" * 55)

print(data["batas"])

print("\n" + "=" * 55)
print("Terima kasih telah menggunakan sistem pakar!")
print("=" * 55)
