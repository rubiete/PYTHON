def sucesionador():
    numero= input("INTRODUCE EL NUMERO HASTA EL QUE DESEAS SUMAR: ")
    suma=0
    for cont in  range(1,numero+1,1):
        suma=suma+cont
    print "resultado=", suma
        
sucesionador()
