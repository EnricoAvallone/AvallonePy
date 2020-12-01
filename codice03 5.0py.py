stringa = input("qual è la parola di cui vuoi sapere le lettere? = ")
stringa1 = list(stringa)
print(stringa1)
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z')

lista = {}
for alphabet in stringa1:
    if stringa1.count(alphabet) > 0:
        lista[alphabet]= stringa1.count(alphabet)
print("le lettere della tua parola sono:", lista)