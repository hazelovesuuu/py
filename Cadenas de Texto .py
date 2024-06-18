   #METODOS PARA CADENAS DE TEXTO

#EJEMPLO NUMERO 1        "METODO NORMAL"

print("EJEMPLO DE CADENA DE TEXTO, MODO NORMAL.")

nombre = "Erwin"     #asignacion de variable
print(len(nombre))      #imprimir el nombre y saber su longitud del mismo.

#EJEMPLO NUMERO 2

nombre1 = "Erwin BM"
print(len(nombre1))



#EJEMPLO NUMERO 3        "METODO DE BUSQUEDA"

print("EJEMPLO DE CADENA DE TEXTO, METODO DE BUSQUEDA.")

#EJEMPLO NUMERO 1

nombre2 = "Rafael"       #asignacion de la variable
print(nombre2.find("e"))    #ubicar una "letra" en un texto

#EJEMLPO NUMERO 2
nombre3 = ("Rafael SV")
print(nombre3.find("l"))



#EJEMPLO NUMERO 4      "METODO DE CAPITALIZE"

print("EJEMPLO DE CADENA DE TEXTO, METODO DE CAPITALIZE.")

#EJEMPLO NUMERO 1

nombre4 = ("elliot")    #asignacion de la variable
print(nombre4.capitalize())   #poner la primera letra de un texto en MAYUSCULA. #asignacion de la variable

#EJEMPLO NUMERO 2

nombre5 = ("darwin")
print(nombre5.capitalize())



#EJEMPLO NUMERO 5  "METODO UPPER"

print("EJEMPLO DE CADENA DE TEXTO, METODO DE UPPER")


#EJEMPLO NUMERO 1

nombre6 = "pryce"   #asignacion de la variable
print(nombre6.upper())   #convertir el texto a MAYUSCULAS

#EJEMPLO NUMERO 2

nombre7 = "tom"
print(nombre7.upper())


#EJEMPLO NUMERO  6 "METODO IS DIGIT"

print("EJEMPLO DE CADENA DE TEXTO, METODO DE IS DIGIT")

#EJEMPLO NUMERO 1

nombre8 = ("Siva")   # asignacion de la variable     #FALSE no son digitos
print(nombre8.isdigit()) # convertir el texto a TRUE O FALSE

#EJEMPLO NUMERO 2

nombre9 = ("12345")                                #TRUE son digitos
print(nombre9.isdigit())

#EJEMPLO DE CADENA DE TEXTO, METODO "IS ALPHA"

print("EJEMPLO DE CADENA DE TEXTO, IS ALPHA")

#EJEMPLO NUMERO 1

nombre11 =( "Carmine_Benjamin")   #asignacion de la vatriable  "FALSE", no estan juntos.
print(nombre11.isalpha())    #juntar textos

#EJEMPLO NUMERO 2

nombre12 =( "CarmineBenjamin")
print(nombre12.isalpha())

#EJEMPLO NUMERO 7, "NOMBRE COUNT"


print("EJEMPLO DE CADENA DE TEXTO, NOMBRE COUNT")

#EJEMPLO  NUMERO 1

nombre13 = "Dominic"      #se asgina la variable
print(nombre13.count("o"))  #se utiliza para ubicar letras y numeros

#EJEMPLO NUMERO 2

nombre14 = "Valer1a Marquez111"
print(nombre14.count("1"))

#EJEMLPLO NUMERO 8, #REPLACE"

print("EJEMPLO DE CADENA DE TEXTO, REPLACE")

#EJEMPLO NUMERO 1

nombre15 = ("Alfredo Cisneros Gomez")    #se asigna la variable
print(nombre15.replace("e","c"))   #se  utiliza para remplazar letras.

#EJEMPLO NUMERO 2

nombre16 = ("Wilfred Cisneros Alvarado")
print(nombre16.replace("i", "o"))


#EJEMPLO NUMERO 8, METODO "MULTIPLICAR"

print("EJEMPLO DE CADENA DE TEXTO, MULTIPLICACION")

#EJEMPLO NUMERO 1, MULTIPLICACION.

nombre17= ("Javier")   #se asigna la variable
print(nombre17*5)     #la cantidad de veces por la que se desea multiplicar











