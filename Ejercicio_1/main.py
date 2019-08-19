'''

Problema:
La mediana de los números M se define como el número del medio después de ordenarlos en orden si M es
impar. O es el promedio de los dos números del medio si M es par. Empiezas con un vacío
lista de números Luego, puede agregar números a la lista o eliminar los números existentes. Después
cada operación de agregar o quitar, genera la mediana.

Ejemplo:
Para un conjunto de M = 5 números 9, 2, 8, 4, 1, la mediana es el tercer número en el conjunto ordenado 1, 2,
4, 8, 9, que es 4. Del mismo modo, para un conjunto de M = 4 números, 5, 2, 10, 4, la mediana es el
promedio del segundo y tercer elemento en el conjunto ordenado 2, 4, 5, 10, que es (4 + 5) / 2 = 4.5.

/************** TODO: *************/

Input:
La primera línea es un número entero, N, que indica el número de operaciones.
Cada uno de los próximos N las líneas son a x o r x:

1. a x indica que x se agrega al conjunto
2. r x indica que x es eliminado del conjunto.

Output:
Para cada operación: si la operación es agregar, genera la mediana después de agregar x en una sola línea.
Si la operación es eliminar y el número x no está en la lista, la salida ¡Incorrecto! En una sola línea. Si
la operación es eliminar y el número x está en la lista, muestra la mediana después de eliminar x en
Una sola línea. (Si el resultado es un entero, NO envíe el punto decimal. Y si el resultado es un
número real, NO muestre ceros finales).

Nota: Si su mediana es 3.0, imprima solo 3. Y si su mediana es 3.50, imprima solo 3.5. Cuando
necesita imprimir la mediana y la lista está vacía, imprima Wrong

Restricciones:
1. 0 < N <= 10**5

Para cada a x o r x, x siempre será un entero con signo (que se ajustará en 32 bits).

Sample Input:

7
r1
a1
a2
a1
r1
r2
r1

Sample Output:

Wrong!
1
1,5
1
1,5
1
Wrong!

Nota: Como es evidente desde la última línea de la entrada, si después de la operación de eliminación
la lista se convierte vacío, tienes que imprimir Wrong!
'''

from Median import Median

if __name__ == "__main__":

    MAX_OPERACIONES = 10**5  # Numero de operaciones permitidas por el usuario

    try:
        # Se pide el numero de operaciones al usuario
        number_of_operations = int(
            input('Ingrese el numero de operaciones que desea realizar: '))

        if number_of_operations >= 0:
            if number_of_operations <= MAX_OPERACIONES:

                # instanciacion de la clase Median
                median = Median()

                for _ in range(number_of_operations):

                    operation_with_number = input(
                        'ingrese la operacion y el numero ejemplo: r1 > ')

                    ''' 
                    El bloque if not median.validate_operation(operation_with_number):
                    tiene la finalidad de llamar recursivamente la funcion en caso
                    de que la operacion no se encuentre entre las validas
                    '''

                    if not median.validate_operation(operation_with_number):
                        operation_with_number = input(
                            'Ingrese una operacion valida > ')
                        median.validate_operation(operation_with_number)
            else:
                print('el numero de operaciones es mayor de lo permitido')
        else:
            print('el numero de operaciones es menor o igual a 0')

    except ValueError:
        print('Inserte un valor numerico')
