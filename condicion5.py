#condicion5

#Distancia de la Escuela 
print("Programa de Becas 2019")
print("----------------------")
distancia_escuela= int(input("Ingrese la distancia a la Escuela en KM:"))
print("Distancia de la escuela :" + str(distancia_escuela) + " KM")

#numeros de hermanos 

numero_hermanos=int(input("Intruduce el numero de hermanos :"))
print("El numero de hermanos es" + str(numero_hermanos))

salario_familiar = int(input("Ingresa el Monto Salarial Anual :"))
print("El monto salarial Bruto familiar es :" + str(salario_familiar))

#if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tiene derecho a beca")
else:
	print("No tiene derecho a Beca")



