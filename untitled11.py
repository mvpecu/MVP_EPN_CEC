#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 19:02:58 2022

@author: mvp
"""

file = open("devices.txt", "a")
while True:
newItem = input("Ingrese un nuevo elemento al inventario: ")
if newItem == "exit":
print("todo OK")
break
file.write(newItem + "\n")
file.close()
