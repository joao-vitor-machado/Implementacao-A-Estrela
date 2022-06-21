import os
import networkx as nx
from elementos_do_mapa.distancias_Euclidianas_Entre_Cidades import Distancias_Euclidianas_Entre_Cidades
from elementos_do_mapa.mapa_class import Mapa
import pandas as pd


Distancias_Euclidianas_Entre_Cidades.instance().set_db(pd.read_excel("./elementos_do_mapa/planilha_distancias.xlsx", sheet_name=None)) 

no_incial = "Araraquara"
no_objetivo = "Presidente_Prudente"

# print(Heuristica.calculate(no_incial, ""))

# print(distancia_real_entre_nos/velocidade_maxima_entre_nos) + (distancia_euclidiana_ate_no_objetivo/media_velocidade_maxima)

print(Mapa.instance().a_star_imp(no_incial, no_objetivo))