from flask import Flask, render_template, request, redirect, url_for
from tabela_hash import TabelaHash

app = Flask(__name__)

tabela_pacientes = TabelaHash()


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


@app.route("/triagem")
def triagem():
    return render_template("pagina.html", titulo="Triagem")


@app.route("/medicos")
def medicos():
    return render_template("pagina.html", titulo="Médicos")


@app.route("/atendimentos")
def atendimentos():
    return render_template("pagina.html", titulo="Atendimentos")


@app.route("/historico")
def historico():
    return render_template("pagina.html", titulo="Histórico")

# Exclusao de pacientes
@app.route("/pacientes/excluir/<int:id>", methods=["POST"])
def excluir_paciente(id):
    paciente = tabela_pacientes.buscar(id)

    if paciente is not None:
        tabela_pacientes.remover(id)

    return redirect(url_for("pacientes"))


if __name__ == "__main__":
    app.run(debug=True)
