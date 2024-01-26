'''BATU GUNTING KERTAS'''

import random # Random untuk mengacak tindakan komputer di dalam game

'''Menggunakan Perulangan WhileLoop untuk bermain tanpa batas'''
while True:
    user_action = input("Masukan Pilihan (batu, kertas, gunting): ") # input pilihan user
    possible_actions = ["batu", "kertas", "gunting"] # Buat agar komputer memilih
    computer_action = random.choice(possible_actions) # Komputer memilih
    print(f"\nKamu pilih {user_action}, computer pilih {computer_action}.\n") # Hasil input user & input bot

    '''Menentukan pemenang menggunakan if, elif, else'''
    if user_action == computer_action:
        print(f"Keduanya memilih {user_action}. Ini Seri!")
    elif user_action == "batu":
        if computer_action == "gunting":
            print("Batu menghancurkan gunting! Kamu Menang!") # Hasil jika user Batu & bot Gunting
        else:
            print("Kertas menutup batu! Kamu Kalah.") # Hasil jika user Batu & bot Kertas
    elif user_action == "kertas":
        if computer_action == "batu":
            print("Kertas menutup batu! Kamu Menang!") # Hasil jika user Kertas & bot Batu
        else:
            print("Gunting memotong kertas! Kamu Kalah.") # Hasil jika user Kertas & bot Gunting
    elif user_action == "gunting":
        if computer_action == "kertas":
            print("Gunting memotong kertas! Kamu Menang!") # Hasil jika user Gunting & bot Kertas
        else:
            print("Batu menghancurkan gunting! Kamu Kalah.") # Hasil jika user Gunting & bot Batu

    '''Menentukan ingin lanjut atau tidak nya permainan'''
    play_again = input("Main Lagi? (y/n): ")
    if play_again.lower() != "y":
        break