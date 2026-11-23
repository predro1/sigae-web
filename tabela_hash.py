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

    def redimensionar(self):
        tamanho_antigo = self.tabela
        self.tamanho *= 2
        self.tabela = [[] for i in range(self.tamanho)]
        
        for lista in tamanho_antigo:
            for paciente in lista:
                self.inserir(paciente[0], paciente[1])