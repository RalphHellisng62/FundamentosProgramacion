import math 
cat1 = input("escribe el cateto 1 ") 
cat1 = int (cat1)
cat2 = int(input("escribe el cateto 2 "))
hipo = cat1 * cat1 + cat2 * cat2
hipo = hipo ** (1/2)
print("la hpotenusa es hipo:" , hipo)
