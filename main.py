import os
import networkx as nx
from elementos_do_mapa.distancias_Euclidianas_Entre_Cidades import Distancias_Euclidianas_Entre_Cidades
from elementos_do_mapa.mapa_class import Mapa
import pandas as pd


Distancias_Euclidianas_Entre_Cidades.instance().set_db(pd.read_excel("./elementos_do_mapa/tabelas_info/planilha_distancias.xlsx", sheet_name=None)) 

no_incial = "Barretos"
no_objetivo = "Taubate"

print("Caminho encontrado: "+str(Mapa.instance().run_a_Estela(no_incial, no_objetivo)))