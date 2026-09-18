"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
mensaje = "¡Hola, Mundo!"
print(mensaje)
"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
mensaje = "Hello world!"
print(mensaje)

#Hemos cambiado el valor del mensaje por tanto, ahora aparece inscrito el nuevo mensaje

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
texto = "Hola"
entero = 5
decimal = 3.14
bool = True
lista = ["Carne", "pescado", "verdura",]
inmutable = (6, 7, 8)
planta = {
    "Arbol" : "Cerezo", 
    "Fruta" : "Cereza"}
conjunto = {1,2,3}

print("string:", texto, type(texto))
print("init:", entero, type(entero))
print("float:", decimal, type(decimal))
print("bool:", bool, type(bool))
print("list:", lista, type(lista))
print("tuple:", inmutable, type(inmutable))
print("dictionary:", planta, type(planta))
print("set:", conjunto, type(conjunto))


