from F14_F15_load_dan_save import load, save
from F16_help import bantuan
from F17_exit import exit
import sys


load()

print("\nLoading...")
print('\n\nSelamat datang di "Kantong Ajaib"!')
while True:
    print("\nApa yang ingin kamu lakukan di kantong ajaib?\n1. register\n2. login"
            "\n3. help\n4. keluar\n5. save")
    perintah_pertama = input("Ketikkan perintah: ")
    if perintah_pertama == "help":
        bantuan()
    elif perintah_pertama == "save":
        save()
    elif perintah_pertama == "keluar":
        exit()