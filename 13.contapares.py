def contapares():
    numero= input("Introduce el n�mero: ")
    pares=0
    while numero>0:
        if (numero%2)==0:
            pares=pares+1
        numero=numero/10
    print "Su n�mero tiene", pares,"cifras pares."    
contapares()
