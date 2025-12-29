from time import sleep
from services.db import insert_saldo, get_saldo
Rekening = 0

def format_uang(jumlah):
  return f"{jumlah:,.0f}".replace(",", ".")

def load_saldo():
  global Rekening
  Rekening = get_saldo()
  return Rekening

def Tambah_saldo():
  global Rekening
  Tambah_Saldo = int(input("Masukkan saldo : Rp "))
  Rekening += Tambah_Saldo
  print(f"Rp {format_uang(Tambah_Saldo)} Berhasil Masuk Ke Rekening ! ")
  save = insert_saldo(Tambah_Saldo, 0, "Tambah Saldo", Rekening)
  print(save)

def Lihat_saldo():
  if Rekening == 0:
    print('Rekening Mu Kosong !!!!')
  else:
    print(f'Saldo Kamu Sekarang ===> Rp {format_uang(Rekening)}')

def Ambil_saldo():
  global Rekening
  print(f'Saldo Kamu Sekarang ====> Rp {format_uang(Rekening)}')
  uang = int(input('Masukkan Saldo Yang Mau Di Ambil :'))
  print(f'Rp {format_uang(uang)} Saldo Yang Akan Diambil')
  if uang <= Rekening:
    Rekening -= uang
    keterangan = input('Alasan Pengambilan : ')
    save = insert_saldo(0, uang, keterangan, Rekening)
    print(f'Rp {format_uang(uang)} => Telah Diambil Dari Rekening ')
    print(save)
  else:
    print(f'Saldo tidak cukup!')

def Keluar():
    print("Anda Akan Keluar...")
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Terima Kasih Sudah Menggunakan Tabungan Ini !')
    exit()
  

