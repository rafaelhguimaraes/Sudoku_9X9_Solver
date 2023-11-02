 # ! Esse aqui é a classe Nó preparada pro Escalonamento de tarefas, classe MAE no.py
class No:
  def __init__(self, Dados: list, Caminho: list):
        if Caminho is None:
            Caminho = []
        self.Dados = Dados
        self.Caminho = Caminho + [self]

  def calculaCusto(self):
    pass

  def calculaHeuristica(self):
    pass

  # Calcula a soma dos Custos f(x) pelo caminho até chegar nesse nó Atual
  def calculaCustoCaminho(self):
    c = 0
    for no in self.Caminho[:-1]:
      c+= no.Custo
    return c

  # Calcula o Custo no caso que utiliza uma função heurística
  def calculaCustoCaminhoHeuristico(self):
    self.Heuristica = self.calculaHeuristica()
    return self.calculaCustoCaminho() + self.Heuristica

  def nosFilhos(self):
    pass

  def verificarFinal(self):
    pass

  def funcaoAvaliacao(self):
    pass
  
  def criarInicioSubidaDeEncosta(self):
    pass

  def gerarVizinhos(self):
    pass

def printarCaminho(self, Visitados: list):
    print("Solução: ")

    # Verifica se os dados são uma lista de dicionários (para NoProcessador)
    if isinstance(self.Dados[0], dict):
        for no in self.Caminho:
            print(no.Dados)  # Imprime as tarefas
    else:
        # Assume que os dados são uma matriz 2D (para NoSudoku)
        n = len(self.Dados)
        for i in range(n):
            for j in range(n):
                print(self.Caminho[0].Dados[i][j], end="   ")
            print()  # Pula para a próxima linha

        for no in self.Caminho[1:]:
            print("-->")
            for i in range(n):
                for j in range(n):
                    print(no.Dados[i][j], end="   ")
                print()

    # Printa outras informações
    print()
    print(f'Número de nós visitados: {len(Visitados)}')
    print(f'Profundidade: {len(self.Caminho) - 1}')
    print(f'Custo Total: {self.calculaCustoCaminho()}')