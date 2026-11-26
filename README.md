# SIGAE WEB

Sistema Integrado de Gestão de Atendimento de Emergência.

Aplicação WEB para gestão de triagem e atendimento hospitalar de emergência, desenvolvida como projeto acadêmico de Estruturas de Dados.

## Objetivo

O SIGAE WEB tem como objetivo simular o gerenciamento do atendimento hospitalar, desde o cadastro dos pacientes até o registro dos atendimentos realizados.

O sistema utiliza estruturas de dados para organizar pacientes por prioridade, distribuir atendimentos entre médicos e armazenar o histórico de forma eficiente.

## Tecnologias utilizadas

- Python
- Flask
- HTML5
- CSS3
- Jinja2
- Git
- GitHub

## Estruturas de dados implementadas

### 1. Tabela Hash

Responsável pelo gerenciamento dos pacientes cadastrados.

Funcionalidades:

- Inserção de pacientes.
- Busca por ID.
- Atualização de cadastro.
- Exclusão de pacientes.
- Tratamento de colisões por encadeamento.
- Redimensionamento automático da tabela.

### 2. Heap Binário

Responsável pela organização da fila de triagem.

Os pacientes são organizados conforme sua prioridade e, em caso de empate, pela ordem de chegada.

Classificação das prioridades:

| Prioridade | Classificação |
| --- | --- |
| 1 | Emergência |
| 2 | Muito urgente |
| 3 | Urgente |
| 4 | Pouco urgente |
| 5 | Não urgente |

O sistema permite inserir pacientes na fila, alterar suas prioridades e remover registros.

### 3. Heap de Médicos

Responsável pela distribuição equilibrada dos atendimentos entre os médicos cadastrados.

O médico com a menor quantidade de atendimentos recebe o próximo paciente.

Em caso de empate, o sistema considera a última atribuição e o ID do médico como critérios de desempate.

### 4. Árvore Rubro-Negra

Responsável pelo armazenamento e organização do histórico de atendimentos.

A estrutura utiliza rotações e recolorações para manter seu balanceamento.

Funcionalidades:

- Inserção de registros.
- Busca por identificador.
- Busca por horário.
- Remoção de registros.
- Percurso em ordem.
- Validação das propriedades da árvore.
- Contagem de rotações.
- Cálculo da altura negra.

Cada atendimento possui um identificador único, permitindo que um mesmo paciente seja atendido mais de uma vez.

## Complexidade dos algoritmos

| Estrutura | Operação | Complexidade |
| --- | --- | --- |
| Tabela Hash | Busca | O(1) em média |
| Tabela Hash | Inserção | O(1) amortizado em média |
| Tabela Hash | Atualização | O(1) em média |
| Tabela Hash | Exclusão | O(1) em média |
| Heap Binário | Inserção | O(log n) |
| Heap Binário | Remoção da raiz | O(log n) |
| Heap Binário | Alteração de prioridade por ID | O(n) |
| Heap Binário | Remoção por ID | O(n) |
| Heap de Médicos | Inserção com verificação de duplicidade | O(n) |
| Heap de Médicos | Remoção da raiz | O(log n) |
| Árvore Rubro-Negra | Inserção | O(log n) |
| Árvore Rubro-Negra | Busca por ID indexado | O(1) em média |
| Árvore Rubro-Negra | Remoção | O(log n) em média |
| Árvore Rubro-Negra | Percurso em ordem | O(n) |
| Árvore Rubro-Negra | Validação | O(n) |

As complexidades consideram as implementações utilizadas no projeto.

## Funcionalidades do sistema web

### Dashboard

- Total de pacientes cadastrados.
- Quantidade de pacientes aguardando atendimento.
- Quantidade de médicos disponíveis.
- Total de atendimentos realizados.
- Visualização da fila de atendimento.
- Atalhos para as principais funcionalidades.

### Pacientes

- Cadastro de pacientes.
- Consulta por ID.
- Edição de cadastro.
- Exclusão de pacientes.
- Validação de IDs duplicados.

### Triagem

- Classificação por prioridade.
- Organização automática da fila.
- Alteração de prioridade.
- Remoção de pacientes da fila.

