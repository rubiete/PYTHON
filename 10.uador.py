def uador():
    texto=raw_input("Inserte el texto que quiere que sea uado: ")
    lista1= list(texto)
    for cont in range (0,len(texto),1):
        if texto[cont]=="a":
            lista1[cont]="u"
        if texto[cont]=="e":
            lista1[cont]="u"
        if texto[cont]=="i":
            lista1[cont]="u"
        if texto[cont]=="o":
            lista1[cont]="u"
    string="".join(lista1)
    print string

uador()    

def pig_latin():
    texto=raw_input("Inserte el texto que quiere que sea uado: ")
    for cont in range (0,len(texto),1):
        if texto[cont]=="a" or texto[cont]=="A" or texto[cont]=="e" or texto[cont]=="E" or texto[cont]=="i" or texto[cont]=="I" or texto[cont]=="o" or texto[cont]=="O":
            print "u",
        else:
            print texto[cont],
  
pig_latin()
