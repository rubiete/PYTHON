import math
def ecuacionador():
    a=input("Introd�ceme el coeficiente de x**2: ")
    b=input("Introd�ceme el coeficiente de x: ")
    c=input("Introd�ceme el termino independiente: ")
    formula1= ((-b+(math.sqrt(b**2-4*a*c)))/(2*a))
    formula2= ((-b-(math.sqrt(b**2-4*a*c)))/(2*a))
    if (b**2-4*a*c)>0:
       print "La primera soluci�n es x vale", formula1
       print "La segunda soluci�n es x vale", formula2
    
    if (b**2-4*a*c)==0:
       print "La �nica soluci�n es x=", formula1

    if (b**2-4*a*c)<0:
       print "No tiene soluci�n."
    
ecuacionador()
