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
Si la base de datos principal sufre un colapso, una base de datos secundaria tomara su puesto asi logrando la continuidad de la prestacion del servicio. Esta replicacion es visible en la GUI de la pagina de MongoDB Atlas en:

    Databasses > NombreDelCluster > Overview

En el se puede visualizar la cantidad de replicas existentes y su jerarquia. Mas sin embargo solo es posible hacer cambios avanzados por medio del Mongo Shell.
 <br>

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
      <!-- Enlaces a archivos CSS y Bootstrap -->
      <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css')}}" >
      <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css')}}" >
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    </head>
    
Aquí se establece la estructura básica de un documento HTML, se configura la codificación de caracteres, la escala inicial para dispositivos móviles y se enlazan archivos CSS y la librería Bootstrap para el estilo de la página.

    <body>
      <center>
        <!-- Mostramos el nombre de la tabla, aunque en el código Python no se está usando -->
        <h1>{{ data.tabla }}</h1>
        <!-- Botón para crear un nuevo empleado -->
        <button type="button" class="btn btn-primary" onclick="redirectToCrear()">Crear Empleado</button>
        <!-- Tabla para mostrar los empleados -->
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Nombre</th>
                <th scope="col">Opciones</th>
              </tr>
            </thead>
            <tbody>
              <!-- Iniciamos un ciclo para mostrar los empleados -->
              {% for c in data.empleados %} 
                <tr>
                  <th>{{ loop.index }}</th> <!-- Utiliza loop.index para obtener el índice de la iteración -->
                    <td>{{ c['Nombre'] }}</td> <!-- Muestra el nombre del empleado -->
                    <td>
                      <!-- Enlace para redirigir a la página de actualización -->
                      <a href="{{ url_for('redirigir_a_actualizar', id=c['_id']) }}" class="btn btn-outline-info btn-sm">
                        <i class="bi bi-pencil"></i> Editar 
                      </a>
                      <!-- Botón para eliminar un empleado -->
                      <button type="button" class="btn btn-outline-danger btn-sm" id="{{ c._id }}">
                        <i class="bi bi-trash"></i> Borrar
                      </button>
                    </td>
                  </tr>
              {% endfor %}
            </tbody>
          </table>
      </center>

    <!-- Script para manejar el evento de click en los botones de eliminación -->
    <script>
        // JavaScript code...
    </script>
    </body>
    </html>
Dentro del cuerpo del HTML, se muestra el nombre de la tabla (aunque parece que no se está utilizando actualmente en el código Python), se incluye un botón para crear un nuevo empleado y se genera una tabla para mostrar la lista de empleados. Para cada empleado en la lista, se genera una fila en la tabla que muestra el índice, el nombre del empleado y dos opciones: editar y borrar.

    <!-- Script para manejar el evento de click en los botones de eliminación -->
    <script>
      document.addEventListener('DOMContentLoaded', function () {
        const deleteButtons = document.querySelectorAll('.btn-outline-danger');

        deleteButtons.forEach(button => {
            button.addEventListener('click', async function () {
                const id = this.getAttribute('id');

                // Mostrar mensaje de confirmación
                const confirmed = window.confirm('¿Estás seguro de que deseas eliminar este empleado?');

                if (confirmed) {
                    try {
                        const response = await fetch(`/empleados/${id}`, {
                            method: 'DELETE'
                        });

                        const data = await response.json();
                        // Manejar la respuesta de la API DELETE según sea necesario
                        console.log(data);
                        // Refrescar la página después de eliminar el empleado
                        window.location.reload();
                    } catch (error) {
                        console.error('Error al eliminar empleado:', error);
                    }
                }
            });
        });
      });

      // Función para redirigir a la página de creación de empleado
      function redirectToCrear() {
        window.location.href = '/crear';  // Cambiar a la ruta de Flask que deseas (/crear en este caso)
      }
    </script>
