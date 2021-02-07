from classMaterial import Material
from classPersona import Persona
#Prestamos
listaPrestamos = []

class Prestamo():
    def __init__(self, persona, material, cantidad, fecha):
        self.idPersona = persona
        self.material = material
        self.cantidad = cantidad
        self.fecha = fecha

    @staticmethod
    def getDicccionarioPrest():
        dic = []
        for i in listaPrestamos:
            dic.append({"persona":i.get('persona'), "material":i.get('material'), "cantidad":i.get('cantidad'), "fecha":i.get('fecha')})
        return dic
    
    def updateListaPrestamos(lista):
        listaPrestamos.extend(lista)
        return listaPrestamos

    def SolicitarPrestamo(persona, material, cantidad, fecha): 
        listaMateriales = Material.getLista()
        listaPersonas = Persona.getLista()
        for objPersona in listaPersonas:
            if objPersona['id'] == persona:
                person = objPersona['nombre']
        for objMaterial in listaMateriales:
            if objMaterial['id'] == material:
                article = objMaterial['articulo']
                cant = objMaterial['cantidad']
                if cant >= cantidad:
                    cant = cant - cantidad
                    Material.updateMaterial(material, article, cant)
                    prestamos = {}
                    prestamos['persona'] = person
                    prestamos['material'] = article
                    prestamos['cantidad'] = cantidad
                    prestamos['fecha'] = fecha
                    listaPrestamos.append(prestamos)
                    print("\n   ¡¡Prestamo exitoso!!\n")
                    return True
                print ("\n   ¡No está disponible la cantidad solicidad!\n")
                return False

    def obtenerPrestamos():
        for prestamo in listaPrestamos:
            persona = prestamo.get('persona')
            material = prestamo.get('material')
            cant = prestamo.get('cantidad')
            fecha = prestamo.get('fecha')
            print(str(persona) + ' ' + str(material) + ' ' + str(cant) + ' ' + str(fecha))

    def removePrestamo(indice=None):
        if indice!=None:
            listaPrestamos.pop(indice)
            return print('\n ¡Préstamo eliminado!\n')
        return print ('\n ¡El id no existe!\n')

    def devolverMaterial(indice=None): 
        listaMateriales = Material.getLista()
        if indice!=None:
            for objPrestamo in listaPrestamos:
                for objMaterial in listaMateriales:
                    if objMaterial['articulo'] == objPrestamo['material']:
                        cant = objMaterial['cantidad']
                        id = objMaterial['id']
                        material = objMaterial['articulo']
                        cantidad = objPrestamo['cantidad']
                        cantid = cant + cantidad
                        Material.updateMaterial(id, material, cantid)
                        Prestamo.removePrestamo(indice)
                        print("\n   ¡¡Devolución exitosa!!\n")
                        return True
        print ("\n   ¡El préstamo no existe!\n")
        return False