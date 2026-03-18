from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"

def conectar():
    return sqlite3.connect(DATABASE)

@app.route("/")
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    conn.close()
    return render_template("index.html", empleados=empleados)

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")

@app.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form["nombre"]
    cargo = request.form["cargo"]
    salario = request.form["salario"]
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO empleados(nombre,cargo,salario) VALUES(?,?,?)",
        (nombre, cargo, salario),
    )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/editar/<id>")
def editar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados WHERE id=?", (id,))
    empleado = cursor.fetchone()
    conn.close()
    return render_template("editar.html", empleado=empleado)

@app.route("/actualizar", methods=["POST"])
def actualizar():
    id = request.form["id"]
    nombre = request.form["nombre"]
    cargo = request.form["cargo"]
    salario = request.form["salario"]
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE empleados
        SET nombre=?, cargo=?, salario=?
        WHERE id=?
        """,
        (nombre, cargo, salario, id),
    )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/eliminar/<id>")
def eliminar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM empleados WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)