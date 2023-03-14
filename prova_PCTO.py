#from smtplib import OLDSTYLE_AUTH


eta = 31
città = "roma"
quartiere = "vomero"
contatore = 1



if eta > 2 and quartiere == "mare" or città == "roma":
    print("sei vecchio")
else:
    print("non sei tanto vecchio")

if eta > 30:
    print("sei vecchio")
    dove = input("dove abiti")
    if dove == "napoli":
        print("perfetto")
    else:
        print("non sie buono")
elif eta == 30:
    print("ahahahhaha")
else:
    print("sei giovane")

#while contatore < 11:
 #   print("ciao")
  #  contatore += 1

#numero_segreto = 14
#numero_inserito = int(input("indovina il numeor segreto da 0 a 20: "))
#sbagli = 0
#while numero_inserito != numero_segreto:
 #   print("sbagliato")
  #  sbagli +=1
   # numero_inserito = int(input("riprova: "))
#print("corretto")
#print("hai sbagliato", sbagli, "volte")

#for lettera in "ciao":
 #   print("siamo alla lettera: ", lettera)

#for contatorie in range(1,11):
 #   print(contatorie)

#i = 5
#while i < 5:
#    print(i)
 #   i += 1
#else:
 #   print("numero", i)

#lista_citta = ["Napoli", "Milano", "Bari", "Roma"]
#lista_citta(-1) #roma
#lista_citta(0:2) #range Napoli-Bari
#lista_citta(2:) #range Napoli fino alla fine
#lista_citta(:2) #range dall'inizio fino a Napoli
#utilizzando i due punti non andrà in errore, 
#mentre se si usano i numeri interi e non si trova il valore corrispondente retituirà errore


#print(lista_citta)
#del lista_citta[:] #per eliminare il contenuto di una lista
#print(lista_citta)

#lista_citta.append("Salerno") #se non serve metterlo in una posizione specifica
#lista_citta.insert(2,"Salerno") #se si vuole inserire in una posizione specifica
#print(lista_citta)

#for citta in lista_citta:
    #print("la città è", citta)

#for citta_indice in range (len(lista_citta)):
#    print("Indice corrente", citta_indice, "|città corrente:", lista_citta[citta_indice])

#materie_scuola = ["Matematica", "Italiano", "Scienze", "Storia", "Inglese"]
#for indice_materia in range(len(materie_scuola)):
#    print("L'indice della materia è:", indice_materia, "La materia è:", materie_scuola[indice_materia])

#spese = [1,5,6,8]
#somma = 0
#for spesa in spese:
 #   somma += spesa
#print("Hai speso:", somma)

#citta_1 = "napoli"
#citta_2 = "Roma"

#temp = citta_1
#citta_1 = citta_2
#citta_2 = temp
#print(citta_2, citta_1)

#lista_citta = ["Napoli", "Milano", "Bari", "Roma"]
#print(lista_citta)
#lista_citta[0], lista_citta[1] = lista_citta[1], lista_citta[0]
#print(lista_citta)

#lista_citta.sort() #sort mette le parole in ordine alfabetico ed i numeri in ordine numerico
#lista_citta.sort(reverse = True) #mette le parole in ordine alfabetico al contrario
#print(sorted(lista_citta)) #printa la lista in ordine alfabetico senza salvarla, la printa soltanto

#invitati = ["Marco", "Antonio", "Enrico", "Davide"]
#nome = input("Inserisci il tuo nome: ")
#if nome not in invitati:
 #   print("Va vattem")
#else:
#    print("Benvenuto")

#numeri = [1, 2, 3]
#nuovo_numero = numeri
#numeri[0] = -5
#print(numeri)
#print(nuovo_numero) #così non si crea una nuova lista che si può cambiare


#numeri = [1, 2, 3]
#nuovo_numero = numeri[:1]
#numeri[0] = -5
#print(numeri)
#print(nuovo_numero)

#numeri = []
#for i in range(1,101):
#    numeri.append(i)
#print(numeri)

#numeri2 = [i for i in range(1,101)]
#print(numeri2)

#numeri3 = [i for i in range(1,101) if i % 3 != 0]
#print(numeri3)

#celle = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
#print(celle[0]) # 0 così prende l'intera prima lista
#print(celle[0][0]) #così si prende il primo elemento della prima lista
#for x in celle:
#    for y in x:
#        print("elemento: ", y)
#    print("elemento: ", x)

#lista1 = ["Roma", "Napoli"]
#lista2 = ["Milano", "Bari"]
#lista_somma = lista1 + lista2
#print(lista_somma)

#lista_numeri = [0,1] * 10 #non moltiplica i numeri interni alla lista ma li ripete per 10 volte
#print(lista_numeri)

#testo = "palla bianca"
#testo_maiuscolo = testo.upper()
#print(testo_maiuscolo)

