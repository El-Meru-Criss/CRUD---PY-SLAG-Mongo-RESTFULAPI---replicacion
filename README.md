# CRUD---PY-SLAG-Mongo-RESTFULAPI---replicacion
Implementacin de mongo, python, slag y restful API con replicacion
<br>
<center>
  <h1>MARCO TEÓRICO</h1>
  <h2>RESTFUL API</h2>
  Rest es la lógica y API es el método para interactuar con un sistema. Un RESTFUL API es la implementación de estos dos conceptos, aplicando la lógica del REST en los medios de comunicación API
  <h2>Rest</h2>
  Rest es una lógica de comunicación como lo expone <a href="https://bravedeveloper.com/2021/09/01/que-es-rest-restful-api-restful-y-json/" target="_blank">(Azabache, 2021)</a>:
Sus siglas vienen de Representational State Transfer, es un estilo de arquitectura de software para realizar una comunicación cliente-servidor. Se apoya en el protocolo HTTP para la comunicación al servidor y los mensajes que se envían y reciben pueden estar en XML o JSON del cual abordaremos más abajo.
Utiliza peticiones que son llamados como verbos como son los siguientes: GET, POST, PUT y DELETE.
<h2>API</h2>
  Una API es una forma de interactuar con un sistema, así como lo expone <a href="https://bravedeveloper.com/2021/09/01/que-es-rest-restful-api-restful-y-json/" target="_blank">(Azabache, 2021)</a>: 
Un API es un conjunto de funcionalidades o recursos que nos expone un sistema para poder interactuar con él desde otro sistema, esto sin importar ni los lenguajes de programación en que cada uno de ellos esté escrito ni la tecnología ni nada, y esto es gracias a que trabaja con una capa de abstracción
  <h2>Python:</h2>
Basándose en la información de <a href="https://aws.amazon.com/es/what-is/python/" target="_blank">(Amazon Web Services, Inc., n.d.)</a>:
Python es un lenguaje de programación gratuito, eficiente y fácil de aprender; muy útil en la programación web, desarrollo de software y machine learning. 
  <h2>Flask(python):</h2>
  “Flask es un “micro” Framework escrito en Python y concebido para facilitar el desarrollo de Aplicaciones Web bajo el patrón MVC.” <a href="https://openwebinars.net/blog/que-es-flask/" target="_blank">(Muñoz, 2017)</a> esto para facilitar el desarrollo del CRUD y agiliza el desarrollo
 <h2>MongoDB:</h2> 
“MongoDB (enlace externo a IBM) es un sistema de gestión de bases de datos (DBMS) no relacional de código abierto que utiliza documentos flexibles en lugar de tablas y filas para procesar y almacenar diversas formas de datos.” <a href="https://www.ibm.com/mx-es/topics/mongodb" target="_blank">(IBM Cloud®, n.d.)</a>
  <h2>POSTMAN:</h2>
“Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs—faster.” <a href="https://www.postman.com/" target="_blank">(Postman, Inc., n.d.)</a>
<h2>TRADUCCIÓN:</h2>
Postman es una plataforma API para crear y utilizar API. Postman simplifica cada paso del ciclo de vida de la API y agiliza la colaboración para que puedas crear mejores API y más rápido.

<h1>Marco Metodologico</h1>

<h2>Creacion de base de datos con MongoDB - Atlas</h2>
Con el fin de obtener una base de datos remota para almecenar informacion se identificaron los siguientes pasos para crear una BD:
<ul>
  <li>Registrarse en la pagina oficial de <a href="https://www.mongodb.com/es">MondoDB</a> </li>
  <li>Crear un nuevo proyecto</li>
  <li>Automaticamente mongo requerira que cree un usuario y contraseña para este proyeccto</li>
  <li>Dentro del proyecto crea un cluster que contendra las BD (solo 1 cluster gratis por proyecto)</li>
  <li>Dentro del  cluster crea una base de datos. Puede crear tantas tablas como reuiera</li>
