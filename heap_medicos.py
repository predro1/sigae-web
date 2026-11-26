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

    def remover(self):
        if len(self.heap) == 0:
            return None

        medico_removido = self.heap[0]
        ultimo_medico = self.heap.pop()

        if len(self.heap) == 0:
            return medico_removido

        self.heap[0] = ultimo_medico
        posicao = 0

        while True:
            filho_esquerdo = 2 * posicao + 1
            filho_direito = 2 * posicao + 2
            menor = posicao

            if filho_esquerdo < len(self.heap):
                if self.heap[filho_esquerdo] < self.heap[menor]:
                    menor = filho_esquerdo

            if filho_direito < len(self.heap):
                if self.heap[filho_direito] < self.heap[menor]:
                    menor = filho_direito

            if menor == posicao:
                break

            self.heap[posicao], self.heap[menor] = self.heap[menor], self.heap[posicao]
            posicao = menor

        return medico_removido
