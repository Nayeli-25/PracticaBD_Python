from os import path
import json
from classPrestamo import Prestamo

class FilePrestamo:
    @staticmethod
    def save():
        with open("prestamos.json", "w", encoding="utf-8") as file:
            json.dump(Prestamo.getDicccionarioPrest(), file, indent=4, ensure_ascii=False)

    @staticmethod
    def read():
        if path.exists("prestamos.json"): 
            with open ('prestamos.json', 'r', encoding="utf-8") as file:
                new_dic = json.load(file)
            return new_dic