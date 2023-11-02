from No import No
from NoSudoku import NoSudoku
from NoEsc import NoProcessador
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

def subidaDeEncosta(x0: No, Maximo = 300) -> bool:
    x0.criarInicioSubidaDeEncosta()
    noAtual = x0  
    melhorSolucao = x0
    Movimentos = 0
    Visitados = []

    while True:

        Vizinhos = noAtual.gerarVizinhos()
        melhorVizinho = max(Vizinhos, key= lambda x: x.funcaoAvaliacao())
        Visitados.extend(Vizinhos)

        if melhorVizinho.funcaoAvaliacao() <= noAtual.funcaoAvaliacao():
            if noAtual.verificarFinalSubidaDeEncosta() or Movimentos == Maximo:
                if melhorSolucao.funcaoAvaliacao() <= noAtual.funcaoAvaliacao():
                     melhorSolucao = noAtual
                melhorSolucao.printarCaminho(Visitados)
                if noAtual.verificarFinalSubidaDeEncosta():
                    return True
                return False
            else:
                if melhorSolucao.funcaoAvaliacao() <= noAtual.funcaoAvaliacao():
                    melhorSolucao = noAtual
                # Escolhe aleatoriamente um novo nível da árvore para fazer a busca
                noAtual = random.choice(Vizinhos)
                Movimentos += 1
                continue
        noAtual = melhorVizinho  

noRaiz = NoSudoku([
    #? Médio 1 = 50% de zeros
    # [2, 1, 0, 0],
    # [0, 0, 0, 2],
    # [0, 2, 0, 0],
    # [0, 0, 2, 0]
    #? Médio 2
    # [0, 0, 0, 0],
    # [1, 0, 3, 0],
    # [4, 3, 1, 0],
    # [2, 0, 0, 0]
    # [1,0,0,0],
    # [0,2,0,0],
    # [0,0,3,0],
    # [0,0,0,4]
    #! Difícil
    # [0,0,0,3],
    # [0,4,0,0],
    # [0,0,3,2],
    # [0,0,0,0]
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
], [])
Teste = subidaDeEncosta(noRaiz)
print(Teste)

#!  Definindo as tarefas para teste
# tarefas = [
#     {'id': 1, 'tempo': 10, 'processador': None, 'dependencias': []},
#     {'id': 2, 'tempo': 15, 'processador': None, 'dependencias': []},
#     {'id': 3, 'tempo': 20, 'processador': None, 'dependencias': []},
#     {'id': 4, 'tempo': 30, 'processador': None, 'dependencias': []},
#     {'id': 5, 'tempo': 40, 'processador': None, 'dependencias': []},
#     {'id': 6, 'tempo': 50, 'processador': None, 'dependencias': []},
#     {'id': 7, 'tempo': 60, 'processador': None, 'dependencias': []},
#     {'id': 8, 'tempo': 70, 'processador': None, 'dependencias': []},
#     {'id': 9, 'tempo': 80, 'processador': None, 'dependencias': []},
#     {'id': 10,'tempo':90,'processador' :None,'dependencias':[5 ,6]}
# ]


# noRaiz = NoProcessador(tarefas)
# buscaProfundidadeIterativa(noRaiz)
# buscaAstar(noRaiz)
# buscaGulosa(noRaiz)

