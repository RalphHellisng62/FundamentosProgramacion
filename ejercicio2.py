'''
Ejercicio 2:
Escribir un programa que calcule el perimetro y area de un rectangulo dada su base y su altura

'''
base = input("ingresa la base: ")
base = int(base)
alt = input("altura: ")
alt = int(alt)
area = base * alt
peri = (base + alt)*2

print ("el area del rectangulo es: ", area)
print ("el perimetro del rectangulo es", peri)
