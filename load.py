import argparse
from os import path

def load():
    load_parser = argparse.ArgumentParser()  #masukkan line ke variabel supaya lebih mudah
    load_parser.add_argument("nama_folder", help="python kantongajaib.py <nama_folder>")  # menambah argumen nama folfer pada command line
    args = load_parser.parse_args()
    if path.isdir(args.nama_folder):  # mengecek apakah ada folder sesuai dengan nama folder yang dimasukkan pada argumen
        return True
    else:
        return False

if __name__ == '__main__':
    load()