### Médicos

- Cadastro de médicos.
- Listagem de profissionais.
- Controle da quantidade de atendimentos realizados.

### Atendimentos

- Seleção automática do paciente mais urgente.
- Seleção do médico com menor quantidade de atendimentos.
- Atualização da fila de triagem.
- Atualização do heap de médicos.
- Registro do atendimento no histórico.

### Histórico

- Listagem dos atendimentos realizados.
- Identificação do paciente e do médico responsável.
- Registro da prioridade e do horário.
- Exibição da quantidade de rotações da árvore.
- Exibição da altura negra.
- Validação das propriedades da árvore rubro-negra.

## Fluxo de funcionamento

1. Cadastro do paciente na Tabela Hash.
2. Classificação do paciente na triagem.
3. Inserção do paciente no Heap Binário.
4. Cadastro dos médicos no Heap de Médicos.
5. Seleção automática do paciente e do médico.
6. Realização do atendimento.
7. Registro na Árvore Rubro-Negra.
8. Atualização dos indicadores do dashboard.

## Estrutura do projeto

    sigae-web/
    |
    |-- static/
    |   |-- style.css
    |
    |-- templates/
    |   |-- index.html
    |   |-- pacientes.html
    |   |-- editar_paciente.html
    |   |-- triagem.html
    |   |-- medicos.html
    |   |-- atendimentos.html
    |   |-- historico.html
    |   |-- pagina.html
    |
    |-- app.py
    |-- tabela_hash.py
    |-- heap_binario.py
    |-- heap_medicos.py
    |-- rubro_negra.py
    |-- teste_tabela_hash.py
    |-- teste_heap.py
    |-- teste_heap_medicos.py
    |-- teste_rubro_negra.py
    |-- requirements.txt
    |-- .gitignore
    |-- README.md

## Como executar o projeto

### Pré-requisitos

- Python 3 instalado.
- Git instalado, caso utilize a clonagem pelo terminal.

### 1. Obter o projeto

Clone o repositório pelo GitHub Desktop ou faça o download dos arquivos pelo GitHub.

### 2. Acessar a pasta do projeto

Abra a pasta sigae-web no Visual Studio Code.

### 3. Instalar as dependências

Execute no terminal:

```bash
python -m pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python app.py
```

### 5. Acessar o sistema

Abra o navegador e acesse:

http://127.0.0.1:5000

## Testes

O projeto possui arquivos destinados aos testes individuais das estruturas de dados.

Para executá-los, utilize os seguintes comandos:

```bash
python teste_tabela_hash.py
python teste_heap.py
python teste_heap_medicos.py
python teste_rubro_negra.py
```

Também foram realizados testes manuais na interface web para verificar o cadastro de pacientes, a organização da triagem, a distribuição de atendimentos, o histórico e a atualização dos indicadores.

## Limitações atuais

- Os dados são armazenados em memória.
- Os registros são apagados quando o servidor é reiniciado.
- O sistema não utiliza banco de dados.
- Os médicos voltam a ficar disponíveis imediatamente após cada atendimento.
- Os indicadores são atualizados ao carregar a página.
- A aplicação não possui autenticação de usuários.
- O histórico utiliza o horário em minutos do dia como chave principal de ordenação.
- As operações de busca e remoção da árvore não estão disponíveis diretamente na interface web.

## Possíveis melhorias futuras

- Integração com banco de dados.
- Sistema de autenticação.
- Controle de disponibilidade dos médicos.
- Filtros de pesquisa no histórico.
- Atualização dos indicadores em tempo real.
- Registro de data e horário completos.
- Geração de relatórios de atendimento.

## Considerações finais

O SIGAE WEB demonstra a aplicação prática de estruturas de dados em um sistema web integrado.

A utilização da Tabela Hash, do Heap Binário, do Heap de Médicos e da Árvore Rubro-Negra permite explorar diferentes técnicas de armazenamento, organização, busca e gerenciamento de informações.

O projeto possui finalidade exclusivamente acadêmica e não deve ser utilizado como sistema hospitalar real.