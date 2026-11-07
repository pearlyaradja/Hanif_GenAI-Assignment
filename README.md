# Tugas GenAI - Template Mahasiswa

## Cara mendapatkan repo Anda sendiri dari template ini

**Jangan kerjakan langsung di repo template ini.** Anda harus membuat salinan
repo ini dulu, lalu bekerja di salinan Anda sendiri.

1. Pastikan Anda sudah login GitHub dan sudah di-invite jadi anggota organisasi
   `AI-IF-TelU` (cek email/notifikasi GitHub Anda, klik accept kalau belum).
2. Buka halaman repo ini: **https://github.com/AI-IF-TelU/genai-assignment-template**
3. Klik tombol hijau **`Use this template`** di kanan atas, lalu pilih
   **`Create a new repository`**.
4. Di form yang muncul:
   - **Owner**: pilih `AI-IF-TelU` (organisasi), **bukan** akun pribadi Anda.
   - **Repository name**: ikuti `NIM-nama-genai`.
   - **Visibility**: pilih **Private**.
   - Klik **Create repository**.
5. Repo baru akan muncul di `https://github.com/AI-IF-TelU/<nama-repo-Anda>`.
   **Inilah repo Anda** - dosen menilai langsung dari isi repo ini, jadi semua
   pekerjaan (semua tugas, Task 1/2/3/dst) dikerjakan dan di-push ke repo ini,
   bukan ke repo template.

Kalau tombol `Use this template` tidak muncul atau Anda tidak bisa membuka
repo ini sama sekali, kemungkinan Anda belum di-invite atau undangannya belum
di-accept - hubungi dosen, jangan coba akses lewat cara lain.

## Daftar tugas

Repo hasil `Use this template` Anda berisi beberapa folder tugas. Kerjakan
sesuai yang diumumkan dosen (biasanya satu per satu, tidak sekaligus):

| Folder | Tugas |
|---|---|
| `assignment-01-convnet/` | Task 1 - ConvNet (PyTorch, CIFAR-10) |
| `assignment-02-autoregressive/` | Task 2 - Char-LSTM, PixelRNN, PixelCNN (PyTorch) |
| `assignment-03-network-viz/` | Task 3 - Saliency Maps, Class Visualization, Fooling Images (SqueezeNet) + RNN Hidden Activation (DistilBERT) |
| `assignment-04-style-transfer/` | Task 4 - Neural Style Transfer (SqueezeNet) |
| `assignment-05-vae/` | Task 5 - Convolutional AutoEncoder & Variational AutoEncoder (MNIST) |
| `assignment-06-gan/` | Task 6 - Generative Adversarial Network: Vanilla GAN, LS-GAN, DC-GAN (MNIST) |

## Mendapatkan tugas baru (Task 7 dst.) tanpa bikin repo baru

Kalau dosen menambah folder assignment baru di template ini (misal
`assignment-07-xxx/` - persis seperti yang terjadi saat Task 4, 5, dan 6,
`assignment-04-style-transfer/`, `assignment-05-vae/`, dan
`assignment-06-gan/`, ditambahkan setelah tugas-tugas sebelumnya sudah
berjalan) setelah Anda sudah punya repo sendiri, **Anda tidak perlu bikin
repo baru / `Use this template` lagi**. Repo Anda sekarang sudah berisi
pekerjaan tugas sebelumnya, jadi
cukup "tarik" folder baru itu ke repo Anda yang sudah ada:

### Cara A - pakai git (direkomendasikan, aman walau sudah banyak file yang Anda ubah)

Jalankan di terminal, di dalam clone lokal repo Anda (sekali per repo, lewati
langkah 1-2 kalau sudah pernah):

```bash
# 1. Clone repo Anda sendiri (kalau belum ada secara lokal)
git clone https://github.com/AI-IF-TelU/<nama-repo-Anda>.git
cd <nama-repo-Anda>

# 2. Tambahkan repo template sebagai remote tambahan (sekali saja)
git remote add template https://github.com/AI-IF-TelU/genai-assignment-template.git

# 3. Setiap kali dosen mengumumkan ada tugas baru:
git fetch template
git merge template/main --allow-unrelated-histories -m "Sync tugas baru dari template"
```

Langkah 3 akan menambahkan folder tugas baru secara otomatis **tanpa
menyentuh folder tugas lama yang sudah Anda kerjakan**. Kemungkinan besar
Git akan melaporkan **conflict** pada file yang sudah pernah Anda ubah
(misalnya `assignment-01-convnet/student_template.ipynb` yang sudah Anda
isi) - itu normal dan aman, bukan berarti rusak. Selesaikan dengan:

