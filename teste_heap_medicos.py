
from heap_medicos import HeapMedicos

print("1- Inserindo medicos")

fila = HeapMedicos()

fila.inserir(101, 3, 5)
fila.inserir(102, 1, 8)
fila.inserir(103, 2, 3)

fila.mostrar()

print("Medico duplicado:", fila.inserir(102, 1, 8))


print("2- Chamando medicos")

fila2 = HeapMedicos()

fila2.inserir(101, 3, 5)
fila2.inserir(102, 1, 8)
fila2.inserir(103, 2, 3)

print("Primeiro medico:", fila2.remover())
print("Segundo medico:", fila2.remover())
print("Terceiro medico:", fila2.remover())
print("Fila vazia:", fila2.remover())



print("3- Desempate entre medicos")

fila3 = HeapMedicos()

fila3.inserir(103, 2, 10)
fila3.inserir(102, 2, 5)
fila3.inserir(101, 2, 5)

print("Ordem de escolha:")

print(fila3.remover())
print(fila3.remover())
print(fila3.remover())



print("4- Medico ocupado")

fila4 = HeapMedicos()

fila4.inserir(101, 0, 0)
fila4.inserir(102, 0, 0)
fila4.inserir(103, 0, 0)

medico_ocupado = fila4.remover()

print("Medico em atendimento:", medico_ocupado)

print("Proximo medico:", fila4.remover())

print("Medico ocupado continua fora da fila:")
fila4.mostrar()



print("5- Medico voltando apos concluir atendimento")

fila5 = HeapMedicos()

fila5.inserir(101, 0, 0)
fila5.inserir(102, 0, 0)
fila5.inserir(103, 0, 0)

medico = fila5.remover()

print("Medico chamado:", medico)

medico[0] += 1
medico[1] = 1

fila5.inserir(medico[2], medico[0], medico[1])

print("Fila depois da conclusao:")
fila5.mostrar()

print("Proximo medico escolhido:", fila5.remover())



print("6- Medico voltando apos cancelamento")

fila6 = HeapMedicos()

fila6.inserir(101, 0, 0)
fila6.inserir(102, 0, 0)
fila6.inserir(103, 0, 0)

medico_cancelado = fila6.remover()

print("Medico chamado:", medico_cancelado)

medico_cancelado[1] = 1

fila6.inserir(
    medico_cancelado[2],
    medico_cancelado[0],
    medico_cancelado[1]
)

print("Fila depois do cancelamento:")
fila6.mostrar()

print("Proximo medico escolhido:", fila6.remover())



print("7- Todos os medicos ocupados")

fila7 = HeapMedicos()

fila7.inserir(101, 0, 0)
fila7.inserir(102, 0, 0)
fila7.inserir(103, 0, 0)

print("Primeiro medico:", fila7.remover())
print("Segundo medico:", fila7.remover())
print("Terceiro medico:", fila7.remover())

print("Tentando chamar outro medico:", fila7.remover())

print("Fila de medicos disponiveis:")
fila7.mostrar()



print("8- Balanceamento entre medicos")

fila8 = HeapMedicos()

fila8.inserir(101, 0, 0)
fila8.inserir(102, 0, 0)
fila8.inserir(103, 0, 0)

for numero in range(1, 7):
    medico = fila8.remover()

    print("Atendimento", numero, "- Medico:", medico[2])

    medico[0] += 1
    medico[1] = numero

    fila8.inserir(medico[2], medico[0], medico[1])

print("Fila depois dos atendimentos:")
fila8.mostrar()


print("9- Medicos com cargas diferentes")

fila9 = HeapMedicos()

fila9.inserir(101, 5, 10)
fila9.inserir(102, 2, 8)
fila9.inserir(103, 3, 5)
fila9.inserir(104, 1, 12)

print("Ordem de escolha:")

while len(fila9.heap) > 0:
    print(fila9.remover())



print("10- Chamada, cancelamento e conclusao")

fila10 = HeapMedicos()

fila10.inserir(101, 0, 0)
fila10.inserir(102, 0, 0)
fila10.inserir(103, 0, 0)

medico1 = fila10.remover()
print("Primeiro medico chamado:", medico1)

medico1[1] = 1
fila10.inserir(medico1[2], medico1[0], medico1[1])

print("Medico devolvido apos cancelamento")

medico2 = fila10.remover()
print("Segundo medico chamado:", medico2)

medico2[0] += 1
medico2[1] = 2
fila10.inserir(medico2[2], medico2[0], medico2[1])

print("Medico devolvido apos conclusao")

print("Proximo medico escolhido:", fila10.remover())

print("Fila restante:")
fila10.mostrar()
