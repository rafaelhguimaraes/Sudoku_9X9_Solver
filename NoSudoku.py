from No import No
import copy
import math

class NoSudoku(No):

  def __init__(self, Dados: list, Caminho: list):
    super().__init__(Dados, Caminho)

  # Calcula g(h), que é o número de zeros na linha e coluna do valor adicionado
  def calculaHeuristica(self):
    h = 0
    n = len(self.Dados)
    for i in range(n):
      for j in range(n):
        if self.Dados[i][j] == 0:
          h +=4
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

            # for l in range(subgrade_linha, subgrade_linha + m):
            #     for c in range(subgrade_coluna, subgrade_coluna + m):
            #         if self.Dados[l][c] == self.Dados[i][j] and i != l and j != c and self.Dados[l][c] != 0:
            #             teste = False

            # # Se poder colocar um número X nessa posição, adicionar um Novo Nó filho
            # if teste == True:
            #   temp = copy.deepcopy(self.Dados)
            #   temp[i][j] = x
            #   lista.append(NoSudoku(temp, self.Caminho))

    return lista

  # Verifica se não tem nenhum 0 na Matriz
  def verificarFinal(self):
    if any(0 in l for l in self.Dados):
      return False
    return True