```bash
# Untuk tiap file conflict yang MEMANG sudah Anda kerjakan, pertahankan versi Anda:
git checkout --ours -- <path-file-yang-conflict>
git add <path-file-yang-conflict>

# Setelah semua conflict diselesaikan:
git commit
git push
```

(Sudah diuji: folder tugas baru masuk bersih tanpa conflict, dan file yang
sudah Anda kerjakan tetap utuh setelah `--ours` - yang conflict cuma file
yang memang Anda ubah, folder lama yang belum disentuh tidak akan konflik.)

### Cara B - tanpa git, lewat GitHub web UI (kalau tidak familiar git)

1. Buka folder tugas baru di repo template:
   `https://github.com/AI-IF-TelU/genai-assignment-template/tree/main/assignment-07-xxx`
   (nama folder sesuai pengumuman dosen).
2. Buka tiap file di folder itu, klik tombol **Download raw file** untuk
   menyimpannya ke komputer Anda (minimal `student_template.ipynb`).
3. Di repo Anda sendiri, klik **Add file -> Upload files**, lalu di kotak
   path tujuan ketik nama folder tugas baru (misal `assignment-07-xxx/`)
   sebelum nama file, lalu commit.

Cara B hanya menyalin file yang Anda unduh - kalau folder tugas baru punya
banyak file pendukung, Cara A (git) lebih praktis.

## Langkah mengerjakan tiap tugas

Lakukan ini di **repo Anda sendiri** (hasil `Use this template`), bukan di
repo template.

1. Buka `<folder-tugas>/student_template.ipynb` **dari repo Anda** di Google
   Colab: *File -> Open notebook -> GitHub*, cari repo Anda (bukan
   `genai-assignment-template`) - atau clone repo Anda lalu upload manual
   file `.ipynb`-nya ke Colab.
2. Kerjakan semua cell bertanda `EXERCISE`:
   - Isi `NIM` dan `Nama` (`Nama = "Budi"`, NIM tanpa tanda kutip), bukan `??`.
   - Ganti **semua** `??`. Tidak boleh tersisa satu pun.
   - **Jangan menghapus/mengubah cell yang diberi komentar "JANGAN diubah"**
     (cell seed, misalnya `AUTOGRADESEED01`/`02`/`03`) - cell ini menghitung
     parameter unik dari NIM Anda dan dipakai untuk mengecek keaslian jawaban
     Anda. Lihat tabel di bawah untuk tahu apa yang dipersonalisasi di tiap
     tugas.
   - Jangan menghapus/menambah/memindah cell exercise lain, dan jangan ubah
     id cell (jangan copy-paste ulang cell dari notebook lain atau dari
     teman).
3. Jalankan seluruh notebook di Colab (*Runtime -> Run all*) dan pastikan
   tidak ada error. Target akurasi/loss ada di masing-masing cell
   `EXPECTED OUTPUT` di notebook (informasi saja, bukan patokan lulus/gagal
   otomatis di sini).
4. **Simpan/unduh notebook dari Colab** (*File -> Download -> Download
   .ipynb*), dengan output hasil eksekusi tetap tersimpan di dalamnya (jangan
   "Clear all outputs" sebelum mengunduh).
5. **Push file itu ke repo Anda sendiri**, menimpa
   `<folder-tugas>/student_template.ipynb` (lewat GitHub web UI *Add file ->
   Upload files*, atau `git add` / `commit` / `push` dari lokal kalau sudah
   terbiasa pakai git). Ini yang jadi pengumpulan Anda - tidak ada langkah
   submit terpisah.
6. Push memicu cek otomatis (tab **Actions** di repo Anda), dua tahap
   berurutan per folder tugas:
   1. **Cek struktur** - placeholder `??` sudah diganti semua, identitas
      terisi, cell tidak terhapus. Cepat (hitungan detik).
   2. **Quick check** - kalau cek struktur lolos, notebook Anda dijalankan
      beneran, tapi cuma bagian yang "murah" (definisi fungsi exercise +
      sanity-check bawaan notebook yang pakai data/iterasi kecil). Ini
      **mendeteksi bug logika** (salah formula, salah dimensi tensor, dll)
      yang tidak ketahuan dari cek struktur saja - karena cek struktur cuma
      baca teks, tidak pernah benar-benar menjalankan kode Anda. Training
      penuh (yang makan waktu lama) **tidak** dijalankan di sini, jadi
      quick check tetap cepat (biasanya di bawah 1 menit).
   Kalau salah satu gagal (tanda silang merah), klik run yang gagal untuk
   baca pesan errornya - pesannya menyebutkan persis exercise/cell mana yang
   bermasalah dan error aslinya (mis. `NameError`, `RuntimeError: shape
   mismatch`, dst). Perbaiki, lalu push lagi sebelum tenggat.
