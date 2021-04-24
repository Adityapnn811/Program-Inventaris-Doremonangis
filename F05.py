# F05 - Menambahkan item

def validate_id_gadget(datas_gadget, input_id):
    found = False
    for i in range(len(datas_gadget)):
        if input_id == datas_gadget[i][0]:
            found = True
    return found

def validate_id_consum(datas_consum, input_id):
    found = False
    for i in range(len(datas_consum)):
        if input_id == datas_consum[i][0]:
            found = True
    return found

def validate_rarity(input_rarity):
    if input_rarity != 'C' and input_rarity != 'B' and input_rarity != 'A' and input_rarity != 'S':
        return False
    else:
        return True

def tambah_item(datas_gadget, datas_consumable):
    print("")
    id_input = input("Masukkan ID: ")
    if id_input[0] == "G":
        # validate id dulu, klo valid baru lanjut
        if not validate_id_gadget(datas_gadget, id_input):
            nama = input("Masukkan Nama: ")
            deskripsi  = input("Masukkan Deskripsi: ")
            jumlah = int(input("Masukkan Jumlah: "))
            rarity = input("Masukkan Rarity: ")
            while not validate_rarity(rarity):
                print("Input rarity tidak valid! Rarity yang valid adalah C, B, A, S")
                rarity = input("Masukkan Rarity: ")
            tahun_ditemukan = input("Masukkan tahun ditemukan: ")
            data_gadget_baru = [id_input,nama,deskripsi,jumlah,rarity, tahun_ditemukan]
            datas_gadget.append(data_gadget_baru)
            print("\nItem telah berhasil ditambahkan ke database!")
        else:
            print("\nGagal menambahkan item karena ID sudah ada")
    elif id_input[0] == "C":
        # validate id dulu, klo valid baru lanjut
        if not validate_id_consum(datas_consumable, id_input):
            nama = input("Masukkan Nama: ")
            deskripsi  = input("Masukkan Deskripsi: ")
            jumlah = int(input("Masukkan Jumlah: "))
            rarity = input("Masukkan Rarity: ")
            while not validate_rarity(rarity):
                print("Input rarity tidak valid! Rarity yang valid adalah C, B, A, S")
                rarity = input("Masukkan Rarity: ")
            data_consumable_baru = [id_input,nama,deskripsi,jumlah,rarity]
            datas_consumable.append(data_consumable_baru)
            print("\nItem telah berhasil ditambahkan ke database!")
        else:
            print("\nGagal menambahkan item karena ID sudah ada")
    else :
        print("\nGagal menambahkan item karena ID tidak valid!")