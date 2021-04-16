from F14_F15_load_dan_save import *
from F16_help import help_user, help_admin
from F17_exit import exit
from F02 import login
from F01 import input_username
from F08 import *
from F09 import *
import sys

load()

print("\nLoading...")
print('\n==========Selamat datang di "Kantong Ajaib"!==========')
print("\nSebelum masuk ke kantong ajaib, login dulu ya!")

if (login(datas_user)) == "ADM":  # Udah manggil fungsi login, jadi ngga usah dipanggil dulu sebelumnya
    while True:
        userid = "ADM"
        print(userid)
        print("\nApa yang ingin kamu lakukan di kantong ajaib?\n1. register"
              "\n2. carirarity\n3. caritahun\n4. tambahitem\n5. hapusitem\n6. ubahjumlah\n7. riwayatpinjam"
              "\n8. riwayatkembali\n9.riwayatambil\n10. save\n11. help\n12. exit")
        perintah_pertama = input("Ketikkan perintah: ")
        if perintah_pertama == "help":
            help_admin()
        elif perintah_pertama == "register":
            input_username(datas_user)
        elif perintah_pertama == "save":
            save()
        elif perintah_pertama == "exit" or perintah_pertama == "Exit" or perintah_pertama == "EXIT":
            exit()
        else:
            print("\nPerintah tidak valid, harap ulangi.")
else:
    while True:
        userid = "user"
        print("\nApa yang ingin kamu lakukan di kantong ajaib?"
              "\n1. carirarity\n2. caritahun\n3. pinjam\n4. kembalikan\n5. minta\n6. save\n7. help\n8. exit")
        perintah_pertama = input("Ketikkan perintah: ")
        if perintah_pertama == "help":
            help_user()
        elif perintah_pertama == "pinjam":
            borrow_gadget(userid, datas_gadget, datas_gadget_borrow_history)
        elif perintah_pertama == "kembalikan":
            return_borrowed(userid, datas_gadget, datas_gadget_borrow_history, datas_gadget_return_history)
        elif perintah_pertama == "save":
            save()
        elif perintah_pertama == "exit" or perintah_pertama == "Exit" or perintah_pertama == "EXIT":
            exit()
        else:
            print("\nPerintah tidak valid, harap ulangi.")
