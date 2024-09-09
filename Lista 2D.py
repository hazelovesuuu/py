                    #LISTAS 2D EN PYTHON O MULTIDIMENSIONALES

#EJEMPLO NUMERO 1

print("EJEMPLO NUMERO 1")

bebidas= ["cafe", "soda", "cerveza", "vino","te"]
cena=["pan", "pollo", "carne",]                       #Se procede a crear 3 listas.
postre=["helado," "papas", ]

comida= [bebidas, cena, postre]         #Se adjuntan las [3 listas en 1 sola]
print(comida)

#EJEMPLO NUMERO 3

print("EJEMPLO NUMERO 2")

bebidas1= ["cafe", "soda", "cerveza", "vino","te"]
cena1=["pan", "pollo", "carne",]
postre1=["helado," "papas", ]

comida2=[bebidas1]        #Si se necesita 1 lista se pone en la variable [seguido del nombre], ejemplo ''bebidas1¿¿.
print(comida2)


#EJEMPLO NUMERO 3

print("EJEMPLO NUMERO 3")

bebidas2= ["cafe", "soda", "cerveza", "vino","te","ron", "tepache"]
cena2=["pan", "pollo", "carne","cerdo"]   #Si se necesita ubicar un valor en especifico, se pone[0] y [0] de acuerdo a la posicion que este.
postre2=["helado," "papas","chocolate"]

comida=[bebidas2, cena2, postre2]
print(comida[0][1])

#EJEMPLO NUMERO 4

print("EJEMPLO NUMERO 4")
bebidas3= ["cafe", "soda", "cerveza", "vino","te"]
cena3=["pan", "pollo", "carne",]
postre3=["helado," "papas", ]

comida= [bebidas3,cena3, postre3]
print(comida[0],[2])






