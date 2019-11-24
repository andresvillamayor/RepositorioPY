#condicionin

print("Asignaturas")
print("Informatica - Test - Desarrollo")

curso=str(input("Ingresar la Asignatura :"))

if curso in ("Informatica", "Test", "Desarrollo"):
	print ("Asignatura elegida" + curso)
else:
	print ("Asignatura no existe ")