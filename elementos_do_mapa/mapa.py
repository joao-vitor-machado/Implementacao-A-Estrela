from copy import deepcopy
import enum
import networkx as nx

from elementos_do_mapa.colecao_no import Colecao_No

class Mapa:

    def __init__(self, nome_no_incial, nome_no_objetivo):
        self._cidade_inicial = nome_no_incial
        self._cidade_objetiva = nome_no_objetivo
        self._lista_abertos = []
        self._lista_fechados = []
        self.add_lista_fechados(nome_no_incial)
        
        self._grafo = nx.read_weighted_edgelist('./elementos_do_mapa/grafos/cidades.txt', delimiter =",")


    def get_no_atual(self):
        return self.get_lista_fechados()[-1]

    def get_lista_abertos(self):
        return deepcopy(self._lista_abertos)

    def add_lista_abertos(self, nome_no):
        self._lista_abertos.append(nome_no)
        return "no: " + nome_no + " foi adicionado à lista de abertos"

    def remove_lista_abertos(self, nome_no):
        try:
            self._lista_abertos.remove(nome_no)
            return "no: " + nome_no + " foi removido da lista de abertos"
        except:
            return "não há nó com esse nome para ser removido"

    def get_lista_fechados(self):
        return deepcopy(self._lista_fechados)

    def add_lista_fechados(self, nome_no):
        self._lista_fechados.append(nome_no)
        return "no: " + nome_no + " foi adicionado à lista de fechados"

    def get_nos_adjacentes(self, nome_no):
        map = self._grafo[nome_no]
        lista_adjacentes = []

        for grafo in map:
            lista_adjacentes.append(grafo)
        
        return lista_adjacentes

    #Isso pode ser um ponto a se verificar depois por conta de desempate de custos
    def get_no_menor_custo(self, lista_nos):
        menor_custo = float("inf")
        no_com_menor_custo = None

        for nome_no in lista_nos:
            no = Colecao_No.instance().get_um_no(nome_no)
            if no.get_distancia_euclidiana() < menor_custo:
                menor_custo = no.get_distancia_euclidiana()
                no_com_menor_custo = no

        return no_com_menor_custo

    def ir_para_no(self, nome_no):
        self.add_lista_fechados(nome_no)
        self.remove_lista_abertos(nome_no)

    def run_A_estela(self):
        no_atual = self.get_no_atual()
        while no_atual != self._cidade_objetiva:
            lista_nos_adjacentes = self.get_nos_adjacentes(no_atual)
            no_menor_custo = self.get_no_menor_custo(lista_nos_adjacentes).get_nome()
            no_atual = no_menor_custo

            self.add_lista_fechados(no_atual)
            self.remove_lista_abertos(no_atual)


        return self.get_lista_fechados()
    