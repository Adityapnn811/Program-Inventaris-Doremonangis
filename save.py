from os import path
import os.path

def save(DATABASE, data):
    nama_folder = input("Masukkan nama folder penyimpanan: ")
    if not os.path.exists(nama_folder):   # Ntar buat folder baru
        f = open(DATABASE, "w")
        f.write(data)
        f.close()
        print("\nSaving...")
        print("Data telah disimpan pada folder {}!".format(nama_folder))
    else:  #Ntar ditimpa aja