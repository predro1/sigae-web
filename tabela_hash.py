class TabelaHash:
    def __init__(self):
        self.tamanho = 5
        self.tabela = [[] for i in range(self.tamanho)]
        self.quantidade = 0

    def funcao_hash(self, id):
        return id % self.tamanho

    def inserir(self, id, nome):
        indice = self.funcao_hash(id)

        for paciente in self.tabela[indice]:
            if paciente[0] == id:
                print(f"Paciente com ID {id} já existe.")
                return

        self.tabela[indice].append([id, nome])
        self.quantidade += 1

        if self.quantidade / self.tamanho >=0.75:
            self.redimensionar()

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
                self.quantidade -= 1
                return
            
        print(f"Paciente com ID {id} não encontrado.")

    def redimensionar(self):
        tamanho_antigo = self.tabela

        self.tamanho *= 2
        self.tabela = [[] for i in range(self.tamanho)]

        for lista in tamanho_antigo:
            for paciente in lista:
                indice = self.funcao_hash(paciente[0])
                self.tabela[indice].append(paciente)