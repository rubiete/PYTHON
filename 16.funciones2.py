#FUNCIONES ARRIBA Y CUERPO PRINCIPAL ABAJO
#3 PREGUNTAS
#¿QUÉ DATOS RECIBE?
#¿QUÉ DEVUELVE?
#¿CÓMO LO HACE?

def suma(n1,n2):
    respuesta=n1+n2
    return respuesta
def multiplicacion(n1,n2):
    respuesta=n1*n2
    return respuesta
def resta(n1,n2):
    respuesta=n1-n2
    return respuesta
def division(n1,n2):
    respuesta=n1/n2
    return respuesta

def menu_operacion():
    seguir="Sí"
    n1= input("Dime un número: ")
    n2= input("Dime un número: ")
    while (seguir== "Sí"):
        print "¿Qué deseas hacer con los números?"
        print "1.SUMARLOS"
        print "2.MULTIPLICARLOS"
        print "3.RESTARLOS"
        print "4.DIVIDIRLOS"
        respuesta= input()
        #if (respuesta==1):
        #    suma= n1+n2
        #    print suma
        #if (respuesta==2):
        #    multiplicar= n1*n2
        #    print multiplicar
        #if (respuesta==3):
        #   resta= n1-n2
        #    print suma
        #COMO LO ENTENDERIAMOS
        if (respuesta==1):
            print "LA SUMA ES" ,suma(n1,n2)
        if (respuesta==2):
            print "EL PRODUCTO ES" ,multiplicacion(n1,n2)
        if (respuesta==3):
            print "LA RESTA ES", resta(n1,n2)
        if (respuesta==4):
            print "EL COCIENTE ES", division(n1,n2)
        
      
menu_operacion()
