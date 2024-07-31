#Challenge 9 --- THE HUDDLE -JULIO

#Recursión Factorial: Implementa una función recursiva para calcular el factorial de un número pequeño (por ejemplo, 5).

def factorial(N): 
    """Factorial de cualquier numero"""
    if N == 0:
        return 1 #Significa que el factorial de 0 seria 1
    else:
        return N * factorial(N - 1)
    

#Llamar a la funcion factorial
print(factorial(5))


#Si queremos saber el nro factorial de 5 entonces debemos multiplicar 
#5! = 5*4*3*2*1

#factorial(N)= N * factorial (N-1)
# Si N = 0
# factorial(N) = 1

#El factorial de un número es el producto de todos los números naturales positivos menores o iguales a ese número. 
# El factorial se denota con un signo de exclamación (!) después del número.
# Por definición, el factorial de 0 (0!) es 1.
# Esto se debe a que el factorial de un número es el producto de todos los números naturales positivos menores o iguales a ese número,
# y en el caso de 0, no hay números naturales positivos menores que él. Por lo tanto, el producto de ningún número es 1, 
# lo que se conoce como la identidad multiplicativa.