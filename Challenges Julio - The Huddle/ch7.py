#Challenge 7 --- THE HUDDLE -JULIO
#Piloto de eventos (Priority Queue): 
# Implementa una cola de prioridad utilizando una lista para insertar y eliminar 5 elementos.

from queue import PriorityQueue

#Primero debemos instanciar
fila = PriorityQueue() # Crear una instancia de PriorityQueue

lista = [2, 5, 4, 3, 1]

# Agregar elementos a la cola con prioridad
fila.put(lista[0]) 
fila.put(lista[1]) 
fila.put(lista[2]) 
fila.put(lista[3]) 
fila.put(lista[4]) 

# Mostrar la cola completa
print(fila.queue) 

while fila.not_empty():
    # Obtener el elemento con la prioridad más alta y eliminarlo de la cola
    element = fila.get() # Obtener el elemento con la prioridad más alta de la cola con prioridad y eliminarlo de la cola, asignando su valor a la variable elemento
    print(element) # Imprimir el valor de la variable elemento
    
    # Mostrar la cola después de las eliminaciones
    print("Cola después de las eliminaciones:", list(fila.queue))

    