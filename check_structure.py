"""
Cek struktural ringan untuk student_template.ipynb - dijalankan otomatis oleh
GitHub Actions setiap Anda push (lihat .github/workflows/check_structure.yml).

Usage: python3 check_structure.py <folder-assignment>
  contoh: python3 check_structure.py assignment-01-convnet

Ini BUKAN penilaian akhir. Cek ini hanya menangkap kesalahan umum sebelum
dosen menilai secara batch:
  - NIM/Nama sudah diisi (bukan "??")
  - Tidak ada placeholder "??" yang tersisa
  - Semua cell exercise masih ada (tidak terhapus/berpindah), daftarnya
    dibaca dari <folder-assignment>/required_cells.json
  - Cell seed (AUTOGRADESEED0N) masih ada dan tidak diubah

Nilai/umpan balik akurasi atau loss tetap diberikan dosen lewat penilaian
batch terpisah, bukan dari status lulus/gagal cek ini.
"""

import json
import re
import sys
from pathlib import Path


def cell_source(cell) -> str:
    src = cell.get("source", "")
    return "".join(src) if isinstance(src, list) else src


PLACEHOLDER_RE = re.compile(r"(?<![\w'\"])\?\?(?![\w'\"])")
NIM_RE = re.compile(r"NIM\s*=\s*\?\?")
NAMA_RE = re.compile(r"Nama\s*=\s*\?\?")


def check_folder(folder: Path) -> list[str]:
    notebook_path = folder / "student_template.ipynb"
    required_cells_path = folder / "required_cells.json"

    if not notebook_path.exists():
        return [f"Notebook tidak ditemukan: {notebook_path}"]

    required_ids = []
    if required_cells_path.exists():
        required_ids = json.loads(required_cells_path.read_text(encoding="utf-8"))

    nb = json.loads(notebook_path.read_text(encoding="utf-8"))
    code_cells = [c for c in nb["cells"] if c.get("cell_type") == "code"]
    ids_present = {c.get("metadata", {}).get("id") for c in code_cells}

    errors = []

    missing_ids = [cid for cid in required_ids if cid not in ids_present]
    if missing_ids:
        errors.append(
            "Cell exercise berikut hilang/terhapus/id-nya berubah (jangan hapus, pindah, "
            f"atau copy-paste cell manual): {missing_ids}"
        )

    found_identity_cell = False
    for cell in code_cells:
        src = cell_source(cell)
        if "NIM" in src and "Nama" in src:
            found_identity_cell = True
            if NIM_RE.search(src):
                errors.append("NIM belum diisi (masih '??').")
            if NAMA_RE.search(src):
                errors.append("Nama belum diisi (masih '??').")
    if not found_identity_cell:
        errors.append("Cell identitas (NIM/Nama) tidak ditemukan.")

    offending = []
    for idx, cell in enumerate(code_cells):
        if PLACEHOLDER_RE.search(cell_source(cell)):
            offending.append(idx)
    if offending:
        errors.append(f"Masih ada placeholder '??' di cell code index: {offending}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 check_structure.py <folder-assignment>")
        return 2

    folder = Path(sys.argv[1])
    errors = check_folder(folder)

    if errors:
        print(f"[GAGAL] Cek struktur '{folder}' menemukan masalah:\n")
        for e in errors:
            print(f"  - {e}")
        print(
            "\nPerbaiki lalu push lagi. Ini cek struktur saja - akurasi/loss model dinilai "
            "terpisah oleh dosen."
        )
        return 1

    print(f"[OK] Cek struktur '{folder}' lolos: identitas terisi, tidak ada placeholder '??', "
          "semua cell exercise ada.")
    print("Catatan: ini bukan nilai akhir. Model akan dinilai terpisah oleh dosen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
