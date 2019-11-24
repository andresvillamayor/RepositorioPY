#python
#andy
# funciones por referencia

def imprimir(impresion):
     print(impresion)

def calular(valor1,valor2):
    if valor1>valor2:
        a= "valor1 es mayor"
        imprimir(a)
    else:
        b= "valor2 es mayor"
        imprimir(b)
valora = input ("Ingresar valor 1 :")
valorb = input ("Ingresar valor 2 : ")

calular(valora,valorb)
