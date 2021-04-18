database_kembali_gadget = datas_gadget_return_history 

def cek_id_user(id_user, database_kembali_gadget):
    # Ngecek apakah user pernah ngembaliin gadget
    found = False
    for i in range(len(database_kembali_gadget)):
        if database_kembali_gadget[i][1] == id_user:
            found = True
    return found


def riwayat_kembali_gadget(database_kembali_gadget, datas_user, database_riwayat_gadget, datas_gadget, id_user):
    if cek_id_user(id_user, database_kembali_gadget) == False:
        print("Anda belum pernah mengembalikan gadget. Tidak ada riwayat ditemukan.")
    elif (len(database_riwayat_gadget)) <= 5:
        # panjangnya ga nyampe 6, jadi cuman sekali print gabsa next
        for i in range (len(database_kembali_gadget)):
            print("ID Pengembalian      : " + database_kembali_gadget[i][0])
            for j in range (len(datas_user)):
                if database_riwayat_gadget[i][1] == datas_user[j][0]: #id user
                    print("Nama Pengambil       : " + datas_user[j][2]) #nama user
            for j in range (len(datas_gadget)):
                if database_riwayat_gadget[i][2] == datas_gadget[j][0]: #id gadget
                    print("Nama Gadget          : " + datas_gadget[j][1]) #nama gadget
            print("Tanggal Pengembalian     : " + database_kembali_gadget[i][3])
    else: # panjangnya lebih dri 5, artinya bisa dinext
        max_next = (len(database_kembali_gadget)-1)//5
        jumlah_next = 0
        for i in range (len(database_kembali_gadget)):
            n = 1
            while (n <= 5):
                print("ID Pengembalian      : " + database_kembali_gadget[i][0])
                for j in range (len(datas_user)):
                    if database_riwayat_gadget[i][1] == datas_user[j][0]: #id user
                        print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                for j in range (len(datas_gadget)):
                    if database_riwayat_gadget[i][2] == datas_gadget[j][0]: #id gadget
                        print("Nama Gadget          : " + datas_gadget[j][1]) #nama gadget
                print("Tanggal Pengembalian     : " + database_kembali_gadget[i][3])
                n += 1
        next = input("Next? (y/n): ")
        while (next != 'y') and (next != 'Y') and (next != 'n') and (next != 'N'):
            print("Masukkan pilihan yang benar!")
            next = input("Next? (y/n): ")
        while (next == 'y') or (next == 'Y'):
            n = 5*(jumlah_next+1) # biar i nya mulai dri i+5, i+10, dst
            jumlah_next += 1
            if (jumlah_next < max_next):
                for (i + n) in range (len(database_kembali_gadget)):
                    print("ID Pengembalian      : " + database_kembali_gadget[i+n][0])
                    for j in range (len(datas_user)):
                        if database_riwayat_gadget[i+n][1] == datas_user[j][0]: #id user
                            print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                    for j in range (len(datas_gadget)):
                        if database_riwayat_gadget[i+n][2] == datas_gadget[j][0]: #id gadget
                            print("Nama Gadget          : " + datas_gadget[j][1]) #nama gadget
                    print("Tanggal Pengembalian     : " + database_kembali_gadget[i+n][3])
                next = input("Next? (y/n): ")
            elif (jumlah_next == max_next):
                for (i + n) in range (len(database_kembali_gadget)):
                    print("ID Pengembalian      : " + database_kembali_gadget[i+n][0])
                    for j in range (len(datas_user)):
                        if database_riwayat_gadget[i+n][1] == datas_user[j][0]: #id user
                            print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                    for j in range (len(datas_gadget)):
                        if database_riwayat_gadget[i+n][2] == datas_gadget[j][0]: #id gadget
                            print("Nama Gadget          : " + datas_gadget[j][1]) #nama gadget
                    print("Tanggal Pengembalian     : " + database_kembali_gadget[i+n][3])
                print("Ini halaman terakhir.")
        if (next == 'n') or (next == 'N'):
            print("Sampai jumpa kembali!")  