from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def inicio():

    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])

def ejercicio1():

    nombre = ""

    total = 0

    descuento = 0

    total_pagar = 0

    if request.method == "POST":

        nombre = request.form["nombre"]

        edad = int(request.form["edad"])

        cantidad = int(request.form["cantidad"])

        total = cantidad * 9000

        if 18 <= edad <= 30:

            descuento = total * 0.15

        elif edad > 30:

            descuento = total * 0.25

        total_pagar = total - descuento

    return render_template(

        "ejercicio1.html",

        nombre=nombre,

        total=total,

        descuento=descuento,

        total_pagar=total_pagar

    )

@app.route("/ejercicio2", methods=["GET", "POST"])

def ejercicio2():

    mensaje = ""

    if request.method == "POST":

        usuario = request.form["usuario"]

        clave = request.form["clave"]

        if usuario == "juan" and clave == "admin":

            mensaje = "Bienvenido administrador juan"

        elif usuario == "pepe" and clave == "user":

            mensaje = "Bienvenido usuario pepe"

        else:

            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)

if __name__ == "__main__":

    app.run(debug=True)