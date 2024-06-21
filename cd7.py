#Challenge Dia 7 - 19/06/24

import random

#Juego de Piedra, Papel o Tijeras:
#  Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.

options = ["rock", "paper", "scissors"]

def get_user_choice(): 
    while True:
        user_choice = input("Ingrese una palabra entre: Rock, Paper or Scissors: ").lower() # Asegurar que lo que ingrese la variable
                                                                                            # lo albergue en minúsculas.
        if valid_choice(user_choice):
            return user_choice
        else:
            print("La palabra ingresada no es válida. Intente de nuevo.")

def valid_choice(user_choice): 
    if user_choice in options:
        print(f"Has elegido {user_choice}")
        return True # La palabra pertenece a una de las opciones de la lista
    else:
        return False # La palabra no pertenece a una de las opciones de la lista
    

def check_winner(user_choice, pc_choice):
    if user_choice == pc_choice:
        print("Es un empate")
    else:
        if user_choice == options[0] and pc_choice == options [1]:
            print("GANASTEE!!")
        elif user_choice == options[1] and pc_choice == options [2]:
            print("Looseeeer!! :c ")
        elif user_choice == options[2] and pc_choice == options [0]:
            print("Looseeeer!! :c ")
        elif user_choice == options[2] and pc_choice == options [1]:
            print("GANASTEE!!")
        elif user_choice == options[0] and pc_choice == options [2]:
            print("GANASTEE!! ")
        elif user_choice == options[1] and pc_choice == options [0]:
            print("Looseeeer!! :c ")

# Obtener la elección del usuario
user_choice = get_user_choice()

# Elección aleatoria de la computadora
pc_choice = random.choice(options)
print(f"La computadora ha elegido {pc_choice}")

# Determinar el ganador
check_winner(user_choice, pc_choice)






