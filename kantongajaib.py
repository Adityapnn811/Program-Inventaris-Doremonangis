from F14_F15_load_dan_save import *
from F16_help import help_user, help_admin
from F17_exit import exit
from F02 import login
from F01 import input_username
import sys


load()

print("\nLoading...")
print('\nSelamat datang di "Kantong Ajaib"!')
print("Sebelum masuk ke kantong ajaib, login dulu ya!")

if (login(datas_user)) == "ADM":  # Udah manggil fungsi login, jadi ngga usah dipanggil dulu sebelumnya
    while True:
        print("\nApa yang ingin kamu lakukan di kantong ajaib?\n1. register"
              "\n2. help\n3. exit\n4. save")
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
        print("\nApa yang ingin kamu lakukan di kantong ajaib?"
              "\n1. help\n2. exit\n3. save")
        perintah_pertama = input("Ketikkan perintah: ")
        if perintah_pertama == "help":
            help_user()
        elif perintah_pertama == "save":
            save()
        elif perintah_pertama == "exit" or perintah_pertama == "Exit" or perintah_pertama == "EXIT":
            exit()
        else:
            print("\nPerintah tidak valid, harap ulangi.")
