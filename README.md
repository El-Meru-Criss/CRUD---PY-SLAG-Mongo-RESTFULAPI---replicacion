<h1> Espacio del Criss -------------- </h1>
En este espacio se adjuntaran los protetipos que realice criss.
- Encargado de la BD

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
