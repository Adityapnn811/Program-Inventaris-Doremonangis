from load import load
from help import bantuan
import sys

if load() == False:
    print("\nTidak ada nama folder yang diberikan!")
    print("Usage: python kantongajaib.py <nama_folder>")
    sys.exit(1)
else:
    flag_exit = False
    print("\nLoading...")
    print('\n\nSelamat datang di "Kantong Ajaib"!')
    while not flag_exit:
        print("\nApa yang ingin kamu lakukan di kantong ajaib?\n1. Register\n2. Login"
                         "\n3. Help\n4. Keluar")
        perintah_pertama = int(input())
        if perintah_pertama == 3:
            bantuan()
        elif perintah_pertama == 4:
            sys.exit(1)
