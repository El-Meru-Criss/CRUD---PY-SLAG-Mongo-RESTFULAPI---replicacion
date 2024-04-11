/* Esta es una plantilla para el uso de MongoDB
Para hacer que realice los cambios, debe estar conectado a la BD
por medio de la extension de VS 
El usuario es: El-Meru-Criss
pass: 12345
URL: mongodb+srv://El-Meru-Criss:<password>@pruebas-criss.neht1oe.mongodb.net/
*/

// Aqui seleccionamos la base de datos que vamos a utilizar
use('empleados'); //Nombre de la BD

// Aqui insertamos datos a una "Tabla" que este dentro de la BD 
//el comando para insertar es "insertMany". Se puede insertar mas de un refistro a la vez
//Mongo no tiene una structura rigida, asi que puede agragar variables aun que no esten definidas
db.getCollection('empleado').insertMany([ //Nombre de la tabla
  { 'Cedula': '1001', 'Nombre': 'Cristian', 'apellido': 'Gonzalez', 'altura': 1.68 }, //la altura es una variable no definida
  { 'Cedula': '1001', 'Nombre': 'Cristian', 'apellido': 'Gonzalez', 'altura': 1.68 },
  { 'Cedula': '1001', 'Nombre': 'Cristian', 'apellido': 'Gonzalez', 'altura': 1.68 }, 
  { 'Cedula': '1002', 'Nombre': 'Steven', 'apellido': 'Porras' },
  { 'Cedula': '1003', 'Nombre': 'Mosquera', 'apellido': 'Mena', 'edad': 21 }, //La edad es una variable no definida
  { 'Cedula': '1003', 'Nombre': 'Mosquera', 'apellido': 'Mena', 'edad': 21 },
  { 'Cedula': '1003', 'Nombre': 'Mosquera', 'apellido': 'Mena', 'edad': 21 }, 
]);

//Consultamos informacion con el comando Find, en este caso queremos ver
//Toda la info de los empleados
var Empleados = db.getCollection('empleado').find({});

//Mostramos  la info optenida
console.log(Empleados);

//Aqui consultamos informacion con el comando find y lo almacenamos en una variable.
//En este caso es un conteo de cuantos empleados hay
var NumEmpleados = db.getCollection('empleado').find({}).count();

// Mostramos la info optenida
console.log(`${NumEmpleados} En la base de datos.`);

//Consultamos informacion con el comando Find, en este caso queremos ver
//Toda la info de un solo empleado
var Empleados = db.getCollection('empleado').find({'Cedula': '1001'});

//Mostramos  la info optenida
console.log(Empleados);

//Primera forma de eliminar Datos:
//Aqui queremos eliminar un  registro segun una cedula (Solo sirve uno a la vez)
db.getCollection('empleado').deleteOne({'Cedula': '1001'});

var NumEmpleados = db.getCollection('empleado').find({}).count();

// Mostramos la info optenida
console.log(`${NumEmpleados} En la base de datos.`);

//Segunda forma de eliminar Datos:
//Aqui queremos eliminar todos los registros Que coincidan con la cedula
db.getCollection('empleado').deleteMany({'Cedula': '1001'});

var NumEmpleados = db.getCollection('empleado').find({}).count();

// Mostramos la info optenida
console.log(`${NumEmpleados} En la base de datos.`);


//Ahora vamos a actualizar Datos

var nuevosDatos = { //Para actualizar, debe tener una variable con los nuevos datos
  $set: { //el operador $se es importante. no olvidar
      'Nombre': 'Brayan'
  }
};

//Primera forma:
//Con esta forma actualiza un dato a la vez

db.getCollection('empleado').updateOne({'Cedula': '1003'}, nuevosDatos); 

//Toda la info de un solo empleado
var Empleados = db.getCollection('empleado').find({'Cedula': '1003'});

//Mostramos  la info optenida
console.log(Empleados);

//Segunda forma:

var nuevosDatos = { //Para actualizar, debe tener una variable con los nuevos datos
  $set: { //el operador $se es importante. no olvidar
      'Nombre': 'Smith'
  }
};

//Con esta forma actualiza todos los dato a la vez que coincidan con la cedula seleccionada

db.getCollection('empleado').updateMany({'Cedula': '1003'}, nuevosDatos); 

//Toda la info de un solo empleado
var Empleados = db.getCollection('empleado').find({'Cedula': '1003'});

//Mostramos  la info optenida
console.log(Empleados);

//Aqui queremos eliminar todo en el documento
db.getCollection('empleado').deleteMany({});
