from copy import deepcopy
import enum
import networkx as nx
from elementos_do_mapa.distancias_Euclidianas_Entre_Cidades import Distancias_Euclidianas_Entre_Cidades
from elementos_do_mapa.colecao_no import Colecao_No

class Mapa:

    _instance = None 

    def __init__(self):
        self._lista_abertos = []
        self._lista_fechados = []
        self._caminho_solucao = []
        
        
        self._grafo = nx.read_edgelist('./elementos_do_mapa/grafos/cidades.txt', delimiter =",", data=[("distancia_real", int), ("velocidade_maxima", int)])

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

    def get_no_atual(self):
        return self.get_lista_solucao()[-1]

    def get_lista_solucao(self):
        return self._caminho_solucao

    def get_lista_abertos(self):
        return deepcopy(self._lista_abertos)

    def add_lista_solucao(self, nome_no):
        self._caminho_solucao.append(nome_no)

    def remove_lista_solucao(self, nome_no):
        try:
            self._caminho_solucao.remove(nome_no)
            return "no: " + nome_no + " foi removido da lista de solução"
        except:
            return "Não há ocorrência desse nó na lista de solução"

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

    def get_nos_adjacentes(self, nome_no):
        map = self._grafo[nome_no]
        lista_adjacentes = []

        for grafo in map:
            if self._lista_fechados.count(grafo) < 1:
                lista_adjacentes.append(grafo)
        
        return lista_adjacentes

    #Isso pode ser um ponto a se verificar depois por conta de desempate de custos

    def get_no_menor_custo(self, lista_nos):
        no_com_menor_custo = None
        menor_custo = float("inf")
        # colecao_euclidianas = Colecao_No(self.get_no_objetivo())
        lista_heuristicas_calculadas = []

        for nome_no in lista_nos:
            nos_adjacentes = self.get_nos_adjacentes(nome_no)
            for no_adjacente in nos_adjacentes:
                # if self.funcao_heuristica(nome_no, no) < self._menor_custo:
                lista_heuristicas_calculadas.append({"no_fechado":nome_no, "no_adjacente": no_adjacente, "f_de_x" : self.funcao_heuristica(nome_no, no_adjacente)})
                #print(lista_heuristicas_calculadas)

        for valor in lista_heuristicas_calculadas:
            if valor["f_de_x"] < menor_custo:
                menor_custo = valor["f_de_x"]
                no_com_menor_custo = valor

        return no_com_menor_custo #é um map com todas as infos

    def ir_para_no(self, nome_no):
        self.add_lista_fechados(nome_no)
        self.remove_lista_abertos(nome_no)

    def calcular_g_de_x(self, nome_no_1, nome_no_2):
        lista_nos_caminho = self.get_lista_solucao()
        #print(lista_nos_caminho)
        #print(range(len(lista_nos_caminho)))
        soma_de_g = 0
        for i in range(len(lista_nos_caminho)):
            try:
                soma_de_distancia = self.get_distancia_real_entre_nos(lista_nos_caminho[i], lista_nos_caminho[i+1])
                soma_de_velocidade = self.get_velocidade_maxima_entre_nos(lista_nos_caminho[i], lista_nos_caminho[i+1])
                # print(soma_de_distancia)
                # print(soma_de_velocidade)
                soma_de_g += soma_de_distancia/soma_de_velocidade
                #print(soma_de_g)
                # soma_de_g += self.get_distancia_real_entre_nos(lista_nos_caminho[i], lista_nos_caminho[i+1])/self.get_velocidade_maxima_entre_nos(lista_nos_caminho[i], lista_nos_caminho[i+1])
            except:
                soma_de_g += 0

        # soma_de_distancia += self.get_distancia_real_entre_nos(nome_no_1, nome_no_2)
        # soma_de_velocidade += self.get_distancia_real_entre_nos(nome_no_1, nome_no_2)
        print(self.get_distancia_real_entre_nos(nome_no_1, nome_no_2))
        print(self.get_velocidade_maxima_entre_nos(nome_no_1, nome_no_2))
        soma_de_g += (self.get_distancia_real_entre_nos(nome_no_1, nome_no_2)) / (self.get_velocidade_maxima_entre_nos(nome_no_1, nome_no_2))

        return soma_de_g


    def funcao_heuristica(self, nome_no_1, nome_no_2):
        #Aqui devemos pegar a aresta com base no no_1 e no_2 e distância euclidiana do nó 2 ao nó obejtivo pelo mapa
        g_de_x = self.calcular_g_de_x(nome_no_1, nome_no_2)
        print("G(x) entre " + nome_no_1 + " e " + nome_no_2 + " = " + str(g_de_x))

        distancia_euclidiana_ate_no_objetivo = Distancias_Euclidianas_Entre_Cidades.instance().get_distancia_entre_cidades(nome_no_2, self.get_no_objetivo())
        velocidade_maxima = 110

        return (g_de_x + (distancia_euclidiana_ate_no_objetivo/velocidade_maxima))




    def run_A_estela(self, nome_no_incial, nome_no_objetivo):
        self._cidade_inicial = nome_no_incial
        self._cidade_objetiva = nome_no_objetivo
        self.add_lista_fechados(nome_no_incial)
        self.add_lista_solucao(nome_no_incial)
        

        no_atual = nome_no_incial

        while no_atual != self._cidade_objetiva:
            self.add_lista_abertos(self.get_nos_adjacentes(no_atual))   
            # print("Lista fechados:")
            # print(self.get_lista_fechados()) 
            # print("Lista abertos:")
            # print(self.get_lista_abertos()) 
            # print("Lista solução:")
            # print(self.get_lista_solucao())

            no_menor_custo = self.get_no_menor_custo(self.get_lista_fechados())
            if no_menor_custo["no_fechado"] != self.get_lista_fechados()[-1]:
                posicao_no_remocao = self.get_lista_solucao().index(no_menor_custo["no_fechado"])
                self._caminho_solucao = self.get_lista_solucao()[-posicao_no_remocao:-1]
                self.add_lista_solucao(no_menor_custo["no_adjacente"])
            no_atual = no_menor_custo["no_adjacente"]

            self.add_lista_fechados(no_atual)
            self.remove_lista_abertos(no_atual)
            self.add_lista_solucao(no_atual)

        return self.get_lista_solucao()
    