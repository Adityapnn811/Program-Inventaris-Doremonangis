#ini buat nampilin output kek biasa
def gadget_service(name, desc, amount, rarity, year):
    print("\nNama: {}".format(name))
    print("Deskripsi: {}".format(desc))
    print("Jumlah: {}".format(amount))
    print("Rarity: {}".format(rarity))
    print("Tahun Ditemukan: {}".format(year))

#F03
def gadget_by_rarity(database_gadget):
    count = 0
    #rarity pasti valid, tidak usah divalidasi
    rarity = input('Masukkan rarity: ')
    print()
    print("Hasil Pencarian: ")
    for i in range(len(database_gadget)):
        if database_gadget[i][4] == rarity:
            count += 1
            gadget_service(database_gadget[i][1], database_gadget[i][2], database_gadget[i][3], database_gadget[i][4], database_gadget[i][5])
    if count == 0:
        print("Gadget tidak ditemukan")


#F04
def gadget_by_year(database_gadget):
    count = 0
    year = int(input("Masukkan tahun: "))
    category = input("Masukkan kategori: ")
    for i in range(len(database_gadget)):
        if category == "=" and int(database_gadget[i][5]) == year:
            count +=1
            gadget_service(database_gadget[i][1], database_gadget[i][2], database_gadget[i][3], database_gadget[i][4], database_gadget[i][5])
        elif category == ">" and (int(database_gadget[i][5])) == (year+1):
            count += 1
            gadget_service(database_gadget[i][1], database_gadget[i][2], database_gadget[i][3], database_gadget[i][4], database_gadget[i][5])
        elif category == "<" and int(database_gadget[i][5]) == (year-1):
            count += 1
            gadget_service(database_gadget[i][1], database_gadget[i][2], database_gadget[i][3], database_gadget[i][4], database_gadget[i][5])
        elif category == ">=" and (int(database_gadget[i][5]) == year) or (int(database_gadget[i][5]) == year+1):
            count += 1
            gadget_service(database_gadget[i][1], database_gadget[i][2], database_gadget[i][3], database_gadget[i][4], database_gadget[i][5])
        elif category == "=" and (int(database_gadget[i][5]) == year) or (int(database_gadget[i][5]) == year-1):
            count += 1
            gadget_service(database_gadget[i][1], database_gadget[i][2], database_gadget[i][3], database_gadget[i][4], database_gadget[i][5])
    if count == 0:
        print("Gadget tidak ditemukan")
