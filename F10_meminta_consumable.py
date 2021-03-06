# F10 meminta consumable
from validate_tanggal import *
from fungsi_parser import *

index = 0

def validate_id(database_consumable, id_consumable):
    # kalo true berarti idnya valid
    # kalo false idnya ngga ada
    valid = False
    found = False
    i = 0
    while (not found) and (i < (len(database_consumable))):
        if id_consumable == database_consumable[i][0]:
            found = True
        i += 1
    i -= 1
    if not found:
        valid = False
        print("ID consumable tidak valid!")
    elif found:
        if database_consumable[i][3] > 0:
            valid = True
        elif database_consumable[i][3] <= 0:
            print("Item habis, masukkin ID consumable yang lain ya!")
            valid = False
    return valid

def validate_jumlah(database_consumable, jumlah_minta, id_consumable):
    # kalo true berarti jumlahnya cukup/pas
    # kalo false berarti jumlahnya kurang
    global index
    valid = False
    copy_consumable = database_consumable       
    for i in range(len(database_consumable)):
        if database_consumable[i][0] == id_consumable:
            stok = copy_consumable[i][3]
            stok -= jumlah_minta
            index = i
            if stok >= 0:
                valid = True
    return valid

def cek_apakah_consumable_masih_ada(database_consumable):
    all_empty = True
    for i in range(len(database_consumable)):
        if database_consumable[i][3] > 0:
            all_empty = False
    return all_empty

def minta_consumable(database_consumable, id_user, database_consumable_history):
    global index
    if cek_apakah_consumable_masih_ada(database_consumable) == True:
        print("\n>>> Semua item sudah habis! Tunggu Doremonangis kembali dari petualangannya ya!")
    else:
        id_consumable = input("Masukkan id item: ")
        # validasi id
        while validate_id(database_consumable, id_consumable) == False:  # Cukup validasi di sini, soalnya ini udah bakal ngeloop sampe valid
            id_consumable = input("Masukkan id item: ")
        jumlah_minta = int(input("Jumlah: "))
        #validasi kalo mintanya negatif
        while jumlah_minta < 0:
            print("Kamu tidak dapat meminta sejumlah negatif barang sobat!")
            jumlah_minta = int(input("Jumlah: "))
        # validasi jumlah
        while validate_jumlah(database_consumable, jumlah_minta, id_consumable) == False:
            print("Stok tidak cukup, stok yang tersedia sekarang sebanyak {}.".format(database_consumable[index][3]))
            print("Harap masukkan ulang jumlah.")
            jumlah_minta = int(input("Jumlah: "))
            validate_jumlah(database_consumable, jumlah_minta, id_consumable)
        database_consumable[index][3] -= jumlah_minta
        tanggal = input("Tanggal permintaan: ")
        arr_tanggal = parser_tanggal(tanggal)
        while not validate_date(arr_tanggal):
            print("Input tanggal tidak valid! Ulangi!")
            tanggal = input("Tanggal peminjaman(DD/MM/YYYY): ")
            arr_tanggal = parser_tanggal(tanggal)
        print("\nItem "+str(database_consumable[index][1])+"(x"+str(jumlah_minta)+") telah berhasil diambil!")
        # Masukin data ke consumable history
        data_history = [(len(database_consumable_history) + 1), id_user, id_consumable, tanggal, jumlah_minta]
        database_consumable_history.append(data_history)
