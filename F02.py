# F02 - LOGIN

# FUNGSI VALIDASI LOGIN

#ini var global buat semua fungsi yang butuh id user
id_user = ""

def validate_login(username, password, database):
    global id_user
    valid = False
    for data in database:
        if data[1] == username and data[4] == password:
            id_user = data[0]
            valid = True
    if valid:
        print("Halo {}! Selamat datang di kantong ajaib".format(username))
        return id_user
    else:
        print("Username/Password salah! Silahkan coba lagi")
        login(database)

#FUNGSI LOGIN (YANG DIPANGGIL DI MAIN)
def login(database):
    global id_user
    username = input("Username: ")
    password = input("Password: ")
    validate_login(username, password, database)
        
