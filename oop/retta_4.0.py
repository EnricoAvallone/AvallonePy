#equazioni implicite ed esplicite
class retta:
    
    def __init__(self,__a, __b, __c, __x):

        self.a = int(__a)
        self.b = int(__b)
        self.c = int(__c)
        self.x = int(__x)
    
    def implicita(self):
        if self.b == 0:
            return f"\nl'equazione è impossibile"
        elif self.a == 0:
            return f"\nl'equazione è impossibile"
        elif self.c == 0:
            return f"\nl'equazione in forma esplicita è: \n {self.a}x + {self.b}y = 0"
        else:
            return f"\nl'equazione in forma implicita è: \n {self.a}x + {self.b}y + {self.c} = 0 "

    def esplicita(self):
        if self.b == 0:
            return f"\nl'equazione è impossibile"
        elif self.a == 0:
            return f"\nl'equazione è impossibile"
        elif self.c == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {(-(self.a ) / (self.b))}x"
        else:
            return f"\nl'equazione in forma esplicita è: \n y = {(-(self.a ) / (self.b))}x  + {-(self.c)}"
    
    def valore_y(self):
        y = (-self.a * self.x) / self.b + (-self.c / self.b)
        return f"\n y = {(-self.a * self.x) / self.b + (-self.c / self.b)}"

    #def punti_retta(self):
        
        #tuple = []
        
        for i in range(600):
            y = (-(self.a ) / (self.b))*(self.x)  + (-(self.c)/(self.b))
            
        return f""

    #def punti(self, int(N, M, x):
        self.__N = N
        self.__M = M
    
        for self.__N in range (self.__M):
            tupla = (x, (-self.a * x) / self.b + (-self.c / self.b))
            x = x + 1
            self.punti.append(tupla)
        return f"\n Le coordinate dei punti appartenenti alla retta sono: \n {self.punti}"   

    def coefficiente_angolare(self):
        if self.b == 0:
            coef_ang = "null"
            return f'\n {coef_ang}'
        else:
            coef_ang = -self.a / self.b
            return f"\n il coefficiente angolare dell'equazione è {coef_ang}"
        
            


valori_a_b_c = retta(input("inresisci il valore di a: "), input("inresisci il valore di b: "), input("inresisci il valore di c: "), input("inresisci il valore di x: "))

print(valori_a_b_c.implicita())
print(valori_a_b_c.esplicita())
print(valori_a_b_c.coefficiente_angolare())
print(valori_a_b_c.valore_y())
print(valori_a_b_c.punti((0, -300, 300))
#print(valori_a_b_c.punti_retta())