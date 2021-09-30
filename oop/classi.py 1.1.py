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
        return f'\nSheda squadriglia: {self1.squadriglia}\n Acetta: {self1.accetta}\n Teloni: {self1.teloni}\n torcia di sq: {self1.torcia_sq}\n cordini: {self1.cordini}\n giornali: {self1.giornali}\n accendini: {self1.accendini}\n sacchi spazzatura: {self1.sacchi_spazzatura}'

Aquile = magazzino("Aquile", 24, 7, 1, 12)
Delfini = magazzino("Delfini", 30, 10, 2, 15)
Falchi = magazzino("Falchi", 27, 13, 3, 13)
Lupi = magazzino("Lupi", 19, 4, 0, 3)

print(Aquile.scheda())
print(Delfini.scheda())
print(Falchi.scheda())
print(Lupi.scheda())
print("\nSquadriglie totali: ",magazzino.num_squadriglie)