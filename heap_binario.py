
class HeapBinario:
    def __init__(self):
        self.heap = []

    def mostrar(self):
        print(self.heap)


    def inserir(self, prioridade, id):
        paciente = [prioridade, id]
        self.heap.append(paciente)

fila = HeapBinario()

fila.inserir(3, 101)
fila.inserir(1, 102)
fila.inserir(2, 103)

fila.mostrar()
