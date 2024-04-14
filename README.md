<center>
  # CRUD---PY-SLAG-Mongo-RESTFULAPI---replicacion
Implementacin de mongo, python, slag y restful API con replicacion
<h1>Rama de steven</h1>
  En esta rama se aportaran los avances de steven
  <h1> Cosas para realizar las API</h1>
 <h2> Para el funcionamiento se necesitan las siguientes librerias: </h2>
  
    from flask import Flask, redirect, jsonify, request
    from pymongo import MongoClient
    from bson import json_util
    
De flask importamos flask para las funciones del framework, redirect para tener response, jsonify para devolver formatos json, request para traer informacion por ejemplo de la base de datos. <br>
De pymongo importamos MongoClient para interactuar con mongodb. <br>
De bson importamos json_util para utilidades con el formato json, por ejemplo volver en formato json la informacion que se trae de la base de datos. <br>
<br>
<h2>Ejemplo de API con el metodo GET</h2>
En la ruta /empleados usamos el metodo GET, definimos get_empleados(), empleados sera igual a una lista buscada en empleados_collection, response sera igual empleados traido en formato json con ayuda de json_util.dumps y retornamos response.
Lo demas es en caso de error


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
</center> 
