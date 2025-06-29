from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/pedir/<nombre>')
def pedir(nombre):
    return f"<h2>Gracias por pedir el brownie de {nombre}. ¡En breve te llegará la felicidad! 🌈🍫</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

