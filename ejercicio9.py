'''
Ejercicio 9:
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar por su compra con descuento
 entradas:
 compra: int

 salidas: 
 precioFinal

'''
compra = input("Ingrese el precio del producto: ")
compra = int(compra)
descuento = (compra*0.15)
precioFinal = (compra - descuento)
print("el total de la compra mas el descuento fue de: ", precioFinal)