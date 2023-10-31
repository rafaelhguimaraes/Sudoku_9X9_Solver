from No import No
from NoSudoku import NoSudoku

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
            print(Fila[0].Dados)
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

noRaiz = NoSudoku([
    [2, 1, 4, 0],
    [0, 0, 0, 2],
    [0, 2, 0, 1],
    [0, 3, 2, 0]
], [])

Teste = buscaGulosa(noRaiz)
print(Teste)