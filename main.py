import os
import networkx as nx
from elementos_do_mapa.distancias_entre_cidades import Distancias_Entre_Cidades
from elementos_do_mapa.mapa import Mapa
import pandas as pd

mapa = Mapa("Araraquara", "Presidente_Prudente")
distancias_entre_cidades = Distancias_Entre_Cidades(pd.read_excel("./elementos_do_mapa/planilha_distancias.xlsx", sheet_name=None)) 

print(distancias_entre_cidades.get_distancia_entre_cidades("Araraquara", "SP"))
