from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt
import csv
from random import randint
import tkinter as tk

def genera_grafico():
    #root = Tk()
    #riquadro1 = tk.Canvas(root, width = 400, height = 400)
    #riquadro1.pack()
    #root.title('Generatore di grafici')
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
    #def graph():
    plt.scatter(coordX, coordY)
    plt.show()
    #c = Button(root,text="premimi per avere il grafico", command=graph)
    #riquadro1.create_window(200, 180, window = c)
    #riquadro1.mainloop()

def getGraphRoot():
    graph = Tk()
    riquadro = tk.Canvas(graph, width = 300, height = 300)
    riquadro.pack()

    richiesta_grafico = Entry(graph)
    riquadro.create_window(200, 140, window=richiesta_grafico)

    scritta=Label(graph, text="inserisci il nome del file")
    riquadro.create_window(200,110, window=scritta)

interfaccia = Tk()
interfaccia1 = tk.Canvas(interfaccia, width = 400, height = 400)
interfaccia1.pack()
button1 = Button( text="clicca qui per generare un grafico", command=genera_grafico)
#button1.grid(row=20, column=15)
button2 = Button( text="Clicca qui per chiudere la scheda", command=interfaccia.destroy)
#button2.grid(row=25, column=20)
richiesta_grafico = Entry(interfaccia)
interfaccia1.create_window(200, 140, window=richiesta_grafico)
scritta=Label(interfaccia, text="inserisci il nome del file")
interfaccia1.create_window(200,110, window=scritta)

button1.pack()
button2.pack()
interfaccia1.mainloop()