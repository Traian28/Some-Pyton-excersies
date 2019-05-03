import random

def cargar():
	lista=[]
	for i in range(10):
		lista.append(random.randint(0,1000))
	return lista

def imprimir(lista):
	print(lista)

def mezclar(lista):
	random.shuffle(lista)


lista=cargar()
print("Se genero la lista automaticamente")
imprimir(lista)
print ("La nueva lista mezclada es")
mezclar(lista)
imprimir(lista)