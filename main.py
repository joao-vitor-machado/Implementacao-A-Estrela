import os
import networkx as nx
from elementos_do_mapa.distancias_entre_cidades import Distancias_Entre_Cidades
from elementos_do_mapa.mapa_class import Mapa
import pandas as pd


Distancias_Entre_Cidades.instance().set_db(pd.read_excel("./elementos_do_mapa/planilha_distancias.xlsx", sheet_name=None)) 

no_incial = "Araraquara"
no_objetivo = "Presidente_Prudente"

print(Mapa.instance().run_A_estela(no_incial, no_objetivo))
