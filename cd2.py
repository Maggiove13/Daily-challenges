#Tabla de Multiplicar: 
# Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

# Pedir al usuario que ingrese un numero
numero_user = int(input("Ingrese un numero aleatorio de 1 al 9: "))
print(f"El numero elegido para la tabla: {numero_user}")

#Iterar los numeros en un rango de 10 y que inicie desde 1
for nros in range(1,11):
    print(f"{nros} x {numero_user} = {nros*numero_user}")

