# introducir nombre del archivo a generar
# Andy
# Generar un archivo
try:
    prompt = 'Desea Crear un Archivo ? :'
    vArchivo = input (prompt)
    #print (vArchivo)
    if (vArchivo) == 'S':
        prompt1 = 'Favor Ingresar el nombre del archivo : '
        vArchivonombre = input (prompt1)
        print (" El nombre del archivo es : " + " " + vArchivonombre)
        prompt2 = 'Esta seguro de crear con ese nombre, Favor ingrese  S = Si  o  N = No '
        vasegurar = input(prompt2)
        if (vasegurar) == 'S':
            #try:
            #    import cPickle as pickle
            #except importError:
            #    import pickle

             fichero = open( vArchivonombre + "." + "txt", "w")
             #nombres = ["Jose","Juan","Pedro"]
             #edades =  [40,30,20]
             #pickle.dump (nombres,fichero)
             #pickle.dump (edades,fichero)
             print (fichero)
             fichero.write("Hola Mundo")
             fichero.close()
            #print ("Se ha creado el Archivo correctamente")
        else:
            print ("No se creo el Archivo - Salir del programa")
            quit()

    else:
       print('Salir')
       quit()

except Exception as e:
    raise
