"""
Quick check: jalankan SEBAGIAN notebook (cell murah: import, definisi fungsi,
dan sanity-check bawaan notebook yang pakai data/iterasi kecil) untuk
memverifikasi exercise Anda **benar secara fungsional** - tanpa menjalankan
training penuh yang mahal (itu baru dijalankan dosen saat penilaian batch).

Ini BUKAN nilai akhir dan BUKAN pengganti cek struktur (`check_structure.py`).
Kalau quick check ini lolos, exercise Anda kemungkinan besar sudah benar
secara logika - tapi akurasi/loss akhir tetap ditentukan training penuh yang
dinilai dosen secara terpisah.

Usage: python3 quick_check.py <folder-assignment>
  contoh: python3 quick_check.py assignment-01-convnet
"""

import json
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


def load_quick_check_cells(folder: Path):
    path = folder / "quick_check_cells.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def build_filtered_notebook(nb, allowed_ids):
    """Salinan notebook yang hanya berisi code cell dalam allowed_ids (urutan asli
    dipertahankan). Markdown dan cell lain (termasuk training penuh) dibuang."""
    filtered = nbformat.v4.new_notebook()
    filtered.metadata = nb.metadata
    for cell in nb.cells:
        if cell.get("cell_type") != "code":
            continue
        cid = cell.get("metadata", {}).get("id")
        if cid in allowed_ids:
            filtered.cells.append(cell)
    return filtered


def run(folder: Path) -> int:
    notebook_path = folder / "student_template.ipynb"
    cells_spec = load_quick_check_cells(folder)

    if not notebook_path.exists():
        print(f"[GAGAL] Notebook tidak ditemukan: {notebook_path}")
        return 1

    if not cells_spec:
        print(f"[DILEWATI] Tidak ada quick_check_cells.json untuk '{folder}', "
              "quick check tidak dijalankan untuk assignment ini.")
        return 0

    labels = {c["id"]: c["label"] for c in cells_spec}
    allowed_ids = list(labels.keys())

    nb = nbformat.read(notebook_path, as_version=4)
    filtered = build_filtered_notebook(nb, allowed_ids)

    found_ids = {c.metadata.get("id") for c in filtered.cells}
    missing = [cid for cid in allowed_ids if cid not in found_ids]
    if missing:
        print(f"[GAGAL] Cell berikut hilang dari notebook (seharusnya ada untuk "
              f"quick check): {missing}")
        print("Kemungkinan cell terhapus/id berubah - cek juga hasil check_structure.py.")
        return 1

    client = NotebookClient(
        filtered,
        timeout=600,
        kernel_name="python3",
        allow_errors=False,  # berhenti di cell pertama yang error
        resources={"metadata": {"path": str(notebook_path.parent)}},
    )

    print(f"Menjalankan quick check '{folder}' ({len(filtered.cells)} cell murah, "
          "training penuh/download besar dilewati)...\n")

    try:
        client.execute()
    except CellExecutionError as e:
        failed_id = None
        for cell in filtered.cells:
            if cell.get("outputs") and any(
                o.get("output_type") == "error" for o in cell["outputs"]
            ):
                failed_id = cell.get("metadata", {}).get("id")
                break
        label = labels.get(failed_id, failed_id or "tidak diketahui")
        print(f"[GAGAL] Quick check berhenti di: {label} (cell id: {failed_id})\n")
        print(str(e)[-2000:])
        print(
            "\nIni artinya ada bug di implementasi exercise tersebut (bukan "
            "sekadar placeholder '??' yang belum diisi - itu sudah lolos cek "
            "struktur). Perbaiki logikanya, lalu push lagi."
        )
        return 1

    print(f"[OK] Quick check lolos: {len(filtered.cells)} cell berhasil dieksekusi "
          "tanpa error.")
    print(
        "Catatan: ini baru verifikasi fungsional cepat, BUKAN nilai akhir. "
        "Akurasi/loss sesungguhnya (training penuh) tetap dinilai terpisah oleh "
        "dosen."
    )
    return 0


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 quick_check.py <folder-assignment>")
        return 2
    return run(Path(sys.argv[1]))


if __name__ == "__main__":
    sys.exit(main())
