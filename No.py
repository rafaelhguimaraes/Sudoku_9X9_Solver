class No:

  # Dados: Matriz, vetor e etc... Que tem os dados para o nó atual
  # Caminho: Contém o caminho percorrido até chegar nesse nó
  # Custo: f(x)
  # Heuristica: g(h)
  # CustoCaminho: Ca
  def __init__(self, Dados: list, Caminho: list= []):
    self.Dados = Dados
    self.Caminho = Caminho + [self]
    self.Custo = self.calculaCusto()
    self.Heuristica = 0

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
    pass