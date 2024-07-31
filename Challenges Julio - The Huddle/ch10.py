
#Challenge 10 --- THE HUDDLE -JULIO

#Eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.


# Definimos la lista de 10 números enteros con duplicados
numList = [1, 3, 3, 4, 5, 6, 6, 8, 9, 10]

# Función para eliminar los números duplicados de la lista
def delete_duplicates(createdList):
    # Convertimos la lista en un conjunto para eliminar duplicados y luego de vuelta a una lista
    no_duplicates_list = list(set(createdList)) #Los conjuntos (set) en Python no permiten elementos duplicados, 
    # por lo que esta operación elimina automáticamente cualquier duplicado en createdList, y lo vuelve a convertir en lista
    return no_duplicates_list #Y esa lista se guardarà en la varible: no_duplicates_list


# Llamada a la función y le pasamos la lista creada: "numlist"
cleaned_list = delete_duplicates(numList)

# Imprimir la lista original
print("Lista original:", numList)

#Imprimimos la lista sin los duplicados
print("Lista sin duplicados:", cleaned_list)
