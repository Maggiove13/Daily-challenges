#Challenge Dia 4 - 14/06/24
#Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

numero = input("Ingrese solo numeros separados con comas; ej: 5,2,3,4 = ")
lista_numeros = [] #Esta lista serà usada para almacenar los numeros que vaya carando el usuario

partes_nros= numero.split(',') #split es una función de las cadenas de texto en Python. Toma un separador (en este caso, la coma ,)
# y divide la cadena en partes donde encuentre ese separador. Devuelve una lista de cadenas.

# Convertir cada parte en un número y agregarla a la lista.
for nro in partes_nros: #Recorrer sobre los numeros en la cadena de numeros ingresados por el user
    convertidos = float(nro) #Convertimos los numeros string a numeros flotantes
    lista_numeros.append(convertidos)

# Ordenar la lista en orden ascendente usando la función sorted()
lista_ordenada = sorted(lista_numeros)

# Redondear los números flotantes a enteros
lista_ordenada_enteros = [round(num) for num in lista_ordenada]
#round =  se utiliza para redondear números flotantes al entero más cercano.

# Mostrar la lista ordenada de enteros en una línea separados por comas
print("Lista de números enteros redondeados y ordenados de menor a mayor:")
print(", ".join(map(str, lista_ordenada_enteros)))
#map()= es una función en Python que aplica una función (en este caso str, que convierte a cadena) a cada elemento de un iterable (en este caso la lista_ordenada_enteros).
#str= Como resultado, obtienes una lista de cadenas donde cada elemento es la representación en cadena de los números enteros en lista_ordenada_enteros.
# .joint= método join une estas cadenas utilizando ", " como separador.




    
