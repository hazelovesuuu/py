                            #TUPLAS EN PYTHON

#Count: Se utiliza para contar cuantas veces se repite un numero.

#Index: Se utiliza para ver cuantas veces se repite un valor.




#EJEMPLO NUMERO 1

print("EJEMPLO NUMERO 1")


estudiantes = ("Diego",  "M" , 23,  "Karime" , "F",  23, "Maria", "F", 23)
#Se crea la variable (estudiantes) y se le adjutan los datos.


print(estudiantes.count(23))
#Se procede a imprimir y se usa la funcion count para localizar datos y contarlos.





#EJEMPLO NUMERO 2

print("EJEMPLO NUMERO 2")

estudiantes1 = ("Alejandro", "M", 34, "Fernando", "F", 32, "Vicente", "NB", 35)
#Se crea la varible (estudiantes2) y se le adjutan lo datos.


print(estudiantes1.index("M"))
#Se usa para localizar las posiciones en este caso localizar el sexo (M), se comienza desde el 0 hasta que se localiza.


#EJEMPLO NUMERO 3

print("EJEMPLO NUMERO 3")

estudiantes3= ( "Viktor", "M", 22,)

for x in estudiantes3:
    print(x)

    #EJEMPLO NUMERO 4

print("EJEMPLO Y MINI EJERCICIO NUMERO 4")

estudiantes4= ("Alfredo", ",M", 24, "Jimena", "F", 39, "Rafael", "M", 77, "Diego", "M", 19)

print(input("Digita el nombre:"))
if "Diego" in estudiantes4:
    print("Aqui esta el valor !!!!!")
elif not estudiantes4:
    print("Aqui no esta el nombre!!!")