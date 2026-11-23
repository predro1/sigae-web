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

    def atualizar(self, id, novo_nome):
        indice = self.funcao_hash(id)

        for paciente in self.tabela[indice]:
            if paciente[0] == id:
                paciente[1] = novo_nome
                return
        print(f"Paciente com ID {id} não encontrado.")


    def remover(self, id):
        indice = self.funcao_hash(id)
        for paciente in self.tabela[indice]:
            if paciente[0] == id:
                self.tabela[indice].remove(paciente)
                return
            
        print(f"Paciente com ID {id} não encontrado.")

paciente = TabelaHash()

paciente.inserir(101, "Ana")
paciente.inserir(102, "Bruno")
paciente.inserir(106, "Carlos")
paciente.inserir(101, "Ana")

paciente.remover(101)

print("Atualzada:", paciente.tabela)
print("Buscando Ana:", paciente.buscar(101))
print("Buscando Carlos:", paciente.buscar(106))
paciente.atualizar(999, "Maria")

