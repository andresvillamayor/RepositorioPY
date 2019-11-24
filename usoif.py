#comparaciones if 

#uso del condicional if 


print ("Programa de evaluacion de Notas de Alumnos")
print ("------------------------------------------")
nota_alumno=input("Ingresar la nota del Alumno: ")



def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"

	return valoracion


print(evaluacion(int(nota_alumno)))





