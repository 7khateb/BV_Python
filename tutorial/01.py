# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:10:46 2021

@author: Abdul
"""

print("Hallo Hier ist Abdul!")

vorname = "Abdul "
nachname = " Nicht gegeben"
alte = 33
status = "Ledig"
beruf = "Student"
jahre = 1998
month = "Juni "
day = 28
geburtsdatum = month + str(jahre)

print(vorname.lower() + nachname.upper())

print("Heir wird der Vorname buchstabiert: ")
for x in range(0,len(vorname)-1):
    print(vorname[x].upper())
    
    
print("Hier wird die Index des Vorname gegeben")
print(vorname.upper().index("U"))
print(vorname.upper().index("B"))
print(vorname.index("A"))
print(vorname.upper().index("L"))
print(vorname.upper().index("D"))

#Wir probieren boolean Variable aus.
a = True
b = False



if a== True:
    print ("You are right!")
    
vorname = "abdul "
if vorname.islower():
    print("Vorname soll mit einem großen Buchstaben anfangen!\n")
    
    
print("17/3 = "+ str(17/3))    #Division mit Rest
print("17//3 = "+str(17//3))   #Division ohne Rest
print("Modulo: 17%3 = "+str(17%3))
print("Exponent: 5**3 = "+ str(5**3))
print("Aufrunden: 132.047583 = "+ str(round(132.047583,3))) #Aufrunden die letzten 3 Ziffern.

print('C:\some\name')
print(r"Um den \n zu überspringe muss man in der Printanweisung r vor dem String schreiben: " "\n" +r'C:\some\name') 


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")