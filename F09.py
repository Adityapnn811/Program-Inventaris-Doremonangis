# NGEMBALIIN GADGET
# uda termasuk bonus

def return_loop(no_pinjam, tanggal_balik, data_pinjam, gadget_id, database_gadget, database_gadget_history,
                database_gadget_return):
    isreturn = False
    for i in range(len(data_pinjam)):
        if i == (no_pinjam - 1):
            jumlah = int(input("Berapa banyak yang akan dikembalikan? stok sekarang {} : ".format(data_pinjam[i][2])))
            stok_now = data_pinjam[i][2] - jumlah
            if jumlah < 0:
                print("Mana mungkin kukembalikan barang negatif sobat??")
                return_loop(no_pinjam, tanggal_balik, data_pinjam, gadget_id, database_gadget, database_gadget_history,
                            database_gadget_return)
            elif stok_now < 0:
                print("Stok tidak mencukupi! Harap masukkan jumlah pengembalian yang valid")
                return_loop(no_pinjam, tanggal_balik, data_pinjam, gadget_id, database_gadget, database_gadget_history,
                            database_gadget_return)
            else:
                # validasi boolean
                if data_pinjam[i][2] - jumlah == 0:
                    isreturn = True
                # ini isreturned gatau buat naon, intinya kalo belom full balikin = False, kalo udah full = True
                append_return = [data_pinjam[i][0], data_pinjam[i][1], tanggal_balik, jumlah, isreturn]
                # id;id_peminjaman;tanggal_peminjaman;jumlah
                database_gadget_return.append(append_return)
                for i in range(len(database_gadget)):
                    if gadget_id[no_pinjam - 1][0] == database_gadget[i][0]:
                        database_gadget[i][3] += jumlah
                        print("Item {} (x{}) berhasil dikembalikan".format(database_gadget[i][1], jumlah))
                        item_hapus = gadget_id[no_pinjam - 1][0]
                        break
                for i in range(len(database_gadget_history)):
                    if database_gadget_history[i][2] == item_hapus:
                        database_gadget_history[i][4] -= jumlah
                        print("\n>>> Riwayat peminjamanmu telah diperbaharui")
                        break


# FUNGSI YANG DIPANGGIL DI MAIN
# parameternya
# user id = id usernya dapet dari F02
# database_gadget = array yang isinya gadget.csv
# database_gadget_history = array yang isinya gadget_borrow_history.csv
# database_gadget_return = array yang isinya gadget_return_history.csv
def return_borrowed(userid, database_gadget, database_gadget_history, database_gadget_return):
    num = 0
    data_pinjam = []
    gadget_id = []
    # LOOP BUAT NUNJUKKIN GADGET YANG UDAH DIPINJEM
    for i in range(len(database_gadget_history)):
        if database_gadget_history[i][1] == userid:
            id_gadget = database_gadget_history[i][2]
            for j in range(len(database_gadget)):
                if database_gadget[j][0] == id_gadget:
                    if database_gadget_history[i][4] != 0:
                        # numnya cuman diincrement kalo jumlah itemnya ga 0
                        num += 1
                        print("{} {}".format(num, database_gadget[j][1]))
                        # ---------------------------------------REVISI-----------------------------
                        # id;id_peminjaman;tanggal_pengembalian;is_returned
                        # simpen history peminjamannya, uda termasuk id sama jumlahnya
                        data_pinjam.append(
                            [len(database_gadget_return), database_gadget_history[i][0], database_gadget_history[i][4]])
                        # isi data_pinjam = [id, nomor peminjaman, jumlah yang dipinjem]
                        gadget_id.append([database_gadget[j][0], database_gadget_history[i][4]])
                        # isi gadget_id = [gadget_id, jumlah yang dipinjam]
    if num == 0:
        print("Kamu belum meminjam barang apapun!")
    else:
        no_pinjam = int(input("Masukkan nomor peminjaman: "))
        tanggal_balik = input("Masukkan tanggal pengembalian: ")
        # Validasi kalo nomor peminjamannya ga valid
        while (no_pinjam) > len(data_pinjam):
            print("Masukkan nomor peminjaman yang benar!")
            no_pinjam = int(input("Masukkan nomor peminjaman: "))
            tanggal_balik = input("Masukkan tanggal pengembalian: ")
        return_loop(no_pinjam, tanggal_balik, data_pinjam, gadget_id, database_gadget, database_gadget_history,
                    database_gadget_return)