                                            #Listas en Python
#LISTA: #Una lista se utiliza para poder almacenar diferentes elementos dentro de una misma variable.



                                             #FUNCIONES EN PYTHON

#Funcion "append": Esta funcion le brinda un nuevo texto a la lista.

#Funcion "remove": Esta funcion remueve un objeto de la lista que se haya seleccionado,

#Funcion "pop": Esta funcion remueve el ultimo objeto de la lista.

#Funcion "insert": Esta funcion inserta un valor en un lugar especifico.

#Funcion "sort" : Esta funcion nos permite ordenar la lista alfabeticamente.

#Funcion "clear": Esta funcion limpia la lista.





#EJEMPLO NUMERO 1

print("EJEMPLO NUMERO 1")

comida= ["Pizza", "Hot-Dog", "Palomitas"]
print(comida)





#EJEMPLO NUMERO 2
print("EJEMPLO NUMERO 2")

snacks= ["M&M", "ICEE", "Swinklees", "Sabritas"]
for x in snacks:
    print(x)






#EJEMPLO NUMERO 3
print("EJEMPLO NUMERO 3")

snacks1= ["´Gomitas", "M&M", "ICEE", "Swinklees"]
snacks1.append("Takis")
for x in snacks1:
    print(x)



#EJERCICIO NUMERO 4

print("EJEMPLO NUMERO 4")

snacks2 = ["Gomitas", "M&M", "ICEE", "Swinklees", "Takis"]
snacks2.remove("ICEE")

for y in snacks2:
    print(y)

#EJERCICIO NUMERO 5

print("EJEMPLO NUMERO 5")


snacks3 = ["Gomitas", "M&M", "ICEE", "Swinklees", "Takis","Chips"]
snacks3.pop()

for z in snacks3:
 print(z)



#EJERCICIO NUMERO 6

print("EJEMPLO NUMERO 6")

snacks4 = ["Gomitas", "M&M", "ICEE", "Swinklees", "Takis","Chips"]
snacks4 [0] = "Nuggets"

for y in snacks4:
    print(y)


#EJEMPLO NUMERO 7
print("EJEMPLO NUMERO 7")

snacks5 = ["Gomitas", "M&M", "ICEE", "Swinklees", "Takis","Chips","Hamburgesa"]
for b in snacks5:
 snacks5.sort()
 print(b)


#EJEMPLO NUMERO 8

print("EJEMPLO NUMERO 8")

snacks6= ["Gomitas", "M&M", "ICEE", "Swinklees", "Takis","Chips","Hamburgesa"]
snacks6.clear()
for v in snacks6:
    print(v)







