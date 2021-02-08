import pymongo

class database:
    def __init__(self):
        self.conectar()

    def conectar():
        client = pymongo.MongoClient("mongodb+srv://nayeli-esquivel:nayeli1@cluster0.r1dmz.mongodb.net/test?retryWrites=true&w=majority")
        mybd = client.centro_deportivo
        return mybd

#Personas--

    def mostrarPersonas(self):
        #client = pymongo.MongoClient("mongodb+srv://Admin:admin@admin.h1pgq.mongodb.net/centro_deportivo?retryWrites=true&w=majority")
        mybd = self.conectar()
        mycol = mybd.personas

        for x in mycol.find():
            print(x)

    def insertarPersona(self, nombre, apellido):
        mybd = self.conectar()
        mycol = mybd.personas


        mydict = { "nombre": nombre, "apellido": apellido }

        mycol.insert_one(mydict)

    def actualizarPersona(self, nombre, apellido, id):
        mybd = self.conectar()
        mycol = mybd.personas

        myquery = { "id": id }
        newvalues = { "$set": { "nombre": nombre, "apellido":apellido } }

        mycol.update_one(myquery, newvalues)

    def eliminarPersona(self, id):
        mybd = self.conectar()
        mycol = mybd.personas

        myquery = {"id": id}
        mycol.delete_one(myquery)

#Materiales--
    def mostrarMateriales(self):
        mybd = self.conectar()
        print(mybd)
        mycol = mybd.materiales
        print(mycol)

        for x in mycol.find():
            print(x)

    def insertarMaterial(self, articulo, cantidad):
        mybd = self.conectar()
        mycol = mybd.materiales


        mydict = { "articulo": articulo, "cantidad": cantidad }

        mycol.insert_one(mydict)

    def actualizarMaterial(self, articulo, cantidad, id):
        mybd = self.conectar()
        mycol = mybd.materiales

        myquery = { "id": id }
        newvalues = { "$set": { "articulo": articulo, "cantidad":cantidad } }

        mycol.update_one(myquery, newvalues)

    def eliminarMaterial(self, id):
        mybd = self.conectar()
        mycol = mybd.materiales

        myquery = {"id": id}
        mycol.delete_one(myquery)

#Prestamos--
    def mostrarPrestamos(self):
        mybd = self.conectar()
        print(mybd)
        mycol = mybd.prestamos
        print(mycol)

        for x in mycol.find():
            print(x)

    def insertarPrestamo(self, persona, material, cantidad, fecha):
        mybd = self.conectar()
        mycol = mybd.prestamos


        mydict = { "id_persona": persona, "id_material": material, "cantidad": cantidad, "fecha": fecha }

        mycol.insert_one(mydict)

    def actualizarPrestamo(self, persona, material, cantidad, fecha, id):
        mybd = self.conectar()
        mycol = mybd.prestamos

        myquery = { "id": id }
        newvalues = { "$set": { "id_persona": persona, "id_material": material, "cantidad": cantidad, "fecha": fecha } }

        mycol.update_one(myquery, newvalues)

    def eliminarPrestamo(self, id):
        mybd = self.conectar()
        mycol = mybd.prestamos

        myquery = {"id": id}
        mycol.delete_one(myquery)
