                                                  #SETS EN PYTHON



#MISMAS FUNCIONES QUE LAS LISTAS SOLO CON UN CAMBIO EN LA ULTIMA

#Funcion "add": Esta funcion agrega un nuevo texto a la lista.

#Funcion "remove": Esta funcion remueve un objeto de la lista que se haya seleccionado,

#Funcion "pop": Esta funcion remueve el ultimo objeto de la lista.

#Funcion "clear": Esta funcion limpia la lista.

#Funcion "update": Esta funcion actualiza un valor en un lugar especifico.

#Funcion "difference" : Esta funcion resalta los valore que son exclusivos.

#Funcion "intersection": Esta funcion devuelve el elemento repetido en las 2 variables.


#EJEMPLO NUMERO 1

print("EJEMPLO NUMERO 1")

utensilios= {"tenedor", "cuchara","cuchillo", "plato", }

for x in utensilios:
    print(utensilios)





#EJEMPLO NUMERO 2

print("EJEMPLO NUMERO 2")


utensilios1 = {"tenedor", "servilletas,", "plato", }
utensilios1.add("cuchara")
print(utensilios1)




#EJEMPLO NUMERO 3

print("EJEMPLO NUMERO 3")
utensilios2 = {"tenedor", "cuchara", "plato", "vaso", "cuchillo"}
utensilios2.remove("vaso")
print(utensilios2)




#EJEMPLO NUMERO 4

print("EJEMPLO MUMERO 4")

utensilios3={"tenedor", "cuchillo", "plato", "vaso", "servilleta"}
utensilios3.pop()
print(utensilios3)




#EJEMPLO NUMERO 5

print("EJEMPLO NUMERO 5")

utensilios4 = {"tenedor", "cuchillo", "plato", "servilleta"}
utensilios4.clear()
print(utensilios4)


#EJEMPLO NUMERO 6

print("EJEMPLO NUMERO 5")

utensilios5 = {"tenedor", "cuchillo", "plato", "servilleta"}
utensilios6 = {"popote", "vaso", "tapa"}
utensilios5.update(utensilios6)
print(utensilios5)

#EJEMPLO NUMERO 7

print("EJEMPLO NUMERO 6")

utensilios7 = {"tenedor","popote", "cuchillo", "cuchara"}
utensilios8 = {"servilleta", "mantel", "cuchara"}
utensilios7.difference(utensilios8)
print(utensilios7)

#EJEMPLO NUMERO 8

print("EJERCICIO NUMERO 7")

utensilios9= {"servilleta", "cuchara", "cuchillo"}
utensilios10 = {"servilleta", "mantel", "tenedor"}
utensilios9.intersection(utensilios10)
print(utensilios9.intersection(utensilios10))


