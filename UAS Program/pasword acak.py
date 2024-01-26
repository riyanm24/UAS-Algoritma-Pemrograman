''' PASSWORD ACAK'''

import string
import random

'''Menghasilkan Kata Sandi'''
huruf = list(string.ascii_letters)
angka = list(string.digits)
karakter_khusus = list("!@#$%^&*()")
karakter = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def menghasilkan_random_password():
	'''Panjang Kata Sandi'''
	panjang = int(input("Masukan panjang kata sandi: "))
	'''Input jumlah huruf, angka, karakter khusus'''
	jumlah_huruf = int(input("Masukan jumlah huruf pada kata sandi: "))
	jumlah_angka = int(input("Masukan jumlah angka pada kata sandi: "))
	jumlah_karakter_khusus = int(input("Masukan jumlah karakter khusus pada kata sandi: "))
	'''Jumlah Total Karakter'''
	jumlah_karakter = jumlah_huruf + jumlah_angka + jumlah_karakter_khusus

	'''Periksa panjang total dengan jumlah karakter'''
	'''Tidak Valid jika jumlahnya lebih besar dari panjangnya'''
	if jumlah_karakter > panjang:
		print("Jumlah total karakter lebih besar dari panjang kata sandi")
		return


	'''Inisial kata sandi'''
	password = []
	
	'''Memilih huruf acak'''
	for i in range(jumlah_huruf):
		password.append(random.choice(huruf))


	'''Memilih digit acak'''
	for i in range(jumlah_angka):
		password.append(random.choice(angka))


	'''Memilih huruf acak'''
	for i in range(jumlah_karakter_khusus):
		password.append(random.choice(karakter_khusus))


	'''Jika jumlah karakter total kurang dari panjang sandi'''
	'''akan menambahkan karakter acak agar sama dengan panjangnya'''
	if jumlah_karakter < panjang:
		random.shuffle(karakter)
		for i in range(panjang - jumlah_karakter):
			password.append(random.choice(karakter))


	'''Mengacak kata sandi yang di hasilkan'''
	random.shuffle(password)

	'''Konversi daftar menjadi string'''
	'''Mencetak daftar'''
	print("".join(password))

'''Meminta Fungsi'''
menghasilkan_random_password()