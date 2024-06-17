# Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas:
# una de claves y otra de valores.


#Creamos las variables de listas
Lista_frutas = ["manzana", "pera", "frutilla", "piña"]
Lista_precios= [3000, 3500, 10000, 8000]
dictionary = {} #Diccionario vacío para almacenar los valores y claves.

#Creamos una funcion que itere los alementos para agregrlos al diccionario vacio por el momento
def fill_dictionary(Lista_frutas, Lista_precios):
    #usamos un bucle for para recorrer las claves y valores emparejados y agregarlos al diccionario.
    for frutas, precios in zip(Lista_frutas, Lista_precios): #con zip emparejamos las claves con los valores
        dictionary[frutas] = precios # Agregamos el par clave-valor (frutas-precios)al diccionario.
    return dictionary

dictionary_filled = fill_dictionary(Lista_frutas, Lista_precios)
print(dictionary_filled)