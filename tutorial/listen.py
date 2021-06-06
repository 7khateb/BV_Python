# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:54:29 2021

@author: Abdul
"""



print("In diesem Abschnitt werden wir Listen in Python kennenlernen.\n")

liste01 = [3,6,9,12,15,18]
print(liste01)               #oder print(liste01[:])
print(liste01[2:4])
print(liste01.index(12))
print(liste01[-2])
print(liste01+[21,24,27])

print("\nIn diesem Abschnitt werden listen bearbeiten.")
cubes = [1,8,27,65,125]
#replace
#wir wollen den Wert 65 mit 64 ersetzen.
cubes[cubes.index(65)] = 64

#Ein Weiters Wert addieren.
cubes.append(216)
