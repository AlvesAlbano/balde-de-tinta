class Matriz:
    
    def __init__(self, caminho: str):
        self.caminho = caminho
        self.matriz = self.ler_matriz()
    
    def get_dimensoes(self):
        """Obtém as dimensões da matriz (altura e largura) do arquivo."""
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            
        altura = len(linhas)
        largura = len(linhas[0].split())
        return altura, largura
    
    def ler_matriz(self):
        """Lê a matriz do arquivo e a preenche automaticamente."""
        altura, largura = self.get_dimensoes()
        matriz = [[None] * largura for _ in range(altura)]
        
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            for i, line in enumerate(arquivo):
                numeros = line.strip().split()
                matriz[i] = [int(num) for num in numeros]
                
        return matriz
    
    def to_string(self):
        """Converte a matriz em uma string formatada para exibição."""
        return "\n".join(" ".join(str(x) for x in row) for row in self.matriz)
    
    def print_matriz(self):
        """Imprime a matriz de forma formatada."""
        print(self.to_string())
