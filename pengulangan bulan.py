# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 02:21:15 2024

@author: Administrator
"""

# Program untuk menentukan jumlah hari dalam suatu bulan
while True:
    #inputan
    print("Enter -1 to stop the program")
    month = int(input("Enter the month (1-12): "))
    
    # command kalo mau user mau stop
    if month == -1:
        break
    
    # Validasi input bulan
    if month < 1 or month > 12:
        print("Invalid month input! Please enter between 1-12")
        continue
    
    # Meminta input tahun dari user
    year = int(input("Please enter the year (e.g., 2023): "))
    
    # Menentukan jumlah hari dalam bulan
    if month in [4, 6, 9, 11]:
        days = 30
    elif month == 2:
        # Mengecek tahun kabisat
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29
        else:
            days = 28
    else:
        days = 31
    
    # Menampilkan hasil
    print(f"There are {days} days in the month")
