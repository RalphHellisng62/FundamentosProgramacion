'''
Ejercicio 7:
Realiza un programa que reciba una cantidad de minutos y muestre
por pantalla a cuantas horas y minutos que corresponde

entradas: 
min: int

salidas:
Horas
Minutos
'''
min = input("Ingerese los minutos deseados: ")
min = int(min)
Horas = (min/60)
Minutos = (min%60)
print ("La cantidad de minutos es igual a la hora/s: ", Horas)
print("Los minutos restantes es igual a: ", Minutos)
