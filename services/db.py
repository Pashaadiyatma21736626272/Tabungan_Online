import mysql.connector

db = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='tabunganku'
)


def insert_saldo(Tambah_Saldo, Ambil_Saldo, Keterangan, Saldo_Akhir):
  cursor = db.cursor()
  cursor.execute("INSERT INTO tabungan_online (Tambah_Saldo, Ambil_Saldo, Keterangan, Saldo_Akhir) VALUES (%s, %s, %s, %s)", (Tambah_Saldo, Ambil_Saldo, Keterangan, Saldo_Akhir))
  db.commit()
  if cursor.rowcount > 0:
    return '==========='
  else:
    return '==========='

def get_saldo():
  cursor = db.cursor()
  cursor.execute("SELECT Saldo_Akhir FROM tabungan_online LIMIT 1")
  result = cursor.fetchone()
  return result[0] if result is not None else 0