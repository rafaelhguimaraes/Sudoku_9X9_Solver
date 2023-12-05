from No import No
import copy
import math
import numpy as np

class NoSudoku(No):

  f: int = 0 # Funcao Avaliacao
  # Calcula g(h), que é o número de zeros na linha e coluna do valor adicionado
  def calculaHeuristica(self):
    h = 0
    n = len(self.Dados)
    for i in range(n):
      for j in range(n):
        if self.Dados[i][j] == 0:
          h +=4
    self.Heuristica = h
    return h

  def calculaCusto(self):
    return 1

  def nosFilhos(self) -> list:
    lista = []
    n = len(self.Dados)
    m = int(math.sqrt(n)) # tamanho das subgrades

    # Ir dos números de 1 até 9
    for x in range(1,n + 1):

      # Pegar coluna e linha da matriz
      for i in range(n):
        for j in range(n):
          teste = True
          # Verificar se pode colocar um número naquela posição
          if(self.Dados[i][j] == 0):

            # Verificar se pode colocar nessa linha
            if x in self.Dados[i]:
              teste = False
            # Verificar se pode colocar nessa coluna
            if x in [self.Dados[l][j] for l in range(n)]:
              teste = False
            
            # Verificar se pode colocar na mesma subgrade
            
            subgrade_linha = (i // m) * m
            subgrade_coluna = (j // m) * m
            subgrade = [self.Dados[l][c] for l in range(subgrade_linha, subgrade_linha + m) for c in range(subgrade_coluna, subgrade_coluna + m)]

            if x in subgrade:
                        teste = False

            if teste:
                        temp = copy.deepcopy(self.Dados)
                        temp[i][j] = x
                        lista.append(NoSudoku(temp, self.Caminho))

    return lista

  # Verifica se não tem nenhum 0 na Matriz
  def verificarFinal(self):
    if any(0 in l for l in self.Dados):
      return False
    return True
  
  def funcaoAvaliacao(self):
    h = 0
    n = len(self.Dados)
    m = int(math.sqrt(n))
    Dados = np.array(self.Dados)
    for col in Dados.T:
      h += len(np.unique(col))
    for i in range(0, m):
        for j in range(0, m):
            sub = Dados[m*i:m*i+m, m*j:m*j+m]
            h += len(np.unique(sub))
    self.f = h
    return h

  def criarInicioSubidaDeEncosta(self):
    n = len(self.Dados)
    for i in range(n):
      for j in range(n):
        if self.Dados[i][j] == 0:
          for x in range(1, n + 1):
             if x not in self.Dados[i]:
                self.Dados[i][j] = x
                break

  def gerarVizinhos(self):
    n = len(self.Dados)
    lista = []
    for i in range(n):
     for j in range(n):
      for x in range(j+1, n):
        temp = copy.deepcopy(self.Dados)
        temp[i][j], temp[i][x] = temp[i][x], temp[i][j]
        lista.append(NoSudoku(temp, self.Caminho))
    return lista
    
  def verificarFinalSubidaDeEncosta(self):
    n = len(self.Dados)
    if self.f < n*n + n*n:
       return False
    return True
  
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