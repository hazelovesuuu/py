                              #BUCLES WHILE
 #EJEMPLO NUMERO 1

#se comento para evitar que se corra el script.

#while 1==1: #Se crea la condicion del bucle y se dan valores ya sean "True" o "False".
    #print("Este es un bucle, y siempre seguira!!!") #Se pone el mensaje que se va a querer imprimir.



#EJERCICIO NUMERO 1

print("EJERCICIO NUMERO 1")

nombre ="" #Se crea un variable y se pide los datos de la misma.

while len(nombre) == 0: #Se usa "while" para el nombre y "len" para la longitud del mismo y se pone la variable que es donde ira.

    nombre= input("Ingresa tu nombre:") #Se usa la variable "nombre" y se le pide los datos con input.


#/////////////////////////////////////////////////////////////////////////////////////



#EJERCICIO NUMERO 2

print("EJERCICIO NUMERO 2")

nombre1 =("") #Aqui arrojar el valor "True", por que no tiene ningun digito entre los parentesis.

print(not nombre1)#Se procede a usar print y se usa "not" para ver si es un valor "True" o "False"



#/////////////////////////////////////////////////////////////////////////////////////


#EJERCICIO NUMERO 3

print("EJERCICIO NUMERO 3")

nombre2= "F" #Aqui arroja el valor "False", por que tiene un digito entre los parentesis.

print(not nombre2)#Se procede a usar print y se usa "not" para ver si es un valor "True" o "False"


#/////////////////////////////////////////////////////////////////////////////////////



#EJERCICIO NUMERO 4

print("EJERCICIO NUMERO 4")

nombre3= ("sfd") #Se crea la variable y se le ponen datos a la misma si es que lo requiere.

while not nombre3: #Mientras esta no tenga datos se saltara y ira con la siguiente .
    nombre3= input("Ingresa tu nombre: ")


#/////////////////////////////////////////////////////////////////////////////////////


print("EJERCICIO NUMERO 4 (PARTE DOS)")

nombre4= "" #Se crea la variable y se le ponen datos a la misma si es que los requiere.

while not nombre4: #Mientras esta no tenga datos seguira en bucle y si tiene datos arrojara un valor "TRUE" o "FALSE".
    nombre4= input("Ingresa tu nombre: ")



#/////////////////////////////////////////////////////////////////////////////////////

print("EJERCICIO NUMERO 5")

nombre5 = ""  #Se procede a dar los datos.
while not nombre5 or len(nombre ) == 0:  #Se procede a pedir la longitud del nombre y ya una vez dada la longitud se le cocatena con los datos.
    nombre5= input("Ingresa tu nombre:")

    print("Hola, ¿Comó estas?..." +nombre5)

