import numpy as np
from DFS import dfs
from utils.graph import Graph

class BaldeTinta:
    
    @staticmethod
    def FloodFill(grafo, v_inicial, nova_cor):
        """ Converte a matriz em grafo, executa o DFS e retorna o grafo modificado """
        
        cor_inicial = grafo.get_color(v_inicial)

        if cor_inicial == nova_cor:
            return grafo  # Se já for da cor desejada, não precisa modificar

        visitados = set()
        dfs(grafo, v_inicial, cor_inicial, nova_cor, visitados)

        return grafo
