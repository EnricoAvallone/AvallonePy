class magazzino:

    accetta = 1
    teloni = 4
    torcia_sq = 1
    num_squadriglie = 0

    def __init__(self1,squadriglia, cordini, giornali, accendini, sacchi_spazzatura):

        self1.squadriglia = squadriglia
        self1.cordini = cordini
        self1.giornali = giornali
        self1.accendini = accendini
        self1.sacchi_spazzatura = sacchi_spazzatura
        magazzino.num_squadriglie += 1 
    
    def scheda(self1):
        return f'\nMagazzino squadriglia {self1.squadriglia}:\n Acetta: {self1.accetta}\n Teloni: {self1.teloni}\n torcia di sq: {self1.torcia_sq}\n cordini: {self1.cordini}\n giornali: {self1.giornali}\n accendini: {self1.accendini}\n sacchi spazzatura: {self1.sacchi_spazzatura}'

        

Aquile = magazzino(input("inserisci il nome della squadriglia:"),input("inserisci il numero di cordini:"),input("inserisci il numero di giornali:"),input("inserisci il numero di accendini:"),input("inserisci numero di sacchi della spazzatura:"))
print("passiamo alla prossima squadriglia")
Delfini = magazzino(input("inserisci il nome della squadriglia:"),input("inserisci il numero di cordini:"),input("inserisci il numero di giornali:"),input("inserisci il numero di accendini:"),input("inserisci numero di sacchi della spazzatura:"))
print("passiamo alla prossima squadriglia")
Falchi = magazzino(input("inserisci il nome della squadriglia:"),input("inserisci il numero di cordini:"),input("inserisci il numero di giornali:"),input("inserisci il numero di accendini:"),input("inserisci numero di sacchi della spazzatura:"))
print("passiamo alla prossima squadriglia")
Lupi = magazzino(input("inserisci il nome della squadriglia:"),input("inserisci il numero di cordini:"),input("inserisci il numero di giornali:"),input("inserisci il numero di accendini:"),input("inserisci numero di sacchi della spazzatura:"))

print(Aquile.scheda())
print(Delfini.scheda())
print(Falchi.scheda())
print(Lupi.scheda())
print("\nSquadriglie totali: ",magazzino.num_squadriglie)