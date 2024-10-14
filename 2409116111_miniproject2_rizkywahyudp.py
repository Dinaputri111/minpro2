from prettytable import PrettyTable

Daftar_obat = [
    {"ID": "DO1", "Nama": "Paracetamol", "Harga": "10000", "Stock":"500"},
    {"ID": "DO2", "Nama": "Amoxcillin", "Harga": "5000", "Stock":"150"},
    {"ID": "DO3", "Nama": "CTM", "Harga": "15000", "Stock":"50"},
    {"ID": "DO4", "Nama": "Alluporinol", "Harga": "10000", "Stock":"100"},
    {"ID": "DO5", "Nama": "Combantrin", "Harga": "28000", "Stock":"50"},
    {"ID": "DO6", "Nama": "imboost", "Harga": "38000", "Stock":"400"},
]

keranjang = []
def tampil_obat():
    tabel = PrettyTable()
    tabel.title = "DAFTAR OBAT"
    tabel.field_names = ["ID","Nama","Harga","Stock"]
    for obat in Daftar_obat:
        tabel.add_row([obat["ID"], obat["Nama"], obat["Harga"], obat["Stock"]])
    print(tabel)

def tambah_obat():
    try:
        ID = input("Masukkan ID obat: ")
        Nama = input("Masukkan nama obat: ")
        Harga= int(input("Masukkan harga obat: Rp."))
        Stock= int(input("Masukkan stock obat: "))
        Daftar_obat.append({"ID": ID, "Nama": Nama, "Harga": Harga, "Stock": Stock})
        print("Obat berhasil ditambahkan!")
    except Exception as T:
        print("Harga dan Stock harus berupa angka!")

def update_obat():
    tampil_obat()
    ID = input("Masukkan id obat: ")
    for obat in Daftar_obat:
        if ID == obat["ID"]:
            print(f"Nama Obat: {obat['Nama']}")
            nama = input("Masukkan Nama obat baru: ") or obat["Nama"]

            print(f"Harga lama: {obat['Harga']}")
            harga = int(input("Masukkan Harga Obat baru: Rp.") or obat["Harga"])

            print(f"Stock lama: {obat['Stock']}")
            stock = int(input("Masukkan Stock Obat baru: ") or obat["Stock"])

            obat["Nama"] = nama
            obat["Harga"] = harga
            obat["Stock"] = stock
            print("Obat berhasil di update.")
            return
    print("ID obat tidak terdaftar!")

def hapus_obat():
    ID = input("Masukkan ID Obat: ")
    for obat in Daftar_obat:
        if ID == obat["ID"]:
            Daftar_obat.remove(obat)
            print("Obat berhasil dihapus!")
            return
    print("ID Obat Tidak Ditemukan!")

def tambah_keranjang():
    ID = input("Masukkan ID obat yang ingin dibeli: ")
    for obat in Daftar_obat:
        if obat["ID"] == ID:
            try:
                jumlah = int(input("Masukkan jumlah pembelian: "))
                if jumlah > int(obat["Stock"]):
                    print("Stok tidak mencukupi.")
                else: 
                    keranjang.append({"Nama": obat["Nama"],"Harga":obat["Harga"],"Jumlah":jumlah})
                    obat["Stock"] = str(int(obat["Stock"]) - jumlah)
                    print("Obat telah berhasil di tambah ke keranjang.")
            except ValueError:
                print("Jumlah pembelian harus berupa angka!")
            return
    print("Obat tidak ada dalam daftar obat!")

def tampil_keranjang():
    if not keranjang:
        print("Keranjang masih kosong, silahkan berbelanja.")
        return 0
    
    tabel = PrettyTable()
    tabel.title = "KERANJANG WICY"
    tabel.field_names = ["Nama obat","Harga","Jumlah","Total Harga"]

    total_pembayaran = 0
    for barang in keranjang:
        harga = int(barang["Harga"].replace("Rp.", ""))
        jumlah = barang["Jumlah"]
        total_harga = harga * jumlah
        total_pembayaran += total_harga
        tabel.add_row([barang["Nama"], barang["Harga"], barang["Jumlah"],f"Rp.{total_harga}"])
    print(tabel)
    print("Total pembelian: Rp.",total_pembayaran)
    return total_pembayaran

