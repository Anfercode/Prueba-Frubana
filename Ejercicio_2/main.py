
'''
Problema:

Se le da un árbol sin raíz de n nodos numerados del 1 al n. cada nodo tiene un color C Sub i
Sea d(i,j) el número de colores diferentes en la ruta entre el nodo i y el nodo j. por
cada nodo i , calcular el valor de la sumatoria de d(i,j)

Tu tarea es imprimir el valor de sumatoria de d(i,j) para cada nodo 1 ≤ i ≤ n.

Restricciones

1 ≤ nodes ≤ 10**5
1 ≤ colour_nodes ≤ 10**5

Sample Input

5
1 2 3 2 3
1 2
2 3
2 4
1 5

Sample Output

10
9
11
9
12
'''

from Graph import Graph

if __name__ == "__main__":

    MAX_OF_NODES = 10**5
    MAX_OF_COLOURS = 10**5

    print(
        f'''Ingrese el numero de nodos que contendra el grafo
(el numero de grafos no puede ser mayor a {MAX_OF_NODES}):
        ''')
    number_of_nodes = int(input('=> '))

    print(
        f'''Ingrese los colores de los nodos separados por un espacio
(El numero de colores no puede ser mayor a {number_of_nodes})
ejemplo: 1 2 3 4 5
        ''')
    colour_of_nodes = input('=> ')

    graph = Graph(number_of_nodes)

    if number_of_nodes <= MAX_OF_NODES:
        if number_of_nodes > 0:
            if number_of_nodes == len(colour_of_nodes.split(' ')):

                graph.define_nodes_colour(colour_of_nodes)

                print('Ingrese las relaciones separadas por un espacio Ej: 1 2')

                for _ in range(number_of_nodes - 1):
                    while True:
                        relation_of_nodes = input('=> ').split()
                        if len(relation_of_nodes) == 2:
                            graph.define_relation(relation_of_nodes)
                            break
                        else:
                            print('Ingrese la relacion como corresponde')

                print('/*********Resultados**********/')

                for i in range(number_of_nodes):
                    print('=>', graph.graph_sum(i))
            else:
                print(
                    'El numero de colores ingresados es mayor o menor que el numero de nodos')
        else:
            print('El numero debe ser de nodos debe ser mayor a 0')
    else:
        print(f'El numero de nodos no debe ser mayor {MAX_OF_NODES}')