</ul>
Con estos pasos realizados la base de datos esta lista para usarse.

<h2>Crear Usuarios</h2>
Para realizar modificaciones a la base de datos se requiere dar uso de los usuarios y contraseñas. Para crear usuarios debe dirigirse a:
  Database Access
Y diligenciar el formulario de creacion. para el presente sistema se crearon los usuarios:

      El-Meru-Criss
      Mosquera
      Steven

<h2>Habilitar IPs</h2>
Mongo cuenta con un sistema de validacion de IPs el cual consiste en registros de IPs publicas validas que pueden modificar la base de datos. Para registrar IPs se debe:
<ul>
  <li>Ir a Network Access</li>
  <li>Diligenciar el formulario de acceso a las IPs</li>
</ul>
Puede habilitar el acceso a todas las IPs publicas pero no es recomendable

<h2>Comandos CRUD con Python usando pymongo</h2>
Con el fin de mostrar las acciones basicas de insercion, edicion, visualizacion y eliminacion de los datos en la mongoDB se recopilaron los siguientes:

<h3>Insercion</h3>
  
    # Insertar documentos en la colección "empleado"
    empleados = db["empleado"]
    empleados.insert_many([
        { 'Cedula': '1001', 'Nombre': 'Cristian', 'apellido': 'Gonzalez', 'altura': 1.68 },
        { 'Cedula': '1001', 'Nombre': 'Cristian', 'apellido': 'Gonzalez', 'altura': 1.68 },
        { 'Cedula': '1001', 'Nombre': 'Cristian', 'apellido': 'Gonzalez', 'altura': 1.68 },
        { 'Cedula': '1002', 'Nombre': 'Steven', 'apellido': 'Porras' },
        { 'Cedula': '1003', 'Nombre': 'Mosquera', 'apellido': 'Mena', 'edad': 21 },
        { 'Cedula': '1003', 'Nombre': 'Mosquera', 'apellido': 'Mena', 'edad': 21 },
        { 'Cedula': '1003', 'Nombre': 'Mosquera', 'apellido': 'Mena', 'edad': 21 }
    ])
  
<h3>Visualizacion</h3>

    # Consultar información de todos los empleados
    empleados = db["empleado"].find()
    
    # Mostrar la información obtenida
    for empleado in empleados:
        print(empleado)

<h3>Edicion</h3>

    # Actualizar todos los datos de los empleados que coincidan con la cedula seleccionada
    nuevos_datos = { //debe crear un objeto con los nuevos datos antes de editar
        "$set": {
            'Nombre': 'Smith'
        }
    }
    db["empleado"].update_many({'Cedula': '1003'}, nuevos_datos)

<h3>Eliminacion</h3>

    # Segunda forma de eliminar todos los registros que coincidan con la cedula
    db["empleado"].delete_many({'Cedula': '1001'})

<h2>Replicacion</h2>

Mondodb Atlas ya crea por default un sistema de replicacion con 3 bases de datos, una es considerada como principal y las demas como secundarias. 
Si la base de datos principal sufre un colapso, una base de datos secundaria tomara su puesto asi logrando la continuidad de la prestacion del servicio.

Para verificar si la replicacion se encuentra activa debe conectarse a la base de datos remota con el shell de mongo.

