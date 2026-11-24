from heap_binario import HeapBinario

print("1- Inserindo pacientes na fila de prioridade:")

fila = HeapBinario()

fila.inserir(3,870,101)
fila.inserir(1, 875,102)
fila.inserir(2,860, 103)

fila.mostrar()

print("2- mesma prioridade")

fila2 = HeapBinario()


fila2.inserir(2, 900, 101)
fila2.inserir(2, 850, 102)
fila2.inserir(2, 850, 100)

fila2.mostrar()