
def cargar_paisespoblacion():
	paises=[]
	for x in range(5):
		nom=input("Ingresar nombre de pais: ")
		cant=int(input("Ingrese cantidad de habitantes: "))
		paises.append((nom,cant))
	return paises

def imprimir(paises):
	print ("Paises y su poblacion: ")
	for x in range (len(paises)):
		print (paises[x][0],paises[x][1])

def pais_maspoblacion(paises):
	may=0
	for x in range(1,len(paises)):
		if paises[x][1]>paises[may][1] :
			may=x
	print ("Pais con mayor poblacion: ", paises[may][0])

paises=cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises)
