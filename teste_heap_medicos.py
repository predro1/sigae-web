
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
