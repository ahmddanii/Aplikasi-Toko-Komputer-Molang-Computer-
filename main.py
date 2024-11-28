from prettytable import PrettyTable
from colorama import Fore, Style, init
from datetime import datetime
import os
import pwinput

init()
os.system("cls")

accounts = [
    {"username" : "dani", "password" : "danigaming123", "level member": "VIP", "saldo" : 120000000,"status" : "aktif", "poin" : 25},
    {"username" : "idan", "password" : "idann.exe", "level member": "Biasa", "saldo" : 540000, "status" : "aktif", "poin" : "Bukan member VIP"},
    {"username" : "dina", "password" : "dina123", "level member": "VIP", "saldo" : 500000,"status" : "aktif","poin" : 50},
    {"username" : "dhan", "password" : "123", "level member": "VIP", "saldo" : 50000000,"status" : "aktif", "poin" : 2500}
]

item_toko = [
    {"brand" : "Acer", "tipe" : "Laptop", "seri" : "Acer Predator Helio G16", "harga" : 16500000},
    {"brand" : "Asus", "tipe" : "Laptop", "seri" : "Asus TUF Gaming A14", "harga" : 28000000},
    {"brand" : "Asus", "tipe" : "Laptop", "seri" : "Asus ROG Zepyhrus G14", "harga" : 21250000},    
    {"brand" : "Lenovo", "tipe" : "Laptop", "seri" : "Lenovo LOQ 15IRX9", "harga" : 17650000},
    {"brand" : "Axioo", "tipe" : "Laptop", "seri" : "Axioo Pongo 725", "harga" : 13500000},
    {"brand": "Corsair", "tipe": "RAM", "seri": "Corsair Vengeance RGB 16GB", "harga": 1200000},
    {"brand": "G.SKILL", "tipe": "RAM", "seri": "G.SKILL Trident Z 32GB", "harga": 2500000},
    {"brand": "Kingston", "tipe": "RAM", "seri": "Kingston Fury Beast 16GB", "harga": 1100000},
    {"brand": "Intel", "tipe": "CPU", "seri": "Intel Core i7-13700K", "harga": 6000000},
    {"brand": "AMD", "tipe": "CPU", "seri": "AMD Ryzen 7 7800X3D", "harga": 7000000},
    {"brand": "ASRock", "tipe": "Motherboard", "seri": "ASRock B550M Pro4", "harga": 2500000},
    {"brand": "MSI", "tipe": "Motherboard", "seri": "MSI MPG Z690 Edge", "harga": 4500000},
    {"brand": "ASUS", "tipe": "Motherboard", "seri": "ASUS ROG Strix B760-A", "harga": 4200000},
    {"brand": "Samsung", "tipe": "SSD", "seri": "Samsung 970 Evo Plus 1TB", "harga": 2000000},
    {"brand": "WD", "tipe": "SSD", "seri": "WD Blue SN570 1TB", "harga": 1500000},
    {"brand": "Crucial", "tipe": "SSD", "seri": "Crucial P3 Plus 1TB", "harga": 1400000},
    {"brand": "Gigabyte", "tipe": "GPU", "seri": "Gigabyte RTX 4070 Gaming OC", "harga": 8500000},
    {"brand": "ASUS", "tipe": "GPU", "seri": "ASUS TUF RX 7900 XTX", "harga": 14000000},
    {"brand": "MSI", "tipe": "GPU", "seri": "MSI Ventus RTX 4060 Ti", "harga": 7000000},
    {"brand": "Cooler Master", "tipe": "Cooling System", "seri": "Cooler Master Hyper 212", "harga": 600000},
    {"brand": "Noctua", "tipe": "Cooling System", "seri": "Noctua NH-D15", "harga": 1200000},
    {"brand": "Dell", "tipe": "Monitor", "seri": "Dell UltraSharp U2723QE", "harga": 9000000},
    {"brand": "LG", "tipe": "Monitor", "seri": "LG UltraGear 27GN950-B", "harga": 10000000},
    {"brand": "ASUS", "tipe": "Monitor", "seri": "ASUS TUF Gaming VG28UQL1A", "harga": 8500000},
    {"brand": "Logitech", "tipe": "Keyboard", "seri": "Logitech G Pro X Mechanical", "harga": 2000000},
    {"brand": "Razer", "tipe": "Keyboard", "seri": "Razer Huntsman V2", "harga": 2500000},
    {"brand": "Corsair", "tipe": "Mouse", "seri": "Corsair Dark Core RGB Pro", "harga": 1200000},
    {"brand": "Logitech", "tipe": "Mouse", "seri": "Logitech G502 HERO", "harga": 1000000},
    {"brand": "HyperX", "tipe": "Headset", "seri": "HyperX Cloud Alpha", "harga": 1800000},
    {"brand": "SteelSeries", "tipe": "Headset", "seri": "SteelSeries Arctis Nova Pro", "harga": 3000000}
]

