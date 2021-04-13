import sys
from F14_F15_load_dan_save import save

# Fungsi buat validasi mau ngesave ato engga
def validate_save(konfirmasi_save):
    save = False
    if konfirmasi_save == 'y' or konfirmasi_save == 'n' or konfirmasi_save == 'Y' or konfirmasi_save == 'N':
        save = True
    else:
        save = False
    return save

def exit():
    konfirmasi_save = input("\nApakah Anda ingin menyimpan data sebelum keluar? (y/n)? : ")
    validate_save(konfirmasi_save)
    while not validate_save(konfirmasi_save):
        print("Mohon masukkan input yang valid.")
        konfirmasi_save = input("\nApakah Anda ingin menyimpan data sebelum keluar? (y/n)? : ")
        validate_save(konfirmasi_save)
    if konfirmasi_save == "y" or konfirmasi_save == 'Y':
        save()
        print("Terima kasih telah menggunakan kantong ajaib!")
        sys.exit(1)
    elif konfirmasi_save =="n" or konfirmasi_save == 'N':
        print("Terima kasih telah menggunakan kantong ajaib!")
        sys.exit(1)