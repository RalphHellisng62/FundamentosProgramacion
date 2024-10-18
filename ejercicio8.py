'''
Ejercicio 8:
Un vendedor recibe un sueldo mas un 10% extra por comision de sus ventas, el vendedor
desea saber cuanto dinero obtendra por concepto de comisiones por las 3 ventas que realiza en el mes 

entradas:
sueldo: int
venta1: int
venta2: int
venta3: int

salidas:
comision 
total
'''
venta1 = input("Ingrese la primera venta: ")
venta1 = int(venta1)
venta2 = input("Ingrese la segunda venta: ")
venta2 = int(venta2)
venta3 = input("Ingrese la tercera venta: ")
venta3 = int(venta3)
sueldo = input("Ingrese el sueldo base del empleado: ")
sueldo = int(sueldo)
comision = (venta1 + venta2 + venta3)*0.10
total = sueldo + comision
print("Las comisiones por ventas fueron: ", comision)
print("el total de ganacia del empleado con sueldo base y las comisiones: ", total)