def mayor(n1,n2):
    if (n1>n2):
        respuesta= n1
    else:
        respuesta=n2
    return respuesta
def comparador_principal():
    n1=input ("Dime un numero: ")
    n2=input ("Dime un número: ")
    print mayor(n1,n2)
    
comparador_principal()   
#FUNCIONES ARRIBA Y CUERPO PRINCIPAL ABAJO

def menu_operacion():
    n1= input("Dime un número: ")
    n2= input("Dime un numéro: ")
    while (seguir== "Sí"):
        print "¿Qué deseas hacer con los números?"
        print "1.SUMARLOS"
        print "2.MULTIPLICARLOS"
        print "3.RESTARLOS"
        print "4.DIVIDIRLOS"
        respuesta= input()

menu_operacion()
