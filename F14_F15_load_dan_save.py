import argparse
import sys
import os.path
from os import path
from fungsi_parser import parser

# Deklarasi variable datas
datas_user = []
datas_gadget = []
datas_consumable = []
datas_consumable_history = []
datas_gadget_borrow_history = []
datas_gadget_return_history = []

# MEngubah baris csv menjadi array dengan memisahkan baris saat bertemu semicolon
def konversi_baris_ke_data(line):
    data_array_mentah = parser(line)
    data_array = [data.strip() for data in data_array_mentah]
    return data_array

def konversi_data_array_ke_tipe_sesuai(data_array, TOTAL_KOLOM, idxjml):  # Fungsi buat ngubah string ke integer
    arr_copy = data_array[:]
    for i in range(TOTAL_KOLOM):
        if i == idxjml:
            arr_copy[i] = int(arr_copy[i])
    return arr_copy

def buat_data_sesuai_tipe_data(datas, lines, TOTAL_KOLOM, idxjml):
    for line in lines:
        data_array = konversi_baris_ke_data(line)
        data_array_sesuai_tipe_data = konversi_data_array_ke_tipe_sesuai(data_array, TOTAL_KOLOM, idxjml)
        datas.append(data_array_sesuai_tipe_data)
    return datas

def buat_data(datas, lines):  # Ntar datas dan lines tergantung csvnya
    for line in lines:
        data_array = konversi_baris_ke_data(line)
        datas.append(data_array)
    return datas

def load():
    global header_user, datas_user, header_gadget, datas_gadget, header_consumable, datas_consumable
    global header_consumable_history, datas_consumable_history, header_gadget_borrow_history, datas_gadget_borrow_history
    global header_gadget_return_history, datas_gadget_return_history
    load_parser = argparse.ArgumentParser()  #masukkan line ke variabel supaya lebih mudah
    load_parser.add_argument("nama_folder", help="python kantongajaib.py <nama_folder>")  # menambah argumen nama folder pada command line
    args = load_parser.parse_args()
    if path.isdir("Kantong/" + args.nama_folder):  # mengecek apakah ada folder sesuai dengan nama folder yang dimasukkan pada argumen
        # Untuk user
        f = open("Kantong/" + args.nama_folder + "\\user.csv", "r") # Mengakses folder
        raw_lines_user = f.readlines() # Membaca semua baris yang ada di csv
        f.close()
        lines_user = [raw_line.replace("\n", "") for raw_line in raw_lines_user] # Menghapus newline pada data dan mengubah ke bentuk array of tuple
        raw_header_user = lines_user.pop(0)  # Buat ngehapus header di csv, jadi engga nyusahin pas ngolah data di fugnsi laen
        header_user = konversi_baris_ke_data(raw_header_user)  #Ntar join di fungsi save
        buat_data(datas_user, lines_user) # Membuat array dari baris

        # Untuk gadget
        f = open("Kantong/" + args.nama_folder + "\\gadget.csv", "r")
        raw_lines_gadget = f.readlines()
        f.close()
        lines_gadget = [raw_line.replace("\n", "") for raw_line in raw_lines_gadget]
        raw_header_gadget = lines_gadget.pop(0)
        header_gadget = konversi_baris_ke_data(raw_header_gadget)  # Ntar join di fungsi save
        buat_data_sesuai_tipe_data(datas_gadget, lines_gadget, 6, 3)

        # Untuk consumable
        f = open("Kantong/" + args.nama_folder + "\\consumable.csv", "r")
        raw_lines_consumable = f.readlines()
        f.close()
        lines_consumable = [raw_line.replace("\n", "") for raw_line in raw_lines_consumable]
        raw_header_consumable = lines_consumable.pop(0)
        header_consumable = konversi_baris_ke_data(raw_header_consumable)  # Ntar join di fungsi save
        buat_data_sesuai_tipe_data(datas_consumable, lines_consumable, 5, 3)

        # Untuk consumable_history
        f = open("Kantong/" + args.nama_folder + "\\consumable_history.csv", "r")
        raw_lines_consumable_history = f.readlines()
        f.close()
        lines_consumable_history = [raw_line.replace("\n", "") for raw_line in raw_lines_consumable_history]
        raw_header_consumable_history = lines_consumable_history.pop(0)
        header_consumable_history = konversi_baris_ke_data(raw_header_consumable_history)  # Ntar join di fungsi save
        buat_data_sesuai_tipe_data(datas_consumable_history, lines_consumable_history, 5, 4)

        # Untuk gadget_borrow_history
        f = open("Kantong/" + args.nama_folder + "\\gadget_borrow_history.csv", "r")
        raw_lines_gadget_borrow_history = f.readlines()
        f.close()
        lines_gadget_borrow_history = [raw_line.replace("\n", "") for raw_line in raw_lines_gadget_borrow_history]
        raw_header_gadget_borrow_history = lines_gadget_borrow_history.pop(0)
        header_gadget_borrow_history = konversi_baris_ke_data(raw_header_gadget_borrow_history)  # Ntar join di fungsi save
        buat_data_sesuai_tipe_data(datas_gadget_borrow_history, lines_gadget_borrow_history, 6, 4)

        # Untuk gadget_return_history
        f = open("Kantong/" + args.nama_folder + "\\gadget_return_history.csv", "r")
        raw_lines_gadget_return_history = f.readlines()
        f.close()
        lines_gadget_return_history = [raw_line.replace("\n", "") for raw_line in raw_lines_gadget_return_history]
        raw_header_gadget_return_history = lines_gadget_return_history.pop(0)
        header_gadget_return_history = konversi_baris_ke_data(raw_header_gadget_return_history)  # Ntar join di fungsi save
        buat_data_sesuai_tipe_data(datas_gadget_return_history, lines_gadget_return_history, 4, 3)

    else:
        print("\nTidak ada nama folder yang diberikan!")
        print("Usage: python kantongajaib.py <nama_folder>")
        sys.exit(1)

