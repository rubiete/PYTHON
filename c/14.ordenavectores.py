def ordenatrescifras():
    numero= input("Dime un n�mero de 3 cifras: ")
    n_cifras=0
    while numero>0:
        numero=numero/10
        n_cifras=n_cifras+1
    print "Tu n�mero tiene" , n_cifras, "cifras."
    return n_cifras

ordenatrescifras()

def ordenavectores():
    numero=input("Introduce tu n�mero: ")
    lista=[numero]
#Vector:Listas []. Listas[0,9,8]+
