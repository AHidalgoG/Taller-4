class Node:

    # se crea la clase nodo
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1
        self.highlighted = False

    #Metodo para obtener el factor de balance
    def balance_factor(self):
        # Se obtiene la altura de los nodos hijos
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        # Se calcula el factor de balance
        return left_height - right_height
    


class AVL:

    # se crea la clase arbol AVL
    def __init__(self):
        self.root = None
        self.size = 0

    #Metodo para quitar el resaltado de todos los nodos
    def unhighlight_all(self, node):
        if node is not None:
            node.highlighted = False
            self.unhighlight_all(node.left)
            self.unhighlight_all(node.right)

# se crean los metodos de la clase arbol AVL

    #Metodo para obtener la altura de un nodo
    def newHeight(self, node):
        while node is not None:
            height_left = node.left.height if node.left else 0
            height_right = node.right.height if node.right else 0
            node.height = 1 + max(height_left, height_right)
            node = node.parent

    #Metodo para agregar un nodo al arbol
    def add(self, value):
        new_node = Node(value)
        # Se crea la raíz si no existe
        if self.root is None:
            self.root = new_node
        else:
            # Se busca la posición para agregar el nuevo nodo
            node = self.root
            while node is not None:
                # Se agrega el nodo a la izquierda si el valor es menor
                if value < node.value:
                    if node.left is None:
                        node.left = new_node
                        new_node.parent = node
                        break
                    else:
                        node = node.left
                # Se agrega el nodo a la derecha si el valor es mayor
                elif value > node.value:
                    if node.right is None:
                        node.right = new_node
                        new_node.parent = node
                        break
                    else:
                        node = node.right
                else:
                    break
        # Se actualiza la altura del nodo y se balancea el árbol
        self.newHeight(new_node)
        self.balance(new_node)

    #Metodo para buscar un nodo en el arbol
    def find(self, value):
        node = self.root
        self.unhighlight_all(self.root)  # Quitamos el resaltado de todos los nodos
        # Buscamos el nodo
        while node is not None:
            if value == node.value:
                node.highlighted = True  # Resaltamos el nodo encontrado
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None

    #Metodo para eliminar un nodo del arbol
    def delete(self, value):
        # Buscamos el nodo a eliminar
        node = self.root
        while node is not None:
            # Si encontramos el nodo
            if value == node.value:
                # Casos para eliminar el nodo

                if node.left is None and node.right is None:
                    # Si el nodo es una hoja
                    if node == self.root:
                        self.root = None
                    else:
                        # Si el nodo es hijo izquierdo
                        if node.parent.left == node:
                            node.parent.left = None
                        else:
                            # Si el nodo es hijo derecho
                            node.parent.right = None
                # Si el nodo tiene dos hijos
                elif node.left is not None and node.right is not None:
                    temp = node.right
                    while temp.left is not None:
                        # Buscamos el nodo más a la izquierda del subárbol derecho
                        temp = temp.left
                    node.value = temp.value
                    node = temp
                    if node.right:
                        # Si el nodo tiene hijo derecho
                        if node.parent.left == node:
                            node.parent.left = node.right
                        else:
                            node.parent.right = node.right
                        node.right.parent = node.parent
                    else:
                        # Si el nodo no tiene hijo derecho
                        if node.parent.left == node:
                            node.parent.left = None
                        else:
                            # Si el nodo es hijo derecho
                            node.parent.right = None
                else:
                    # Si el nodo tiene un solo hijo
                    child = node.left if node.left else node.right
                    # Si el nodo es la raíz
                    if node == self.root:
                        self.root = child
                    else:
                        # Si el nodo es hijo izquierdo
                        if node.parent.left == node:
                            node.parent.left = child
                        else:
                            # Si el nodo es hijo derecho
                            node.parent.right = child
                    # Asignamos el padre al hijo
                    if child is not None:
                        child.parent = node.parent

                # Balanceamos el árbol
                if node.parent:
                    self.newHeight(node.parent)
                    self.balance(node.parent)
                break
            elif value < node.value:
                node = node.left
            else:
                node = node.right

    # Método para balancear el árbol
    def balance(self, node):
        while node is not None:
            # Se actualiza la altura del nodo
            self.newHeight(node)
            # Se calcula el factor de balance
            balance_factor = node.balance_factor()
            # Se balancea el nodo
            if balance_factor > 1:
                # Rotaciones simples y dobles izquierdas
                if node.left.balance_factor() < 0:
                    self.left_R(node.left)
                self.right_R(node)
            elif balance_factor < -1:
                # Rotaciones simples y dobles derechas
                if node.right.balance_factor() > 0:
                    self.right_R(node.right)
                self.left_R(node)
            node = node.parent

    # Método de rotación a la izquierda
    def left_R(self, node):
        newRoot = node.right
        if newRoot is None:
            return
        node.right = newRoot.left
        if newRoot.left:
            newRoot.left.parent = node
        newRoot.parent = node.parent
        if node == self.root:
            self.root = newRoot
        elif node == node.parent.left:
            node.parent.left = newRoot
        else:
            node.parent.right = newRoot
        newRoot.left = node
        node.parent = newRoot
        self.newHeight(node)
        self.newHeight(newRoot)

    # Método de rotación a la derecha
    def right_R(self, node):
        newRoot = node.left
        if newRoot is None:
            return
        node.left = newRoot.right
        if newRoot.right:
            newRoot.right.parent = node
        newRoot.parent = node.parent
        if node == self.root:
            self.root = newRoot
        elif node == node.parent.right:
            node.parent.right = newRoot
        else:
            node.parent.left = newRoot
        newRoot.right = node
        node.parent = newRoot
        self.newHeight(node)
        self.newHeight(newRoot)

    #Rotacion doble izquierda derecha
    def double_left_R(self, node):
        self.right_R(node.left)
        self.left_R(node)

    #Rotacion doble derecha izquierda
    def double_right_R(self, node):
        self.left_R(node.right)
        self.right_R(node)

#Metodos para recorrer el arbol

# Metodos para recorrer el arbol

    # Recorrido en inorden
    def in_order(self, node):
        if node is None:
            return []

        return self.in_order(node.left) + [node.value] + self.in_order(node.right)


    # Recorrido en preorden
    def pre_order(self, node):
        if node is None:
            return []

        return [node.value] + self.pre_order(node.left) + self.pre_order(node.right)


    # Recorrido en postorden
    def post_order(self, node):
        if node is None:
            return []

        return self.post_order(node.left) + self.post_order(node.right) + [node.value]

    #Metodo para obtener la raiz del arbol
    def get_root(self):
        return self.root
    



