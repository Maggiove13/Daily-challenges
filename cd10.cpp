#include <iostream>
#include <algorithm> // Incluimos la biblioteca <algorithm> para usar std::sort()

int main (){

    //Creamos un array de 5 elementos
    int array[5] = {1,3,5,2,4};

    // Ordenamos el array utilizando std::sort()
    std::sort(array, array + 5);//estamos indicando que queremos ordenar el rango de elementos que va desde el primer elemento 
                                //hasta el último elemento del array.

    // Mostramos el array ordenado
    for (int i = 0; i < 5; i++) {
        std::cout << array[i] << " ";//accede al elemento del array en la posición i,
                                    // y luego imprime ese elemento
    }
    std::cout << std::endl;

    return 0;
}

