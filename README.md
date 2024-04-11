<center>
  # CRUD---PY-SLAG-Mongo-RESTFULAPI---replicacion
Implementacin de mongo, python, slag y restful API con replicacion
<h1>Rama de Brayan</h1>
  En esta rama se aportaran los avances de brayan con todo lo relacionado a flask
</center>

<h2>instalamos las librerias</h2>

    pip install flask
    pip install pymongo

instalamos primero las librerias necesarias para el funcionamiento de la aplicacion

<h2>Importaciones:</h2>

    from flask import Flask, render_template, redirect, url_for
    from pymongo import MongoClient
  
Importamos las clases necesarias de Flask (Flask, render_template, redirect, url_for) y de pymongo (MongoClient) para interactuar con MongoDB desde nuestra aplicación Flask.

<h2>Datos de conexión a MongoDB:</h2>

    usuario = "El-Meru-Criss"
    contraseña = "12345"
    host = "pruebas-criss.neht1oe.mongodb.net"
    puerto = 27017
    nombre_bd = "empleados"

    url_conexion = f"mongodb+srv://{usuario}:{contraseña}@{host}/{nombre_bd}"
    
Definimos los datos de conexión a MongoDB, incluyendo el nombre de usuario, contraseña, host, puerto y nombre de la base de datos. Luego, construimos la URL de conexión utilizando estos datos.

<h2>Conexión a MongoDB:</h2>


    cliente = MongoClient(url_conexion)
    db = cliente[nombre_bd]

Creamos una instancia de MongoClient y nos conectamos a la base de datos especificada en la URL de conexión.

<h2>Creación de la aplicación Flask:</h2>

    app = Flask(__name__)
    
Creamos una instancia de la clase Flask y la asignamos a la variable app.
