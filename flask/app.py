# Importamos las clases Flask y render_template desde el paquete Flask
from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient

# Datos de conexión a MongoDB
usuario = "El-Meru-Criss"
contraseña = "12345"
host = "pruebas-criss.neht1oe.mongodb.net"
puerto = 27017  # Puerto por defecto de MongoDB
nombre_bd = "empleados"

# URL de conexión a MongoDB
url_conexion = f"mongodb+srv://{usuario}:{contraseña}@{host}/{nombre_bd}"

# Crear una instancia de MongoClient y conectarse a la base de datos
cliente = MongoClient(url_conexion)
db = cliente[nombre_bd]

# Creamos una instancia de la clase Flask y la asignamos a la variable 'app'
app = Flask(__name__)

# Definimos una ruta principal '/' utilizando el decorador @app.route('/')
@app.route('/')
def index():
    # Consultar información de todos los empleados
    empleados = db["empleado"].find()

    # Creamos un diccionario 'data' con varios datos
    data = {
        'titulo': 'index',                # Título de la página
        'tabla': 'tabla',                 # Nombre de la tabla (aunque aquí no está siendo utilizado)
        'empleados': empleados,           # Tabla de empleados obtenida de la base de datos
        'num_empleados': db["empleado"].count_documents({}) # Número de empleados en la tabla
    }

    # Renderizamos la plantilla HTML 'index.html' y pasamos el diccionario 'data' como contexto
    return render_template('index.html', data=data)

def pagina_no_encontrada(error):
    return redirect(url_for('index'))

# Bloque que ejecuta la aplicación solo si el script se ejecuta directamente (no si se importa como un módulo)
if __name__ == '__main__':
    # Manejo de error 404
    app.register_error_handler(404, pagina_no_encontrada)
    # Iniciamos el servidor Flask en modo de depuración (debug=True)
    app.run(debug=True)