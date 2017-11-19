def anteroposterior():
    numero= input("Introduce un número: ")
    print "Sus números anteriores son" ,numero-1, numero-2, numero-3
    
    print "Sus números posteriores son" ,numero+1, numero+2, numero+3

anteroposterior()

    
def anteroposterior1():
    numero= input("Introduce un número: ")
    for cont in range (numero-3,numero, 1):
        print "Sus números anteriores son" ,cont
    for cont in range (numero,numero+3, 1):
        print "Sus números posteriores son" ,cont
    
anteroposterior1()

    
