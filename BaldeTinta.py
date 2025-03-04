import numpy as np
from DFS import dfs
from utils.graph import Graph

class BaldeTinta:
    
    @staticmethod
    def FloodFill(matriz, x, y, nova_cor):
        """ Converte a matriz em grafo, executa o DFS e retorna o grafo modificado """
        
        rows, cols = len(matriz), len(matriz[0])
        grafo = Graph(rows * cols)
        grafo.matrix_to_graph(matriz)

        vertice_inicial = x * cols + y
        cor_inicial = grafo.get_color(vertice_inicial)

        if cor_inicial == nova_cor:
            return grafo  # Se já for da cor desejada, não precisa modificar

        visitados = set()
        dfs(grafo, vertice_inicial, cor_inicial, nova_cor, visitados)

        return grafo
