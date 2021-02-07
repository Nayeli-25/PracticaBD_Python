from os import path
import json
from classPersona import Persona

class FilePersona:
    @staticmethod
    def save():
        with open("personas.json", "w", encoding="utf-8") as file:
            json.dump(Persona.getDicccionario(), file, indent=4, ensure_ascii=False)

    @staticmethod
    def read():
        if path.exists("personas.json"): 
            with open('personas.json', 'rb') as file:
                new_dic = json.load(file)
        return new_dic
        