# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:13:53 2024

@author: Administrator
"""

input_jumlah = int(input("Masukkan bilangan:"))

for i in range(input_jumlah,0,-1):
    for j in range(i):
        print(i, end=" ")
    print()