discount = [
    {"nama voucher" : "disc1", "jumlah diskon" : 1/100, "status" : "tersedia"},
    {"nama voucher" : "disc3", "jumlah diskon" : 3/100, "status" : "tersedia"},
    {"nama voucher" : "disc5", "jumlah diskon" : 5/100, "status" : "tersedia"}
]

kode_referal = [
    {"kode referal" : "isi100", "jumlah saldo" : 100000},
    {"kode referal" : "isi200", "jumlah saldo" : 200000},
    {"kode referal" : "isi500", "jumlah saldo" : 500000},
    {"kode referal" : "isi1000", "jumlah saldo" : 1000000},
    {"kode referal" : "isi2000", "jumlah saldo" : 2000000},
    {"kode referal" : "isi5000", "jumlah saldo" : 5000000}
]

status_toko = "buka"

def login() : 
    try : 
        os.system("cls")
        chance = 3
        while True:
            print(Fore.BLUE + "\n=================")
            print("|     Login     |")
            print("=================" + Style.RESET_ALL)
            username = input("Username: ")
            password = pwinput.pwinput("Password: ")

            user = next((u for u in accounts if u["username"] == username), None)
            
            if not user:
                print("Username tidak ditemukan.")
                continue

            if user["status"] == "terblokir":
                print(Fore.RED + "Akun Anda telah diblokir. Silakan hubungi administrator untuk membuka blokir." + Style.RESET_ALL)
                return None
        
            if password == user["password"]:
                if user["level member"] == "VIP":
                    print(Fore.CYAN + f"Login berhasil! Selamat datang, {user["username"]}." + Style.RESET_ALL)
                else :
                    print(Fore.GREEN + f"Login berhasil! Selamat datang, {user["username"]}." + Style.RESET_ALL)
                return user
            else:
                chance -= 1
                if chance > 0:
                    print(Fore.YELLOW + f"Password salah. Kesempatan tersisa: {chance}." + Style.RESET_ALL)
                else:
                    user["status"] = "terblokir"
                    print(Fore.RED + "Akun Anda telah diblokir karena terlalu banyak percobaan gagal." + Style.RESET_ALL)
                    return None

    except Exception as e : 
        print(f"Terdapat error {e}")

def isi_saldo(user) :
    kode_saldo = input("Silahkan masukkan kode isi saldo: ")
    kode = next((k for k in kode_referal if k["kode referal"] == kode_saldo), None)

    if kode :
        tambah_saldo = int(kode["jumlah saldo"])
        saldo = f"Rp {kode["jumlah saldo"]:,}".replace(",", ".")

        for account in accounts :
            if account["username"] == user["username"]:
                account["saldo"] = int(account["saldo"] + tambah_saldo)
                user["saldo"] = account["saldo"]
                print(Fore.GREEN + f"Saldo berhasil ditambahkan sebesar {saldo}" + Style.RESET_ALL)
                saldo = f"Rp {user["saldo"]:,}".replace(",", ".")
                print(f"Saldo anda sekarang: {saldo}")
                break
    else :
        print(Fore.LIGHTMAGENTA_EX + "Kode referal tidak ditemukan" + Style.RESET_ALL)

