class TabelaHash:
    def __init__(self):
        self.tamanho = 5
        self.tabela = [[] for i in range(self.tamanho)]
        
    def funcao_hash(self, id):
        return id % self.tamanho

    def inserir(self, id, nome):
        indice = self.funcao_hash(id)

        for paciente in self.tabela[indice]:
            if paciente[0] == id:
                print(f"Paciente com ID {id} já existe.")
                return

        self.tabela[indice].append([id, nome])

    def buscar(self, id):
        indice = self.funcao_hash(id)
        for paciente in self.tabela[indice]:
            if paciente[0] == id:
                return paciente 
        return None

paciente = TabelaHash()

paciente.inserir(101, "Ana")
paciente.inserir(102, "Bruno")

print(paciente.tabela)
print(paciente.buscar(101))
print(paciente.buscar(102))
print(paciente.buscar(103))