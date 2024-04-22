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

<h2>Pruebas de Replicaion</h2>

Con el fin de poner a prueba la replicacion, se intento forzar la replicacion primaria para que seda su puesto a las demas secundarias, durante esta etapa se hayo que:

<h3>Limitaciones del cluster</h3>

Gracias a que el presente proyecto usa un Cluster gratis (M0) muchos comandos de administracion estan desahabilitados asi como lo relata este <a href="https://www.mongodb.com/docs/atlas/unsupported-commands/">ARTICULO</a>

<h3>Soporte de OverLoad</h3>

Al ver que no era posible seder el puesto de la replicacion primario por medio de comandos, se intento inducir un ataque a la base de datos para sobrecargar la primaria y que una secundaria tomara su puesto. Se intento por medio de un ciclo:
      
      While

En el cual se realizaban inserciones sucesivas, pero al llevarlo a cabo la maquina atacante (Un PC de mesa Viejo) murio primero la maquina atacante que la base de datos. Por lo cual se encuentra que su soporte a sobrecarga es bueno
