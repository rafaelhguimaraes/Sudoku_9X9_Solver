from No import No
from NoSudoku import NoSudoku

def profundidadeIterativa(noRaiz: No) -> bool:
    profundidade_maxima = 0
    Visitados = []
    while True:

        resultado = buscaEmProfundidadeLimitada(noRaiz, profundidade_maxima, Visitados)
        if resultado == True:
            return True

        profundidade_maxima += 1

def buscaEmProfundidadeLimitada(noRaiz: No, profundidade_maxima: int, Visitados: list) -> str:
    if profundidade_maxima < 0:
        return False

    if noRaiz.verificarFinal():
        noRaiz.printarCaminho(Visitados)
        return True

    if profundidade_maxima == 0:
        return False

    for filho in noRaiz.nosFilhos():
        Visitados.append(filho)
        resultado = buscaEmProfundidadeLimitada(filho, profundidade_maxima - 1, Visitados)
        if resultado == True:
            return True

    return False

def custoUniforme(noRaiz: No) -> bool:
        # Fila de prioridade com os Nós em relação ao seu Custo
        Fila = [noRaiz]

        # Lista com os Nós já visitados
        Visitados = []

        # Enquanto tem nós para visitar
        while Fila:

            # Pega o primeiro valor da Fila (Maior prioridade, ou seja, menor custo)
            noAtual = Fila.pop(0)
            Visitados.append(noAtual.Dados)

            # Verifica se achou a solução final
            if noAtual.verificarFinal() and not Fila or not noAtual.calculaCustoCaminho() > Fila[0].calculaCustoCaminho():
                noAtual.printarCaminho(Visitados)
                return True

            Filhos = noAtual.nosFilhos()

            for i in range(len(Filhos)):
              if Filhos[i].Dados not in Visitados:
                Fila.append(Filhos[i])
                Visitados.append(Filhos[i].Dados)

            Fila = sorted(Fila, key=lambda x: (x.calculaCustoCaminho()))
        return False

def aStar(noRaiz: No) -> bool:
        Fila = [noRaiz]

        Visitados = []
        while Fila:

            noAtual = Fila.pop(0)
            Visitados.append(noAtual.Dados)

            if noAtual.verificarFinal() and not Fila or not noAtual.calculaCustoCaminho() > Fila[0].calculaCustoCaminho():
                noAtual.printarCaminho(Visitados)
                return True

            Filhos = noAtual.nosFilhos()

            for i in range(len(Filhos)):
              if Filhos[i].Dados not in Visitados:
                Fila.append(Filhos[i])
                Visitados.append(Filhos[i].Dados)

            Fila = sorted(Fila, key=lambda x: (x.calculaCustoCaminhoHeuristico()))
        return False

noRaiz = NoSudoku([
    [2, 1, 4, 0],
    [0, 0, 0, 2],
    [0, 2, 0, 1],
    [0, 3, 2, 0]
], [])

Teste = custoUniforme(noRaiz)
print(Teste)