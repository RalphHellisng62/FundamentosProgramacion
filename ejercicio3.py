'''
Ejercicio 3:
Escribir un programa dado los catetos de un triangulo, rectangulo, calcular su hipotenusa

entradas:
cat1: int
cat2: int

salidas:
hipo
'''
import math 
cat1 = input("escribe el cateto 1 ") 
cat1 = int (cat1)
cat2 = input("escribe el cateto 2 ")
cat2 = int (cat2)
hipo = (cat1 * cat1) + (cat2 * cat2)
print ("la hipotenusa es igual a: ", hipo)