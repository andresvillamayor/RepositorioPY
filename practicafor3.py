
#Agregar un input el codigo de correo 
#enviar el correo a una funcion 
#detnro de la funcion colocar la condicion del for 
#retornar si  es valido o no el correo 

#funcion validar
def f_validar(valido):
	if (valido== True):
		f_imprimir("Correo Valido")
	else:
		f_imprimir("Correo Invalido")

	

#funcion de imprimir 
def f_imprimir(cadena): 
	print (cadena)

	

try:
	email= str(input("ingresa correo electronico :"))
except ValueError:
	print("Error, intente nuevamente")


#email="pepe@gmail.com"
print(email)
valido=False
for i in email:
	if (i=="@"):
		valido=True
	


f_validar(valido)


       

