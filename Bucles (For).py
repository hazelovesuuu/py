                                                 #BUCLES "FOR"
#EJEMPLO NUMERO 1

#COUNTDOWN DEL 1 AL 10

print("EJERCICIO NUMERO 1")

for countdown1 in range(1, 11):
# Para el countdown se usa el "for" y despues el "in" y se le junta con el "range", ahi especificamos la cuenta.

 print(countdown1)
#aqui solo se imprime el script.






#EJEMPLO NUMERO 2

print("EJERCICIO NUMERO 2")

for number  in range (1, 12, 2): #Aqui se le pone el 2 para saltar los numeros y quede 3. 5. 7 etc.

# Para el countdown se usa el "for" y despues el "in" y se le junta con el "range", ahi especificamos la cuenta.

 print(number)
#aqui solo se imprime el script.





#EJEMPLO NUMERO 3

print("EJERCICIO NUMERO 3")

nombre =  input("Ingresa tu nombre, por favor !!")
#Se le pide al usuario ingresar el nombre y despues este lo contara y lo pondra en una misma linea de codigo.

for x in nombre: #Este queda como "for" variable (x)y "in" nombre del usuario.
    print(x)

#EJEMPLO NUMERO 4

print("EJERCICIO NUMERO 4")

import time #Se procede a importar la libreria time.
for a in range (10, 0, -1):#Se usa "for" y la variable (a) y "in" y range especificando la cuenta.
 print(a) #Se imprime la variagble (a)
 time.sleep(3) #Este es el countdown y la velocidad.

print("Feliz Año Nuevo !!!")

