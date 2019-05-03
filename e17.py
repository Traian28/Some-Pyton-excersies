def proceso(cadena):
	indice=-1
	iguales=0
	for x in range(len(cadena)//2):
		if cadena[x]==cadena[indice]:
			iguales+=1
		indice-=1
	print(cadena)
	if iguales==(len(cadena)//2):
		print("Es capicua")
	else:
		print("No es capicua")


proceso(cadena=input("Ingrese cadena para verificar si es capicua: "))