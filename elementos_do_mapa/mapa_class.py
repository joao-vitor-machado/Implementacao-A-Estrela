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

        for no in map:
            lista_adjacentes.append(no)
        
        return lista_adjacentes


    def funcao_heuristica(self, no):

        distancia_euclidiana_ate_no_objetivo = Distancias_Euclidianas_Entre_Cidades.instance().get_distancia_entre_cidades(no, self.get_no_objetivo())
        velocidade_media = 110

        return (float(distancia_euclidiana_ate_no_objetivo/velocidade_media))

    def funcao_heuristica_inadmissivel(self,no):
        distancia_euclidiana_ate_no_objetivo = Distancias_Euclidianas_Entre_Cidades.instance().get_distancia_entre_cidades(no, self.get_no_objetivo())
        velocidade_minima = 60

        return (float(distancia_euclidiana_ate_no_objetivo/velocidade_minima))

    def funcao_avaliacao(self, g, h):
        return g + h

    def g_de_x(self, no_1, no_2):
        return round((self.get_distancia_real_entre_nos(no_1, no_2)/self.get_velocidade_maxima_entre_nos(no_1, no_2)),2)
    
    def f_de_x(self, no, custo_acumulado):
        return self.funcao_avaliacao(custo_acumulado, self.funcao_heuristica_inadmissivel(no))


    def run_a_Estela(self, no_inicial, no_objetivo):

        self._cidade_objetiva = no_objetivo

        custo_acumulado = {}
        custo_acumulado[no_inicial] = 0

        #funciona como se fosse uma lista ligada
        nos_anteriores = {}
        nos_anteriores[no_inicial] = no_inicial

        self.add_lista_abertos(no_inicial)

        while len(self._lista_abertos) > 0:
            no_atual = None

            #está escolhendo qual será o nó atual
            for no_aberto in self._lista_abertos:
                if no_atual == None or self.f_de_x(no_aberto, custo_acumulado[no_aberto]) < self.f_de_x(no_atual, custo_acumulado[no_atual]):
                    no_atual = no_aberto
            
            if no_atual == None:
                break

            if no_atual == no_objetivo:

                self.add_lista_fechados(no_atual)
                self.remove_lista_abertos(no_atual)

                #Coloca o nó atual na solução até encontrar o nó anterior do nó inicial, que é o próprio nó inicial (vide linha 143)
                while nos_anteriores[no_atual] != no_atual:
                    self.add_lista_solucao(no_atual)
                    no_atual = nos_anteriores[no_atual]
                
                self.add_lista_solucao(no_atual)
                self._caminho_solucao.reverse()

                print("")
                print("<-------------------------------------------------------------------------->")
                print("")
                return self.get_lista_solucao()
        
            for no_adjacente in self.get_nos_adjacentes(no_atual):
                if no_adjacente not in self._lista_abertos and no_adjacente not in self._lista_fechados:
                    self.add_lista_abertos(no_adjacente)
                    nos_anteriores[no_adjacente] = no_atual
                    custo_acumulado[no_adjacente] = custo_acumulado[no_atual] + self.g_de_x(no_atual, no_adjacente)

                else:
                    if custo_acumulado[no_adjacente] > custo_acumulado[no_atual] + self.g_de_x(no_atual, no_adjacente): 
                        custo_acumulado[no_adjacente] = custo_acumulado[no_atual] + self.g_de_x(no_atual,no_adjacente) 
                        nos_anteriores[no_adjacente] = no_atual

                        if no_adjacente in self._lista_fechados:
                            self._lista_fechados.remove(no_adjacente)
                            self.add_lista_abertos(no_adjacente)
                
                    
            self.add_lista_fechados(no_atual)
            self.remove_lista_abertos(no_atual)

           
            print(("lista fechados: "+str(self.get_lista_fechados())))
            print("lista abertos: "+str(self.get_lista_abertos()))

        print('Solucao inexistente')
        return None
