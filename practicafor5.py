i=1
while i<=10:
    print("Valor de i =" + str(i))
    i=i+1

print("Fin del While")


edad= int(input("ingresar la edad del aspirante"))

while edad<=18 and edad<=25:
    print ("Error en el ingreso de la Edad, intentelo nuevamente")
    edad= int(input("ingresar la edad del aspirante"))


print("Gracias - El Aspirante tiene la Edad " + str(edad))