<ul>
  <li>MongoDB Shell</li>
  Para la instalacion del Shell se tomo directo de la pagina oficial de <a href="https://www.mongodb.com/try/download/shell">MongoDB</a>. Para el presente proyecto se usara la version 2.2.3 msi
  <li>Conexion a la base de datos</li>
  En la pagina de mongo en donde esta el cluster de la base de datos, procede a darle a conectar y elegir el metodo deseado. En este caso se usara el shell de mongo. 
  Con la linea de comando proporcionada por mongo, procede a ejecutarla por medio de una consola CMD o PowerShell remplazando username con su usuario. luse de la siguiente manera:
      
      mongosh "mongodb+srv://pruebas-criss.neht1oe.mongodb.net/" --apiVersion 1 --username <username>

  Posteriormente debe de proporcionar su contraseña para este usuario.

  <li>Revisar estado de la replicacion</li>

  Con la conexion realizada en la consola de comandos, se procede a ejecutar el comando:

      rs.status()

  Para ver el estado de la replicacion. Al ejecutarlo, debera de apreciarse la cantidad de bases de datos (por lo general 3) realizando la replicacion. En este registro se indica los IDs de las bases de dates he indica su gerarquia en la replicacion (secundarios y primario)
</ul>

<h2>instalamos las librerias para Flask</h2>

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

<h2>Ruta principal '/':</h2>

    @app.route('/')
    def index():
      # Código para consultar la información de todos los empleados de la base de datos
      # Creación del diccionario 'data' con varios datos, incluyendo la tabla de empleados
      # Renderización de la plantilla HTML 'index.html' con el diccionario 'data' como contexto
      return render_template('index.html', data=data)
      
Definimos una ruta principal / utilizando el decorador @app.route('/'). Cuando se accede a esta ruta, se ejecuta la función index(), que consulta la información de todos los empleados de la base de datos, crea un diccionario data con varios datos (incluyendo la tabla de empleados obtenida de la base de datos) y luego renderiza la plantilla HTML index.html con este diccionario como contexto.

<h3>ejemplo de la ruta principal:</h3>

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

asi es como queda la parte de la ruta princial en nuestra aplicacion

<h2>Ruta del formulario /crear</h2>

    @app.route('/crear')
    def crear_empleado():
      return render_template('crear.html')
      
Esta función decorada con @app.route('/crear') indica que se debe ejecutar cuando el usuario accede a la URL /crear. Luego, la función simplemente devuelve el contenido del archivo crear.html utilizando render_template, que es una función de Flask para renderizar plantillas HTML.

<h2>Ruta del formulario editar /mostrar_formulario_actualizar/<id></h2>

    @app.route('/actualizar/<id>', methods=['GET'])
    def redirigir_a_actualizar(id):
      return redirect(url_for('mostrar_formulario_actualizar', id=id))
      
Esta función maneja las solicitudes GET a la URL /actualizar/<id>, donde <id> es un parámetro dinámico en la URL que representa el ID único del empleado a actualizar. La función redirige la solicitud a la ruta mostrar_formulario_actualizar, pasando el ID como argumento.


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
        
Esta función maneja las solicitudes GET a la URL /mostrar_formulario_actualizar/<id>, donde <id> es el ID del empleado a actualizar. Primero verifica si el ID es válido utilizando la función ObjectId.is_valid(id) (supongo que ObjectId viene de pymongo o una biblioteca similar para trabajar con MongoDB). Si el ID no es válido, redirige al usuario a la página principal (index). Luego, intenta obtener los datos del empleado con el ID proporcionado desde la colección de empleados (empleados_collection). Si encuentra al empleado, renderiza el formulario de actualización (actualizar.html) y pasa los datos del empleado como contexto al formulario. Si no encuentra al empleado, también redirige al usuario a la página principal (index).
  
<h2>Manejo de error 404:</h2>

    def pagina_no_encontrada(error):
      return redirect(url_for('index'))

    app.register_error_handler(404, pagina_no_encontrada)
    
Se define la función pagina_no_encontrada para manejar el error 404 y se registra esta función para el manejo de este error.

<h2>Ejecución de la aplicación:</h2>

    if __name__ == '__main__':
      app.run(debug=True)
      
Se inicia el servidor Flask en modo de depuración si el script se ejecuta directamente.

