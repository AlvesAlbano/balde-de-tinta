def dfs(grafo, v, cor_inicial, nova_cor, visitados):
    stack = [v]  # Pilha para controlar a visitação

    while stack:
        vertice = stack.pop()  # Remove o último elemento da pilha
        
        if vertice in visitados:
            continue  # Se já foi visitado, ignora

        visitados.add(vertice)  # Marca como visitado
        grafo.set_color(vertice, nova_cor)  # Pinta o nó

        # Adiciona os vizinhos que têm a mesma cor inicial na pilha
        for vizinho in grafo.adj[vertice]:
            if grafo.get_color(vizinho) == cor_inicial and vizinho not in visitados:
                stack.append(vizinho)
