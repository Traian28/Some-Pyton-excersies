print ("daos de la primera persona: ")


#Estas son variables
nombre1= input("ingrese nombre del producto: ")
precio1=int(input("Ingrese un precio: "))
nombre2=input("Ingrese nombre del producto: ")
precio2=int(input("Ingrese un precio: "))

#esto es una constante
BONIFICACION=20 

precio_compra_total = precio1+precio2

#comparar
comparar=precio1>=precio2
logico= (precio1 < precio2 and precio1 == precio2)

cabecera="resultados del producto {0}. y del producto {1}.: "

print (cabecera.format(nombre1,nombre2)) #conctenas las cadenas de texto cabecera
print ("El precio del primer valor es mayor o igual a el precio del segundo valor:")
print (comparar) 

print ("La suma de los dos productos es: " + str(precio_compra_total))
print (str(nombre1) + " < " + str(nombre2) + " and " + str(precio1) + " == " + str(precio2))
print (logico)

precio_compra_total += BONIFICACION
print ("Al precio total le incrementamos su valor que tiene la constante:" + str (precio_compra_total))

