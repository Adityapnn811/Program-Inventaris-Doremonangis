from F14_F15_load_dan_save import load, save
from F16_help import help_user, help_admin
from F17_exit import exit
import sys

load()

print("\nLoading...")
print('\n\nSelamat datang di "Kantong Ajaib"!')
while True:
    print("\nApa yang ingin kamu lakukan di kantong ajaib?\n1. register\n2. login"
            "\n3. help\n4. exit\n5. save")
    perintah_pertama = input("Ketikkan perintah: ")
    if perintah_pertama == "help":
        help_user()
        help_admin()
    elif perintah_pertama == "save":
        save()
    elif perintah_pertama == "exit" or perintah_pertama == "Exit" or perintah_pertama == "EXIT":
        exit()
    else:
        print("\nPerintah tidak valid, harap ulangi.")
