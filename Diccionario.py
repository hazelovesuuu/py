                     #DICCIONARIO EN PYTHON


#EJEMPLO NUMERO 1

print("EJERCICIO NUMERO 1")

videojuegos={

    "Halo CE": "Halo Combat Evolved!!!",
      "Halo 2 ": "Halo 2 en HTMCC",
         "Halo 3": "Halo 3 EN HTMCC",
            "Halo 4" :"Halo 4 EN HTMCC",
               "Halo 5": "Halo 5 Guardians"

                           }
print(videojuegos["Halo CE"])

#Para querer saber el valor se usa esta linea:

# print(videojuegos["Halo CE"]) 
# En el "Halo CE" va el dato que deseamos consultar.













   #EJEMPLO NUMERO 2
   
print("EJEMPLO NUMERO 2")

comidamexicana={
   
"tacos": "suadero",
    "bebidas":"aguas frescas",
       "salsa roja" : "picante",
         "salsa verde" : "guacamole"
}

print(comidamexicana.get("refresco", "No disponible"))

#Para querer consultar un dato:

#print(comidamexicana.get["refrescos", "No disponible"]) 

#En "refrescos" ponemos el dato que deseamos consultar.








#EJEMPLO NUMERO 3

print("EJEMPLO NUMERO 3")


hardware={

"Procesador":"i9",
  "Grafica":"4090",
   "Memorias RAM":"16",
    "Unidades de disco duro": "HDD",
      "Unidades de estado solido": "SSD"
}

print(hardware.keys())

#Para querer imprimir una cadena de datos con sus claves:
#print(hardware.keys()), esto nos arrojara todos los valores.










#EJEMPLO NUMERO 4

print("EJEMPLO NUMERO 4")

fiesta= {
   
   "Invitados": "personas",
     "Comida":  "banquete",
      "Diversion" : "payaso",
         "Bebidas" : "fuente de sodas"
         
}

print(fiesta.values())
#Para querer imprimir una cadena de texto con sus claves:
#print(fiesta.value())











#EJEMPLO NUMERO 5

print("EJEMPLO NUMERO 5")

tiendadeelectronicos= {
   
   "Tableta": "iPad",
   "Celular": "iPhone",
   "Audifonos": "Earpods",
   "Computodora": "MacBook",
   "Pila recargable": "Magsafe" 
}

print(tiendadeelectronicos.items)


#Para querer imprimir toda la lista del diccionario.

#print(tiendadeelectronicos.items)













#EJEMPLO NUMERO 6

print("EJEMPLO NUMERO 6")


tiendadeelectronicos1= {
   
   "Tableta": "iPad",
   "Celular": "iPhone",
   "Audifonos": "Earpods",
}

for key, value in tiendadeelectronicos1.items():
       print(key, value)
       
#Este metodo nos imprimira los valores del diccionario y lo que este almacenado.
# for key, value in tiendadeelectronicos1.items():
# print(key, value)





#EJEMPLO NUMERO 7

print("EJEMPLO NUMERO 7")

fiesta= {
   
   "Invitados": "personas",
     "Comida":  "banquete",
      "Diversion" : "payaso",
         "Bebidas" : "fuente de sodas",
           "Decoracion": "Globos",
              "Arreglos de mesa": "Flores"
}

fiesta.update({"Volado" : "Dinero"})

#Si se require agregar un valor sera necesario el siguiente comando:
#fiesta.update{"Volado" : "Dinero"} <--- se cambia "Volado" por el valor que se desea agregar y "Dinero" por el mimso valor.



#EJEMPLO NUMERO 8

print("EJEMPLO NUMERO 9")

presentacion= {
  "Invitados": "personas",
     "Comida":  "banquete",
      "Diversion" : "payaso",
         "Bebidas" : "fuente de sodas",
           "Decoracion": "Globos",
              "Arreglos de mesa": "Flores"
}  


presentacion.pop("Areglos de mesa")

#Si se desea eliminar un valor:

#presentacion.pop("Areglos de mesa") <--- (el valor que se desea eliminar.)





#EJEMPLO NUMERO 9

print("EJEMPLO NUMERO 9")

presentaciondeboda= {
  "Invitados": "personas",
     "Comida":  "banquete",
      "Diversion" : "payaso",
         "Bebidas" : "fuente de sodas",
           "Decoracion": "Globos",
              "Arreglos de mesa": "Flores"
}  
   

presentaciondeboda.clear()

