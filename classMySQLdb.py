import mysql.connector

class database:
    def __init__(self):
        self.conectar()
    
    def conectar():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="centro_deportivo"
        )
        return mydb
#--------------- Personas ----------------------
    def mostrarPersonas(self):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM personas")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def insertarPersona(self, nombre, apellido):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        sql = "INSERT INTO personas (nombre, apellido) VALUES (%s, %s)"
        val = (nombre, apellido)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "registro insertado.")

    def actualizarPersona(self, nombre, apellido, id):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        sql = "UPDATE personas SET nombre = %s, apellido = %s WHERE id_persona = %s"
        val = (nombre, apellido, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "registro actualizado.")

    def eliminarPersona(self, id):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        sql = "DELETE FROM personas WHERE id_persona = %s"
        adr = (id, )
        mycursor.execute(sql, adr)
        mydb.commit()
        print(mycursor.rowcount, "registro eliminado")

#--------------- Materiales ----------------------
    def mostrarMateriales(self):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM materiales")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def insertarMaterial(self, articulo, cantidad):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        sql = "INSERT INTO materiales (articulo, cantidad) VALUES (%s, %s)"
        val = (articulo, cantidad)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "registro insertado.")

    def actualizarMaterial(self, articulo, cantidad, id):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        sql = "UPDATE materiales SET articulo = %s, cantidad = %s WHERE id_material = %s"
        val = (articulo, cantidad, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "registro actualizado.")

    def eliminarMaterial(self, id):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        sql = "DELETE FROM materiales WHERE id_material = %s"
        adr = (id, )
        mycursor.execute(sql, adr)
        mydb.commit()
        print(mycursor.rowcount, "registro eliminado")

#--------------- Préstamos ----------------------
    def mostrarPrestamos(self):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM préstamos")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def insertarPrestamo(self, persona, material, cantidad, fecha):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        sql = "INSERT INTO préstamos (id_persona, id_material, cantidad, fecha) VALUES (%s, %s, %s, %s)"
        val = (persona, material, cantidad, fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "registro insertado.")

    def actualizarPrestamo(self, persona, material, cantidad, fecha, id):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        sql = "UPDATE préstamos SET id_persona = %s, id_material = %s, cantidad = %s, fecha = %s WHERE id_prestamo = %s"
        val = (persona, material, cantidad, fecha, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "registro actualizado.")

    def eliminarPrestamo(self, id):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        id =+ 1
        sql = "DELETE FROM préstamos WHERE id_prestamo = %s"
        adr = (id, )
        mycursor.execute(sql, adr)
        mydb.commit()
        print(mycursor.rowcount, "registro eliminado")
