id = ""

def validate_login(username, password, database):
    global id
    valid = False
    for data in database:
        if data[1] == username and data[4] == password:
            id = data[0]
            valid = True
    if valid:
        print("Halo {}! Selamat datang di kantong ajaib".format(username))
        print(id)
    else:
        print("Username/Password salah! Silahkan coba lagi")
        login(database)

#FUNGSI LOGIN (YANG DIPANGGIL DI MAIN)
def login(database):
    global id
    username = input("Username: ")
    password = input("Password: ")
    validate_login(username, password, database)
