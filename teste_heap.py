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


print("6- Atualizando prioridade")

fila5 = HeapBinario()
fila5.inserir(4, 800, 101)
fila5.inserir(2, 810, 102)
fila5.inserir(3, 820, 103)

print("Antes:")
fila5.mostrar()

print("Atualizou:", fila5.atualizar_prioridade(101, 1))
print("Depois de ficar mais urgente:")
fila5.mostrar()

print("Atualizou:", fila5.atualizar_prioridade(101, 5))
print("Depois de ficar menos urgente:")
fila5.mostrar()

print("Paciente inexistente:", fila5.atualizar_prioridade(999, 1))
print("Prioridade invalida:", fila5.atualizar_prioridade(102, 8))


print("7- Removendo paciente por ID")

fila6 = HeapBinario()

fila6.inserir(3, 800, 101)
fila6.inserir(1, 810, 102)
fila6.inserir(2, 820, 103)

print("Antes:")
fila6.mostrar()

print("Removido:", fila6.remover_por_id(103))

print("Depois:")
fila6.mostrar()

print("ID inexistente:", fila6.remover_por_id(999))
print("Proximo paciente:", fila6.remover())



print("8- Testando ordem de remocao")

fila7 = HeapBinario()

fila7.inserir(3, 900, 101)
fila7.inserir(1, 850, 102)
fila7.inserir(2, 800, 103)
fila7.inserir(1, 800, 104)
fila7.inserir(1, 800, 100)

print("Ordem dos pacientes removidos:")

while len(fila7.heap) > 0:
    print(fila7.remover())



print("9- Remocao de paciente no meio da fila")

fila8 = HeapBinario()

fila8.inserir(1, 800, 101)
fila8.inserir(2, 810, 102)
fila8.inserir(3, 820, 103)
fila8.inserir(4, 830, 104)
fila8.inserir(5, 840, 105)

print("Paciente cancelado:", fila8.remover_por_id(103))

print("Pacientes restantes em ordem:")
while len(fila8.heap) > 0:
    print(fila8.remover())
