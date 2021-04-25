from hash import *

#F01 - REGISTER

#FUNGSI VALIDASI USERNAME
def validate_username(user_name, database):
    username_stripped = user_name.strip()
    #ini masi boleh pake spasi di usernamenya
    for i in range(len(database)):
        if database[i][1] == username_stripped:
            print("Username sudah digunakan")
            return False
    return True

#FUNGSI REGISTER USERNAME (YANG DIPANGGIL DI MAIN)
def input_username(database):
    print("\nSilahkan masukkan data user yang akan diregister")
    id = ("U{}".format(len(database)))
    nama = input("Nama: ")
    username = input("Username: ")
    while validate_username(username, database) == False:
        username = input("Username: ")
    password = input("Password: ")
    hashed_pass = hash_try(password, database)
    alamat = input("Alamat: ")
    datas_user = [id,username,nama,alamat,hashed_pass,"user"]
    database.append(datas_user)
    print("\nUser {} telah berhasil register ke dalam kantong ajaib!".format(username))


# F02 - LOGIN

# FUNGSI VALIDASI LOGIN

#ini var global buat semua fungsi yang butuh id user

idx_baris = 0

def validate_login(username, password, database):
    global idx_baris
    valid = False
    for i in range(len(database)):
        for i in range(len(database)):
            cek_hash = validate_pass(password, database[i][4])
            if cek_hash and database[i][1] == username:
                idx_baris = i
                valid = True
    if valid:
        print("\nHalo {}! Selamat datang di kantong ajaib".format(username))
    else:
        print("Username/Password salah! Silahkan coba lagi")
        login(database)

#FUNGSI LOGIN (YANG DIPANGGIL DI MAIN)
def login(database):
    username = input("Username: ")
    password = input("Password: ")
    pass_hashed = hash_try(password, database)
    validate_login(username, pass_hashed, database)
    id_user = database[idx_baris][0]
    return id_user
