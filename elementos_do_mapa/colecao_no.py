
from elementos_do_mapa.distancias_entre_cidades import Distancias_Entre_Cidades
from elementos_do_mapa.no import No
from copy import deepcopy

class Colecao_No:

    _instance = None
    

    def __init__(self, no_objetivo):
        distancias_Entre_Cidades = Distancias_Entre_Cidades.instance()
        lista_nos = []
        lista_nomes = distancias_Entre_Cidades.get_nomes_cidades_relacionadas(no_objetivo)
        #Vai criar a lista com instâncias de nó a partir do map de distâncias euclidianas que está na pasta A_estrela
        for nome in lista_nomes:
            lista_nos.append(No(nome, distancias_Entre_Cidades.get_distancia_entre_cidades(nome, no_objetivo)))

        self._lista_nos = lista_nos

    def get_lista_nos(self):
        #deepcopy faz uma cópia da lista com a certeza de que o python não vai entregar o mesmo objeto
        return deepcopy(self._lista_nos)

    def get_um_no(self, nome_do_no):
        for no in self.get_lista_nos():
            if no.get_nome() == nome_do_no:
                return no
        return "Não há nó com esse nome"