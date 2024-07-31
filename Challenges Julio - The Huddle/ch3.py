#Challenge 3 --- THE HUDDLE -JULIO

# Recorrido en profundidad (DFS): 
# Implementa un recorrido DFS para un grafo simple con 5 nodos.

#Creamos una clase Nodo
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self): #Esta función define cómo se verá el objeto cuando lo imprimamos.(Para representacion)
        return "Node(" + str(self.value) + ")" #Cuando imprimimos el objeto, devuelve una cadena que representa el nodo, mostrando su valor.

    # Método para realizar el recorrido en profundidad (DFS)
    def dfs(self):
        print(self)  #Imprimimos el valor del nodo actual
        if self.left:
            self.left.dfs()  # Recorrido en profundidad del subárbol izquierdo, llamando a la funcion recursivamente
        if self.right:
            self.right.dfs()  # Recorrido en profundidad del subárbol derecho, llamando a la funcion recursivamente


# Definición del árbol

# A tiene dos hijos: B y D
# B tiene de hijo a C
# D tiene de hijo a E

tree = Node('A', Node('B', Node('C')), Node('D', Node('E'))) #Llamamos a la clase Nodo y le agregamos los valores y los nodos hijos

# Llamamos al método dfs para realizar el recorrido DFS
tree.dfs()


# Otra manera de creacion del arbol
# Crear los nodos individualmente
# nodoC = Node('C')---> #C es hijo de B
# nodoB = Node('B', left=nodoC)---> #B es hijo de A
# nodoE = Node('E')---> # E es hijo de D
# nodoD = Node('D', right=nodoE)---> #D es hijo de A
# nodoA = Node('A', left=nodoB, right=nodoD)---> # A nodo inicial, con dos hijos: B y D

# Recorrer el árbol usando DFS
# Aca solo llamariamos al nodo A y asi èste usa a los hijos y los hijos llaman a sus hijos:
# nodoA.dfs()