import os
import pandas as pd

class Distancias_Euclidianas_Entre_Cidades:

    _instance = None

    def __init__(self):
        self._db = None

    @classmethod
    def instance(self):
        if self._instance == None:
            self._instance = Distancias_Euclidianas_Entre_Cidades()
        return self._instance

    def set_db(self, db):
        self._db = db

    def get_db(self):
        if self._db == None:
            return "Não há db ainda"
        return self._db

    def get_distancias(self, nome_cidade):
        return self._db[nome_cidade]["Distancia"]

    def get_nomes_cidades_relacionadas(self, nome_cidade):
            return self._db[nome_cidade]["Cidade"]

    def get_distancia_entre_cidades(self, cidade_1, cidade_2):
        distancias_cidade_1 = self.get_nomes_cidades_relacionadas(cidade_1)
        

        index = None
        for i, cidade in enumerate(distancias_cidade_1):
            if cidade == cidade_2:
                index = i
        return self.get_distancias(cidade_1)[index]    