
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

fila = HeapBinario()

fila.inserir(3,870,101)
fila.inserir(1, 875,102)
fila.inserir(2,860, 103)

fila.mostrar()
