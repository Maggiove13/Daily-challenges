#Challenge Dia 8 - 20/06/24
#Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

import random
import string # Proporciona constantes con caracteres ASCII útiles para construir contraseñas seguras
# --> (ascii_uppercase para letras mayúsculas, ascii_lowercase para letras minúsculas, digits para números y punctuation para símbolos)

def generate_password():
    # Definir los caracteres permitidos para cada categoría
    letras_mayusculas = string.ascii_uppercase #mayusculas
    letras_minusculas = string.ascii_lowercase #Mminusculas
    numeros = string.digits #para números y punctuation para símbolos
    simbolos = string.punctuation  # caracteres especiales
    
    # Combinar todos los caracteres permitidos
    caracteres_permitidos = letras_mayusculas + letras_minusculas + numeros + simbolos
    
    # Generar longitud aleatoria para la contraseña entre 8 y 16 caracteres
    longitud = random.randint(8, 16)
    
    # Generar la contraseña aleatoria
    password = ''.join(random.choice(caracteres_permitidos) for _ in range(longitud))
    
    return password

# Generar y mostrar la password segura
new_password = generate_password()
print(f"La contraseña generada es: {new_password}")
