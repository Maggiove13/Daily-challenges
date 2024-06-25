#include <iostream>
#include <string> //incluimos la biblioteca <string> para poder trabajar con cadenas de caracteres.

//Challenge Dia 11 - 24/06/24
//Palíndromo: Escribir un programa que determine si una cadena de caracteres ingresada por el usuario es un palíndromo 

    //Palindromo ---------> Un palíndromo es una palabra, frase o secuencia de caracteres que se lee igual hacia adelante y hacia atrás. 
                        //Es decir, si lees la palabra de izquierda a derecha o de derecha a izquierda, la secuencia de letras es la misma


int main() {
    std::string user_word;
    std::cout << "Ingrese una palabra: ";
    std::cin >> user_word;

    //Declaramos dos variables enteras -inicio y fin- para llevar un registro de los índices del primer y último carácter de la palabra
    int inicio = 0;
    int fin = user_word.length() - 1; //corresponde al último índice de la cadena. = Ejemplo "Ana" lenfth es 3-1: 2, y al ingresar a los indices seria 0: A, 1:n, 2:a
    bool es_palindromo = true; // Esta variable se utilizará para almacenar el resultado de la comparación de los caracteres de user_word.

  // Comparamos cada par de caracteres de la variable "user_word",
  // empezando por el inicio y el final y avanzando hacia el centro
    while (inicio < fin) {//Si la palabra es un palíndromo, entonces cada par de caracteres simétricos debe ser igual.
        if (user_word[inicio] != user_word[fin]) { // si los caracteres no coinciden entonces es false
        es_palindromo = false;
        break; 
        }
    //Si los caracteres coinciden, simplemente continuamos con la siguiente iteración del buclee incrementamos la variable inicio
    //       y decrementamos la variable fin para avanzar hacia el centro de la palabra y comparar el siguiente par de caracteres.
    inicio++; //incrementamos
    fin--;  //decrementamos 
    }

    if (es_palindromo) {
    std::cout << user_word << " es un palindromo." << std::endl;
    } else {
    std::cout << user_word << " no es un palindromo." << std::endl;
    }

return 0;
}