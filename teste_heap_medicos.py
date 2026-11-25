
from heap_medicos import HeapMedicos

print("1- Inserindo medicos")

fila = HeapMedicos()

fila.inserir(101, 3, 5)
fila.inserir(102, 1, 8)
fila.inserir(103, 2, 3)

fila.mostrar()

print("Medico duplicado:", fila.inserir(102, 1, 8))
