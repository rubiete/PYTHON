def anteroposterior():
    numero= input("Introduce un n�mero: ")
    print "Sus n�meros anteriores son" ,numero-1, numero-2, numero-3
    
    print "Sus n�meros posteriores son" ,numero+1, numero+2, numero+3

anteroposterior()

    
def anteroposterior1():
    numero= input("Introduce un n�mero: ")
    for cont in range (numero-3,numero, 1):
        print "Sus n�meros anteriores son" ,cont
    for cont in range (numero,numero+3, 1):
        print "Sus n�meros posteriores son" ,cont
    
anteroposterior1()

    
