from random import randint as rd
cinq1=["il giallo grano","la fitta pioggia","arcobaleno2","arcobaleno3"]
sett=["tempesta di estate","straripano le sponde","arcobaleno3","arcobaleno2"]
cinq2=["nel campo muore","arcobaleno","arcobaleno2","arcobaleno3"]
for i in range(1):
    str1= cinq1[rd(0,3)]
    str2= sett[rd(0,3)]
    str3= cinq2[rd(0,3)]
print(str1)
print(str2)
print(str3)