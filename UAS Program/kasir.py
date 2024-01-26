'''Mesin Kasir'''

print("--------- THE MARSOS ---------") #Nama RESTORAN
print("Kebab Minimalis Harga Ekonomis")

'''Penginputan pembeli yang memesan'''
pembeli = input("Masukkan nama Pembeli: ") # Input pembeli
alamat = input("Masukkan alamat rumah Pembeli: ") # Input alamat pembeli
No_telp = int(input("Masukkan No. Telepon Pembeli: ")) # Input no pembeli

'''Informasi waktu real-time & Data pembeli'''
import time
hari_ini = time.asctime( time.localtime(time.time()) )
data = pembeli + "di" + alamat + "dengan nomer telepon:"  
print ("Pesanan atas nama :", pembeli) 

'''List Menu Makanan'''
def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n------- FOOD List -------")
   print("1. KIDS MARSOTE Go - Rp 6.000")
   print("2. MARSOTE GoGo - Rp 8.000")
   print("3. CHEESE MARSOTE GO - Rp 10.000")
   print("4. KEBAB MARSOTE - Rp 12.000")
   print("5. KEBAB MARIBET - Rp 15.000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   '''Percabangan untuk membuat hasil program'''
   if nomor==1:
       totalmkn=porsi*6000
       print (porsi," porsi KIDS MARSOTE Go = Rp", totalmkn)
       mkn=("KIDS MARSOTE Go")
   elif nomor==2:
       totalmkn=porsi*8000
       print (porsi," porsi MARSOTE GoGo = Rp", totalmkn)
       mkn=("MARSOTE GoGo")
   elif nomor==3:
       totalmkn=porsi*10000
       print (porsi, " porsi CHEESE MARSOTE GO = Rp", totalmkn)
       mkn=("CHEESE MARSOTE GO")
   elif nomor==4:
       totalmkn=porsi*12000
       print (porsi," porsi KEBAB MARSOTE = Rp", totalmkn)
       mkn=("KEBAB MARSOTE")
   elif nomor==5:
       totalmkn=porsi*15000
       print (porsi," porsi KEBAB MARIBET = Rp", totalmkn)
       mkn=("KEBAB MARIBET")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

'''List Menu Minuman'''
def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----- DRINK List -----")
   print("1. Mineral Water - Rp 6.000")
   print("2. MarTEA Tawar - Rp 8.000")
   print("3. MarTEA Manis - Rp 10.000")
   print("4. Matcha Milk - Rp 15.000")
   print("5. Chocolate Cheese - Rp 15.000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

# Percabangan untuk membuat hasil dari menu minuman
   if nomor==1:
       totalmnm=gelas*6000
       print (gelas," Botol Mineral Water = Rp", totalmnm)
       mnm=(" Botol Mineral Water")
   elif nomor==2:
       totalmnm=gelas*8000
       print (gelas, " Gelas MarTEA Tawar = Rp", totalmnm)
       mnm=("MarTEA Tawar")
   elif nomor==3:
       totalmnm=gelas*10000
       print (gelas, " Gelas MarTEA Manis = Rp", totalmnm)
       mnm=("MarTEA Manis")
   elif nomor==4:
       totalmnm=gelas*15000
       print (gelas," Gelas Matcha Milk = Rp", totalmnm)
       mnm=("Matcha Milk")
   elif nomor==5:
       totalmnm=gelas*15000
       print(gelas," Gelas Chocolate Cheese = Rp", totalmnm)
       mnm=("Chocolate Cheese")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

'''hasil dari total harga dari makanan dan minuman'''
fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

'''visualisasi struk dari hasil pemesanan'''
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))#40000
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("======= S T R U K   B E L I =======")
print("====================================")
print ("Nama\t\t\t:",pembeli)
print ("Alamat\t\t\t:", alamat)
print ("Nomor Telepon\t\t:", "+62",No_telp)
print ("Beli\t\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Total\t\t\t: Rp",totalsemua)
print ("Dibayar\t\t\t: Rp",uang)
print ("Kembalian\t\t: Rp",kembalian)
print ("Tanggal pembelian\t:", hari_ini)
print("==================================")
print("==================================")
