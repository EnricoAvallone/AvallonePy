from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt
from random import randint

root = Tk() 
root.title('leggi sotto')
root.geometry('400x400') 

f = open("dati.txt", 'w')

dati = ""

for riga in range(100):

    for elemento in range(1):

        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))

    dati = dati + "\n"

f.write(dati)
f.close()

f = open("dati.txt", 'r')

coordX = []
coordY = []

for riga in f:
    valori = str(f.readline())  
    Nval = len(valori)          
    valori = valori.strip('\n') 
    valori = valori.split(',')  
    valori = list(valori)       
    print(valori)
    coordX.append(int(valori[0])) 
    coordY.append(int(valori[1])) 

f.close()

print(dati)

print ("X: ",coordX)
print ("Y: ",coordY)

coordX.sort()
coordY.sort()

print("liste ordinate:") 
print ("X: ",coordX)
print ("Y: ",coordY)

print(type(coordX))
print(type(coordY))

def graph():
    plt.scatter(coordX, coordY)
    plt.show()

c = Button(root,text="premimi per avere il grafico", command=graph)
c.pack()
root.mainloop()