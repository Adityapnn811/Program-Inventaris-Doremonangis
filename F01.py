#F01 - REGISTER

#FUNGSI VALIDASI USERNAME
def validate_username(user_name, database):
    username_stripped = user_name.strip()
    #ini masi boleh pake spasi di usernamenya
    for data in database:
        if data[1] == username_stripped:
            print("Username sudah digunakan")
            return False
    return True

#FUNGSI REGISTER USERNAME (YANG DIPANGGIL DI MAIN)
def input_username(lines, database):
    id = ("U{}".format(len(lines)))
    nama = input("Nama: ")
    username = input("Username: ")
    while validate_username(username, database) == False:
        username = input("Username: ")
        validate_username(username, database)
    password = input("Password: ")
    alamat = input("Alamat: ")
    datas_user = [id,username,nama,alamat,password,"user"]
    database.append(datas_user)
    print("user {} telah berhasil register ke dalam kantong ajaib".format(username)) 
