import tkinter as tk
import csv
from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from guizero import App, PushButton, Text
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from PIL import Image, ImageTk
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg


def getGraphRoot():

    rispostagrafico = richiesta_grafico.get()
    
    width = 500
    height = 350

    load = Image.open(rispostagrafico)
    load = load.resize((width,height), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    
    img = Label(image=render)
    img.image = render
    
    
    
    riquadro.create_window(450, 400, window=img)    
    root.mainloop()
        



def genera_grafico():
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

    plt.scatter(coordX, coordY)
    plt.show()

root = Tk()
riquadro = tk.Canvas(root, width = 900, height = 600)
riquadro.pack()

richiesta_grafico = Entry(root)
riquadro.create_window(450, 140, window=richiesta_grafico)

scritta=Label(root, text="inserisci la directory del file")
riquadro.create_window(450,110, window=scritta)

#Bottoni
button1 = Button( text="clicca qui per generare un grafico", command=genera_grafico)
riquadro.create_window(200, 140, window=button1)
button2 = Button( text="Clicca qui per chiudere la scheda", command=riquadro.destroy)
riquadro.create_window(400, 140, window=button2)
button3 = tk.Button(root, text="clicca per confermare", command=getGraphRoot)
riquadro.create_window(450, 180, window=button3)


riquadro.create_window(200, 140, window=richiesta_grafico)

button1.pack()
button2.pack()
root.mainloop()