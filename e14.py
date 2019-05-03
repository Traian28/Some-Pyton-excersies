def cargar():
	diccionario={}
	continua="s"
	while continua=="s":
		caste=input("Ingrese palabra en casetellano: ")
		ing=input("Ingrese una palabra en ingles: ")
		diccionario[caste]=ing
		continua=input("Quiere cargar otra palabra:[s/n] ")
	return diccionario

def imprimir(diccionario):
	print ("Listado completo del diccionario")
	for i in diccionario:
		print (i, diccionario[i])

def consulta_palabra(diccionario):
	pal=input("Ingrese palabra a buscar: ")
	if pal in diccionario:
		print ("En ingles significa: ", diccionario[pal])
	else:
		print ("No esta en el diccionario")

diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)
