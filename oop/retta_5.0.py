class retta:
    
    def __init__(self, p1 = None, p2 = None, p3 = None, p4 = None,):

        self.__a = p1
        self.__b = p2
        self.__c = p3
        self.__punti = []

    def implicita(self):
        if self.__b == 0:
            return f"\n{self.__a}x + {self.__c} = 0"
        elif self.__a == 0:
            return f"\n{self.__b}y + {self.__c} = 0"
        elif self.__c == 0:
            return f"\n{self.__a}x + {self.__b}y = 0"
        else:
            return f"\n{self.__a}x + {self.__b}y + {self.__c} = 0"

    def esplicita(self):
        if self.__b == 0:
            return f"\nl'equazione non può essere scritta in forma esplicita"
        elif self.__c == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {(-(self.__a ) / (self.__b))}x"
        else:
            return f"\nl'equazione in forma esplicita è: \n y = {(-(self.__a ) / (self.__b))}x + {-(self.__c)}"
    
    def getA(self):
        return f"\n a = {self.__a}"
    
    def getB(self):
        return f"\n b = {self.__b}"

    def getC(self):
        return f"\n c = {self.__c}"

    def coefficiente_angolare(self):
        if self.__b == 0:
            return f"\nLa retta è parallela all'asse delle Y \nIl coefficiente angolare è nullo"
        else:
            return f"\nil coefficiente angolare dell'equazione è {-self.__a / self.__b}"
        
    def punti(self, N, M):
        self.__N = N
        self.__M = M
    
        for self.__N in range (self.__M):
            self.__punti = (x, (-self.__a * x) / self.__b + (-self.__c / self.__b))
            x = x + 1
            self.punti.append(self.__punti)
        return f"\n Le coordinate dei punti appartenenti alla retta sono: \n {self.punti}"

valori_a_b_c = retta(input("inresisci il tipo dell'equazione: "), input("inresisci il valore di a: "), input("inresisci il valore di b: "), input("inresisci il valore di c: "))

print(valori_a_b_c.implicita())
print(valori_a_b_c.esplicita())
print(valori_a_b_c.coefficiente_angolare())
print(valori_a_b_c.punti())