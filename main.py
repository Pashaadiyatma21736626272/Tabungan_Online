import libs

Tambah = libs.Tambah_saldo
Lihat = libs.Lihat_saldo
Ambil = libs.Ambil_saldo
Keluar = libs.Keluar

libs.load_saldo()  

while True :
  print("\n==== Tabungan Ku ====")
  print(' Pilih Menu :')
  print('1.Tambah Saldo')
  print('2.Lihat Rekening')
  print('3.Ambil Saldo')
  print('4.Keluar')

  Pilihan = int(input('Pilihan Anda (1-4) :'))

  if Pilihan == 1:
    Tambah()
  elif Pilihan == 2:
    Lihat()
  elif Pilihan == 3:
    Ambil()
  elif Pilihan == 4:
    Keluar()
  else:
    print('Eror, Silahkan Coba Lagi')


