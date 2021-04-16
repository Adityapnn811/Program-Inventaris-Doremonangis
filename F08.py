def validate_borrow(check, id, userid, jumlah, tanggal, database_gadget, database_history):
    already_borrow = False
    #ini buat kalo minjem suatu barang cuman boleh sekali, kalo minjem barang yang sama lagi harus dibalikin dulu
    #kalo mau dibolehin paling nanti harus ubah di F09 ditambahin validasi lagi, tapi harusnya sabi si
    #ini biar gampang aja sebenernya :D
    for i in range(len(database_history)):
        if database_history[i][1] == userid and database_history[i][2] == id and database_history[i][4] != 0:
            print("\n>>> Kamu sudah meminjam gadget ini! Harap kembalikan terlebih dahulu sebelum meminjam kembali!")
            already_borrow = True
            break
            #Ini masi break, mungkin nanti kalo udah dpt program utamanya bisa dikasi fungsi buat pilih layanan lain gitu
    #VALIDASI PINJEMNYA MELEBIHI STOK/NGGA sekaligus konfirmasi pinjemannya
    if not(already_borrow):
        for i in range(len(database_gadget)):
            if database_gadget[i][0] == id:
                stok = database_gadget[i][3]
                stok -= jumlah
                if stok < 0:
                    check += 1
                    print("Stok tidak tersedia, stok yang tersedia sekarang sebanyak {}".format(database_gadget[i][3]))
                    return False
                else:
                    check += 1
                    database_gadget[i][3] = stok
                    borrowed = [len(database_history),userid, database_gadget[i][0], tanggal, jumlah]
                    database_history.append(borrowed)
                    print("Item {} x{} berhasil dipinjam! Stok tersisa sekarang {}".format(database_gadget[i][1], jumlah, stok))
                    return True
    if check == 0 and not(already_borrow):
        print("ID barang tidak ada, masukkan id yang benar!")
        return False

#YANG DIPANGGIL DI MAIN
#parameternya
#userid = id yang login, nanti dapet dari F02
#database_gadget =  array yang isinya data gadget.csv
#database_history = array yang isinya data gadget_return_history.csv
def borrow_gadget(userid, database_gadget, database_history):
    #cek id peminjam
    count = 0 #ngecek idnya ada atau ngga
    id = input("Masukkan id item: ")
    tanggal = input("Tanggal peminjaman(DD/MM/YYYY): ")
    jumlah = int(input("Jumlah peminjaman: "))
    while validate_borrow(count, id, userid, jumlah, tanggal, database_gadget, database_history) == False:
        id = input("Masukkan id item: ")
        tanggal = input("Tanggal peminjaman(DD/MM/YYYY): ")
        jumlah = int(input("Jumlah peminjaman: "))
        validate_borrow(count, id, userid, jumlah, tanggal, database_gadget, database_history)
            
