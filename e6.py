
nota1=int(input("Insert first note: "))
nota2=int(input("Insert second note:"))
nota3=int(input("Insert third note:"))

gpa=(nota1+nota2+nota3) / 3

if gpa >= 7 :
	print ("Promoted")
else :
	if gpa >= 4:
		print ("Regular")
	else :
		print ("Fail")