def pembayaran(total_pembayaran):
    print("-------PILIH METODE PEMBAYARAN---------")
    print("1. QRIS")
    print("2. TRANSFER ")
    print("3. COD")

    while True:
        pilihan = input("Masukkan pilihan metode pembayaran: ")
        if pilihan == "1":
            print("Total pembayaran anda Rp.",str(total_pembayaran),"pembayaran melalui COD telah sukses.")
            break
        elif pilihan == "2":
            print("Total pembayaran anda Rp.",str(total_pembayaran),"pembayaran melalui COD telah sukses.")
            break
        elif pilihan == "3":
            print("Total pembayaran anda Rp.",str(total_pembayaran),"pembayaran melalui COD telah sukses.")
            break
        else:
            print("Pilihan tidak valid!")

    keranjang.clear()

def admin():
    print("----------------WINTER PHARMACY ADMIN------------------")
    print("1. Daftar Obat")
    print("2. Tambah Obat ")
    print("3. Edit Obat")
    print("4. Hapus Obat")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "1":
        tampil_obat()
    elif pilihan == "2":
        tambah_obat()
    elif pilihan == "3":
        update_obat()
    elif pilihan == "4":
        hapus_obat()
    elif pilihan == "5":
        print("Keluar dari program Admin, terima kasih!")
        return False
    else:
        print("Pilihan tidak valid!.") 
    return True

def pembeli():
    while True:
        tampil_obat()
        print("----------------WINTER PHARMACY ADMIN------------------")
        print("1. Keranjang")
        print("2. Tampil Keranjang ")
        print("3. Pembayaran")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == "1":
            tambah_keranjang()
        elif pilihan == "2":
            tampil_keranjang()
        elif pilihan == "3":
            total_harga = tampil_keranjang()
            pembayaran(total_harga)
        elif pilihan == "4":
            print("Keluar dari program Customer, terima kasih!")
            return False
        else:
            print("Pilihan tidak valid!.")
            return True

loginData = [["farmasi", "obatsehat"],
            ["dokterobat", "obatku"],
            ["apoteker", "kapsulobat"]]

def check_login_admin(username, password):
    for user in loginData:
        if user[0] == username and user[1] == password:
            return True
        

def check_login_pembeli(username, password):
    return True

def main():
    while True:
        pilihan = input("Apakah anda ingin login sebagai Admin/Customer? :")
    
        if pilihan.lower() == "admin":
            while True:
                username = input("Masukkan nama Username: ")
                password = input("Masukkan Password: ")
                if check_login_admin(username, password):
                    print("-------------SELAMAT DATANG DI WINTER PHARMACY-------------")
                    print("-------------Anda Login Sebagai Admin WICY!----------------")
                    while admin():
                        pass
                    break
                else:
                    print("Login gagal, silahkan memasukkan username dan password dengan benar.")
        elif pilihan.lower() == "customer":
            while True:
                username = input("Masukkan nama Username: ")
                password = input("Masukkan Password: ")
                if check_login_pembeli(username, password):
                    print("-------------SELAMAT DATANG DI WINTER PHARMACY-------------")
                    print(username+" Anda Login sebagai customer WICY")
                    print("------Kesehatanmu prioritas kami! Silahkan Berbelanja------")
                    while pembeli():
                        pass
                    break
                else:
                    print("pilihan yang dimasukkan tidak valid")

        selesai = input("Apakah anda ingin login kembali? (ya/tidak): ")
        if selesai.lower() == "tidak":
            print("Jaga kesehatanmu, Bersama WICY.Terima kasih!")
            break
main()








