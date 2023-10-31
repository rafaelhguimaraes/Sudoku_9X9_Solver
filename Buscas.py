from No import No
from NoSudoku import NoSudoku
import random

def buscaProfundidadeIterativa(noRaiz: No) -> bool:
    profundidade_maxima = 1
    Visitados = []
    while True:
        
        resultado = buscaProfundidadeLimitada(noRaiz, profundidade_maxima, Visitados)
        if resultado == True:
            return True

        profundidade_maxima += 1

def buscaProfundidadeLimitada(noRaiz: No, profundidade_maxima: int, Visitados: list) -> str:
    if profundidade_maxima < 0:
        return False
    
    Visitados.append(noRaiz)
    if noRaiz.verificarFinal():
        noRaiz.printarCaminho(Visitados)
        return True
    
    for filho in noRaiz.nosFilhos():
        resultado = buscaProfundidadeLimitada(filho, profundidade_maxima - 1, Visitados)
        if resultado == True:
            return True

    return False

def busca(noRaiz: No, func) -> bool:
        Fila = [noRaiz]

        Visitados = []
        Visitados.append(Fila[0].Dados)
        while Fila:
            noAtual = Fila.pop(0)
            if noAtual.verificarFinal():
                noAtual.printarCaminho(Visitados)
                return True

            Filhos = noAtual.nosFilhos()

            for i in range(len(Filhos)):
              if Filhos[i].Dados not in Visitados:
                Fila.append(Filhos[i])
                Visitados.append(Filhos[i].Dados)

            Fila = sorted(Fila, key= func)
        return False

def buscaAstar(noRaiz: No) -> bool:
    return busca(noRaiz, lambda x: x.calculaCustoCaminhoHeuristico())

def buscaUniforme(noRaiz: No) -> bool:
    return busca(noRaiz, lambda x: x.calculaCustoCaminho())

def buscaGulosa(noRaiz: No) -> bool:
    return busca(noRaiz, lambda x: x.calculaHeuristica())

def subidaDeEncosta(noRaiz: No):
    noAtual = noRaiz  
    while True:
        Vizinhos = noAtual.nosFilhos() 
        if not Vizinhos:
            print(noAtual.Dados)
            return True
        Melhor_Vizinho = max(Vizinhos, key= lambda x: x.calculaHeuristica())
        if Melhor_Vizinho.calculaHeuristica() >= noAtual.calculaHeuristica():  
            print(noAtual.Dados)
            return True
        noAtual = Melhor_Vizinho 

def hill_climbing(x0: No, max_moves=10):
    current_node = x0  # Solução inicial
    num_moves = 0

    while True:
        neighbors = current_node.nosFilhos()
        if not neighbors:
            print(current_node.Dados)
            return True

        best_neighbor = max(neighbors, key=lambda x: x.calculaHeuristica())
        if best_neighbor.calculaHeuristica() >= current_node.calculaHeuristica():
            print(current_node.Dados)
            if num_moves >= max_moves:
                return False  # Parar se atingir o limite de movimentos laterais
            else:
                # Faça um movimento lateral, escolhendo um vizinho aleatório
                current_node = random.choice(neighbors)
                num_moves += 1
        else:
            current_node = best_neighbor

noRaiz = NoSudoku([
    #? Médio 1
    # [2, 1, 4, 0],
    # [0, 0, 0, 2],
    # [0, 2, 0, 1],
    # [0, 3, 2, 0]
    #? Médio 2
    # [0, 0, 0, 0],
    # [1, 0, 3, 0],
    # [4, 3, 1, 0],
    # [2, 0, 0, 0]
    #! Difícil
    [0,0,0,3],
    [0,4,0,0],
    [0,0,3,2],
    [0,0,0,0]
], [])

Teste = buscaProfundidadeIterativa(noRaiz)
print(Teste)