def liat_barang() : 
    table = PrettyTable()
    table.field_names = ["Brand", "Jenis", "Seri", "Harga"]
    barang_pagi = item_toko[:7]
    barang_siang = item_toko[8:17]
    barang_malam = item_toko[17:]

    waktu_sekarang = datetime.now().hour    
    global status_toko
    status_toko = "buka"
    if 6 <= waktu_sekarang <= 10 :
        waktu = "Pagi"
        barang_muncul = barang_pagi
        for item in barang_muncul : 
            harga_rupiah = f"Rp {item["harga"]:,}".replace(",", ".")
            table.add_row([item["brand"], item["tipe"], item["seri"], harga_rupiah])
        print(table)

    elif 11<= waktu_sekarang <= 18 :
        waktu = "Siang"
        barang_muncul = barang_siang
        for item in barang_muncul : 
            harga_rupiah = f"Rp {item["harga"]:,}".replace(",", ".")
            table.add_row([item["brand"], item["tipe"], item["seri"], harga_rupiah])
        print(table)
    
    elif 19 <= waktu_sekarang <= 21 :
        waktu = "Malam"
        barang_muncul = barang_malam
        for item in barang_muncul : 
            harga_rupiah = f"Rp {item["harga"]:,}".replace(",", ".")
            table.add_row([item["brand"], item["tipe"], item["seri"], harga_rupiah])
        print(table)
        
    
    else: 
        status_toko = "tutup"
        print(Fore.RED + "Toko sedang tutup" + Style.RESET_ALL)



