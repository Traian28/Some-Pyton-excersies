
x=1
suma=0

while x<=10:
	valor=int(input("Ingrese un valor: "))
	suma +=valor
	x +=1

gpa= suma/10

print ("La suma de los 10 valores es: " + str(suma))

print ("El promedio es: " + str(gpa))


print()
print ("**********Another example************")

cantidad=0
x=1
n=int(input("Load total stock: "))

while x<=n :
	largo=float(input("Insert total length of the piece: "))
	if largo>= 1.2 and largo<= 1.3 :
		cantidad += 1
	x += 1

print ("Total OK pieces are: " + str(cantidad))




