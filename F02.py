# F02 - LOGIN

# FUNGSI VALIDASI LOGIN
def validate_login(username, password, database):
    validate = False
    for i in range(len(database)):
        if database[i][1] == username and database[i][4] == password:
            validate = True
    return validate

#FUNGSI LOGIN (YANG DIPANGGIL DI MAIN)
def login(database):
    username = input("\nUsername: ")
    password = input("Password: ")
    validate_login(username, password, database)
    while validate_login(username, password, database) == False:
        print("Username/Password salah! Silahkan coba lagi")
        username = input("\nUsername: ")
        password = input("Password: ")
        validate_login(username, password, database)
    else:
        print("\nHalo {}! Selamat datang di kantong ajaib".format(username))
    # username id buat tau siapa yang login
    for i in range(len(database)):
        if database[i][1] == username:
            userid = database[i][0]
    return userid

