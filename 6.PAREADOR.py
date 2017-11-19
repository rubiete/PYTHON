def pareador():
    x= input ("Dime un número: ")
    y= input ("Dime otro número: ")
    if (x%2 >0 and y%2 >0):
        print "Los 2 números son impares."
    if (x%2==0 and y%2==0):
        print "Los 2 números son pares."
    if (x%2 >0 and y%2==0):
        print "El primer número es impar y el segundo es par."
    if (x%2==0 and y%2>0):
        print "El primer número es par y el segundo es impar."
pareador()
