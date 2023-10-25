class No:

  # Dados: Matriz, vetor e etc... Que tem os dados para o nó atual
  # Caminho: Contém o caminho percorrido até chegar nesse nó
  # Custo: f(x)
  # Heuristica: g(h)
  # CustoCaminho: Ca
  def __init__(self, Dados: list, Caminho: list):
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

  def custo_A_para_B(self):
    pass

  def printarCaminho(self, Visitados: list):

    # Printa todos os nós que passou
    print("Solução: ")
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


  def noPai(self):
    return self.Caminho[-1]