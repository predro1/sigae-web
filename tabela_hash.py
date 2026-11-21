class TabelaHash:
    def __init__(self):
        self.tamanho = 5
        self.tabela = [[] for i in range(self.tamanho)]

paciente = TabelaHash()

print(paciente.tabela)