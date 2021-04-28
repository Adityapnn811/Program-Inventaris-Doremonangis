# F08 pinjam gadget

def validate_borrow(check, id, userid, jumlah, tanggal, database_gadget, database_history):
    #VALIDASI PINJEMNYA MELEBIHI STOK/NGGA sekaligus konfirmasi pinjemannya
    if not IsBorrowed(database_history, id, userid):
        for i in range(len(database_gadget)):
            if database_gadget[i][0] == id:
                stok = database_gadget[i][3]
                stok -= jumlah
                if stok < 0:
                    check += 1
                    if database_gadget[i][3] == 0:
                        print("Stok habis, tunggu doraemon kembali dari petualangannya!")
                    else:
                        print("Stok tidak tersedia, stok yang tersedia sekarang sebanyak {}".format(database_gadget[i][3]))
                        borrow_gadget(userid, database_gadget, database_history)
                else:
                    check += 1
                    database_gadget[i][3] = stok
                    borrowed = [(len(database_history) + 1), userid, database_gadget[i][0], tanggal, jumlah, False]
                    database_history.append(borrowed)
                    print("\nItem {} x{} berhasil dipinjam! Stok tersisa sekarang {}".format(database_gadget[i][1], jumlah, stok))
    if check == 0 and not IsBorrowed(database_history, id, userid):
        print("ID barang tidak ada, masukkan id yang benar!")
        borrow_gadget(userid, database_gadget, database_history)

def validate_id_gadget(id_gadget, database_gadget):
    found = False
    for i in range(len(database_gadget)):
        if database_gadget[i][0] == id_gadget:
            found = True
    return found

def IsBorrowed(database_history, id, userid):
    already_borrow = False
    # ini buat kalo minjem suatu barang cuman boleh sekali, kalo minjem barang yang sama lagi harus dibalikin dulu
    # kalo mau dibolehin paling nanti harus ubah di F09 ditambahin validasi lagi, tapi harusnya sabi si
    # ini biar gampang aja sebenernya :D
    for i in range(len(database_history)):
        if database_history[i][1] == userid and database_history[i][2] == id and database_history[i][4] != 0:
            already_borrow = True
    return already_borrow

# Buat fungsi yang membuat array isinya id dari semua gadget yang ada di csv
def get_gadget_id(database_gadget):
    id_gadget = []
    for i in range(len(database_gadget)):
        id_gadget.append(database_gadget[i][0])
    return id_gadget

def AllBorrowed(database_history, userid, id_gadget):
    jml_gadget_terpinjam = 0
    for i in range(len(database_history)):
        if database_history[i][1] == userid and database_history[i][4] != 0:
            jml_gadget_terpinjam += 1
    # Apabila terbaca bahwa jml gadget yang dipinjam = jml gadget, artinya user sudah meminjam semua gadget
    if jml_gadget_terpinjam == len(id_gadget):
        return True
    else:
        return False

#YANG DIPANGGIL DI MAIN
#parameternya
#userid = id yang login, nanti dapet dari F02
#database_gadget =  array yang isinya data gadget.csv
#database_history = array yang isinya data gadget_borrow_history.csv
def borrow_gadget(userid, database_gadget, database_history):
    id_gadget = get_gadget_id(database_gadget)
    if AllBorrowed(database_history, userid, id_gadget):
        print("\n>>> Kamu sudah meminjam semua gadget! Kembalikan dulu!")
    else:
        # cek id peminjam
        count = 0  # ngecek idnya ada atau ngga
        id = input("Masukkan id item: ")
        while not validate_id_gadget(id, database_gadget):
            print("ID barang tidak ada, masukkan ID yang benar!")
            id = input("Masukkan id item: ")
        while IsBorrowed(database_history, id, userid):
            print(">>> Kamu sudah meminjam gadget ini! Harap kembalikan terlebih dahulu sebelum meminjam kembali!")
            id = input("Masukkan id item: ")
        tanggal = input("Tanggal peminjaman(DD/MM/YYYY): ")
        jumlah = int(input("Jumlah peminjaman: "))
        while jumlah < 0:
            print("Kamu tidak dapat meminjam sejumlah negatif barang sobat!")
            jumlah = int(input("Jumlah peminjaman: "))
        validate_borrow(count, id, userid, jumlah, tanggal, database_gadget, database_history)
