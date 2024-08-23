numero = int(input("Selecciona un numero: \n"))


if numero % 2 == 0:
    if numero > 0:
        print ("numero par positivo")
    else:
        print ("numero par negativo")
elif numero == 0:
    print ("numero cero")
elif  numero % 2 != 0: #esta linea podria ser remplazada con un else sin condición y funcionaria de igual modo.
    if numero > 0:
        print ("numero impar positivo")   
    else: 
        print("numero impar negativo")



