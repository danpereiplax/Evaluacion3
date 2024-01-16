from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET'])
def ejercicio1():
    return render_template('formulario_notas.html')

@app.route('/procesar_notas', methods=['POST'])
def procesar_notas():
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 40 and asistencia >= 75:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    return f'Promedio: {promedio:.2f}, Estado: {estado}'

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mas_largo = None
    cantidad_caracteres = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encuentra el nombre con la mayor cantidad de caracteres
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

    return render_template('formulario_nombres.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)
# tu_proyecto/app/routes.py

from flask import render_template, request
from app import app

@app.route('/procesar_nombres', methods=['POST'])
def procesar_nombres():
    nombre_mas_largo = None
    cantidad_caracteres = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encuentra el nombre con la mayor cantidad de caracteres
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

    return render_template('formulario_nombres.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)
