def pareador():
    x= input ("Dime un n�mero: ")
    y= input ("Dime otro n�mero: ")
    if (x%2 >0 and y%2 >0):
        print "Los 2 n�meros son impares."
    if (x%2==0 and y%2==0):
        print "Los 2 n�meros son pares."
    if (x%2 >0 and y%2==0):
        print "El primer n�mero es impar y el segundo es par."
    if (x%2==0 and y%2>0):
        print "El primer n�mero es par y el segundo es impar."
pareador()
