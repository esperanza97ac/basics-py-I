"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""

"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
mascotas = ['perro', 'gato', 'loro']
print(mascotas)

print(len(mascotas))

print(mascotas[2])

mascotas.append("urón")
print(mascotas)

mascotas[0] = "hamster"
print(mascotas)

mascotas.remove("gato")
print(mascotas)

"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
plantas = ('cactus', 'orquidea', 'rosas')

print(len(plantas))

print(plantas[2])

plantas[1] = "hoja rota"
# Esto da error ya que las tuplas son inmutables

# Análisis: Al intentar modificar la tupla da error porque una vez creadas, 
# al ser inmutables, no se pueden modificar, ni agregar ni eliminar sus elementos.


"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""

"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""
nombres = {'María', 'Cris', 'Cris', 'Alex'}
# Da error porque hay dos nombres repetidos y en los sets eso no puede ocurrir.

print(len(nombres))

# Los sets no tienen orden por lo que no se puede acceder a ninguna posición

# Escribe el código para agregar una elemento al set, imprimir por consola el set
nombres.add("Lucía")
print(nombres)

# Escribe el código para eliminar un elemento del set, imprimir por consola el set
nombres.remove("Cris")
print(nombres)

"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""

"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario 
"""
ciudad = {"nombre": "Barcelona"
         "país": "España"}

# Escribe el código aqui para acceder y ver por consola el valor de 'nombre'
print(ciudad["nombre"])

# Escribe el código aqui para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'
ciudad["habitantes"] = 150000

# Escribe el código aqui para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola
ciudad['nombre'] = 'Madrid'
print(ciudad)

# Escribe el código aqui para eliminar un par clave-valor de 'ciudad' y verlo por consola
del ciudad['pais']
print(ciudad)