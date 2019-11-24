#for 

mail=False
mimail=input("Ingresar Correo Electronico: ")

for i in mimail:
	if(i=="@" or i=="."):
		mail=True




if mail==True:
	print("Correo Valido")
else:
	print("Correo Invalido")