# Importar las clases necesarias de Flask
from flask import Flask, render_template, redirect, url_for, jsonify, request, Response
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

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

# Crear una instancia de la clase Flask y asignarla a la variable 'app'
app = Flask(__name__)

# Definir la ruta principal '/' utilizando el decorador @app.route('/')
@app.route('/')
def index():
    # Consultar información de todos los empleados
    empleados = db["empleado"].find()

    # Crear un diccionario 'data' con varios datos
    data = {
        'titulo': 'index',                # Título de la página
        'tabla': 'tabla',                 # Nombre de la tabla (aunque aquí no está siendo utilizado)
        'empleados': empleados,           # Tabla de empleados obtenida de la base de datos
        'num_empleados': db["empleado"].count_documents({}) # Número de empleados en la tabla
    }

    # Renderizar la plantilla HTML 'index.html' y pasar el diccionario 'data' como contexto
    return render_template('index.html', data=data)

# Ruta para mostrar el formulario de creación de empleado
@app.route('/crear')
def crear_empleado():
    return render_template('crear.html')

# Ruta para redireccionar al formulario de actualización de empleados
@app.route('/actualizar/<id>', methods=['GET'])
def redirigir_a_actualizar(id):
    return redirect(url_for('mostrar_formulario_actualizar', id=id))

# Ruta para mostrar el formulario de actualización de empleados
@app.route('/mostrar_formulario_actualizar/<id>', methods=['GET'])
def mostrar_formulario_actualizar(id):
    # Verificar si el ID es válido
    if not ObjectId.is_valid(id):
        # Si el ID no es válido, redirigir al índice
        return redirect(url_for('index'))

    # Obtener los datos del empleado con el ID proporcionado
    empleado = empleados_collection.find_one({'_id': ObjectId(id)})
    
    # Verificar si se encontró el empleado con el ID proporcionado
    if empleado:
        # Renderizar el formulario de actualización y pasar los datos del empleado como contexto
        return render_template('actualizar.html', empleado=empleado)
    else:
        # Si no se encuentra el empleado, redirigir a una página de error o a la página principal
        return redirect(url_for('index'))
    
# API método POST para crear un empleado
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
        return not_found()

# API método GET para obtener todos los empleados
@app.route('/empleados', methods=['GET'])
def get_empleados():
    empleados = list(empleados_collection.find())  # Obtener todos los empleados de la colección
    response = json_util.dumps(empleados)  # Convertir la lista de empleados a formato JSON
    return Response(response, mimetype='application/json')  # Devolver la respuesta JSON

# API método GET para obtener un empleado específico por su ID
@app.route('/empleados/<id>', methods=['GET'])
def get_empleado(id):
    empleado = empleados_collection.find_one({'_id': ObjectId(id)})  # Obtener un empleado de la colección
    if empleado:
        response = json_util.dumps(empleado)  # Convertir el empleado a formato JSON
        return Response(response, mimetype='application/json')  # Devolver la respuesta JSON
    else:
        return not_found() # Devolver la respuesta
    
# API método DELETE para eliminar un empleado por su ID
@app.route('/empleados/<id>', methods=['DELETE'])
def delete_empleado(id):
    empleados_collection.delete_one({'_id': ObjectId(id)})  # Elegir a un empleado para eliminar
    response = jsonify({'mensaje' : 'Empleado ' + id + ' ha sido borrado correctamente'})  # Mensaje que el empleado fue borrado correctamente
    return response

# API método PUT para actualizar un empleado por su ID
@app.route('/empleados/<id>', methods=['PUT'])
def update_empleado(id):
    try:
        # Verificar si el ID del empleado es válido
        if not ObjectId.is_valid(id):
            return jsonify({'error': 'ID de empleado no válido'}), 400

        # Verificar si se proporcionó el campo 'nombre' en el JSON
        if 'nombre' not in request.json:
            return jsonify({'error': 'Campo "nombre" requerido'}), 400

        nombre_nuevo = request.json['nombre']

        # Actualizar el empleado en la base de datos
        resultado = empleados_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'Nombre': nombre_nuevo}}
        )

        if resultado.modified_count > 0:
            return jsonify({'mensaje': f'Empleado {id} actualizado correctamente'})
        else:
            return jsonify({'error': 'Empleado no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Manejador de errores para el código de estado 404 (Not Found)
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'mensaje': 'Recurso no encontrado: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

# Función para redireccionar al índice (index) de Flask
def pagina_no_encontrada(error):
    return redirect(url_for('index'))

# Bloque que ejecuta la aplicación solo si el script se ejecuta directamente (no si se importa como un módulo)
if __name__ == '__main__':
    # Manejo de error 404
    app.register_error_handler(404, pagina_no_encontrada)
    # Iniciamos el servidor Flask en modo de depuración (debug=True)
    app.run(debug=True)