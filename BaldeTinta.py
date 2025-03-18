from DFS import dfs

class BaldeTinta:
    
    @staticmethod
    def FloodFill(grafo, v_inicial, nova_cor):
        
        cor_inicial = grafo.get_color(v_inicial)

        if cor_inicial == nova_cor:
            return grafo

        visitados = set()
        dfs(grafo, v_inicial, cor_inicial, nova_cor, visitados)

        return grafo
