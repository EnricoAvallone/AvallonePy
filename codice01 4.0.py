#python3
a = int(input("qual'è il valore di a?= "))
b = int(input("qual'è il valore di b?= "))
x = (-b/a)
print("il valore di x è",x)

if a>b:
    if a>x:
        max = a
    else:
        max = x 
else:
    if b>x:
        max = b
    else:
        max = x
print("tra",a,",",b,"e",x,"il maggiore è",max)