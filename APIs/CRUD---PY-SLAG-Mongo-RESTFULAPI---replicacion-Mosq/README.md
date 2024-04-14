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
