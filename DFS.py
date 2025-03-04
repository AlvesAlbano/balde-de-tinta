def dfs(graph, vertice, cor_inicial, nova_cor, visitados):
    stack = [vertice]  # Pilha para controlar a visitação

    while stack:
        v = stack.pop()  # Remove o último elemento da pilha
        
        if v in visitados:
            continue  # Se já foi visitado, ignora

        visitados.add(v)  # Marca como visitado
        graph.set_color(v, nova_cor)  # Pinta o nó

        # Adiciona os vizinhos que têm a mesma cor inicial na pilha
        for vizinho in graph.adj[v]:
            if graph.get_color(vizinho) == cor_inicial and vizinho not in visitados:
                stack.append(vizinho)
