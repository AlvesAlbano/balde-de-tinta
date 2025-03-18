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
                node = i * cols + j
                self.set_color(node, matrix[i][j])

                # Conectar apenas vizinhos com a mesma cor
                # Manhattan
                #neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                # Chebyshev
                neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

                for di, dj in neighbors:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbor = ni * cols + nj
                        if matrix[ni][nj] == matrix[i][j]:
                            self.add_edge(node, neighbor)


