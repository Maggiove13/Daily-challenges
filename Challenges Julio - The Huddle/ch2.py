#Challenge 2 --- THE HUDDLE -JULIO

#Ordenamiento simple: 
# Escribe una función que ordene una lista de 5 enteros utilizando cualquier método de ordenamiento que prefieras 
# (por ejemplo, burbuja, inserción, selección).

#Definimos la lista a ordenar
array = [5,3,4,8,7]


#Ordenamiento por el algoritmo Burbuja
def bubbleSort(array):
    
    #Primero debemos recorrer toda la lista, pero primero necesitamos la longitud de la lista
    lenght = len(array) - 1 #Va a reccorrer todos los elementos -1 (por que siempre todo conteo incia con  0)

    #Iteraremos todos los elementos de la lista || Bucle para las pasadas, en este caso 5 pasadas
    for i in range(0, lenght): #Recorreremos toda la lista desde el indice 0 hasta el numero guardado en la variale lenght

        #Otro bucle que se encargara de hacer las comparaciones e intercambios
        for j in range(0, lenght):
            if array[j] > array[j + 1]: #Si el numero del indice 0, es mayor al numero adyacente
                temp = array[j] #Guardamos en una variable temporal el valor del indice 0 ya que, en la siguiente linea el siguinte indice
                                #pasa a ser el indice 0, pero lo guardamos para poder cambiar de lugar
                
                array[j] = array[j + 1] #entnces el nuevo indice 0, seria el adyacente
                array[j + 1] = temp #y aca se hace el cambio
        return array

print("Antes de ordenar. ")
print(array)
print("Despues de ordenar. ")
sorted = bubbleSort(array)
print(sorted)


