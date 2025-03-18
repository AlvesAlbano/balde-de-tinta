from utils.stack import Stack

def dfs(grafo, v, cor_inicial, nova_cor, visitados):
    pilha = Stack()
    pilha.push(v)

    while not pilha.is_empty():
        vertice = pilha.pop()
        
        if vertice in visitados:
            continue  # Ignora se já foi visitado

        visitados.add(vertice)  # Marca como visitado
        grafo.set_color(vertice, nova_cor)

        # Adiciona os vizinhos que têm a mesma cor inicial na pilha
        for vizinho in grafo.adj[vertice]:
            if grafo.get_color(vizinho) == cor_inicial and vizinho not in visitados:
                pilha.push(vizinho)
