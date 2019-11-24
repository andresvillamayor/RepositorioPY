#condicional 


sueldo_gerenteg=int(input("Ingresar Sueldo del Gerente General:"))

sueldo_gerente=int(input("Ingresar Sueldo del Gerente :"))

sueldo_contador=int(input("Ingresar Sueldo del Contador :"))

sueldo_auxiliar=int(input("Ingresar Sueldo del Contable")) 


print ("Presidente :" + str(sueldo_gerenteg))
print ("Gerente :" + str(sueldo_gerente))
print ("Contador :" + str(sueldo_contador))
print ("Auxiliar :" + str(sueldo_auxiliar))



if sueldo_auxiliar<sueldo_contador<sueldo_gerente<sueldo_gerenteg:
	print("Todo anda Bien ")
else:
	print("Algo Anda Mal ")



