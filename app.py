from heap_medicos import HeapMedicos
from heap_binario import HeapBinario
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from tabela_hash import TabelaHash
from rubro_negra import ArvoreRubroNegra

app = Flask(__name__)

tabela_pacientes = TabelaHash()
fila_triagem = HeapBinario()
fila_medicos = HeapMedicos()
cadastro_medicos = {}
lista_atendimentos = []
contador_atribuicoes = 0
arvore_historico = ArvoreRubroNegra()


@app.route("/")
def inicio():
    return render_template("index.html")


# Cadastro e listagem de pacientes
@app.route("/pacientes", methods=["GET", "POST"])
def pacientes():
    mensagem = ""

    if request.method == "POST":
        id_paciente = request.form.get("id", type=int)
        nome = request.form.get("nome", "").strip()

        if id_paciente is None or id_paciente <= 0 or not nome:
            mensagem = "Preencha os campos corretamente."

        elif tabela_pacientes.buscar(id_paciente) is not None:
            mensagem = "Já existe um paciente com esse ID."

        else:
            tabela_pacientes.inserir(id_paciente, nome)
            return redirect(url_for("pacientes"))

    lista_pacientes = []

    for lista in tabela_pacientes.tabela:
        for paciente in lista:
            lista_pacientes.append(paciente)

    return render_template(
        "pacientes.html",
        pacientes=lista_pacientes,
        mensagem=mensagem
    )


# Busca de pacientes pela tabela hash
@app.route("/pacientes/buscar")
def buscar_paciente():
    id_paciente = request.args.get("id", type=int)

    paciente_encontrado = None
    mensagem_busca = ""

    if id_paciente is None or id_paciente <= 0:
        mensagem_busca = "Informe um ID válido."

    else:
        paciente_encontrado = tabela_pacientes.buscar(id_paciente)

        if paciente_encontrado is None:
            mensagem_busca = "Paciente não encontrado."

    lista_pacientes = []

    for lista in tabela_pacientes.tabela:
        for paciente in lista:
            lista_pacientes.append(paciente)

    return render_template(
        "pacientes.html",
        pacientes=lista_pacientes,
        paciente_encontrado=paciente_encontrado,
        mensagem_busca=mensagem_busca
    )


# Edicao de pacientes
@app.route("/pacientes/editar/<int:id>", methods=["GET", "POST"])
def editar_paciente(id):
    paciente = tabela_pacientes.buscar(id)

    if paciente is None:
        return redirect(url_for("pacientes"))

    mensagem = ""

    if request.method == "POST":
        novo_nome = request.form.get("nome", "").strip()

        if not novo_nome:
            mensagem = "Informe um nome válido."

        else:
            tabela_pacientes.atualizar(id, novo_nome)
            return redirect(url_for("pacientes"))

    return render_template(
        "editar_paciente.html",
        paciente=paciente,
        mensagem=mensagem
    )


# Triagem de pacientes
@app.route("/triagem", methods=["GET", "POST"])
def triagem():
    mensagem = ""

    if request.method == "POST":
        id_paciente = request.form.get("id", type=int)
        prioridade = request.form.get("prioridade", type=int)

        paciente = tabela_pacientes.buscar(id_paciente) if id_paciente is not None else None

        if paciente is None:
            mensagem = "Paciente não encontrado."

        elif prioridade not in range(1, 6):
            mensagem = "Selecione uma prioridade válida."

        elif any(item[2] == id_paciente for item in fila_triagem.heap):
            mensagem = "Este paciente já está na fila de triagem."

        else:
            horario = datetime.now().isoformat()

            fila_triagem.inserir(
                prioridade,
                horario,
                id_paciente
            )

            return redirect(url_for("triagem"))

    lista_pacientes = []

    for lista in tabela_pacientes.tabela:
        for paciente in lista:
            lista_pacientes.append(paciente)

    fila = []

    for item in sorted(fila_triagem.heap):
        paciente = tabela_pacientes.buscar(item[2])

        if paciente is not None:
            fila.append({
                "prioridade": item[0],
                "horario": item[1][11:19],
                "id": item[2],
                "nome": paciente[1]
            })

    return render_template(
        "triagem.html",
        pacientes=lista_pacientes,
        fila=fila,
        mensagem=mensagem
    )


