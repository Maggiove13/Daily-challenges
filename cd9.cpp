//Challenge Dia 9 - 21/06/2
//Escribir un programa que pida al usuario dos números y los sume. ¡Pero esta vez hazlo en C++! :)

#include <iostream>

using namespace std;

int main (){

    int numero1;
    int numero2;
    
    cout << "Agrega un numero entero cualquiera del 1 al 100 sin comas: ";
    cin >> numero1;
    cout << "Agrega otro numero entero cualquiera del 1 al 100 sin comas: ";
    cin >> numero2;
    
    int suma = numero1 + numero2;

    cout <<"El resultado de la suma de los numeros es: " << suma <<'\n';

    return 0;
}