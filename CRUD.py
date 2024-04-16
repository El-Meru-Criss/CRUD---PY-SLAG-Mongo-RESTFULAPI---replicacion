from pymongo import MongoClient

# Datos de conexión
usuario = "El-Meru-Criss"
contraseña = "12345"
host = "pruebas-criss.neht1oe.mongodb.net"
puerto = 27017  # Puerto por defecto de MongoDB
nombre_bd = "empleados"

# URL de conexión a MongoDB
url_conexion = f"mongodb+srv://{usuario}:{contraseña}@{host}/{nombre_bd}"

# Crear una instancia de MongoClient y conectarse a la base de datos
cliente = MongoClient(url_conexion)
db = cliente[nombre_bd]

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

# Consultar información de todos los empleados
empleados = db["empleado"].find()

# Mostrar la información obtenida
for empleado in empleados:
    print(empleado)

# Contar el número de empleados
num_empleados = db["empleado"].count_documents({})

# Mostrar el número de empleados en la base de datos
print(f"{num_empleados} En la base de datos.")

# Consultar información de un solo empleado
empleado = db["empleado"].find({'Cedula': '1001'})

# Mostrar la información obtenida
print(empleado)

# Primera forma de eliminar un registro según una cedula (Solo uno a la vez)
db["empleado"].delete_one({'Cedula': '1001'})

# Contar el número de empleados
num_empleados = db["empleado"].count_documents({})

# Mostrar el número de empleados en la base de datos
print(f"{num_empleados} En la base de datos.")

# Segunda forma de eliminar todos los registros que coincidan con la cedula
db["empleado"].delete_many({'Cedula': '1001'})

# Contar nuevamente el número de empleados
num_empleados = db["empleado"].count_documents({})

# Mostrar el número de empleados en la base de datos
print(f"{num_empleados} En la base de datos.")

# Actualizar un dato de un empleado
nuevos_datos = {
    "$set": {
        'Nombre': 'Brayan'
    }
}
db["empleado"].update_one({'Cedula': '1003'}, nuevos_datos)

# Consultar información del empleado actualizado
empleados_actualizados = db["empleado"].find({'Cedula': '1003'})
for empleado in empleados_actualizados:
    print(empleado)

# Actualizar todos los datos de los empleados que coincidan con la cedula seleccionada
nuevos_datos = {
    "$set": {
        'Nombre': 'Smith'
    }
}
db["empleado"].update_many({'Cedula': '1003'}, nuevos_datos)

# Consultar información de los empleados actualizados
empleados_actualizados = db["empleado"].find({'Cedula': '1003'})
for empleado in empleados_actualizados:
    print(empleado)

# Eliminar todos los documentos en la colección 'empleado'
db["empleado"].delete_many({})