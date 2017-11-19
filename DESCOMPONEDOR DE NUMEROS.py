def descomponedor():
    n=input("Introdúceme el número que deseas descomponer en factores: ")
    i=2
    if n==1:
        print 1
    else:
        while n>0:
            if n%i==0:
                n=n/i
                print i
            else:
                i=i+1


def descomponedor1():
    x=input("Introdúceme el número que deseas descomponer en factores1: ")
    for cont in range (2,x,1):
        while x%cont==0:
            print cont
            x=x/cont
    
descomponedor1()
 
