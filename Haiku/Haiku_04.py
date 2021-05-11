from random import randint as rd
import os
import csv

os.chdir(r"C:\Users\enric\OneDrive\Desktop\Progetti di Python\Haiku") 

f = open("cinq1.txt")
line = csv.reader(f)
v1 = [row for row in line]

g = open("sette.txt")
line = csv.reader(g)
v2 = [row for row in line]

h = open("cinq2.txt")
line = csv.reader(h)
v3 = [row for row in line]

verso1 = v1[rd(0,5)]
verso2 = v2[rd(0,5)]
verso3 = v3[rd(0,7)]

print(verso1)
print(verso2)
print(verso3)