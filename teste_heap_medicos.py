
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
