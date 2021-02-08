import sys
import os
from os import system, name as sysname
import json
from classArchivoPersona import FilePersona
from classArchivoMaterial import FileMaterial
from classArchivoPrestamo import FilePrestamo
from classPersona import Persona
from classMaterial import Material
from classPrestamo import Prestamo
from classMySQLdb import database
#from classMongodb import database

class main: 
    def __init__(self):
        self.listaPersonas = Persona
        self.listaMateriales = Material
        self.listaPrestamos = Prestamo
        
        self.pers = FilePersona.read()
        Persona.updateLista(self.pers)
        
        self.materiales = FileMaterial.read()
        Material.updateLista(self.materiales)
        self.prestamos = FilePrestamo.read()
        Prestamo.updateListaPrestamos(self.prestamos)
        self.opcion = -1
        self.persona=None
        self.material=None

    def menu(self):
        print("|************************|")
        print("|    CENTRO DEPORTIVO    |")
        print("|************************|")
        print("| 1. Clientes            |")
        print("| 2. Materiales          |")
        print("| 3. Préstamos           |")
        print("| 0. Salir               |")
        print(" ************************\n")
        self.opcion = int(input("¿Qué acción desea realizar? "))
        if self.opcion== 1:
            self.menuPersona()
        elif self.opcion== 2:
            self.menuMaterial()
        elif self.opcion== 3:
            self.menuPrestamo()
        elif self.opcion == 4:
            idPersona = int(input("ID del ciente: "))
            database.eliminar(database, idPersona)
        elif self.opcion == 5:
            idPersona = int(input("ID del ciente: "))
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo appellido: ")
            database.actualizar(database, nombre, apellido, idPersona)
        elif self.opcion == 0:
            sys.exit(0)
        else: 
            print('\n  ¡Opción inválida!')
        os.system("pause")

    def menuPersona(self):
        self.clear()
        print("|******************************|")
        print("| Clientes                     |")
        print("|******************************|")
        print("| 1. Ver clientes              |")
        print("| 2. Registrar cliente         |")
        print("| 3. Buscar cliente por nombre |")
        print("| 4. Buscar cliente por ID     |")
        print("| 5. Actualizar cliente        |")
        print("| 6. Eliminar cliente          |")
        print("| 0. Salir.....................|")
        print(" ******************************\n")
        respuesta=int(input("¿Qué acción desea realizar? "))
        if respuesta == 1:
            print("\n________Clientes________")
            #Persona.obtener()
            database.mostrarPersonas(database)

        elif respuesta == 2:
            print("\n_____Registrar Cliente_____")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese appellido: ")
            self.listaPersonas.Registrar(nombre, apellido)
            FilePersona.save()
            database.insertarPersona(database, nombre, apellido)
            print("\n   ¡¡Registro exitoso!!")

        elif respuesta == 3:
            print("\n_____Buscar Cliente_____")
            nombre = input("Ingrese nombre: ")
            self.listaPersonas.searchPersona(nombre)

        elif respuesta == 4:
            print("\n_____Buscar Cliente_____")
            idPersona = int(input("Ingrese id: "))
            self.listaPersonas.searchIdPersona(idPersona)

        elif respuesta == 5:
            print("\n_____Actualizar Cliente_____")
            idPersona = int(input("ID del ciente: "))
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo appellido: ")
            self.listaPersonas.updatePersona(idPersona, nombre, apellido)
            FilePersona.save()
            database.actualizarPersona(database, nombre, apellido, idPersona)

        elif respuesta == 6:
            print("\n_____Eliminar Cliente_____")
            idPersona = int(input("ID del ciente: "))
            self.listaPersonas.removePersona(idPersona)
            FilePersona.save()
            database.eliminarPersona(database, idPersona)

        elif(respuesta== 0):
            self.clear()
        return respuesta

    def menuMaterial(self):
        self.clear()
        print("|******************************|")
        print("| Materiales                   |")
        print("|******************************|")
        print("| 1. Ver materiales            |")
        print("| 2. Registrar material        |")
        print("| 3. Buscar material por nombre|")
        print("| 4. Buscar material por ID    |")
        print("| 5. Actualizar material       |")
        print("| 6. Eliminar material         |")
        print("| 0. Salir.....................|")
        print(" ******************************\n")
        respuesta=int(input("¿Qué acción desea realizar? "))
        if respuesta == 1:
            print("\n________Artículos________")
            #Material.obtener()
            database.mostrarMateriales(database)

        elif respuesta == 2:
            print("\n_____Registrar Artículo_____")
            articulo = input("Ingrese artículo: ")
            cantidad = int(input("Ingrese cantidad: "))
            self.listaMateriales.Registrar(articulo, cantidad)
            FileMaterial.save()
            database.insertarMaterial(database, articulo, cantidad)
            print("\n   ¡¡Registro exitoso!!\n")

        elif respuesta == 3:
            print("\n_____Buscar Artículo_____")
            nombre = input("Ingrese nombre: ")
            print(self.listaMateriales.searchMaterial(nombre))

        elif respuesta == 4:
            print("\n_____Buscar Artículo_____")
            idMaterial = int(input("Ingrese id: "))
            print(self.listaMateriales.searchIdMaterial(idMaterial))

        elif respuesta == 5:
            print("\n_____Actualizar Artículo_____")
            idMaterial = int(input("ID del artículo: "))
            nombre = input("Nuevo nombre: ")
            cantidad = int(input("Nueva cantidad: "))
            self.listaMateriales.updateMaterial(idMaterial, nombre, cantidad)
            FileMaterial.save()
            database.actualizarMaterial(database, nombre, cantidad, idMaterial)

        elif respuesta == 6:
            print("\n_____Eliminar Artículo_____")
            idMaterial = int(input("ID del artículo: "))
            self.listaMateriales.removeMaterial(idMaterial)
            FileMaterial.save()
            database.eliminarMaterial(database, idMaterial)
        
        elif(respuesta== 0):
            self.clear()
        return respuesta

    def menuPrestamo(self):
        self.clear()
        print("|******************************|")
        print("| Préstamos                    |")
        print("|******************************|")
        print("| 1. Lista de préstamos        |")
        print("| 2. Registrar préstamo        |")
        print("| 3. Devolver artículo         |")
        print("| 0. Salir.....................|")
        print(" ******************************\n")
        respuesta=int(input("¿Qué acción desea realizar? "))
        if respuesta == 1:
            print("\n_____Préstamos_____")
            Prestamo.obtenerPrestamos()
            #database.mostrarPrestamos(database)

        elif respuesta == 2:
            print("\n_____Nuevo Préstamo_____")
            print("\n_____Clientes_____")
            Persona.obtener()
            idPersona = int(input("\nID del ciente: "))
            if Persona.searchIdPersona(idPersona) == False:
                os.system("pause")
                return menu()
            print("\n_____Artículos_____")
            Material.obtener()
            idMaterial = int(input("\nID del artículo: "))
            if Material.searchIdMaterial(idMaterial) == False:
                os.system("pause")
                return menu()
            cantidad = int(input("Cantidad: "))
            fecha = input("Fecha: ")
            self.listaPrestamos.SolicitarPrestamo(idPersona, idMaterial, cantidad, fecha)
            FileMaterial.save()
            FilePrestamo.save()
            database.insertarPrestamo(database, idPersona, idMaterial, cantidad, fecha)

        elif respuesta == 3:
            print("\n_____Péstamos Pendientes_____")
            Prestamo.obtenerPrestamos()
            idPrestamo = int(input("\nÍndice del préstamo: "))
            Prestamo.devolverMaterial(idPrestamo)
            FileMaterial.save()
            FilePrestamo.save()
            database.eliminarPrestamo(database, idPrestamo)
        
        elif(respuesta== 0):
            self.clear()
        return respuesta

    def clear(self):
        if sysname == 'nt':
            _ = system('cls')


if __name__ == "__main__":
    main=main()    
    while main.opcion!='0':
        main.menu()
