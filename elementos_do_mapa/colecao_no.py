from time import sleep
from A_star.distancias_euclidianas import distancia_euclidiana, euclidianas
from elementos_do_mapa.no import No
from copy import deepcopy


class Colecao_No:

    _instance = None

    def __init__(self, lista_nomes):
        lista_nos = []
        #Vai criar a lista com instâncias de nó a partir do map de distâncias euclidianas que está na pasta A_estrela
        for nome in lista_nomes:
            lista_nos.append(No(nome, distancia_euclidiana(nome)))

        self._lista_nos = lista_nos

    #Singleton
    @classmethod
    def instance(self):
        if self._instance is None:
            self._instance = Colecao_No(euclidianas)
        return self._instance

    def get_lista_nos(self):
        #deepcopy faz uma cópia da lista com a certeza de que o python não vai entregar o mesmo objeto
        return deepcopy(self._lista_nos)

    def get_um_no(self, nome_do_no):
        for no in self.get_lista_nos():
            if no.get_nome() == nome_do_no:
                return no
        return "Não há nó com esse nome"