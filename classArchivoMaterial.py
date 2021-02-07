from os import path
import json
from classMaterial import Material

class FileMaterial:
    @staticmethod
    def save():
        with open("materiales.json", "w", encoding="utf-8") as file:
            json.dump(Material.getDicccionario(), file, indent=4, ensure_ascii=False)

    @staticmethod
    def read():
        if path.exists("materiales.json"): 
            with open ('materiales.json', 'r', encoding="utf-8") as file:
                new_dic = json.load(file)
            return new_dic