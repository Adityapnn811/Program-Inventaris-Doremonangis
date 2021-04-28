from F14_F15_load_dan_save import *
from F16_help import help_user, help_admin
from F17_exit import exit
from F02 import *
from F01 import input_username
from F08 import *
from F09 import *
from F10_meminta_consumable import *
from F11_F12_F13 import *
from F05 import *
from F06 import *
from F07 import *
from F3_F4 import *

# Memanggil fungsi load untuk inisiasi array data
load()

print("\nLoading...\n")
print(''' ___  ____        _       ____  _____  _________    ___   ____  _____   ______         _          _____     _       _____  ______    
|_  ||_  _|      / \     |_   \|_   _||  _   _  | .'   `.|_   \|_   _|.' ___  |       / \        |_   _|   / \     |_   _||_   _ \   
  | |_/ /       / _ \      |   \ | |  |_/ | | \_|/  .-.  \ |   \ | | / .'   \_|      / _ \         | |    / _ \      | |    | |_) |  
  |  __'.      / ___ \     | |\ \| |      | |    | |   | | | |\ \| | | |   ____     / ___ \    _   | |   / ___ \     | |    |  __'.  
 _| |  \ \_  _/ /   \ \_  _| |_\   |_    _| |_   \  `-'  /_| |_\   |_\ `.___]  |  _/ /   \ \_ | |__' | _/ /   \ \_  _| |_  _| |__) | 
|____||____||____| |____||_____|\____|  |_____|   `.___.'|_____|\____|`._____.'  |____| |____|`.____.'|____| |____||_____||_______/ ''')
print('\n==========Selamat datang di "Kantong Ajaib"!==========')
print("\nSebelum masuk ke kantong ajaib, login dulu ya!")

id_user = login(datas_user) # memanggil fungsi login sekaligus assign id user

if id_user == "ADM":
    while True:
        print("\nApa yang ingin kamu lakukan di kantong ajaib?\n1. register"
              "\n2. carirarity\n3. caritahun\n4. tambahitem\n5. hapusitem\n6. ubahjumlah\n7. riwayatpinjam"
              "\n8. riwayatkembali\n9. riwayatambil\n10. save\n11. help\n12. exit")
        perintah_pertama = input("Ketikkan perintah: ")
        if perintah_pertama == "help":
            help_admin()
        elif perintah_pertama == "register":
            input_username(datas_user)
        elif perintah_pertama == "carirarity":
            gadget_by_rarity(datas_gadget)
        elif perintah_pertama == "caritahun":
            gadget_by_year(datas_gadget)
        elif perintah_pertama == "tambahitem":
            tambah_item(datas_gadget, datas_consumable)
        elif perintah_pertama == "hapusitem":
            hapus_item(datas_gadget, datas_consumable)
        elif perintah_pertama == "ubahjumlah":
            ubahjumlah(datas_gadget, datas_consumable)
        elif perintah_pertama == "riwayatpinjam":
            gadget_borrow_history_info(datas_gadget_borrow_history, datas_user, datas_gadget)
        elif perintah_pertama == "riwayatkembali":
            gadget_return_history_info(datas_gadget_return_history, datas_user, datas_gadget, datas_gadget_borrow_history)
        elif perintah_pertama == "riwayatambil":
            consum_request_history_info(datas_consumable_history, datas_user, datas_consumable)
        elif perintah_pertama == "save":
            save()
        elif perintah_pertama == "exit" or perintah_pertama == "Exit" or perintah_pertama == "EXIT":
            exit()
        else:
            print("\nPerintah tidak valid, harap ulangi.")
else:
    while True:
        print("\nApa yang ingin kamu lakukan di kantong ajaib?"
              "\n1. carirarity\n2. caritahun\n3. pinjam\n4. kembalikan\n5. minta\n6. save\n7. help\n8. exit")
        perintah_pertama = input("Ketikkan perintah: ")
        if perintah_pertama == "help":
            help_user()
        elif perintah_pertama == "carirarity":
            gadget_by_rarity(datas_gadget)
        elif perintah_pertama == "caritahun":
            gadget_by_year(datas_gadget)
        elif perintah_pertama == "pinjam":
            borrow_gadget(id_user, datas_gadget, datas_gadget_borrow_history)
        elif perintah_pertama == "kembalikan":
            return_borrowed(id_user, datas_gadget, datas_gadget_borrow_history, datas_gadget_return_history)
        elif perintah_pertama == "minta":
            minta_consumable(datas_consumable, id_user, datas_consumable_history)
        elif perintah_pertama == "save":
            save()
        elif perintah_pertama == "exit" or perintah_pertama == "Exit" or perintah_pertama == "EXIT":
            exit()
        else:
            print("\nPerintah tidak valid, harap ulangi.")