def beli_barang(user) :
    try :
        global status_toko
        if status_toko != "tutup":
            liat_barang()
            print("\n Note : ")
            print(" [x] Kembali ")
            nama_barang = input("Masukkan nama barang yang ingin dibeli: ")
            if nama_barang == "x":
                print(Fore.LIGHTBLUE_EX + "Kembali ke menu sebelumnya" + Style.RESET_ALL)
                return
            jumlah_barang = int(input("Berapa jumlah yang ingin dibeli: "))
            barang = next((b for b in item_toko if b["seri"] == nama_barang), None)
            total_pembelian = jumlah_barang * int(barang["harga"])
            fdiskon = "-"

            if barang : 
                if int(user["saldo"]) >= total_pembelian :
                    kode_voucher = input("Masukkan kode voucher (enter jika tidak ada): ")
                    kode = next((k for k in discount if k["nama voucher"] == kode_voucher), None)

                    if kode :
                        if kode["status"] == "tersedia" : 
                            diskon = total_pembelian * kode["jumlah diskon"]
                            fdiskon = f"Rp {int(diskon):,}".replace(",", ".")
                            harga_akhir = total_pembelian - diskon
                            fharga_akhir = f"Rp {int(harga_akhir):,}".replace(",", '.')
                            print(Fore.LIGHTBLUE_EX + f"Kode diskon berhasil digunakan!! anda mendapatkan diskon sebesar: {fdiskon}" + Style.RESET_ALL)
                            print(f"Total harga setelah diskon: {fharga_akhir}")
                            kode["status"] = "terpakai"

                        else : 
                            harga_akhir = total_pembelian
                            fharga_akhir = f"Rp {harga_akhir:,}".replace(",", '.')
                            print(Fore.LIGHTMAGENTA_EX + "Kode voucher tidak berlaku" + Style.RESET_ALL)
                            print(f"Total yang harus dibayarkan adalah{fharga_akhir}")

                    else :
                        harga_akhir = total_pembelian
                        fharga_akhir = f"Rp {harga_akhir:,}".replace(",", '.')
                        print(Fore.LIGHTRED_EX + "Kode voucher tidak tersedia" + Style.RESET_ALL)
                        print(f"Total yang harus dibayarkan adalah: {fharga_akhir}")

                    diskon_vip = 0
                    if user["level member"] == "VIP" :
                        if user["poin"] < 100 :
                            print(f"Poin anda saat ini: {user["poin"]} poin")
                            print(Fore.CYAN + "Anda mendapatkan diskon sebesar Rp 10.000" + Style.RESET_ALL)
                            diskon_vip = 10000
                            total = harga_akhir - diskon_vip
                        elif user["poin"] < 500 :
                            print(f"Poin anda saat ini: {user["poin"]} poin")
                            print(Fore.CYAN + "Anda mendapatkan diskon sebesar Rp 20.000" + Style.RESET_ALL)
                            diskon_vip = 20000
                            total = harga_akhir - diskon_vip
                        elif user["poin"] < 1000 :
                            print(f"Poin anda saat ini: {user["poin"]} poin")
                            print(Fore.CYAN + "Anda mendapatkan diskon sebesar Rp 100.000" + Style.RESET_ALL)
                            diskon_vip = 100000
                            total = harga_akhir - diskon_vip
                        elif user["poin"] < 2000 :
                            print(f"Poin anda saat ini: {user["poin"]} poin")
                            print(Fore.CYAN + "Anda mendapatkan diskon sebesar Rp 200.000" + Style.RESET_ALL)
                            diskon_vip = 200000
                            total = harga_akhir - diskon_vip
                        elif user["poin"] > 2000 :
                            print(f"Poin anda saat ini: {user["poin"]} poin")
                            print(Fore.CYAN + "Anda mendapatkan diskon sebesar Rp 300.000" + Style.RESET_ALL)
                            diskon_vip = 300000
                            total = harga_akhir - diskon_vip
                        else :
                            total = harga_akhir
                            print("Poin tidak mencukupi")

                    else:
                        total = harga_akhir

                    user["saldo"] -= total
                    saldo = f"Rp {int(user["saldo"]):,}".replace(",", ".")

                    if user["level member"] == "VIP" :
                        poin_belanja = 25
                        tambah_poin = user["poin"] + poin_belanja
                        user["poin"] = tambah_poin
                        print(Fore.GREEN + f"Pembelian berhasil!! anda mendapatkan {poin_belanja} poin" + Style.RESET_ALL)
                        print(Fore.LIGHTCYAN_EX + f"Poin anda sekarang : {tambah_poin} poin \n" + Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + f"Pembelian berhasil!! saldo anda sekarang {saldo} \n" + Style.RESET_ALL)
                        
                    harga_barang = f"Rp {barang["harga"]:,}".replace(",", ".")
                    fdiskon_vip = f"Rp {int(diskon_vip):,}".replace(",", ".")
                    ftotal = f"Rp {int(total):,}".replace(",", ".")
                    ftotal_pembelian = f"Rp {int(total_pembelian):,}".replace(",", ".")
                    print("   Invoice Pembelian " + Fore.BLUE +  "PT Molang Computer Sejahtera" + Style.RESET_ALL)
                    print("  Jalan Sendawar Raya No 120, Barong Tongkok 75576")
                    print("====================================================\n")
                    print(f"Nama item yang dibeli    : {nama_barang}")
                    print(f"Jumlah item yang dibeli  : {jumlah_barang} pcs")
                    print(f"Harga satuan             : {harga_barang}")
                    print(f"Diskon                   : {fdiskon}")
                    if user["level member"] == "VIP" :
                        print(f"Diskon VIP               : {fdiskon_vip}")
                    else :
                        print(f"Diskon VIP               : Bukan member VIP")
                    print(f"Total sebelum diskon     : {ftotal_pembelian}\n")
                    print(f"Total akhir              : {ftotal}\n")
                    print("====================================================")
                    print("Yang Terhormat,")
                    print("   Pembeli                              Staff Toko  \n\n\n")
                    print(f"    {user["username"]}                                  Azril")
                else : 
                    print("Saldo tidak mencukupi")

            else :
                print("barang tidak ada")

        else :
            print(Fore.RED + "Toko Sedang Tutup" + Style.RESET_ALL)

    except ValueError:
        print("Keyword yang anda masukkan tidak sesuai")
    except TypeError:
        print("Item tidak tersedia")


