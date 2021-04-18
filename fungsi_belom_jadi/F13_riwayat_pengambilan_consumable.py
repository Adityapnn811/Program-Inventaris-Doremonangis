database_riwayat_consumable = datas_consumable_history

def riwayat_ambil_consumable:   
    if (len(database_riwayat_consumable)) == 0:
        print("Anda belum pernah mengambil consumable. Tidak ada riwayat ditemukan.")
    elif (len(database_riwayat_consumable)) <= 5:
        # panjangnya ga nyampe 6, jadi cuman sekali print gabsa next
        for i in range (len(database_riwayat_consumable)):
            print("ID Pengambilan        : " + database_riwayat_consumable[i][0])
            for j in range (len(datas_user)):
                if database_riwayat_consumable[i][1] == datas_user[j][0]: #id user
                    print("Nama Pengambil       : " + datas_user[j][2]) #nama user
            for j in range (len(datas_gadget)):
                if database_riwayat_consumable[i][2] == datas_consumable[j][0]: #id consumable
                    print("Nama Consumable      : " + datas_consumable[j][1]) #nama consumable
            print("Tanggal Pengambilan  : " + database_riwayat_consumable[i][3])
            print("Jumlah               : " + database_riwayat_consumable[i][4])
    else: # panjangnya lebih dri 5, artinya bisa dinext
        max_next = (len(database_ambil_consumable)-1)//5
        jumlah_next = 0
        for i in range (len(database_ambil_consumable)):
            n = 1
            while (n <= 5):
                print("ID Pengambilan        : " + database_riwayat_consumable[i][0])
                for j in range (len(datas_user)):
                    if database_riwayat_consumable[i][1] == datas_user[j][0]: #id user
                        print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                for j in range (len(datas_gadget)):
                    if database_riwayat_consumable[i][2] == datas_consumable[j][0]: #id consumable
                        print("Nama Consumable      : " + datas_consumable[j][1]) #nama consumable
                print("Tanggal Pengambilan  : " + database_riwayat_consumable[i][3])
                print("Jumlah               : " + database_riwayat_consumable[i][4])
                n += 1
        next = input("Next? (y/n): ")
        while (next != 'y') and (next != 'Y') and (next != 'n') and (next != 'N'):
            print("Masukkan pilihan yang benar!")
            next = input("Next? (y/n): ")
        while (next == 'y') or (next == 'Y'):
            n = 5*(jumlah_next+1) # biar i nya mulai dri i+5, i+10, dst
            jumlah_next += 1
            if (jumlah_next < max_next): # klo blm max next masih muncul input next
                for (i+n) in range (len(database_ambil_consumable)):
                    print("ID Pengambilan        : " + database_riwayat_consumable[i+n][0])
                    for j in range (len(datas_user)):
                        if database_riwayat_consumable[i+n][1] == datas_user[j][0]: #id user
                            print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                    for j in range (len(datas_gadget)):
                        if database_riwayat_consumable[i+n][2] == datas_consumable[j][0]: #id consumable
                            print("Nama Consumable      : " + datas_consumable[j][1]) #nama consumable
                    print("Tanggal Pengambilan  : " + database_riwayat_consumable[i+n][3])
                    print("Jumlah               : " + database_riwayat_consumable[i+n][4]) 
                next = input("Next? (y/n): ")
            elif (jumlah_next == max_next): # udh max next jadi ngga ada input next lgi
                for (i+n) in range (len(database_ambil_consumable)):
                    print("ID Pengambilan        : " + database_riwayat_consumable[i+n][0])
                    for j in range (len(datas_user)):
                        if database_riwayat_consumable[i+n][1] == datas_user[j][0]: #id user
                            print("Nama Pengambil       : " + datas_user[j][2]) #nama user
                    for j in range (len(datas_gadget)):
                        if database_riwayat_consumable[i+n][2] == datas_consumable[j][0]: #id consumable
                            print("Nama Consumable      : " + datas_consumable[j][1]) #nama consumable
                    print("Tanggal Pengambilan  : " + database_riwayat_consumable[i+n][3])
                    print("Jumlah               : " + database_riwayat_consumable[i+n][4])
                print("Ini halaman terakhir.")
        if (next == 'n') or (next == 'N'):
            print("Sampai jumpa kembali!")
