'''
Ejercicio 12:
Pide al usuario dos pares de numeros x1, y1 -  x2,y2 que representan dos puntos en el plano. Calcula la distancia y muestra
la distancia entre ellos

entradas:
x1:int
y1:int
x2:int
y2:int

salidas:
distancia

'''
import math

#Pide los puntos al usuario

x1= float(input("ingrese la coordenada x del primer punto: "))
y1= float(input("ingrese la coordenada y del primer punto: "))
x2= float(input("ingrese la coordenada x del segundo punto: "))
y2= float(input("ingrese la coordenada y del segundo punto: "))

distancia= math.sqrt ((x2-x1)**2 + (y2-y1)**2)
print("La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: ", distancia)