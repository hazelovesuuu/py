                             #BREAK CONTINUE O PASS

#BREAK: Se usa para terminar completamente el bucle.
#CONTINUE: Se usa para quitar caractere especiales.
#PASS: No tiene ningun uso, solo es un marcador de posiciones.




print("EJEMPLO NUMERO 1, USO DE ''BREAK''")
#EJEMPLO DE USO DE BREAK
while True: #Mientras se tenga el valor, este sera "True"
    nombre= input("Ingresa tu nombre:") #Se crea una variable (nombre) y se le pide la entrada de datos (input).
    if nombre != "": #Mientras se tengan los datos, el bucle termina.
        break #Rompe el bucle.



#EJEMPLO DE USO DE CONTINUE
print("EJEMPLO NUMERO 2, USO DE ''CONTINUE'' ")
telefono= "123-456-789-00" #Se crea la variable (telefono) y se le adjuntan los datos.
for i in telefono: #Se le dan instrucciones para la variable (i) en (telefono_).
     if i =="-":#Si la variable (i) tiene "-", se continua y se le quitan.
         continue
         print(i, end="") #Se imprime con los caracteres especiales.




#EJEMPLO DE USO DE PASS
print("EJEMPLO NUMERO 3. USO DE ''BREAK''")

for i in range(1,21):  #Se procede a hacer usar for y (i) in range, se ponen los numeros acontinuacion.
    if i == 13: #Si el numero en la variable es 13, se salta y se sigue con los demas,
        pass #NIGUNA FUNCION, SOLO OMITE EL CARACTER.
    else:
        print(i) #Imprime el script.
