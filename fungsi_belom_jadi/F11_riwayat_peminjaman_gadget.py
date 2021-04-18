database_riwayat_gadget = datas_gadget_borrow_history

def riwayat_pinjam_gadget():
    # indexnya bisa jadi masih salah krna ak blm cocokin sm csvnya maap
    if (len(database_riwayat_gadget)) == 0:
        print("Anda belum pernah meminjam gadget. Tidak ada riwayat ditemukan.")
    elif (len(database_riwayat_gadget)) <= 5:
        # panjangnya ga nyampe 6, jadi cuman sekali print gabsa next
        for i in range (len(database_riwayat_gadget)):
            print("ID Peminjaman        : " + database_riwayat_gadget[i][0])
            for j in range (len(datas_user)):
                if database_riwayat_gadget[i][1] == datas_user[j][0]: #id user
                    print("Nama Pengambil       : " + datas_user[j][2]) #nama user
            for j in range (len(datas_gadget)):
                if database_riwayat_gadget[i][2] == datas_gadget[j][0]: #id gadget
                    print("Nama Gadget          : " + datas_gadget[j][1]) #nama gadget
            print("Tanggal Peminjaman   : " + database_riwayat_gadget[i][3])
            print("Jumlah               : " + database_riwayat_gadget[i][4])
    else: # panjangnya lebih dri 5, artinya bisa dinext
        max_next = (len(database_riwayat_gadget)-1)//5
        jumlah_next = 0
        for i in range (len(database_riwayat_gadget)):
            n = 1
            while (n <= 5): # biar keprint 5 riwayat
                print("ID Peminjaman        : " + database_riwayat_gadget[i][0])
                for j in range (len(datas_user)):
                    if database_riwayat_gadget[i][1] == datas_user[j][0]: #id user
                        print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                for j in range (len(datas_gadget)):
                    if database_riwayat_gadget[i][2] == datas_gadget[j][0]: #id gadget
                        print("Nama Gadget          : " + datas_gadget[j][1]) #nama gadget
                print("Tanggal Peminjaman   : " + database_riwayat_gadget[i][3])
                print("Jumlah               : " + database_riwayat_gadget[i][4])
                n += 1
        next = input("Next? (y/n): ")
        while (next != 'y') and (next != 'Y') and (next != 'n') and (next != 'N'):
            print("Masukkan pilihan yang benar!")
            next = input("Next? (y/n): ")
        while (next == 'y') or (next == 'Y'):
            n = 5*(jumlah_next+1) # biar i nya mulai dri i+5, i+10, dst
            jumlah_next += 1
            if (jumlah_next < max_next):
                for (i+n) in range (len(database_riwayat_gadget)):
                    print("ID Peminjaman        : " + database_riwayat_gadget[i+n][0])
                    for j in range (len(datas_user)):
                        if database_riwayat_gadget[i+n][1] == datas_user[j][0]: #id user
                            print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                    for j in range (len(datas_gadget)):
                        if database_riwayat_gadget[i+n][2] == datas_gadget[j][0]: #id gadget
                            print("Nama Gadget          : " + datas_gadget[j][1]) #nama gadget
                    print("Tanggal Peminjaman   : " + database_riwayat_gadget[i+n][3])
                    print("Jumlah               : " + database_riwayat_gadget[i+n][4])
                next = input("Next? (y/n): ")
            elif (jumlah_next == max_next):
                for (i+n) in range (len(database_riwayat_gadget)):
                    print("ID Peminjaman        : " + database_riwayat_gadget[i+n][0])
                    for j in range (len(datas_user)):
                        if database_riwayat_gadget[i+n][1] == datas_user[j][0]: #id user
                            print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                    for j in range (len(datas_gadget)):
                        if database_riwayat_gadget[i+n][2] == datas_gadget[j][0]: #id gadget
                            print("Nama Gadget          : " + datas_gadget[j][1]) #nama gadget
                    print("Tanggal Peminjaman   : " + database_riwayat_gadget[i+n][3])
                    print("Jumlah               : " + database_riwayat_gadget[i+n][4])
                print("Ini halaman terakhir.")
        if (next == 'n') or (next == 'N'):
            print("Sampai jumpa kembali!")