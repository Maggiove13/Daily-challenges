# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

#Crear una variable frase
frase = "Juegos del hambre"

# Crear una lista de las vocales que debe analizar si hay
vocales = ["a", "e", "i", "o", "u"]

# contador de vocales
contador_vocales = 0

# Recorrer cada caracter en la frase
for letra in frase:
  # Verifica si de entre todas las letras recorridas existen vocales como en la lista
  if letra in vocales:
    # Incrementar el contador de vocales
    contador_vocales += 1


print(f"La frase tiene {contador_vocales} vocales")