Este script JavaScript maneja el evento de clic en los botones de eliminación. Cuando se hace clic en uno de esos botones, muestra un mensaje de confirmación y, si se confirma, envía una solicitud DELETE al servidor para eliminar al empleado correspondiente. Luego, recarga la página para mostrar la lista actualizada de empleados. Además, hay una función redirectToCrear que redirige al usuario a la página de creación de empleado.
    
Comentarios detallados:

{{ data.titulo }}: Renderiza el título de la página utilizando el valor proporcionado en el diccionario data desde la aplicación Flask.<br>
{{ data.tabla }}: Muestra el nombre de la tabla, aunque este valor no está siendo utilizado en el código Python.
{% if data.num_empleados > 0 %}: Verifica si hay empleados en la tabla utilizando el número de empleados proporcionado en el diccionario data.<br>
{% for empleado in data.empleados %}: Itera sobre cada empleado en la lista de empleados obtenida desde la base de datos.<br>
{{ loop.index }}: agrega loop.index para obtener el índice de la iteración.<br>
{{ c.['_id']  }}: agrega el valor del id correspondiente al hipervinculo.<br>
{{ c._id  }}: agrega el valor del id correspondiente al boton.<br>
{{ empleado['Nombre'] }}: Muestra el nombre de cada empleado en un elemento de la tabla.<br>
{% else %}: Se ejecuta si no hay empleados en la tabla, mostrando un mensaje indicando que no existen empleados.

<h3>crear</h3>

    <!DOCTYPE html>
    <html lang="en">

    <head>
      <!-- Definimos la codificación de caracteres y la escala inicial para dispositivos móviles -->
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Crear Empleado</title>
    </head>
    
Se inicia el documento HTML con la declaración <!DOCTYPE html> y se establecen metadatos como la codificación de caracteres y la escala inicial para dispositivos móviles en la sección <head>. El título de la página se establece como "Crear Empleado".

    <body>
      <h1>Crear Empleado</h1>
      <form id="createForm">
        <!-- Etiqueta y campo de entrada para el nombre del empleado -->
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
        <br><br>
        <!-- Botón para enviar el formulario y crear el empleado -->
        <button type="submit">Crear Empleado</button>
        <!-- Botón para volver al índice -->
        <button id="redirectBtn" type="button" class="btn btn-primary">Volver al Índice</button>
      </form>

      <!-- Div para mostrar la respuesta de la creación del empleado -->
      <div id="response"></div>
      
En el cuerpo del HTML, se encuentra el contenido principal de la página. Hay un encabezado que indica "Crear Empleado". Luego, hay un formulario con ID "createForm" que permite al usuario ingresar el nombre del empleado. El formulario tiene un botón de tipo "submit" para enviar los datos y crear el empleado. También hay un botón con ID "redirectBtn" para volver al índice de la aplicación Flask. Además, hay un div con ID "response" que se utilizará para mostrar la respuesta de la creación del empleado.

    <script>
      // Obtener el formulario y el div de respuesta por su ID
      const form = document.getElementById('createForm');
      const responseDiv = document.getElementById('response');

      // Agregar un evento 'submit' al formulario
      form.addEventListener('submit', async function (e) {
        e.preventDefault(); // Evitar el comportamiento por defecto del formulario

        // Obtener el valor del nombre del empleado
        const nombre = document.getElementById('nombre').value;

        try {
            // Realizar una solicitud POST a la API para crear un nuevo empleado
            const response = await fetch('/empleados', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ Nombre: nombre }) // Enviar el nombre del empleado en formato JSON
            });

            // Obtener la respuesta en formato JSON
            const data = await response.json();
            // Mostrar la respuesta en el div de respuesta
            responseDiv.innerHTML = JSON.stringify(data, null, 2);

            // Redirigir al usuario a la página principal después de la creación
            window.location.href = '/';
        } catch (error) {
            // Mostrar un mensaje de error en el div de respuesta en caso de error
            responseDiv.innerHTML = JSON.stringify({ error: 'Error al realizar la solicitud' }, null, 2);
        }
      });

      // Función para redirigir al índice al hacer clic en el botón 'Volver al Índice'
      function redirectToIndex() {
        window.location.href = '/';  // Cambia '/' a la ruta del índice de tu aplicación Flask si es diferente
      }

      // Agregar un evento 'click' al botón y llamar a la función de redirección
      document.getElementById('redirectBtn').addEventListener('click', redirectToIndex);
    </script>
