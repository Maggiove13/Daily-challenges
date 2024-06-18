#Challenge Dia 6 - 18/06/24
#Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

celsius_user = float(input("Agregue el grado de hoy en celsius "))

#convertir a Fahrenheit.
grados_convertidos = celsius_user*9/5 +32

print(f"Hace {grados_convertidos} grados Fahrenheit el dia de hoy")
