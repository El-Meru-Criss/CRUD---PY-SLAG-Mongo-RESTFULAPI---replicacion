# Importamos las clases Flask y render_template desde el paquete Flask
from flask import Flask, render_template, redirect, url_for, jsonify, request
from pymongo import MongoClient
from bson import json_util


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

# Obtener la colección de empleados
empleados_collection = db["empleado"]

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

@app.route('/empleados', methods=['POST'])
def post_empleados():
    # Recibir los datos del JSON de la solicitud
    datos = request.get_json()

    # Verificar si el campo 'Nombre' está presente en los datos recibidos
    if 'Nombre' in datos:
        nombre = datos['Nombre']

        # Insertar el nuevo empleado en la colección de empleados
        id = empleados_collection.insert_one({'Nombre': nombre}).inserted_id
        
        # Crear la respuesta JSON con el ID generado y el nombre del empleado
        response = {
            'id': str(id),
            'nombre': nombre
        }

        # Devolver la respuesta JSON
        return jsonify(response)
    else:
        # Si no se proporciona el campo 'Nombre', devolver un mensaje de error
        # return not_found()
        return jsonify({'mensaje': 'Campo "Nombre" no proporcionado en la solicitud'}), 400
        
    
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'mensaje': 'resource Not Fount: ' + request.url,
        'status': 404
    }

    return message

def pagina_no_encontrada(error):
    return redirect(url_for('index'))

#API metodo GET todos los empleados
@app.route('/empleados', methods=['GET'])
def get_empleados():
    empleados = list(empleados_collection.find())
    response = json_util.dumps(empleados)
    return response

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'mensaje': 'Recurso no encontrado: ' + request.url,
        'status': 404
    }
    return jsonify(message), 404

#API buscar empleado por nombre
@app.route('/empleados', methods=['GET'])
def get_empleado():
    # Verificar si se proporciona un parámetro de consulta 'nombre'
    Nombre = request.args.get('Nombre')
    if Nombre:
        # Buscar un empleado por su nombre en la colección
        empleado = empleados_collection.find_one({'Nombre': Nombre})
        if empleado:
            return json_util.dumps(empleado)
        else:
            return jsonify({'mensaje': 'Empleado no encontrado'}), 404
    else:
        # Si no se proporciona un nombre, devolver todos los empleados
        empleados = list(empleados_collection.find())
        return json_util.dumps(empleados)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'mensaje': 'Recurso no encontrado: ' + request.url,
        'status': 404
    }
    return jsonify(message), 404
#buscar uno por ip
@app.route('/empleados', methods=['GET'])
def get_empleado_ip():
    # Obtener la IP de la solicitud
    ip = request.remote_addr

    # Buscar al empleado por su IP
    empleado = empleados_collection.find_one({'ip': ip})
    if empleado:
        return json_util.dumps(empleado)
    else:
        return jsonify({'mensaje': 'Empleado no encontrado para esta IP'}), 404
#eliminar uno por ip
@app.route('/empleados', methods=['DELETE'])
def delete_empleado():
    # Obtener la IP de la solicitud
    ip = request.remote_addr

    # Eliminar al empleado por su IP
    resultado = empleados_collection.delete_one({'ip': ip})
    if resultado.deleted_count == 1:
        return jsonify({'mensaje': 'Empleado eliminado correctamente'})
    else:
        return jsonify({'mensaje': 'Empleado no encontrado para esta IP'}), 404

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'mensaje': 'Recurso no encontrado: ' + request.url,
        'status': 404
    }
    return jsonify(message), 404


# Bloque que ejecuta la aplicación solo si el script se ejecuta directamente (no si se importa como un módulo)
if __name__ == '__main__':
    # Manejo de error 404
    app.register_error_handler(404, pagina_no_encontrada)
    # Iniciamos el servidor Flask en modo de depuración (debug=True)
    app.run(debug=True)