# Cadastro e listagem de medicos
@app.route("/medicos", methods=["GET", "POST"])
def medicos():
    mensagem = ""

    if request.method == "POST":
        id_medico = request.form.get("id", type=int)
        nome = request.form.get("nome", "").strip()

        if id_medico is None or id_medico <= 0 or not nome:
            mensagem = "Preencha os campos corretamente."

        elif id_medico in cadastro_medicos:
            mensagem = "Já existe um médico com esse ID."

        else:
            if fila_medicos.inserir(id_medico):
                cadastro_medicos[id_medico] = nome
                return redirect(url_for("medicos"))

            mensagem = "Não foi possível cadastrar o médico."

    lista_medicos = []

    for medico in sorted(fila_medicos.heap):
        lista_medicos.append({
            "id": medico[2],
            "nome": cadastro_medicos[medico[2]],
            "atendimentos": medico[0]
        })

    return render_template(
        "medicos.html",
        medicos=lista_medicos,
        mensagem=mensagem
    )


# Gerenciamento de atendimentos
@app.route("/atendimentos", methods=["GET", "POST"])
def atendimentos():
    global contador_atribuicoes

    mensagem = ""

    if request.method == "POST":

        if not fila_triagem.heap:
            mensagem = "Não há pacientes na fila de atendimento."

        elif not fila_medicos.heap:
            mensagem = "Não há médicos cadastrados."

        else:
            paciente = fila_triagem.remover()
            medico = fila_medicos.remover()

            id_paciente = paciente[2]
            id_medico = medico[2]

            dados_paciente = tabela_pacientes.buscar(id_paciente)

            contador_atribuicoes += 1

            agora = datetime.now()

            atendimento = {
                "id": contador_atribuicoes,
                "paciente": dados_paciente[1],
                "id_paciente": id_paciente,
                "medico": cadastro_medicos[id_medico],
                "id_medico": id_medico,
                "prioridade": paciente[0],
                "horario": agora.strftime("%H:%M:%S")
            }

            # Registro na arvore rubro-negra
            horario_min = agora.hour * 60 + agora.minute

            arvore_historico.inserir(
                horario_min,
                atendimento["id"],
                atendimento
            )

            lista_atendimentos.append(atendimento)

            # Atualizacao do heap de medicos
            fila_medicos.inserir(
                id_medico,
                medico[0] + 1,
                contador_atribuicoes
            )

            return redirect(url_for("atendimentos"))

    return render_template(
        "atendimentos.html",
        atendimentos=lista_atendimentos,
        pacientes_aguardando=len(fila_triagem.heap),
        medicos_disponiveis=len(fila_medicos.heap),
        mensagem=mensagem
    )


# Historico de atendimentos pela arvore rubro-negra
@app.route("/historico")
def historico():
    registros = arvore_historico.ordem()

    historico_atendimentos = [
        registro["dados"] for registro in registros
    ]

    informacoes_arvore = arvore_historico.validar()

    return render_template(
        "historico.html",
        historico=historico_atendimentos,
        informacoes=informacoes_arvore
    )


# Exclusao de pacientes
@app.route("/pacientes/excluir/<int:id>", methods=["POST"])
def excluir_paciente(id):
    paciente = tabela_pacientes.buscar(id)

    if any(item[2] == id for item in fila_triagem.heap):

        lista_pacientes = []

        for lista in tabela_pacientes.tabela:
            for paciente_cadastrado in lista:
                lista_pacientes.append(paciente_cadastrado)

        return render_template(
            "pacientes.html",
            pacientes=lista_pacientes,
            mensagem="Não é possível excluir um paciente que está na fila de atendimento."
        )

    if paciente is not None:
        tabela_pacientes.remover(id)

    return redirect(url_for("pacientes"))


# Alteracao de prioridade na triagem
@app.route("/triagem/alterar/<int:id>", methods=["POST"])
def alterar_prioridade(id):
    nova_prioridade = request.form.get("prioridade", type=int)

    if nova_prioridade in range(1, 6):
        fila_triagem.atualizar_prioridade(id, nova_prioridade)

    return redirect(url_for("triagem"))


# Remocao de pacientes da fila
@app.route("/triagem/remover/<int:id>", methods=["POST"])
def remover_triagem(id):
    fila_triagem.remover_por_id(id)

    return redirect(url_for("triagem"))


if __name__ == "__main__":
    app.run(debug=True)