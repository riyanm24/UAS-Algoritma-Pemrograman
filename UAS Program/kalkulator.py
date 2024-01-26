'''Kalkulator Sederhana'''

'''Membuat inputan user'''
print('=' * 25)
print('Operasi Matematika')
print(' 1. Jumlah \t [+]')
print(' 2. Kurang \t [-]')
print(' 3. Kali \t [*]')
print(' 4. Bagi \t [/]')
print('=' * 25)
operasi = input('Pilih operasi (1/2/3/4): ') # Pemilihan operasi

'''Logika percabangan dasar'''
'''Memeriksa isi dari variabel operasi, apakah bernilai 1,2,3,atau 4'''
print('=' * 25)
if operasi == '1':
  print('User memilih penjumlahan') # Hasil operasi 1 penjumlahan
elif operasi == '2':
  print('User memilih pengurangan') # Hasil operasi 2 pengurangan
elif operasi == '3':
  print('User memilih perkalian') # Hasil operasi 3 perkalian
elif operasi == '4':
  print('User memilih pembagian') # Hasil operasi 4 pembagian
else:
  print('Tidak valid')

'''Input bilangan'''
print('=' * 25)
bilangan_1 = eval(input('Masukan bilangan pertama: ')) # Bilangan pertama yang ingin di operasikan
bilangan_2 = eval(input('Masukan bilangan kedua: ')) # Bilangan kedua yang ingin di operasikan

'''Menghitung Hasil Operasi'''
print('=' * 25)
if operasi == '1':
 hasil = bilangan_1 + bilangan_2
 print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}') # Hasil Penjumlahan bilangan 1 & 2
elif operasi == '2':
 hasil = bilangan_1 - bilangan_2
 print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}') # Hasil Pengurangan bilangan 1 & 2
elif operasi == '3':
 hasil = bilangan_1 * bilangan_2 
 print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}') # Hasil Perkalian bilangan 1 & 2
elif operasi == '4': 
 hasil = bilangan_1 / bilangan_2 
 print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}') # Hasil Pembagian bilangan 1 & 2
else: 
 print('Tidak valid')