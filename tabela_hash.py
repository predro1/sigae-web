class TabelaHash:
    def __init__(self):
        self.tamanho = 5
        self.tabela = [[] for i in range(self.tamanho)]
        
    def funcao_hash(self, id):
        return id % self.tamanho

    def inserir(self, id, nome):
        indice = self.funcao_hash(id)
        self.tabela[indice].append([id, nome])
paciente = TabelaHash()

paciente.inserir(101, "Ana")
paciente.inserir(102, "Bruno")

print(paciente.tabela)
 