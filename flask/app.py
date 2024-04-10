# Importamos las clases Flask y render_template desde el paquete Flask
from flask import Flask, render_template

# Creamos una instancia de la clase Flask y la asignamos a la variable 'app'
app = Flask(__name__)

# Definimos una ruta principal '/' utilizando el decorador @app.route('/')
@app.route('/')
def index():
    # Lista de nombres
    nombres = ['brayan', 'steven', 'cristian', 'ana', 'sebastian', 'jaider', 'harold', 'david', 'felipe', 'maicol']

    # Creamos un diccionario 'data' con varios datos
    data = {
        'titulo': 'index',                # Título de la página
        'tabla': 'tabla',                 # Nombre de la tabla (aunque aquí no está siendo utilizado)
        'nombres': nombres,               # Lista de nombres
        'numero_nombres': len(nombres)    # Número de nombres en la lista
    }

    # Renderizamos la plantilla HTML 'index.html' y pasamos el diccionario 'data' como contexto
    return render_template('index.html', data=data)

# Bloque que ejecuta la aplicación solo si el script se ejecuta directamente (no si se importa como un módulo)
if __name__ == '__main__':
    # Iniciamos el servidor Flask en modo de depuración (debug=True)
    app.run(debug=True)