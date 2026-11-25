class HeapMedicos:
    def __init__(self):
        self.heap = []

    def mostrar(self):
        print(self.heap)


    def inserir(self, id, atendimentos=0, ultima_atribuicao=0):
        for medico in self.heap:
            if medico[2] == id:
                return False

        medico = [atendimentos, ultima_atribuicao, id]
        self.heap.append(medico)

        posicao = len(self.heap) - 1

        while posicao > 0:
            pai = (posicao - 1) // 2

            if self.heap[posicao] < self.heap[pai]:
                self.heap[posicao], self.heap[pai] = self.heap[pai], self.heap[posicao]
                posicao = pai
            else:
                break

        return True
