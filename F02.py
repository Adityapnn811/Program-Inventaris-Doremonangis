# F02 - LOGIN

# FUNGSI VALIDASI LOGIN

#ini var global buat semua fungsi yang butuh id user
user_id = ""

def validate_login(username, password, database):
    validate = False
    for data in database:
        if data[1] == username and data[4] == password:
            validate = True
    if validate:
        print("Halo {}! Selamat datang di kantong ajaib".format(username))
        return True
    else:
        print("Username/Password salah! Silahkan coba lagi")
        return False

#FUNGSI LOGIN (YANG DIPANGGIL DI MAIN)
def login(database):
    global user_id
    username = input("Username: ")
    password = input("Password: ")
    while validate_login(username, password, database) == False:
        username = input("Username: ")
        password = input("Password: ")
        validate_login(username, password, database)
    # username id buat tau siapa yang login
    for i in range(len(database)):
        if database[i][1] == username:
            user_id = database[i][0]
