from tabela_hash import TabelaHash

paciente = TabelaHash()

print(" 1 - Cadastro de pacientes")
paciente.inserir(101, "Ana")
paciente.inserir(102, "Bruno")
paciente.inserir(106, "Carlos")
print(paciente.tabela)

print("2 - Id duplicado")
paciente.inserir(101, "Ana")

print("3 - colisão de hash")
print("Indice da Ana:", paciente.funcao_hash(101))
print("Indice do Carlos:", paciente.funcao_hash(106))
print("Pacientes no indice 1:", paciente.tabela[1])


print(" 4 - Busca de pacientes")
print(paciente.buscar(101))
print(paciente.buscar(999))


print("5 - Atualização de pacientes")
paciente.atualizar(101, "Ana Clara")
print(paciente.buscar(101))

print("6 - Removendo pacientes")
paciente.remover(101)
print(paciente.buscar(101))
print(paciente.buscar(106))


print(" 7 - Inserindo e removendo paciente inexistente")
paciente.atualizar(999, "Maria")
paciente.remover(999)

print(" 8 - Redimensionando tabela")
nova_tabela = TabelaHash()
nova_tabela.inserir(101, "Ana")
nova_tabela.inserir(102, "Bruno")
nova_tabela.inserir(106,"Carlos")

print("Tabela antes do redimensionamento:", nova_tabela.tabela)
nova_tabela.redimensionar()

print("Tabela após o redimensionamento:", nova_tabela.tabela)
print("Tamanho: ", nova_tabela.tamanho)

print(nova_tabela.buscar(101))
print(nova_tabela.buscar(106))