Este script JavaScript maneja la lógica de la página de creación de empleados:
<ul>
    <li>Obtiene el formulario y el div de respuesta por sus IDs.</li>
    <li>Agrega un evento 'submit' al formulario para capturar el envío de datos.</li>
    <li>Dentro del evento 'submit':</li>
    <ul>
      <li>Evita el comportamiento por defecto del formulario.</li>
      <li>Obtiene el valor del nombre del empleado del campo de entrada.</li>
      <li>Realiza una solicitud POST a la API de Flask para crear un nuevo empleado, enviando el nombre del empleado en formato JSON.</li>
      <li>Muestra la respuesta de la creación del empleado en el div de respuesta.</li>
      <li>Redirige al usuario a la página principal después de la creación del empleado.</li>
    </ul>
    <li>Define una función redirectToIndex para redirigir al índice al hacer clic en el botón "Volver al Índice".</li>
    <li>Agrega un evento 'click' al botón "Volver al Índice" para llamar a la función de redirección cuando se hace clic en él.</li>
</ul>

<center>                              
  <h1> Herramientas para realizar las API</h1>
 <h2> Para el funcionamiento se necesitan las siguientes librerias: </h2>
  
    from flask import Flask, redirect, jsonify, request
    from pymongo import MongoClient
    from bson import json_util
    
De flask importamos flask para las funciones del framework, redirect para tener response, jsonify para devolver formatos json, request para traer informacion por ejemplo de la base de datos. <br>
De pymongo importamos MongoClient para interactuar con mongodb. <br>
De bson importamos json_util para utilidades con el formato json, por ejemplo volver en formato json la informacion que se trae de la base de datos. <br>
<br>
<h2>Ejemplo de API con el metodo GET para obtener los empleados</h2>
En la ruta /empleados usamos el metodo GET, definimos get_empleados(), empleados sera igual a una lista buscada en empleados_collection, response sera igual empleados traido en formato json con ayuda de json_util.dumps y retornamos response.
Lo demas es en caso de error


           # API método GET para obtener todos los empleados
            @app.route('/empleados', methods=['GET'])
            def get_empleados():
                empleados = list(empleados_collection.find())  # Obtener todos los empleados de la colección
                response = json_util.dumps(empleados)  # Convertir la lista de empleados a formato JSON
                return Response(response, mimetype='application/json')  # Devolver la respuesta JSON
<h2>Ejemplo API con el metodo GET para buscar a un empleado</h2>
Se crea la ruta /empleados/<id> utilizando el metodo GET, se define get_empleado(id), se busca en la coleccion de empleados uno por medio del id, si se encuentra se convierte la informacion a json y se devuelve la respuesta, en caso de que no se encuentre se retorna la respuesta negativa.


    # API método GET para obtener un empleado específico por su ID
    @app.route('/empleados/<id>', methods=['GET'])
    def get_empleado(id):
        empleado = empleados_collection.find_one({'_id': ObjectId(id)})  # Obtener un empleado de la colección
        if empleado:
            response = json_util.dumps(empleado)  # Convertir el empleado a formato JSON
            return Response(response, mimetype='application/json')  # Devolver la respuesta JSON
        else:
            return not_found() # Devolver la respuesta
