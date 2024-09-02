                              #BUCLES ANIDADOS

                 #EJEMPLO NUMERO 1


fila = int(input("¿Cuántas filas quieres?"))
#Se procede a hacer otra variable (fila) y se le pone le "int" por que tendremos un valor entero de entrada.

columna = int(input("¿Cuántas columnas?"))
#Se procede a hacer otra variable(columnna) y se le pone le "int" por que tendremos un valor entero de entrada.

simbolo= input("Ingrese un símbolo:")
#Se procede a hacer otra variable(simbolo) y se le pone le "int" por que tendremos un valor entero de entrada.

for i in range (fila):
#Se usa el "for" y la variable (i) y "in" y range por la longitud.
   for j in range(columna):
#Se usa el "for" y la variable (j) y "in" y range por la longitud.
       print(simbolo, end="")
#Se procede  a hacer print de la variable (simbolo) y se pone "end" para finalizar.
       print()
#Se procede a correr el script.