def save():
    global header_user, datas_user, header_gadget, datas_gadget, header_consumable, datas_consumable
    global header_consumable_history, datas_consumable_history, header_gadget_borrow_history, datas_gadget_borrow_history
    global header_gadget_return_history, datas_gadget_return_history

    # Mengubah array yang berisi data ke dalam bentuk string baris per baris
    def konversi_data_ke_string(datas, header):
        string_data = ";".join(header) + "\n"
        for arr_data in datas:
            arr_data_all_string = [str(val) for val in arr_data]
            string_data += ";".join(arr_data_all_string)
            string_data += "\n"
        datas = string_data
        return datas

    # Input nama folder dan mengecek apakah nama folder sudah ada
    nama_folder = input("\nMasukkan nama folder penyimpanan: ")
    if not os.path.exists("Kantong/" + nama_folder):
        os.mkdir("Kantong/" + nama_folder)

    print("\nSaving...")

    # Untuk user
    f = open("Kantong/" + nama_folder + "\\user.csv", "w+")
    f.write(konversi_data_ke_string(datas_user, header_user))
    f.close()

    # Untuk gadget
    f = open("Kantong/" + nama_folder + "\\gadget.csv", "w+")
    f.write(konversi_data_ke_string(datas_gadget, header_gadget))
    f.close()

    # Untuk consumable
    f = open("Kantong/" + nama_folder + "\\consumable.csv", "w+")
    f.write(konversi_data_ke_string(datas_consumable, header_consumable))
    f.close()

    # Untuk consumable_history
    f = open("Kantong/" + nama_folder + "\\consumable_history.csv", "w+")
    f.write(konversi_data_ke_string(datas_consumable_history, header_consumable_history))
    f.close()

    # Untuk gadget_borrow_history
    f = open("Kantong/" + nama_folder + "\\gadget_borrow_history.csv", "w+")
    f.write(konversi_data_ke_string(datas_gadget_borrow_history, header_gadget_borrow_history))
    f.close()

    # Untuk gadget_return_history
    f = open("Kantong/" + nama_folder + "\\gadget_return_history.csv", "w+")
    f.write(konversi_data_ke_string(datas_gadget_return_history, header_gadget_return_history))
    f.close()

    print("Data telah disimpan pada folder " + nama_folder + "!")

if __name__ == '__main__':
    load()
