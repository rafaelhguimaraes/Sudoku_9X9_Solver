 # ! Esse código é o nó do processador do problema de escalonamento de tarefas
from No import No
import copy

class NoProcessador(No):
    
    Custo: int
    Heuristica: int
    def __init__(self, Dados: list, Caminho: list, Config: list):
        self.Dados = Dados
        if Caminho is None:
            self.Caminho = [self]
        else:
            self.Caminho = Caminho + [self]
        self.Config = Config
        

    def calculaHeuristica(self):
        return 1

    def calculaCusto(self):
        return 0
    
    def calculaCustoCaminho(self):
        return max((par[2] for processador in self.Dados for par in processador if par), default=0)
    
    def calculaCustoCaminhoHeuristico(self):
        return self.calculaCustoCaminho() + self.Heuristica
         
    def nosFilhos(self):
        lista = []

        for tarefa in self.Config:
            teste = True
            for processador in self.Dados:
                for T in processador:
                    if tarefa['id'] == T[0]:
                        teste = False
                        break
            if teste:
                dependencias = copy.deepcopy([par for par in tarefa['dependencias']])
                d = len(dependencias)
                minimo = 0
                h = 10000000
                for processador in self.Dados:
                    for T in processador:
                        for par in dependencias:
                            if T[0] == par[0]:
                                if T[2] > minimo:
                                    minimo = T[2]
                                    if par[1] < h:
                                        h = par[1]
                                d -= 1
                if h == 10000000:
                    h = 0
                if d == 0:
                    for processador in self.Dados:
                        x, y = 0,0
                        if len(processador) == 0:
                            if minimo == 0:
                                x = 0
                                y = tarefa['tempo']
                            else:
                                x = minimo
                                y = minimo + tarefa['tempo']
                        elif processador[-1][2] >= minimo:
                            x = processador[-1][2]
                            y = processador[-1][2]+tarefa['tempo']
                        else:
                            x = minimo
                            y = minimo + tarefa['tempo']
                        processador.append([tarefa['id'], x, y])
                        prs = copy.deepcopy(self.Dados)
                        novoNo = NoProcessador(prs, self.Caminho, self.Config)
                        novoNo.Custo= tarefa['tempo']
                        novoNo.Heuristica = h
                        lista.append(novoNo)
                        processador.pop()
        return lista
    
    def printarCaminho(self, Visitados: list):
        print("Solução: ")
        for no in self.Caminho:
            print(no.Dados)  # Imprime as tarefas
            print("-----------------------------------------------------")
        print()
        print(f'Número de nós visitados: {len(Visitados)}')
        print(f'Profundidade: {len(self.Caminho) - 1}')
        print(f'Custo Total: {self.calculaCustoCaminho()}')

    def verificarFinal(self):
        print(sum(len(processador) for processador in self.Dados))
        if len(self.Config) == sum(len(processador) for processador in self.Dados):
            return True
        else:
            return False
    
