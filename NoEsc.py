 # ! Esse código é o nó do processador do problema de escalonamento de tarefas
from No import No
import copy

class NoProcessador(No):
    def __init__(self, dados, caminho=None):
        super().__init__(dados, caminho)
        self.Dados = dados  # Dados representa o estado atual do escalonamento
        self.Caminho = caminho if caminho else []
        self.Custo = self.calculaCusto()  # Adicione esta linha


    def calculaHeuristica(self):
        # número total de tarefas não escalonadas ainda
        return sum(1 for tarefa in self.Dados if tarefa['processador'] is None)

    def calculaCusto(self):
        # O custo pode ser o tempo total de execução das tarefas já escalonadas
        # se escalonou, custo +=1
        return sum(tarefa['tempo'] for tarefa in self.Dados if tarefa['processador'] is not None)

    def nosFilhos(self):
        lista = []
        for i, tarefa in enumerate(self.Dados):
            if tarefa['processador'] is None:
                for processador in range(2):  # Supondo que temos 2 processadores p0 e p1
                    novos_dados = copy.deepcopy(self.Dados)
                    novos_dados[i]['processador'] = processador
                    lista.append(NoProcessador(novos_dados, self.Caminho + [self]))
        return lista
    
    def printarCaminho(self, Visitados: list):
        print("Solução: ")
        for no in self.Caminho:
            print(no.Dados)  # Imprime as tarefas
        print()
        print(f'Número de nós visitados: {len(Visitados)}')
        print(f'Profundidade: {len(self.Caminho) - 1}')
        print(f'Custo Total: {self.calculaCustoCaminho()}')

    def verificarFinal(self):
        return all(tarefa['processador'] is not None for tarefa in self.Dados)
    
