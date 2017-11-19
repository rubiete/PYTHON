def reloj():
    hora=input("¿Que hora es?: ")
    if hora>=6 and hora<14:
           print "Buenos días"
    if hora>=14 and hora<20:
           print "Buenas tardes"
    if hora>=20 and hora<24:
           print "Buenas noches"
    if hora>=0 and hora<6:
           print "Buenas noches"
reloj()

