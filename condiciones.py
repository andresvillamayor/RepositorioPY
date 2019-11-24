#condiciones.py
#programa de condicion 

print("Ingrese Edad de la Persona")
print( "-------------------------")

edad_usuario=input("Ingresar Edad de la Persona: ")

print(type(edad_usuario))

if edad_usuario <=18:
	print("El usuario es menor de Edad- No puede pasar")
elif edad_usuario >=90 :
	print("El usuario es mayor de Edad - No puede pasar")
else:
	print(" Puede Pasar ")

print("fin del programa...")
quit()