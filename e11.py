
def sumarDeValores(lista):
	suma=0
	for x in range(len(lista)):
		suma += lista[x]
	return suma

def valorMayor(lista):
	may=lista[0]
	for x in range(1,len(lista)):
		if lista[x]>may:
			may=lista[x]
	return may

def valorMenor(lista):
	men=lista[0]
	for x in range(1,len(lista)):
		if lista[x]<men:
			men=lista[x]
	return men

datos=[5454, 43430, 3222, 12222, 666,65656, 545, 2333, 21212, 23, 6565]

print("Total de datos", datos)

print("El total de sumar los valores del array es: ", sumarDeValores(datos))
print("Valor mayor del array", valorMayor(datos))
print("Valor menor del array", valorMenor(datos))