#condiciones2.py

print("Calificaciones del alumno :")
print("---------------------------")


nota_alumno= int(input("Ingrese la Nota del Alumno"))

if nota_alumno <2:
	print("Aplazado")
elif nota_alumno <3:
	print("BIEN")
elif nota_alumno< 4:
	print("MUY BIEN")
else:
	print("EXCELENTE")


print("Fin del Programa....")
quit()

