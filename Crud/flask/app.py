# Importamos las clases Flask, request y jsonify
from flask import Flask, request, jsonify, url_for, redirect
from pymongo import MongoClient

# Creamos una instancia de la clase Flask y la asignamos a la variable 'app'
app = Flask(__name__)

def pagina_no_encontrada(error):
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Manejo de error 404
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)

#credenciales para acceder a la base de datos
mongo_uri = "mongodb+srv://El-Meru-Criss:12345@Pruebas-criss.neht1oe.mongodb.net/empleados"
cliente = MongoClient(mongo_uri)
db = cliente['empleados']
#datos de los emleados
empleados_collection = db['empleado']
#Dedinicion de rutas/APIs
#buscar todos los empleados (GET)
@app.route('/empleados', methods=['GET'])
def get_empleados():
    empleados = list(empleados_collection.find({}, {'_id': 0}))
    return jsonify(empleados)


#Crear empleado
@app.route('/empleados', methods=['POST'])
def add_empleados():
    empleado = request.json
    if not empleado.get('_id') or empleados_collection.find_one({"_id": empleado["_id"]}):
         return jsonify({"message": "ID de empleado es requerido y debe ser unico"}), 400
    empleados_collection.insert_one(empleado)
    return jsonify({"message": "Estudiante creado!"}), 201