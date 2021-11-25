class parabola:
    def __init__(self, p1 = None, p2 = None, p3 = None):
        
        self.__a = float(p1)
        self.__b = float(p2)
        self.__c = float(p3)
    
    def esplicita(self):
        if self.__b == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {self.__a}x^2 + {self.__c}"
        elif self.__c == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {self.__a}x^2 + {self.__b}x "
        else:
            return f"\nl'equazione in forma esplicita è: \n y = {self.__a}x^2 + {self.__b}x + {self.__c}"

    def cordinateV(self):
        Xv = 0
        Yv = 0
        if self.__b == 0:
            Xv = 0
        else:
            Xv = - (self.__b) / self.__a*2
        Yv = (self.__b * self.__b - 4 * self.__c * self.__a) / (4 * self.__a)
        return f"\nle cordinate del vertice sono V =({Xv};{Yv})"
    
    def cordinateF(self):
        Xf = 0
        Yf = 0
        if self.__b == 0:
            Xf = 0
        else:
            Xf = - (self.__b) / self.__a*2
        Yf = (1 - (self.__b * self.__b - 4 * self.__c * self.__a)) / (4 * self.__a)
        return f"\nle cordinate del fuoco sono F =({Xf};{Yf})"
    
    def eqdirettrice(self):
        return f"\nl'equazione della direttrice è: y = {- (1 + (self.__b * self.__b - 4 * self.__c * self.__a)) / (4 * self.__a)}"

valori_a_b_c = parabola(input("\ninresisci il valore di a: "), input("inresisci il valore di b: "), input("inresisci il valore di c: "))

print(valori_a_b_c.esplicita())
print(valori_a_b_c.cordinateV())
print(valori_a_b_c.cordinateF())
print(valori_a_b_c.eqdirettrice())