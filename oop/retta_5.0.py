class retta:
    
    def __init__(self, p1 = None, p2 = None, p3 = None):

        self.__a = float(p1)
        self.__b = float(p2)
        self.__c = float(p3)
        self.__punti = []

    def implicita(self):
        if self.__b == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__c} = 0"
        elif self.__a == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__b}y + {self.__c} = 0"
        elif self.__c == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__b}y = 0"
        else:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__b}y + {self.__c} = 0"

    def esplicita(self):
        if self.__b == 0:
            return f"\nl'equazione non può essere scritta in forma esplicita"
        elif self.__a == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {-self.__c  / self.__b}x"
        elif self.__c == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {-self.__a  / self.__b}x" 
        else:
            return f"\nl'equazione in forma esplicita è: \n y = {-self.__a  / self.__b}x + {-self.__c / self.__b}"
    
    def getA(self):
        return f"\n a = {self.__a}"
    
    def getB(self):
        return f"\n b = {self.__b}"

    def getC(self):
        return f"\n c = {self.__c}"

    def coefficiente_angolare(self):
        if self.__b == 0:
            return f"\nla retta è parallela all'asse delle Y \nil coefficiente angolare è non definito"
        else:
            return f"\nil coefficiente angolare dell'equazione è {-self.__a / self.__b}"

    def y(self, x):
        self.__x = float(x)
        if self.__b == 0:
            return f"\nla retta è parallela all'asse delle Y"
        elif self.__a == 0:
            return f" y = {-self.__c / self.__b}"
        elif self.__c == 0:
            return f" y = {-self.__a * self.__x / self.__b}" 
        else:
            return f" y = {-self.__a * self.__x / self.__b + (-self.__c / self.__b)}"
        
    def punti(self, n, m):
        self.__n = int(n)
        self.__m = int(m)
        if self.__b == 0:
            return f"\nnull"
        elif self.__a == 0:
            return f"\nnull"
        else:
            for self.__n in range (self.__m):
                tupla = (self.__x, (-self.__a * self.__x) / self.__b + (-self.__c / self.__b))
                self.__x = self.__x + 1
                self.__punti.append(tupla)
            return f"\ni punti che appartengono alla retta sono: \n {self.__punti}"




valori_a_b_c = retta(input("inresisci il valore di a: "), input("inresisci il valore di b: "), input("inresisci il valore di c: "))

print(valori_a_b_c.implicita())
print(valori_a_b_c.esplicita())
print(valori_a_b_c.coefficiente_angolare())
print(valori_a_b_c.y(input("\ninserisci il valore della x = ")))
print(valori_a_b_c.punti(input('\ninizio range = ') , input('fine range = ')))