# F02 - LOGIN

# FUNGSI VALIDASI LOGIN
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
    username = input("Username: ")
    password = input("Password: ")
    while validate_login(username, password, database) == False:
        username = input("Username: ")
        password = input("Password: ")
        validate_login(username, password, database)
    # username id buat tau siapa yang login
    for i in range(len(database)):
        if database[i][1] == username:
            userid = database[i][0]
    return userid

#Ini buat manggil fungsi di mainnya

log = file2.login(datas)

#datas ini nanti yang isinya array user.csv
for data in datas:
  if data[0] == log:
    user_now = log
#user_now isinya id user yg login buat nanti akses
