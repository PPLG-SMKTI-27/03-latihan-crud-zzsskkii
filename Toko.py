items = [
    {"nama":"pulpen", "stok":"40", "harga":"8000"},
    {"nama":"pensil", "stok":"20", "harga":"4000"},
    {"nama":"buku tulis", "stok":"20", "harga":"50000"},
    {"nama":"penghapus", "stok":"16", "harga":"3000"},
    {"nama":"penggaris", "stok":"5", "harga":"10000"},
]

def tampilkan_data():
    for i in range (len(items)):
      print(i+1, end=" ")
      print(items[i]["nama"],"\t""\t", items[i]["stok"],"\t""\t", items[i]["harga"])
     

def tambah_data():
    print("Menambahkan Data")
    nama = input("Nama Barang:")
    stok = input("Jumlah Stok:")
    harga = input("Harga Barang:")
    item = {"nama":nama, "stok":stok, "harga":harga}
    items.append(item)

def edit_data():
    print("Mengubah Data")
    indeks_ubah = int(input("Masukkan data menu yang ingin diubah berdasarkan nomor:"))-1
    nama = input("Nama Barang:")
    stok = input("Jumlah Stok:")
    harga = input("Harga Barang:")

    data_ubah = {"nama":nama,"stok":stok,"harga":harga}
    items[indeks_ubah]= data_ubah

    print("Data berhasil diubah")
    

def hapus_data():
    print("Menghapus Data")
    data_hapus = int(input("Masukkan Nomor Menu Yang Ingin Dihapus: "))-1
    del items[data_hapus]
    menu()

def menu():
    while True :

        print(" ======== Menu ======== ")
        print("1. Tampilkan Data Barang")
        print("2. Tambah Data Barang")
        print("3. Edit Data Barang")
        print("4. Hapus Data Barang")
        print("[x]Keluar")
        menu = input("Masukkan Pilihan Menu:")


        match menu:

            case"1":
                tampilkan_data()

            case"2":
                tambah_data()
            
            case"3":
                edit_data()

            case"4":
                hapus_data()

            case "x" | "X":
                exit()

            case _:
                print("Input harus bilangan(1-4) atau huruf \'x\'")

menu()




