'''
Ejercicio 10:
Un alumno desea saber cual sera su calificacion final en la materia de algoritmos dicha calificacion compone de las siguientes componentes:
55% promedio de las 3 calificaciones
30% calificacion del examen final
15% calificacion del trabajo final
entradas:
califparciales
cal1: int
cal2: int
cal3: int

salidas:
promedio
calfinal

'''
print("Calificaciones de los parciales ")
cal1= input("ingrese la primera calificacion: ")
cal1 = int(cal1)
cal2= input("Ingrese la segunda calificacion: ")
cal2 = int(cal2)
cal3= input("ingrese la tercera calificacion: ")
cal3= int(cal3)
promedio= (cal1+cal2+cal3)/3
examen= float(input("Calificacion del examnen: "))
trabajo= float(input("Calificacion del trabajo final: "))
calificacionFinal= (promedio*0.55) + (0.30*examen) + (0.15*trabajo)
print("El promedio de los 3 parciales es: ", promedio)
print("La calificacion final es: ", calificacionFinal)

