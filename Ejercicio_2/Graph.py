import collections


class Graph:
    nodes = list()
    relations = dict()

    def __init__(self, number_of_nodes):
        """
        * Descripcion:
        * Este es el metodo constructor de la clase Graph
        *
        * parametros:
        * @param number_of_nodes: El atributo que contiene el numero de nodos que va a tener el grafo
        """
        self.number_of_nodes = number_of_nodes
        self.relations = {i: [] for i in range(self.number_of_nodes)}

    def define_nodes_colour(self, colour_of_nodes):
        """
        * Descripcion:
        * metodo se encargado de asignar los colores a los nodos
        *
        * Parametros:
        * @param colour_of_nodes: El atributo del color del nodo
        """
        self.nodes = colour_of_nodes.split(' ')

    def define_relation(self, relation_of_nodes):
        """
        * Descripcion:
        * Metodo encargado de realizar las relaciones entre los nodos
        *
        * Parametros:
        * @param relation_of_nodes: El atributo encargado de tomar una lista con las relaciones 1 a 1 de los nodos
        """
        node_one, node_two = [int(i) - 1 for i in relation_of_nodes]
        if node_one < (self.number_of_nodes) and node_two < (self.number_of_nodes):
            self.relations[node_one].append(node_two)
            self.relations[node_two].append(node_one)
        else:
            print(
                'La relacion no se pudo realizar porque alguno de los nodos relacionados no existe en el grafo')
            correction = input('=> ').split()
            self.define_relation(correction)

    def graph_sum(self, number_of_node):
        """
        * Descripcion:
        * Metodo encargado de realizar la suma cuando los colores de los nodos son diferentes
        *
        * Parametros:
        * @param number_of_node: Atributo del numero del nodo del grafo
        *
        * Return: Retorna la suma de los colores de los nodos cumpliendo con la logica del color diferente
        """

        result = 0

        processed = {number_of_node}
        deque_nodes = collections.deque(
            [(number_of_node, {self.nodes[number_of_node]})])

        while deque_nodes:
            node, node_relation = deque_nodes.popleft()

            result += len(node_relation)

            for i in self.relations[node]:
                if i not in processed:
                    processed.add(i)
                    deque_nodes.append((i, node_relation | {self.nodes[i]}))

        return result
