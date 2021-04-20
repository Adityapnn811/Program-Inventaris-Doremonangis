from os import urandom

#ini protoype hashing password yg gw buat, masi bisa diubah jdi lebih bagus si harusnya
#STEP:
#Jadi ini sebenrnya gw cmn ubah ke ord ascii trus selipin string random dari os.urandom
#gw generate 1000000 biar pass sepanjang apapun(orang normal), random stringnya ga abis
#step ngeceknya
# - String yang sama hasil hashnya beda, tapi posisinya bakalan sama
# ---------------Ini contoh hash dari "yudhit" 2 kali ---------------
# hash 1 -> 12h11x10|10x10|11\1f7|0b4|5x6\
# hash 2 -> 12\11\10\10f10\11|1x7x0\4e5x6e
# Sebenernya yang perlu diperhatiin angkanya aja, karena walaupun beda tapi panjang stringnya sama
# Trus angka dan posisinya juga bakal sama
#jadi ngeceknya pas login nanti tinggal buat validator di fungsi validate_pass yang ngeluarin angkanya doang
#trus nanti angka dari hashednya itu dibandingin, kalo sama bakal true
#kelar deh :D


#ini buat ngerandom stringnya, soalnya gabole pake random trus gw cari ada urandom tapi sebenrnya gatau si itu apaan
#intinya dapet string random 
def random_salt(database_user):
    listrandom = '|'
    random = str(urandom(len(database_user) + 1000000))
    ranlist = []
    for i in random:
        ranlist.append(i)
    for i in range(len(ranlist)):
        if ranlist[i].isdigit():
                ranlist[i] = listrandom
    return ranlist


#ini fungsi utamanya buat ngehash password
def hash_try(password, salt):
    front = []
    back = []
    hashed = ""
    randomsalt = random_salt(salt)
    for i in password:
        asc = str(ord(i))
        if len(asc) < 2:
            front.append(0)
            back.append(asc)
            front.append(randomsalt[ord(i)])
            back.append(randomsalt[-ord(i)])
        elif len(asc) == 2:
            front.append(asc[0])
            back.append(asc[1])
            back.append(randomsalt[ord(i)])
        else: #ascii maksimal 127
            front.append(asc[0])
            front.append(asc[1])
            back.append(asc[2])
            front.append(randomsalt[ord(i)])
            back.append(randomsalt[-ord(i)])
    complete = front + back
    for i in complete:
        hashed += i
    return hashed

#ini fungsi validator yang nanti dipake kalo login buat nyocokin 
#password yang di database sama password inputan user
def validate_pass(password_login, password_stored):
    login_num = ""
    login_stored = ""
    for i in range(len(password_login)):
        if password_login[i].isdigit():
            login_num += str(password_login[i])
    for i in range(len(password_stored)):
        if password_stored[i].isdigit():
            login_stored += str(password_stored[i])
    if login_num == login_stored:
        return True
    else:
        return False

#ini kalo mo nyoba liat hashnya
#print(hash_try("yudhit", "qerwefewef"))
