import mysql.connector

#Conexion a base de datos

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# La conexion se ha establecido?
#print(database)

#PERMITE EJECUTAR CONSULTAS
cursor = database.cursor(buffered=True)


# CREAR BASE DE DATOS
#cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#MOSTRAR BASES DE DATOS
#cursor.execute("SHOW DATABASES")
#for bd in cursor:
#    print(bd)


#CREAR TABLAS

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10, 2) not null,
    CONSTRAINT pk_vehiculos PRIMARY KEY(id) 
)
""")


#MOSTRAR TABLAS
"""
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
"""

#INSERTAR DATOS EN UNA TABLA
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', '18500')")



coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 25000),
    ('Citroen', 'Saxo', 50000),
    ('Mercedes', 'Clase C', 15000)
]


# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)



#GUARDAR CAMBIOS
database.commit()


cursor.execute("SELECT * FROM vehiculos")



# SACAR DATOS, tambien puede utilizarse fectchone para sacar el primer dato
result = cursor.fetchall()

print("-----TUS COCHES-----")
for coche in result:
    print(coche[1], coche[3])



# CONDICIONES CON WHERE

#cursor.execute("SELECT * FROM vehiculos WHERE precio > 5000 AND marca = 'Seat' ")


# BORRAR

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Citroen' ")
print(cursor.rowcount, 'Borrados!')


#ACTUALIZAR DATOS!!
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")

print(cursor.rowcount, "Actualizados!!")

#GUARDAR CAMBIOS
database.commit()

