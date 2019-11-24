#python
# Archivo
#archivo_texto=open("datos.txt","w")
#frase= "buenas tardes \n buenas noches"
#archivo_texto.write(frase)
#archivo_texto.close()

#archivo_texto=open("datos.txt","a")
#frase2= "\n good \n bad"
#archivo_texto.write(frase2)
#archivo_texto.close()

archivo_texto=open("datos.txt","r")
lectura=archivo_texto.readline()
archivo_texto.close()
print(lectura)
