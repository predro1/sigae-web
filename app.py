from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/pacientes")
def pacientes():
    return render_template("pagina.html", titulo="Pacientes")

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

if __name__ == "__main__":
    app.run(debug=True)
