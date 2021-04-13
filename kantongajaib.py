from fungsi_load_dan_save import load, save
from help import bantuan
import sys

def validate_save(konfirmasi_save):
    save = False
    if konfirmasi_save == 'y' or konfirmasi_save == 'n':
        save = True
    else:
        save = False
    return save

load()

#flag_exit = False
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
        konfirmasi_save = input("\nApakah Anda ingin menyimpan data sebelum keluar? (y/n)? : ")
        validate_save(konfirmasi_save)
        while not validate_save(konfirmasi_save):
            print("Mohon masukkan input yang valid.")
            konfirmasi_save = input("\nApakah Anda ingin menyimpan data sebelum keluar? (y/n)? : ")
            validate_save(konfirmasi_save)
        if konfirmasi_save == "y":
            save()
            print("Terima kasih telah menggunakan kantong ajaib!")
            sys.exit(1)
        elif konfirmasi_save =="n":
            print("Terima kasih telah menggunakan kantong ajaib!")
            sys.exit(1)
