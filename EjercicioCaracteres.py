print("EJERCICIO DE DETECCION DE CANTIDAD DE CARACTERES EN UN STRING")
print("**************************************")
repetir = True
while repetir:
    texto = input("Ingrese un texto: ")
    if not texto.isalpha():
        print("Ingrese un texto correctamente")
        repetir = True
    else:
        longitud = len(texto)
        print("El texto ingresado tiene una longitud de " + str(longitud))
        repetir = False