# F06 Menghapus gadget atau consumable

# Deklarasi variable global indeks_item
indeks_item = 0

def IsGadget(datas_gadget, idItem):
    global indeks_item
    found = False
    for i in range(len(datas_gadget)):
        if idItem == datas_gadget[i][0]:
            found = True
            indeks_item = i
    return found

def IsConsumable(datas_consumable, idItem):
    global indeks_item
    found = False
    for i in range(len(datas_consumable)):
        if idItem == datas_consumable[i][0]:
            found = True
            indeks_item = i
    return found

def DeleteItem(datas_gadget, datas_consumable, idItem, idx_item):
    if IsGadget(datas_gadget, idItem):
        datas_gadget.remove(datas_gadget[idx_item])
    elif IsConsumable(datas_consumable, idItem):
       datas_consumable.remove(datas_consumable[idx_item])

def validate_konfirm(konfirm):
    if konfirm == 'Y' or konfirm == 'N':
        return True
    else:
        return False

def hapus_item(datas_gadget, datas_consumable):
    global indeks_item
    idItem = input("Masukkan ID item yang ingin dihapus: ")
    # Kalo yang mau dihapus gadget
    if IsGadget(datas_gadget, idItem):
        idx_item = indeks_item
        konfirm = input(f"Apakah kamu yakin ingin menghapus {datas_gadget[idx_item][1]} (Y/N)? ")
        while not validate_konfirm(konfirm):
            print("Input konfirmasi tidak valid! Harap ulangi!")
            konfirm = input(f"Apakah kamu yakin ingin menghapus {datas_gadget[idx_item][1]} (Y/N)? ")
        if konfirm == 'Y':
            DeleteItem(datas_gadget, datas_consumable, idItem, idx_item)
            print("\nItem telah berhasil dihapus dari database.")
        elif konfirm == 'N':
            print("\nItem tidak jadi dihapus.")
    # Kalo yang mau dihapus consumable
    elif IsConsumable(datas_consumable, idItem):
        idx_item = indeks_item
        konfirm = input(f"Apakah kamu yakin ingin menghapus {datas_consumable[idx_item][1]} (Y/N)? ")
        while not validate_konfirm(konfirm):
            print("Input konfirmasi tidak valid! Harap ulangi!")
            konfirm = input(f"Apakah kamu yakin ingin menghapus {datas_consumable[idx_item][1]} (Y/N)? ")
        if konfirm == 'Y':
            DeleteItem(datas_gadget, datas_consumable, idItem, idx_item)
            print("\nItem telah berhasil dihapus dari database.")
        elif konfirm == 'N':
            print("\nItem tidak jadi dihapus.")
    else:
        print("\nTidak ada item dengan ID tersebut.")