import json

listaPersonas = []

class Persona():
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.prestamos = []

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def getDicccionario():
        dic = []
        for i in listaPersonas:
            dic.append({"id":i.get('id'), "nombre":i.get('nombre'), "apellido":i.get('apellido')})
        return dic

    def updateLista(lista):
        listaPersonas.extend(lista)
        return listaPersonas

    def obtener():
        for objLista in listaPersonas:
            id = objLista.get('id')
            nombre = objLista.get('nombre')
            apellido = objLista.get('apellido')
            print(str(id) + '  ' + nombre + '  ' + apellido)

    def Registrar(nombre, apellido): 
        idList = len(Persona.getDicccionario())
        idList += 1
        personas = {}
        personas['id'] = idList
        personas['nombre'] = nombre
        personas['apellido'] = apellido
        listaPersonas.append(personas)

    def searchPersona(nombre=None):
        if nombre!=None:
            i=0
            for persona in listaPersonas:
                if persona['nombre'] == nombre:
                    print('  ¡Cliente encontrado! -> ' + str(persona.get('id')) + ' ' + persona.get('nombre') + ' ' + persona.get('apellido'))
                    return True
                i += 1
            print ('  ¡El cliente no existe!') 
            return False
        return None

    def searchIdPersona(id=None):
        if id!=None:
            i=0
            for persona in listaPersonas:
                if persona['id'] == id:
                    print('  ¡Cliente encontrado! -> ' + str(persona.get('id')) + ' ' + persona.get('nombre') + ' ' + persona.get('apellido'))
                    return True
                i += 1
            print ('  ¡El cliente no existe!') 
            return False
        return None
    
    def updatePersona(id, nombre, apellido):
        if id!=None:
            for persona in listaPersonas:
                if persona['id'] == id:
                    persona['nombre'] = nombre
                    persona['apellido'] = apellido
                    return print('\n¡Datos actualizados!\n')
            return print (' ¡El id no existe!\n')
        return None

    def removePersona(id=None):
        if id!=None:
            i=0
            for persona in listaPersonas:
                if persona['id'] == id:
                    listaPersonas.pop(i)
                    return print(' ¡Cliente eliminado!')
                i+=1
            return print (' ¡El id no existe!\n')
        return None

    def getLista():
        return listaPersonas