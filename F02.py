# F02 - LOGIN

# FUNGSI VALIDASI LOGIN

#ini var global buat semua fungsi yang butuh id user

idx_baris = 0

def validate_login(username, password, database):
    global idx_baris
    valid = False
    for i in range(len(database)):
        if database[i][1] == username and database[i][4] == password:
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
    validate_login(username, password, database)
    id_user = database[idx_baris][0]
    return id_user