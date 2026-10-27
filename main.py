from Arbol_AVL import AVL
from typing import List, Optional, Tuple

arbolAVL = AVL()

#Prueba de inserción

datos: List[int] = [(50), (20), (70), (10), (30), (60), (80), (25), (40),]

for valor in datos:
    arbolAVL.add(valor)

#imprimir
print(arbolAVL.in_order(arbolAVL.root))

#eliminar
arbolAVL.delete(20)

#imprimir

print(arbolAVL.in_order(arbolAVL.root))