def liat_profil(user) :
    table = PrettyTable()
    table.field_names = ["Username", "Status User", "Saldo", "Poin"]

    print(Fore.LIGHTCYAN_EX + "\n                     Profil" + Style.RESET_ALL)
    print("=================================================")
    saldo = f"Rp {int(user["saldo"]):,}".replace(",", ".")
    table.add_row([user["username"], user["level member"], saldo, user["poin"]])
    print(table)

def vip_info(user):
    print(Fore.CYAN + f"Selamat datang, {user["username"]}." + Style.RESET_ALL)
    print("Berikut adalah beberapa benefit menjadi user VIP:")
    print(Fore.CYAN + "[1] Mendapatkan poin sebesar 25 setiap transaksi")
    print("[2] Mendapatkan diskon secara otomatis dengan ketentuan: ")
    print("    - Poin dibawah 100 mendapatkan diskon Rp 10.000")
    print("    - Poin diatas 100 dan dibawah 500 mendapatkan diskon Rp 20.000")
    print("    - Poin diatas 500 dan dibawah 1000 mendapatkan diskon Rp 100.000")
    print("    - Poin diatas 1000 dan dibawah 2000 mendapatkan diskon Rp 200.000")
    print("    - Poin diatas 2000 mendapatkan diskon Rp 300.000")
    print("[3] Menjadi prioritas ketika berbelanja " + Style.RESET_ALL)


def vip_menu(user) :
    while True :
        try :
            print("\nSelamat datang di" +  Fore.BLUE + " Molang Computer" + Style.RESET_ALL)
            print("=================================\n")
            print("Menu :")
            print("[1] Lihat Barang")
            print("[2] Belanja")
            print("[3] Lihat Profil")
            print("[4] Topup Saldo")
            print("[5] VIP Info")
            print("[6] Keluar")

            pilihan = input("Silahkan masukkan pilihan: ")

            if pilihan == "1" : 
                liat_barang()
            elif pilihan == "2" :
                beli_barang(user)

            elif pilihan == "3" :
                liat_profil(user)

            elif pilihan == "4" : 
                isi_saldo(user)

            elif pilihan == "5" :
                vip_info(user)

            elif pilihan == "6" :
                print("\n=============================================")
                print("Terimakasih telah mengunjungi" + Fore.BLUE +" Molang Computer" + Style.RESET_ALL)
                break

            else :
                print(Fore.RED + "Menu tidak tersedia" + Style.RESET_ALL)
        except EOFError as e :
            print(e)

def user_menu() :
    while True :
        try :
            print("\nSelamat datang di" +  Fore.BLUE + " Molang Computer" + Style.RESET_ALL)
            print("=================================\n")
            print("Menu :")
            print("[1] Lihat Barang")
            print("[2] Belanja")
            print("[3] Topup Saldo")
            print("[4] Lihat Profil")
            print("[5] Keluar")

            pilihan = input("Silahkan masukkan pilihan: ")

            if pilihan == "1" : 
                liat_barang()

            elif pilihan == "2" :
                beli_barang(user)

            elif pilihan == "3" : 
                isi_saldo(user)

            elif pilihan == "4" :
                liat_profil(user)

            elif pilihan == "5" :
                print("\n=============================================")
                print("Terimakasih telah mengunjungi" + Fore.BLUE +" Molang Computer" + Style.RESET_ALL)
                break

            else :
                print(Fore.RED + "Menu tidak tersedia" + Style.RESET_ALL)

        except EOFError as e :
            print(e)


try : 
    user = login()
    if user:
        if user["level member"] == "VIP":
            vip_menu(user)
        else:
            user_menu()
    input()

except KeyboardInterrupt : 
    print(Fore.RED + "\nProgram dihentikan" + Style.RESET_ALL)