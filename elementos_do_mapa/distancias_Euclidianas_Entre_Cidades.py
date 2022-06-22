import os
import pandas as pd

class Distancias_Euclidianas_Entre_Cidades:
    #O db que essa classe cuida nada mais é do que um dataframe pandas que lê os valores de uma tabela excel. Ele possui os valores de distância heurística entre uma cidade pra qualquer outra do grafo. Pra achar a lista de distâncias em relação a uma cidade você deve pegar esse df e acessar a chave com o nome da cidade pra qual você quer essas distâncias: grafo[cidade_que_quero] retorna todas as cidades e distâncias

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
        #vai pegar o índice da lista em que o nome da cidade da lista de distâncias bate com a cidade 2 e, usando esse index, ele acessa o mesmo index na lista de distâncias
        for i, cidade in enumerate(distancias_cidade_1):
            if cidade == cidade_2:
                index = i
        return self.get_distancias(cidade_1)[index]    