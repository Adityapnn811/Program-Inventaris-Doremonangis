# F07 mengubah jumlah gadget atau consumable

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

def validate_jumlah_gadget(datas_gadget, jumlah, id_input):
    for i in range(len(datas_gadget)):
        if datas_gadget[i][0] == id_input:
            stok = datas_gadget[i][3] + jumlah
            if stok < 0:
                print("\n>>> {} {} gagal dibuang karena stok kurang. Stok sekarang: {} (< {})".format((-1 * jumlah),
                                                                                                datas_gadget[i][1],
                                                                                                datas_gadget[i][0],
                                                                                                (-1 * jumlah)))
            else: # Kalo stok nya >= 0
                datas_gadget[i][3] += jumlah
                if jumlah < 0:
                    print("\n>>> {} {} berhasil dibuang. Stok sekarang: {}".format((-1 * jumlah),datas_gadget[i][1], stok))
                elif jumlah >= 0:
                    print("\n>>> {} {} berhasil ditambahkan. Stok sekarang: {}".format(jumlah, datas_gadget[i][1], stok))

def validate_jumlah_consumable(datas_consum, jumlah, id_input):
    for i in range(len(datas_consum)):
        if datas_consum[i][0] == id_input:
            stok = datas_consum[i][3] + jumlah
            if stok < 0:
                print("\n>>> {} {} gagal dibuang karena stok kurang. Stok sekarang: {} (< {})".format((-1 * jumlah),
                                                                                                datas_consum[i][1],
                                                                                                datas_consum[i][3],
                                                                                                (-1 * jumlah)))
            else: # Kalo stok nya >= 0
                datas_consum[i][3] += jumlah
                if jumlah < 0:
                    print("\n>>> {} {} berhasil dibuang. Stok sekarang: {}".format((-1 * jumlah),datas_consum[i][1], stok))
                elif jumlah >= 0:
                    print("\n>>> {} {} berhasil ditambahkan. Stok sekarang: {}".format(jumlah, datas_consum[i][1], stok))


def ubahjumlah(datas_gadget, datas_consumable):
    print("")
    id_input = input("Masukkan ID: ")
    # Mengolah jumlah gadget
    if id_input[0] == 'G':
        if validate_id_gadget(datas_gadget, id_input):
            jumlah = int(input("Masukkan Jumlah: "))
            validate_jumlah_gadget(datas_gadget, jumlah, id_input)
        else:
            print("\nTidak ada item dengan ID tersebut!")
    # Mengolah jumlah consumable
    elif id_input[0] == 'C':
        if validate_id_consum(datas_consumable, id_input):
            jumlah = int(input("Masukkan Jumlah: "))
            validate_jumlah_consumable(datas_consumable, jumlah, id_input)
        else:
            print("\nTidak ada item dengan ID tersebut!")
    else:
        print("\nTidak ada item dengan ID tersebut!")