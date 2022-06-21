from copy import deepcopy
import enum
import random
import networkx as nx
from elementos_do_mapa.distancias_Euclidianas_Entre_Cidades import Distancias_Euclidianas_Entre_Cidades


class Mapa:

    _instance = None 

    def __init__(self):
        self._lista_abertos = []
        self._lista_fechados = []
        self._caminho_solucao = []
        
        self._grafo = nx.read_edgelist('./elementos_do_mapa/tabelas_info/cidades.txt', delimiter =",", data=[("distancia_real", int), ("velocidade_maxima", int)])


    @classmethod
    def instance(self):
        if self._instance == None:
            self._instance = Mapa()
        return self._instance



    def get_velocidade_maxima_entre_nos(self, nome_no_1, nome_no_2):
        properties_aresta = self._grafo[nome_no_1][nome_no_2]

        return properties_aresta["velocidade_maxima"]


    def get_distancia_real_entre_nos(self, nome_no_1, nome_no_2):
        properties_aresta = self._grafo[nome_no_1][nome_no_2]

        return properties_aresta["distancia_real"]


    def get_no_objetivo(self):
        return self._cidade_objetiva
   

    def get_lista_solucao(self):
        return self._caminho_solucao


    def get_lista_abertos(self):
        return deepcopy(self._lista_abertos)


    def add_lista_solucao(self, nome_no):
        self._caminho_solucao.append(nome_no)


    def add_lista_abertos(self, value):
        if type(value) is str:
            if self._lista_abertos.count(value) < 1 and self._lista_fechados.count(value) < 1:
                self._lista_abertos.append(value)
                return "no: " + value + " foi adicionado à lista de abertos"

        if type(value) is list:
            for no in value:
                if self._lista_abertos.count(no) < 1 and self._lista_fechados.count(no) < 1:
                    self._lista_abertos.append(no)
                    return "nos adicionados à lista de abertos"


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
        lista_nos_adjacentes = self.get_nos_adjacentes(nome_no)

        for no in lista_nos_adjacentes:
            self.add_lista_abertos(no)

        return "no: " + nome_no + " foi adicionado à lista de fechados"


    def remove_lista_solucao(self, nome_no):
        try:
            self._caminho_solucao.remove(nome_no)
            return "no: " + nome_no + " foi removido da lista de solução"
        except:
            return "Não há ocorrência desse nó na lista de solução"


    def get_nos_adjacentes(self, nome_no):
        map = self._grafo[nome_no]
        lista_adjacentes = []

        for grafo in map:
            #if self._lista_fechados.count(grafo) < 1:
            lista_adjacentes.append(grafo)
        
        return lista_adjacentes


    def funcao_heuristica(self, no):

        distancia_euclidiana_ate_no_objetivo = Distancias_Euclidianas_Entre_Cidades.instance().get_distancia_entre_cidades(no, self.get_no_objetivo())
        velocidade_media = 110

        return (float(distancia_euclidiana_ate_no_objetivo/velocidade_media))

    def funcao_heuristica_inadmissivel(self,no):
        distancia_euclidiana_ate_no_objetivo = Distancias_Euclidianas_Entre_Cidades.instance().get_distancia_entre_cidades(no, self.get_no_objetivo())
        velocidade_minima = 60

        return (float(distancia_euclidiana_ate_no_objetivo/velocidade_maxima))

    def funcao_avaliacao(self, g, h):
        return g + h
    

    def a_star_imp(self, no_inicial, no_objetivo):
        self._cidade_objetiva = no_objetivo

        custo_acumulado = {}
        custo_acumulado[no_inicial] = 0

        nos_anteriores = {}
        nos_anteriores[no_inicial] = no_inicial

        self.add_lista_abertos(no_inicial)

        while len(self._lista_abertos) > 0:
            no = None

            for n in self._lista_abertos:
                if no == None or self.funcao_avaliacao(custo_acumulado[n], self.funcao_heuristica(n)) < self.funcao_avaliacao(custo_acumulado[no], self.funcao_heuristica(no)):
                    no = n

            if no == None:
                break

            if no == no_objetivo:
                while nos_anteriores[no] != no:
                    self.add_lista_solucao(no)
                    no = nos_anteriores[no]
                
                self.add_lista_solucao(no_inicial)
                self._caminho_solucao.reverse()

                print("lista abertos: "+str(self.get_lista_abertos()))
                print(("lista fechados: "+str(self.get_lista_fechados())))

                return self.get_lista_solucao()
        
            for no_vizinho in self.get_nos_adjacentes(no):
                if no_vizinho not in self._lista_abertos and no_vizinho not in self._lista_fechados:
                    self.add_lista_abertos(no_vizinho)
                    nos_anteriores[no_vizinho] = no
                    custo_acumulado[no_vizinho] = custo_acumulado[no] + (self.get_distancia_real_entre_nos(no, no_vizinho)/self.get_velocidade_maxima_entre_nos(no, no_vizinho)) #funcao g(x)

                elif custo_acumulado[no_vizinho] > custo_acumulado[no] + (self.get_distancia_real_entre_nos(no, no_vizinho)/self.get_velocidade_maxima_entre_nos(no, no_vizinho)): #funcao g(x)
                    custo_acumulado[no_vizinho] = custo_acumulado[no] + (self.get_distancia_real_entre_nos(no, no_vizinho)/self.get_velocidade_maxima_entre_nos(no, no_vizinho)) #funcao g(x)
                    nos_anteriores[no_vizinho] = no

                    if no_vizinho in self._lista_fechados:
                        self.remove_lista_fechados(no_vizinho)
                        self.add_lista_abertos(no_vizinho)
                
                    
            self.add_lista_fechados(no)
            self.remove_lista_abertos(no)

            print("lista abertos: "+str(self.get_lista_abertos()))
            print(("lista fechados: "+str(self.get_lista_fechados())))

        print('Solucao inexistente')
        return None
