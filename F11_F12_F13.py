from datetime import datetime


# convertan id ke nama user, gadget, sama consumable
def convert_user_id_name(id, database_user):
    for i in range(len(database_user)):
        if id == database_user[i][0]:
            return database_user[i][2]


def convert_gadget_id_name(id, database_gadget):
    for i in range(len(database_gadget)):
        if id == database_gadget[i][0]:
            return database_gadget[i][1]


def convert_consum_id_name(id, database_consum):
    for i in range(len(database_consum)):
        if id == database_consum[i][0]:
            return database_consum[i][1]


# ini fungsi buat ambil id user sama id gadget dari no_kembali
def convert_nokembali_iduser(no_kembali, gadget_borrow_history):
    for i in range(len(gadget_borrow_history)):
        if no_kembali == gadget_borrow_history[i][0]:
            return gadget_borrow_history[i][1]


def convert_nokembali_idgadget(no_kembali, gadget_borrow_history):
    for i in range(len(gadget_borrow_history)):
        if no_kembali == gadget_borrow_history[i][0]:
            return gadget_borrow_history[i][2]


# biar ga panjang euy
# gadget bisa diganti consumable, nyesuain aje
def show_log_gadget(i, date_sorted_olah, database_user, database_need, deskripsi, type, kode, kode2):
    print("\nID {}: {}".format(deskripsi, date_sorted_olah[i][0]))
    print("Nama {}: {}".format(kode2, convert_user_id_name(date_sorted_olah[i][1], database_user)))
    print("Nama {}: {}".format(type, convert_gadget_id_name(date_sorted_olah[i][2], database_need)))
    print("Tanggal {}: {}".format(kode, date_sorted_olah[i][3]))
    print("Jumlah: {}".format(date_sorted_olah[i][4]))


# ini loop dari show_log
def show_history(date_sorted_olah, database_user, database_gadget, deskripsi, type, kode, kode2):
    prekon = len(date_sorted_olah)
    if prekon != 0:
        hitung = 0
        for i in range(len(date_sorted_olah)):
            # 1,2,3,4
            if hitung == 0:
                show_log_gadget(i, date_sorted_olah, database_user, database_gadget, deskripsi, type, kode, kode2)
                hitung += 1
            elif hitung % 5 != 0:
                show_log_gadget(i, date_sorted_olah, database_user, database_gadget, deskripsi, type, kode, kode2)
                hitung += 1
            elif hitung % 5 == 0:
                print("\n>>>Next?(y/n)")
                choice = str(input()).lower()
                if choice == "y":
                    show_log_gadget(i, date_sorted_olah, database_user, database_gadget, deskripsi, type, kode, kode2)
                    hitung += 1
                else:
                    break
    else:
        print("Belum ada riwayat {}!".format(kode))


def gadget_borrow_history_info(database_history, database_user, database_gadget):
    list_show = []
    date_history = []
    date_sorted_done = []
    for i in range(len(database_history)):
        if database_history[i][4] != 0:  # proses item yang jumlah > 0 alias belom dibalikin
            data_show = [database_history[i][0], database_history[i][1], database_history[i][2], database_history[i][3],
                         database_history[i][4]]
            # ubah ke string dlu biar bisa dipakein fungsi
            date_history.append(str(database_history[i][3]))
            list_show.append(data_show)
    # sort tanggalnya
    date_history.sort(key=lambda date: datetime.strptime(date, '%d/%m/%Y'))
    # loop buat bikin list_show yang terurut tanggal
    for i in range(len(list_show)):
        for j in range(i, len(list_show)):
            if date_history[i] == list_show[j][3]:
                data_temp = list_show[i]
                list_show[i] = list_show[j]
                list_show[j] = data_temp
    # Reverse hasil list show
    for i in range(len(list_show) - 1, -1, -1):
        date_sorted_done.append(list_show[i])
    show_history(date_sorted_done, database_user, database_gadget, "peminjaman", "gadget", "peminjaman", "peminjam")


# F12
def gadget_return_history_info(database_return, database_user, database_gadget, database_gadget_borrow):
    list_show = []
    date_history = []
    date_sorted_done = []
    for i in range(len(database_return)):
        # if database_history[i][4] != 0: #khusus f12 gausah validasi ini
        # id;id_peminjaman;tanggal_pengembalian;jumlah;is_returned
        # dikonvert dari atas ke bawah pake fungsi yang ada
        # id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah
        # ini ngeconvert dari nomor peminjaman ke id gaget sama id user aja
        id_peminjam = convert_nokembali_iduser(database_return[i][1], database_gadget_borrow)
        id_gadget = convert_nokembali_idgadget(database_return[i][1], database_gadget_borrow)
        data_show = [database_return[i][1], id_peminjam, id_gadget, database_return[i][2], database_return[i][3]]
        # ubah ke string dlu biar bisa dipakein fungsi
        date_history.append(str(database_return[i][2]))
        list_show.append(data_show)
    # sort tanggalnya
    date_history.sort(key=lambda date: datetime.strptime(date, '%d/%m/%Y'))
    # loop buat bikin list_show yang terurut tanggal
    for i in range(len(list_show)):
        for j in range(i, len(list_show)):
            if date_history[i] == list_show[j][3]:
                data_temp = list_show[i]
                list_show[i] = list_show[j]
                list_show[j] = data_temp
    # Reverse hasil list show
    for i in range(len(list_show) - 1, -1, -1):
        date_sorted_done.append(list_show[i])
    show_history(date_sorted_done, database_user, database_gadget, "peminjaman", "gadget", "pengembalian", "pengembali")


# F13
def consum_request_history_info(database_consum_history, database_user, database_consumable):
    list_show = []
    date_history = []
    date_sorted_done = []
    for i in range(len(database_consum_history)):
        if database_consum_history[i][4] != 0:
            data_show = [database_consum_history[i][0], database_consum_history[i][1], database_consum_history[i][2],
                         database_consum_history[i][3], database_consum_history[i][4]]
            # ubah ke string dlu biar bisa dipakein fungsi
            date_history.append(str(database_consum_history[i][3]))
            list_show.append(data_show)
    # sort tanggalnya
    date_history.sort(key=lambda date: datetime.strptime(date, '%d/%m/%Y'))
    # loop buat bikin list yang udah sorted berdasarkan tanggal
    tentu = len(date_history) - 1
    # loop buat bikin list_show yang terurut tanggal
    for i in range(len(list_show)):
        for j in range(i, len(list_show)):
            if date_history[i] == list_show[j][3]:
                data_temp = list_show[i]
                list_show[i] = list_show[j]
                list_show[j] = data_temp
    # Reverse hasil list show
    for i in range(len(list_show) - 1, -1, -1):
        date_sorted_done.append(list_show[i])
    show_history(date_sorted_done, database_user, database_consumable, "permintaan", "consumable", "pengambilan",
                 "peminta")