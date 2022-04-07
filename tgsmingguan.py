from tkinter import N
import psycopg2
import os

db = psycopg2.connect(
  host="localhost",
  port=30602,
  user="didin",
  password="Fadill546",
  database="tutut"
)

def insert_data(db):
  idmhs = input("Masukan Idmhs: ")
  nim = input("Masukan Nim: ")
  nama = input("Masukan Nama: ")
  idfakultas = (input("Masukan idfakultas: "))
  idprodi = (input("Masukan idProdi: "))
  val = (idmhs, nim, nama, idfakultas, idprodi)
  cursor = db.cursor()
  sql = "INSERT INTO mahasiswa (idmhs, nim, nama, idfakultas, idprodi) VALUES (%s,%s,%s,%s,%s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM mahasiswa"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  idmhs= input("Masukan IDmhs: ")
  nim = input ("Masukan Nim Baru: ")
  nama = input("Masukan Nama Baru: ")
  idfakultas = input("Masukan idfakultas Baru: ")
  idprodi = input("Masukan idProdi Baru: ")
  sql = "UPDATE mahasiswa SET nim=%s, nama=%s, idfakultas=%s, idprodi=%s WHERE idmhs=%s"
  val = (nim, nama, idfakultas, idprodi, idmhs)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  idmhs = input("masukan idmhs> ")
  sql = "DELETE FROM mahasiswa WHERE idmhs=%s"
  val = (idmhs,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci NIM/NAMA : ")
  sql = "SELECT * FROM mahasiswa WHERE nama LIKE %s OR nim LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("-----Fadhilah Ruhiyah-----")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  #os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)