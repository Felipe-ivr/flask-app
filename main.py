from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        notas = [int(request.form['nota1']), int(request.form['nota2']), int(request.form['nota3'])]
        asistencia = int(request.form['asistencia'])
        promedio = sum(notas) / 3
        resultado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
        return render_template('ejercicio1.html', promedio=promedio, resultado=resultado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]
        nombre_largo = max(nombres, key=len)
        longitud = len(nombre_largo)
        return render_template('ejercicio2.html', nombre_largo=nombre_largo, longitud=longitud)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
