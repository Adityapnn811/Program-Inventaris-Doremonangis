# F02 - LOGIN
from hash import *
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
