
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


    
    def atualizar_prioridade(self, id, nova_prioridade):
        if nova_prioridade < 1 or nova_prioridade > 5:
            return False

        for i in range(len(self.heap)):
            if self.heap[i][2] == id:
                self.heap[i][0] = nova_prioridade
                posicao = i

                while posicao > 0:
                    pai = (posicao - 1) // 2

                    if self.heap[posicao] < self.heap[pai]:
                        self.heap[posicao], self.heap[pai] = self.heap[pai], self.heap[posicao]
                        posicao = pai
                    else:
                        break

                while True:
                    esquerdo = 2 * posicao + 1
                    direito = 2 * posicao + 2
                    menor = posicao

                    if esquerdo < len(self.heap):
                        if self.heap[esquerdo] < self.heap[menor]:
                            menor = esquerdo

                    if direito < len(self.heap):
                        if self.heap[direito] < self.heap[menor]:
                            menor = direito

                    if menor == posicao:
                        break

                    self.heap[posicao], self.heap[menor] = self.heap[menor], self.heap[posicao]
                    posicao = menor

                return True

        return False

    def remover_por_id(self, id):
        for i in range(len(self.heap)):
            if self.heap[i][2] == id:
                paciente_removido = self.heap[i]
                ultimo_paciente = self.heap.pop()

                if i == len(self.heap):
                    return paciente_removido

                self.heap[i] = ultimo_paciente
                posicao = i

                while posicao > 0:
                    pai = (posicao - 1) // 2

                    if self.heap[posicao] < self.heap[pai]:
                        self.heap[posicao], self.heap[pai] = self.heap[pai], self.heap[posicao]
                        posicao = pai
                    else:
                        break

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

        return None
