'''
Ejercicio 6:
Hacer un programa que calcule la media de 3 numeros pedidos por teclado

entradas:
num1: int
num2: int
num3: int

salidas: 
media
'''

num1 = input("ingrese el primer numero: ")
num1= int(num1)
num2 = input("el segundo numero: ")
num2= int(num2)
num3 = input("el tercer numero: ") 
num3= int(num3)
media = (num1+num2+num3)/3
print ("la media de los 3 numeros es igual a: ", media)