'''
Ejercicio 11:
Pide al usuario 2 numeros y muestra la distancia entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)

entradas:
num1: int
num2: int

salidas:
distancia 

'''
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
distancia= (num1-num2)
distancia= abs (num1-num2)
print("La distancia de los dos numeros es: ", distancia)