7. **Quick check lolos bukan berarti nilai Anda bagus** - itu cuma
   mengonfirmasi exercise Anda jalan tanpa error pada skala kecil. Akurasi/
   loss sesungguhnya (training penuh/skala besar) tetap dinilai dosen lewat
   penilaian batch terpisah setelah tenggat, bukan otomatis dari tab
   Actions. Tunggu pengumuman dosen soal cara melihat hasil.

   Catatan: quick check tidak selalu bisa mengecek 100% exercise (ada
   beberapa bagian yang hanya praktis dicek lewat training penuh, misalnya
   Part 4.2 di Task 1 yang menggabungkan arsitektur + training dalam satu
   cell) - lolos quick check itu sinyal bagus, tapi bukan jaminan mutlak.

### Apa yang dipersonalisasi per NIM di tiap tugas

| Tugas | Cell seed | Yang dipersonalisasi |
|---|---|---|
| Task 1 | `AUTOGRADESEED01` | `channel_1`/`channel_2` di Part 4.2 |
| Task 2 | `AUTOGRADESEED02` | `embedding_dim`/`hidden_dim` di Part 1 (Char-LSTM) |
| Task 3 | `AUTOGRADESEED03` | `TARGET_CLASS_ID` di Part 4 (Fooling Images) - kelas ImageNet yang wajib Anda jadikan target |
| Task 4 | `AUTOGRADESEED04` | `CONTENT_WEIGHT_MULT` di sanity check `AUTOGRADECHECK04` - pengali `content_weight` unik (params1/2/3 yang hasil visualnya dibandingkan ke Expected Output TIDAK dipersonalisasi) |
| Task 5 | `AUTOGRADESEED05` | `BETA_MULT` di sanity check `AUTOGRADECHECK05` - pengali bobot KL (beta) unik (training 50 epoch Part 1/2 TIDAK dipersonalisasi, supaya Train/Val Loss semua mahasiswa bisa dibandingkan ke Expected Output yang sama) |
| Task 6 | `AUTOGRADESEED06` | `GEN_LOSS_MULT` di sanity check `AUTOGRADECHECK06` - pengali loss generator unik (training 10 epoch Part 1/2/3 TIDAK dipersonalisasi, supaya hasil gambar semua mahasiswa bisa dibandingkan ke Expected Output yang sama) |

## Penyebab gagal cek struktur yang umum

| Pesan | Arti |
|---|---|
| `Masih ada placeholder '??'` | Ada `??` yang belum diganti |
| `Cell exercise berikut hilang/terhapus` | Cell exercise terhapus/id berubah; ambil ulang dari template, jangan copy-paste manual dari notebook lain |
| `NIM belum diisi` / `Nama belum diisi` | Isi cell identitas dengan benar |
| `Cell identitas tidak ditemukan` | Cell NIM/Nama terhapus |

## Penyebab gagal quick check yang umum

Quick check gagal dengan pesan `[GAGAL] Quick check berhenti di: <nama exercise> (cell id: ...)`
diikuti error Python asli. Beberapa yang sering muncul:

| Error | Arti |
|---|---|
| `NameError: name 'NIM' is not defined` | Cell identitas belum dijalankan/terhapus - cek ulang cell `NIM`/`Nama` |
| `RuntimeError: ... shape ...` / `size mismatch` | Dimensi tensor salah - cek urutan argumen (mis. `gather(1, ...)` bukan `gather(0, ...)`), urutan matrix multiplication, atau parameter `kernel_size`/`padding` |
| `AssertionError` dari cell `AUTOGRADECHECK...` | Sanity check bawaan notebook gagal - baca pesan assert-nya, biasanya menyebutkan nilai yang diharapkan vs yang didapat |
| `AttributeError: 'NoneType' object has no attribute ...` | Ada baris yang lupa diisi (variabel masih `None` bawaan Python, bukan hasil pemanggilan fungsi) |
| Error lain (`TypeError`, `IndexError`, dst) | Baca traceback-nya - biasanya menunjuk tepat ke baris exercise yang salah |

## Aturan penggunaan AI

Ikuti aturan yang diumumkan dosen di kelas/LMS soal penggunaan AI (ChatGPT/Claude/dll)
untuk tugas ini. Kalau diizinkan dengan syarat (misal wajib mencatat prompt), penuhi
syarat tersebut.
