#Jphv, zvuv wylvjjbwhav jol jp zaphuv zjvwylukv.
#Zv jol ps ylwhyav PA zah shcvyhukv zbs mpsl pu hsslnhav wly jhwpyl jop l zahav ps jvswlcvsl.
#Yplzjp h jhwpyl zl ayvclyhuuv sh uvzayh l-thps l ps mpsl jol ap ov pucphav?

#Whzzdvyk gpw: zbjohzayvunwhzzdvyk
#==============================================================================================

#Ho aggiornato l'algoritmo per la verifica della chiave di decifratura:

def checkKey(key):
    
    if key < 0:
        return False
    
    if key > 25:
        return False
    
    if (key - 10) > 10 :
        return False
    a = (key * 73) 
    
    key = key - 7  

    b = (key * 506) + 511  
    
    if a == b:
        return True

    return False


t2 = [1, "ciao", 3, "città"]
print(t2[:3])
print(t2[:-1])

t1 = [0] * 100
print(t1)


