# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:33:45 2024

@author: Administrator
"""

def cek_kabisat(tahun):
   if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
       return True
   return False

def hitung_hari(bulan, tahun=2024):
   if bulan == 0:
       print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
       return
       
   hari_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   
   if cek_kabisat(tahun) and bulan == 2:
       print("29 hari dalam sebulan")
   else:
       print(f"{hari_bulan[bulan]} hari dalam sebulan")

print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
print("Masukkan 0 untuk menghentikan program")

while True:
   bulan = int(input("masukkan bulan (1-12): "))
   if bulan == 0:
       hitung_hari(0)
       break
   elif bulan < 1 or bulan > 12:
       print("Bulan tidak valid!")
       continue
       
   hitung_hari(bulan)