import os
import pandas as pd

class Distancias_Entre_Cidades:
    def __init__(self, db):
        self.db = db

    def get_distancias(self, nome_cidade):
        return self.db[nome_cidade]["Distancia"]

    def get_nomes_cidades_relacionadas(self, nome_cidade):
            return self.db[nome_cidade]["Cidade"]

    def get_distancia_entre_cidades(self, cidade_1, cidade_2):
        distancias_cidade_1 = self.get_nomes_cidades_relacionadas(cidade_1)

        index = None
        for i, cidade in enumerate(distancias_cidade_1):
            if cidade == cidade_2:
                index = i
        return self.get_distancias(cidade_1)[index]    