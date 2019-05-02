
def sumarizar (lista):
	suma=0
	for x in range (len(lista)):
		suma += lista[x]
	return suma

def mayor (lista):
	may=lista[0]
	for x in range(len(lista)):
		if lista[x]>may:
			may=lista[x]
	return may

def menor (lista):
	men=lista[0]
	for x in range(len(lista)):
		if lista[x]<men:
			men=lista[x]
	return men

listavalores=[10,56,23,34,190,298]
print("Lista completa: ")
print (listavalores)
print("Suma de los elmentos: ", sumarizar(listavalores))
print("El mayor numero: ", mayor(listavalores))
print("El menor numero: ", menor(listavalores))

print("++++++++++++++++++++ Another example +++++++++++++++++++++++++")
print()
print()

def cargar_lista():
	li=[]
	for x in range(5):
		valor= int(input("Introduce un valor: "))
		li.append(valor)
	return li

def imprimir_mayor (li):
	print ("Valores de la lista mayores a 10: ")
	for x in range(len(li)):
		if li[x]>10:
			print (li[x])


lista=cargar_lista()
imprimir_mayor(lista)

