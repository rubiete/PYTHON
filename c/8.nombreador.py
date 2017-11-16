def nombreador():
    nombre=raw_input ("Dime tu nombre: ")
    numero= len(nombre)
    print "Tu nombre tiene",numero,"letras."
    print "La inicial de tu nombre es la", nombre[0]

nombreador()

def palabreador():
    palabra= raw_input ("Dime una palabra: ")
    sumaa=0
    sumae=0
    sumai=0
    sumao=0
    sumau=0
    for cont in range (0,len(palabra),1):
        if palabra[cont]=="a":
            sumaa=sumaa+1
        if palabra[cont]=="e":
            sumae=sumae+1
        if palabra[cont]=="i":
            sumai=sumai+1
        if palabra[cont]=="o":
            sumao=sumao+1
        if palabra[cont]=="u":
            sumau=sumau+1
    print"En la palabra", palabra, "hay" ,sumaa, "letras A"
    print"En la palabra", palabra, "hay" ,sumae, "letras E"
    print"En la palabra", palabra, "hay" ,sumai, "letras I"
    print"En la palabra", palabra, "hay" ,sumao, "letras O"
    print"En la palabra", palabra, "hay" ,sumau, "letras U"
    sumavocales=sumaa+sumae+sumai+sumao+sumau
    print"En la palabra", palabra, "hay" ,sumavocales, "vocales"

palabreador()
