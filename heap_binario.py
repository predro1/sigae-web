
class HeapBinario:
    def __init__(self):
        self.heap = []

    def mostrar(self):
        print(self.heap)


    def inserir(self, prioridade,horario, id):
        paciente = [prioridade,horario, id]
        self.heap.append(paciente)

        posicao = len(self.heap) - 1

        while posicao > 0:
            pai = (posicao - 1) // 2

            if self.heap[posicao]< self.heap[pai]:
                self.heap[posicao], self.heap[pai] = self.heap[pai], self.heap[posicao]
                posicao = pai
            else:
                break

    def remover(self):
        if len(self.heap) == 0:
            return None

        paciente_removido = self.heap[0]
        ultimo_paciente = self.heap.pop()

        if len(self.heap) == 0:
            return paciente_removido

        self.heap[0] = ultimo_paciente
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

        return paciente_removido