<h2>Ejemplo API con el metodo POST para crear empleados</h2>
En la ruta /empleados se usa el metodo POST, se define post_empleados, con request se reciben los datos en json, se verifica si Nombre esta entre los datos, se prepara para insertar el empleado en la coleccion con un json y el id generado,  al  final retorna la respuesta; en caso de que no se proporcione un nombre deberia generar error.


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
<h2>Ejemplo de API con el metodo DELETE para eliminar un empleado</h2>
En la ruta /empleados/<id> se usa el metodo DELETE, se define delete_empleado(id), se elije un empleado de la coleccion para eliminar por medio del id, se guarda el mensaje de que se borro y se retorna este.


    # API método DELETE para eliminar un empleado por su ID
    @app.route('/empleados/<id>', methods=['DELETE'])
    def delete_empleado(id):
        empleados_collection.delete_one({'_id': ObjectId(id)})  # Elegir a un empleado para eliminar
        response = jsonify({'mensaje' : 'Empleado ' + id + ' ha sido borrado correctamente'})  # Mensaje que el empleado fue borrado correctamente
        return response
<h2>Ejemplo de API con el metodo PUT para actualizar un empleado</h2>
En la ruta /empleados/<id> se usa el metodo PUT, se define update_empleado(id), se verifica el si el id es valido, se verifica si el nombre esta en el json, se actualiza el empleado en la base de datos, en el caso de que los datos sean invalidos esto no procede.


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
<h2>Manejo del eror 404 para las APIs</h2>
Se usa el controlador de error de cabesera errorhandler(404), se define not_found(error=None), en response se guarda el mensaje en json y se retorna este mensaje ademas del status.

    # Manejador de errores para el código de estado 404 (Not Found)
    @app.errorhandler(404)
    def not_found(error=None):
        response = jsonify({
            'mensaje': 'Recurso no encontrado: ' + request.url,
            'status': 404
        })
        response.status_code = 404
        return response
<h1>Pruebas en Postman</h1><br>
<h2>Mostrar todos GET</h2>

![MostrarTodos](imgs_postman/postman_mostrartodos.jpeg)
<h2>Mostrar uno GET</h2>

![Mostraruno](imgs_postman/postman_mostraruno.jpeg)
<h2>Crear uno Post</h2>

![Crear](imgs_postman/postman_crear.jpeg)
<h2>Actualizar uno PUT</h2>

![Actualizar](imgs_postman/postman_actualizar.jpeg)
<h2>Eliminar uno DELETE</h2>

![Eliminar](imgs_postman/postman_eliminar.jpeg)
<h1>Uso de REST en las API y que las hace una APIRESTFUL</h1>
El enfoque REST se basa en principios simples y utiliza el protocolo HTTP para realizar operaciones sobre recursos identificados por URLs; este código sigue el enfoque REST al utilizar URLs para identificar recursos, métodos HTTP para definir operaciones sobre esos recursos y formatos de datos estándar (como JSON) para representar los datos. Esto hace que la API sea RESTful porque sigue los principios de REST para diseñar servicios web.
<h2>operaciones CRUD (Crear, Leer, Actualizar, Eliminar) se implementan utilizando los métodos HTTP estándar</h2>
POST crea un nuevo empleado.<br>
GET obtiene todos los empleados o un empleado específico por su ID.<br>
DELETE elimina un empleado por su ID.<br>
PUT actualiza un empleado por su ID.<br>
</center> 

  
<h2>References</h2>
Azabache, G. (2021, September 1). Qué es REST, RESTFul, API RESTFul y JSON. Brave Developer. Retrieved April 5, 2024, from https://bravedeveloper.com/2021/09/01/que-es-rest-restful-api-restful-y-json/<br>
IBM Cloud®. (n.d.). ¿Qué es MongoDB? IBM. Retrieved April 5, 2024, from https://www.ibm.com/mx-es/topics/mongodb<br>
Muñoz, J. D. (2017, November 17). Qué es Flask y ventajas que ofrece. OpenWebinars. Retrieved April 5, 2024, from https://openwebinars.net/blog/que-es-flask/<br>
Postman, Inc. (n.d.). Postman API Platform | Sign Up for Free. Retrieved April 5, 2024, from https://www.postman.com/<br>
Amazon Web Services, Inc. (n.d.). ¿Qué es Python? - Explicación del lenguaje Python - AWS. Amazon AWS. Retrieved April 6, 2024, from https://aws.amazon.com/es/what-is/python/
</center>
