n = int(input("Selecciona un numero: \n"))


if n % 2 == 0:
    if n > 0:
        print ("numero par positivo")
    else:
        print ("numero par negativo")
elif n == 0:
    print ("numero cero")
elif  n % 2 != 0: #esta linea podria ser remplazada con un else sin condición y funcionaria de igual modo.
    if n > 0:
        print ("numero impar positivo")   
    else: 
        print("numero impar negativo")


