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


print("3- Removendo paciente mais urgente")

fila3 = HeapBinario()

fila3.inserir(3, 870, 101)
fila3.inserir(1, 875, 102)
fila3.inserir(2, 860, 103)

print("Paciente removido:", fila3.remover())
print("Fila depois da remocao:")
fila3.mostrar()


print("4- Removendo todos os pacientes")

print("Paciente removido:", fila3.remover())
print("Paciente removido:", fila3.remover())
print("Fila vazia:", fila3.remover())


print("5- Removendo de uma fila com um paciente")

fila4 = HeapBinario()
fila4.inserir(1, 800, 104)

print("Paciente removido:", fila4.remover())
fila4.mostrar()
