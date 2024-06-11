# Paso 1
# Solicitar al usuario que agregue una frase
cadena = input("Agregue una frase aqui")

#Paso 2
# Funcion para invertir la cadena de caracteres
def invertir_caracteres(cadena):
    # Si la longitud de la cadena es igual a 0, se ejecutará el siguiente bloque de código.
    if len(cadena) == 0:
        return "" 
    else:
        return cadena[-1] + invertir_caracteres(cadena[:-1])
# cadena[-1]: Obtiene el último carácter de la cadena.
# cadena[:-1]. Esto crea una nueva cadena que contiene todos los caracteres de la cadena original, excepto el último.

#Paso 3
# Mostrar el resultado
resultado = invertir_caracteres(cadena) 
print(f"La frase invertida es: {resultado}")