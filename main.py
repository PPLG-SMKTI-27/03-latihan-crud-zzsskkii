# data buku
books = [
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":"", "tanggal_kembali":""},
]

def tampilkan_data():
        print("---=== DATA BUKU ===---")
        if not books:
            print("Tidak ada data buku.")
         

        for book in books:
            print(f"isbn: {book['isbn']}, Judul: {book['judul']}, Pengarang: {book['pengarang']}, Jumlah: {book['jumlah']}, Terpinjam: {book['terpinjam']}")


def tambah_data():
    isbn = input("Masukkan isbn: ")
    judul = input("Masukkan Judul: ")
    pengarang = input("Masukkan Pengarang: ")
    jumlah = int(input("Masukkan Jumlah: "))
    
    
    for book in books:
        if book['isbn'] == isbn:
            print("Buku dengan ISBN ini sudah ada.")
            return
    
  
    books.append({"isbn": isbn, "judul": judul, "pengarang": pengarang, "jumlah": jumlah, "terpinjam": 0})
    print("Buku berhasil ditambahkan.")


def edit_data():
    isbn = input("Masukkan ISBN buku yang ingin diedit: ")
    for book in books:
        if book['isbn'] == isbn:
            judul = input("Masukkan Judul baru: ")
            pengarang = input("Masukkan Pengarang baru: ")
            jumlah = int(input("Masukkan Jumlah baru: "))
            book['judul'] = judul
            book['pengarang'] = pengarang
            book['jumlah'] = jumlah
            print("Data buku berhasil diubah.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")

def hapus_data():
    isbn = input("Masukkan ISBN buku yang ingin dihapus: ")
    for book in books:
        if book['isbn'] == isbn:
            books.remove(book)
            print("Buku berhasil dihapus.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")

def tampilkan_peminjaman():
    print("---=== DATA PEMINJAMAN ===---")
    if not records:
        print("Tidak ada data peminjaman.")
        return

    for record in records:
        print(f"isbn: {record['isbn']}, Status: {record['status']}, Tanggal Pinjam: {record['tanggal_pinjam']}, Tanggal Kembali: {record['tanggal_kembali']}")  

def tampilkan_belum():
    print("---=== PEMINJAMAN BELUM KEMBALI ===---")
    if not records:
        print("Tidak ada data peminjaman.")
        return

    for record in records:
        if record['status'] == "Belum":
            print(f"isbn: {record['isbn']}, Tanggal Pinjam: {record['tanggal_pinjam']}, Tanggal Kembali: {record['tanggal_kembali']}")

def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    for book in books:
        if book['isbn'] == isbn:
            if book['jumlah'] > book['terpinjam']:
                book['terpinjam'] += 1
                records.append({"isbn": isbn, "status": "Belum", "tanggal_pinjam": "2025-03-21", "tanggal_kembali": ""})
                print("Buku berhasil dipinjam.")
            else:
                print("Buku sudah habis dipinjam.")
            return
    print("Buku ini tidak ditemukan.")

def pengembalian():
    isbn = input("Masukkan ISBN buku yang ingin dikembalikan: ")
    balik_buku = input("tanggal buku pas mau di kembalikan:")
    for book in books:
        if book['isbn'] == isbn:
            if book['terpinjam'] > 0:
                book['terpinjam'] -= 1
                for record in records:
                    if record['isbn'] == isbn and record['status'] == "Belum":
                        record['status'] = "Selesai"
                        record['tanggal_kembali'] = balik_buku
                        break
                print("Buku berhasil dikembalikan.")
            else:
                print("Buku ini tidak sedang dipinjam.")
            return
    print("Buku ini tidak ditemukan.")

while True:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    if menu == "1":
        tampilkan_data()

    elif menu == "2":
        tambah_data()

    elif menu == "3":
        edit_data()

    elif menu == "4":
        hapus_data()

    elif menu == "5":
        tampilkan_peminjaman()

    elif menu == "6":
        tampilkan_belum()

    elif menu == "7":
        peminjaman()

    elif menu == "8":
        pengembalian()
        
    elif menu.lower() == "x":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
   
    input("Tekan Enter untuk melanjutkan...")