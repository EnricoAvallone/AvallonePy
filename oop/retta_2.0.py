class retta:

    x = 0
    y = 0
    
    def __init__(self,a, b, c):

        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    
    def implicita(self):
        return f"\nl'equazione in forma implicita è: \n {self.a}x + {self.b}y + {self.c} = 0 "

    def esplicita(self):
        return f"\nl'equazione in forma esplicita è: \n {self.b}y = {-(self.a)}x + {-(self.c)}"
    
    def punti_retta(self):
        print("\n---------------------------------------\nle coordinate dei punti della retta sono: ")
        for i in range(10):
            retta.x +=1
            retta.y +=1
            
            print(f'\n x= {(- self.b * retta.y - self.c) / self.a} \n y = {(-self.a * retta.x - self.c) / self.b}')
        
    
valori_a_b_c = retta(input("inresisci il valore di a: "), input("inresisci il valore di b: "), input("inresisci il valore di c: "))

print(retta.implicita(valori_a_b_c))
print(retta.esplicita(valori_a_b_c))
print(retta.punti_retta(valori_a_b_c))