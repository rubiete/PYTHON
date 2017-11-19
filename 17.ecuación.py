import math
def ecuacionador():
    a=input("Introdúceme el coeficiente de x**2: ")
    b=input("Introdúceme el coeficiente de x: ")
    c=input("Introdúceme el termino independiente: ")
    formula1= ((-b+(math.sqrt(b**2-4*a*c)))/(2*a))
    formula2= ((-b-(math.sqrt(b**2-4*a*c)))/(2*a))
    if (b**2-4*a*c)>0:
       print "La primera solución es x vale", formula1
       print "La segunda solución es x vale", formula2
    
    if (b**2-4*a*c)==0:
       print "La única solución es x=", formula1

    if (b**2-4*a*c)<0:
       print "No tiene solución."
    
ecuacionador()
