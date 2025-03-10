"""
   Execution:    python graph.py input.txt
   Dependencies: Bag.java Stack.java In.java StdOut.java
   Data files:   https://algs4.cs.princeton.edu/41graph/tinyG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumG.txt
                 https://algs4.cs.princeton.edu/41graph/largeG.txt
 
   A graph, implemented using an array of sets.
   Parallel edges and self-loops allowed.
 
   % python graph.py < tinyG.txt
   13 vertices, 13 edges 
   0: 6 2 1 5 
   1: 0 
   2: 0 
   3: 5 4 
   4: 5 6 3 
   5: 3 4 0 
   6: 0 4 
   7: 8 
   8: 7 
   9: 11 10 12 
   10: 9 
   11: 9 12 
   12: 11 9 
 
   % python graph.py < mediumG.txt
   250 vertices, 1273 edges 
   0: 225 222 211 209 204 202 191 176 163 160 149 114 97 80 68 59 58 49 44 24 15 
   1: 220 203 200 194 189 164 150 130 107 72 
   2: 141 110 108 86 79 51 42 18 14 
   ...
 """
from utils.bag import Bag


class Graph:

    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = {}
        self.colors = {}
        for v in range(self.V):
            self.adj[v] = Bag()

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w)
                                               for w in self.adj[v])) for v in range(self.V))
        return s

    def set_color(self, v, color):
        self.colors[v] = color

    def get_color(self, v):
        return self.colors.get(v, None)

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        max_deg = 0
        for v in self.V:
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count

    def matrix_to_graph(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                node = i * cols + j  # Índice do nó no grafo
                self.set_color(node, matrix[i][j])  # Salva a cor do pixel

                # Conectar apenas vizinhos com a mesma cor
                #neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direções: direita, abaixo, esquerda, acima
                neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)] # + Diagonais

                for di, dj in neighbors:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:  # Dentro dos limites da matriz
                        neighbor = ni * cols + nj
                        if matrix[ni][nj] == matrix[i][j]:  # Apenas conecta se a cor for a mesma
                            self.add_edge(node, neighbor)

if __name__ == '__main__':
    import sys

    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    g = Graph(V)
    for i in range(E):
        v, w = sys.stdin.readline().split()
        g.add_edge(v, w)
    print(g)
