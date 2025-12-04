# Data disimpan dalam list bersisi dictionary
catatan = []

# Fungsi untuk memuat data dari file
def muat_data():
    try:
        with open("keuangan.txt", "r") as f:
            for baris in f:
                tanggal, keterangan, tipe, jumlah = baris.strip().split("|")
                catatan.append({
                    "tanggal": tanggal,
                    "keterangan": keterangan,
                    "tipe": tipe,
                    "jumlah": int(jumlah)
                })
    except FileNotFoundError:
        pass  # File belum ada → tidak masalah

# Fungsi untuk menyimpan data ke file
def simpan_data():
    with open("keuangan.txt", "w") as f:
        for c in catatan:
            f.write(f"{c['tanggal']}|{c['keterangan']}|{c['tipe']}|{c['jumlah']}\n")

# Tambah data
def tambah_data():
    print("\n=== Tambah Catatan Keuangan ===")
    tanggal = input("Tanggal (dd/mm/yyyy): ")
    keterangan = input("Keterangan: ")
    tipe = input("Tipe (masuk/keluar): ").lower()
    jumlah = input("Jumlah (angka): ")

    if not jumlah.isdigit():
        print("Jumlah harus berupa angka!")
        return

    catatan.append({
        "tanggal": tanggal,
        "keterangan": keterangan,
        "tipe": tipe,
        "jumlah": int(jumlah)
    })

    simpan_data()
    print("Data berhasil ditambahkan!\n")

# Tampilkan semua data
def tampilkan_data():
    print("\n=== Daftar Catatan Keuangan ===")
    if len(catatan) == 0:
        print("Belum ada catatan.\n")
        return

    for i, c in enumerate(catatan):
        print(f"{i+1}. [{c['tanggal']}] {c['keterangan']} - {c['tipe']} - Rp {c['jumlah']}")
    print()

# Edit data
def edit_data():
    tampilkan_data()
    if len(catatan) == 0:
        return

    try:
        idx = int(input("Pilih nomor catatan yang ingin diedit: ")) - 1
        if idx < 0 or idx >= len(catatan):
            print("Nomor tidak valid!")
            return
    except ValueError:
        print("Input harus angka!")
        return

    print("\nKosongkan input jika tidak ingin mengubah.")
    tanggal = input("Tanggal baru: ")
    keterangan = input("Keterangan baru: ")
    tipe = input("Tipe baru (masuk/keluar): ")
    jumlah = input("Jumlah baru: ")

    if tanggal != "":
        catatan[idx]["tanggal"] = tanggal
    if keterangan != "":
        catatan[idx]["keterangan"] = keterangan
    if tipe != "":
        catatan[idx]["tipe"] = tipe
    if jumlah.isdigit():
        catatan[idx]["jumlah"] = int(jumlah)

    simpan_data()
    print("Data berhasil diperbarui!\n")

# Hapus data
def hapus_data():
    tampilkan_data()
    if len(catatan) == 0:
        return

    try:
        idx = int(input("Pilih nomor yang ingin dihapus: ")) - 1
        if idx < 0 or idx >= len(catatan):
            print("Nomor tidak valid!")
            return
    except ValueError:
        print("Input harus angka!")
        return

    del catatan[idx]
    simpan_data()
    print("Data berhasil dihapus!\n")

# Cari / filter data
    key = input("\nMasukkan kata kunci pencarian: ").lower()

    hasil = []
    for c in catatan:
        if key in c["tanggal"].lower() or key in c["keterangan"].lower() or key in c["tipe"].lower():
            hasil.append(c)

    print("\n=== Hasil Pencarian ===")
    if len(hasil) == 0:
        print("Tidak ada data ditemukan.\n")
    else:
        for i, c in enumerate(hasil):
            print(f"{i+1}. [{c['tanggal']}] {c['keterangan']} - {c['tipe']} - Rp {c['jumlah']}")
        print()

# Menu Utama
def menu():
    muat_data()
    while True:
        print("=== CATATAN KEUANGAN HARIAN ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Cari / Filter Data")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            edit_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            cari_data()
        elif pilihan == "6":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!\n")

# Jalankan program
menu()
