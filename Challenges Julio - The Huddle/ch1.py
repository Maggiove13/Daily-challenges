#Challenge 1 --- THE HUDDLE -JULIO

# Búsqueda en lista ordenada:
# Implementa una función de búsqueda binaria que determine si un número está en una lista ordenada de 10 elementos.

#Definimos la lista
numList = [1,2,3,4,5,6,7,8,9,10]

#Pedimos al usuario que ingrese un numero entero
num_wanted = int(input("Ingrese un numero entero: ")) #Definimos cual sera el numero que deseamos encontrar en la lista


#La funcion nos devolvera True si el elemento esta en la lista y False si no esta en la lista

def binarySearch(numList, num_wanted):
    #Difinimos las variables, Inicio, final y medio
    
    start = 0
    end = len(numList) - 1
    
    while start <= end:
        #necesitamos el indice del numero que esta en el medio de la lista
        mid = (start + end) // 2 # Division sin resto para determinar la mitad
        
        #Comprobaremos si encontramos el elemento
        if numList[mid] == num_wanted:
            return True
        
        #Si el nro que buscamos es mayor al numero del medio entonces se redefine el inicio, 
        # Se descartaran los nros menores a ese nro del medio
        elif numList[mid] < num_wanted:
            start = mid + 1
        
        #Si el numero del medio es mayor al numero que buscamos entonces se redefine el final, 
        # descartaremos todos los numeros mayores al medio
        else: 
            end = mid -1
            
    #Si el nro no esta en la lista, devuelve False       
    return False


# Llamamos a la función y mostramos el resultado
if binarySearch(numList, num_wanted):
    print(f"El número {num_wanted} está en la lista.")
else:
    print(f"El número {num_wanted} no está en la lista.")


