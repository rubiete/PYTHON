def contapares():
    numero= input("Introduce el número: ")
    pares=0
    while numero>0:
        if (numero%2)==0:
            pares=pares+1
        numero=numero/10
    print "Su número tiene", pares,"cifras pares."    
contapares()