<h3>ejemplo de la ejecucion y manejo del error 404:</h3>

    def pagina_no_encontrada(error):
      return redirect(url_for('index'))

    # Bloque que ejecuta la aplicación solo si el script se ejecuta directamente (no si se importa como un módulo)
    if __name__ == '__main__':
      # Manejo de error 404
      app.register_error_handler(404, pagina_no_encontrada)
      # Iniciamos el servidor Flask en modo de depuración (debug=True)
      app.run(debug=True)
aqui se ve como deberia quedar ordenado el proceso de error 404 y la ejecucion de la aplicacion

<h2>render_template:</h2>

El render_template es una función de Flask que se utiliza para renderizar plantillas HTML y pasarles datos dinámicos desde la aplicación Flask, hay que tomar encuenta que se crea la carpeta llamada templates ya que flask reconoce este nombre de manera automatica y no habria que especificar la ruta del archivo html, al menos que se cree una carpeta dentro de templates, aqui explico el codigo html que usamos:

<h3>index</h3>

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <!-- Definimos la codificación de caracteres y la escala inicial para dispositivos móviles -->
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <!-- El título de la página se toma del diccionario 'data' que se pasa desde la aplicación Flask -->
      <title>{{ data.titulo }}</title>
    </head>
    <body>
      <!-- Mostramos el nombre de la tabla, aunque en el código Python no se está usando -->
      <h1>{{ data.tabla }}</h1>
    
      <!-- Comprobamos si hay empleados en la tabla -->
      {% if data.num_empleados > 0 %}
      <!-- Si hay empleados, mostramos una tabla con los nombres -->
      <table style="border: 10cm;">
        <tr>
            <th>Empleados</th> <!-- Encabezado de la columna de nombres -->
        </tr>
        
        <!-- Iteramos sobre cada empleado en la lista de empleados -->
        {% for empleado in data.empleados %}
            <tr>
                <td>
                    <!-- Mostramos el nombre de cada empleado en un elemento de la tabla -->
                    {{ empleado['Nombre'] }}
                </td>
            </tr>
        {% endfor %}
        
      </table>
      <!-- Si no hay empleados en la tabla, mostramos un mensaje -->
    {% else %}
      <h2>No existen empleados</h2>
    {% endif %}
    </body>
    </html>
    
Comentarios detallados:

{{ data.titulo }}: Renderiza el título de la página utilizando el valor proporcionado en el diccionario data desde la aplicación Flask.<br>
{{ data.tabla }}: Muestra el nombre de la tabla, aunque este valor no está siendo utilizado en el código Python.
{% if data.num_empleados > 0 %}: Verifica si hay empleados en la tabla utilizando el número de empleados proporcionado en el diccionario data.<br>
{% for empleado in data.empleados %}: Itera sobre cada empleado en la lista de empleados obtenida desde la base de datos.<br>
{{ empleado['Nombre'] }}: Muestra el nombre de cada empleado en un elemento de la tabla.<br>
{% else %}: Se ejecuta si no hay empleados en la tabla, mostrando un mensaje indicando que no existen empleados.

  
<h2>References</h2>
Azabache, G. (2021, September 1). Qué es REST, RESTFul, API RESTFul y JSON. Brave Developer. Retrieved April 5, 2024, from https://bravedeveloper.com/2021/09/01/que-es-rest-restful-api-restful-y-json/<br>
IBM Cloud®. (n.d.). ¿Qué es MongoDB? IBM. Retrieved April 5, 2024, from https://www.ibm.com/mx-es/topics/mongodb<br>
Muñoz, J. D. (2017, November 17). Qué es Flask y ventajas que ofrece. OpenWebinars. Retrieved April 5, 2024, from https://openwebinars.net/blog/que-es-flask/<br>
Postman, Inc. (n.d.). Postman API Platform | Sign Up for Free. Retrieved April 5, 2024, from https://www.postman.com/<br>
Amazon Web Services, Inc. (n.d.). ¿Qué es Python? - Explicación del lenguaje Python - AWS. Amazon AWS. Retrieved April 6, 2024, from https://aws.amazon.com/es/what-is/python/
</center>
