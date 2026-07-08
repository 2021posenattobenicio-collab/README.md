from flask import Flask, render_template, request

app = Flask(__name__)

def dar_consejo(temp, lluvia):
    if temp < 10:
        consejo = "Ponete una campera abrigada. "
    elif temp <= 24:
        consejo = "Con un buzo estás bien. "
    else:
        consejo = "En remera estás bien. "

    if lluvia == "s":
        consejo += "Llevá paraguas"

    return consejo

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""

    if request.method == "POST":
        temperatura = int(request.form["temperatura"])
        llueve = request.form["llueve"]

        resultado = dar_consejo(temperatura, llueve)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)