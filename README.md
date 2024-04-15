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
  
<h2>References</h2>
Azabache, G. (2021, September 1). Qué es REST, RESTFul, API RESTFul y JSON. Brave Developer. Retrieved April 5, 2024, from https://bravedeveloper.com/2021/09/01/que-es-rest-restful-api-restful-y-json/<br>
IBM Cloud®. (n.d.). ¿Qué es MongoDB? IBM. Retrieved April 5, 2024, from https://www.ibm.com/mx-es/topics/mongodb<br>
Muñoz, J. D. (2017, November 17). Qué es Flask y ventajas que ofrece. OpenWebinars. Retrieved April 5, 2024, from https://openwebinars.net/blog/que-es-flask/<br>
Postman, Inc. (n.d.). Postman API Platform | Sign Up for Free. Retrieved April 5, 2024, from https://www.postman.com/<br>
Amazon Web Services, Inc. (n.d.). ¿Qué es Python? - Explicación del lenguaje Python - AWS. Amazon AWS. Retrieved April 6, 2024, from https://aws.amazon.com/es/what-is/python/
</center>