#numero_inserito = input("inserisci un numero ")
#if numero_inserito.isnumeric():
#    print("Grazie")
#else:
#    print("mi dispiace")

# una lista può essere modificata, invece una tupla una volta creata non rimane quella. 
# Non si può aggiungere né levare niente né si possono scambiare i dati all'interno

#dati_utente = ("Antonio", "Esposito", 1992) + ("perditempo") # questo non funzionerebbe
#dati = [dati_utente, "perditempo"]

#capitali = [("Londra", "Uk", 8.98), ("Roma", "IT", 1.0)]
#for capitale in capitali:
#    print("Città: ", capitale[0], ", Paese: ", capitale[1], ", Popolazione: ", capitale[2])

#emails = {
#    "Antonio": "antonio@gmail.com",
#    "Marco": "marco@gmail.com"
#}
#print(emails)

#voti = {}
#voti["Antonio"] = "5--"
#voti["Giovanni"] = "2-"
#print(voti)
#voti.update({"Giovanni": "2--"})
#print(voti)
#print(len(voti))

#print("ciao") #funzione
#input("inserisci ") #funzione

#def bene():
#    print("ciao")

#print(bene())


def fai_la_media(numeri_inseriti):
    somma = 0.0
    for numero in numeri_inseriti:
        somma += numero
    media = somma / len(numeri_inseriti)
    print(media)

numeri_inseriti = [3,4,5,6,2,3,5,7,8,9,10,0]
#fai_la_media([5.0,4.0])

def conta_lettere(testo,lettera):
    contatore = 0
    for carattere in testo:
        if carattere == lettera:
            contatore += 1
    print("La", lettera, "è inclusa", contatore, "volte")

#parola = (input("inserisci la parola: "))
#let = (input("inserisci la lettera: "))
#print(conta_lettere(parola, let))

def mostra_verita():
    mistero = "no"
    print(mistero)

mistero = "risolto"
#print(mistero)
#mostra_verita()
#print(mistero)


def mostra_verita():
    global mistero
    mistero.append = ("no")
    print(mistero)

mistero = "risolto"
#print(mistero)
#mostra_verita()
#print(mistero)

#ciao = print("ciao")
#print(ciao) #restituisce none perché il secondo print non ha niente al suo interno
#x = None

def fai_la_media(numeri_inseriti):
    somma = 0.0
    for numero in numeri_inseriti:
        somma += numero
    media = somma / len(numeri_inseriti)
    return(media)

numeri_inseriti = [3,4,5,6,2,3,5,7,8,9,10,0]
#lamedia = fai_la_media([5.0,4.0,5.0,7.0,9.0,1.0])
#print(lamedia * 2)

#def uguaglianza(numeri):
 #   if (numeri[0] == numeri[1]):
#        return True
 #   else:
  #      return False

#print(uguaglianza(4))

def pari_dispari(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#print(pari_dispari(4))

#3! = 1*2*3 =
#6! = 1*2*3*4*5*6 =
#7! = 6! * 7 =

def fattoriale(numero):
    fattoriale = 1
    for x in range(1, numero +1):
        fattoriale *= x
    return fattoriale

#print(fattoriale(6))

def fattoriale_ricorsivo(numero):
    if numero <=1:
        return 1
    return numero*fattoriale_ricorsivo(numero-1)

#print(fattoriale_ricorsivo(6))


def numero():
    for i in range(1,4):
        yield i

#print(numero())
#generatore = numero()
#print(next(generatore))
#print(next(generatore))
#print(next(generatore))

#import redis
from random import *

#r = redis.StrictRedis(host='localhost', port=6379, db=0)

# inizializzo la lista delle chiavi del DB
#r.keys()

# r.set('chiave, "valore')

#r.set('mario', 'ilSuoValore')
#value = r.get('mario') 
#print(value)

#a = 5
#b = a<<2
#print(b)



def func(num):
    if num % 2 == 0:
        return True
    else:
        return False

#print(not func(2))

#a = 1, 5, "palla"
#print(list(a))

#def mano(a, b, c):
    return(a*b*c)
#print(mano(c=2, a=3, 6))

#mylist = [1, 2, 3]
#mylist.insert(1,4)
#mylist.append(5)
#print(mylist)

#name= input()
#print(name =="palla")

#m = p = c = "ciao"
#print(p)
#for i in range (1, 16, 2):
    #print(i, end = ",")

#var = 1
#while var < 10:
 #   print("#")
   # print(var)
    #var = var << 1

#l = 12 & 4
#print(l)


#f = 0
#while f <= 3:
 #   f += 2
  #  print("*")

#for h in range(1):
    #print("*")
#else:
    #print("*")

#dictionary = {"gatto": "cane", "palla": "gioco", "palo" : "luce"}
#v=dictionary["gatto"]
#for k in range(len(dictionary)):
#    v = dictionary[v]

#rint(v)



