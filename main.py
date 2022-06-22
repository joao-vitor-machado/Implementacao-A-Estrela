import os
import networkx as nx
from elementos_do_mapa.distancias_Euclidianas_Entre_Cidades import Distancias_Euclidianas_Entre_Cidades
from elementos_do_mapa.mapa_class import Mapa
import pandas as pd

'''
OBSERVAÇÃO [1]: 

O código está configurado inicialmente para utilizar a heurística admissível.

Para utilizar a heurística inadmissível, troque a linha 131 do arquivo mapa_class.py:

anteriormente:
        return self.funcao_avaliacao(custo_acumulado, self.funcao_heuristica(no))

por:
        return self.funcao_avaliacao(custo_acumulado, self.funcao_heuristica_inadmissivel(no))


'''

'''
OBSERVAÇÃO [2]:

Para ver as opções de cidades inicial e destino a serem inseridas como valores no_incial e no_objetivo, acesse:

https://docs.google.com/spreadsheets/d/1WM2paiLwoMV4Ia1qWzuLPRp0SwrB4CCpaqiPFZlrt5s/edit?usp=sharing

'''

Distancias_Euclidianas_Entre_Cidades.instance().set_db(pd.read_excel("./elementos_do_mapa/tabelas_info/planilha_distancias.xlsx", sheet_name=None)) 

no_incial = input("Insira cidade inicial: ")
no_objetivo = input("Insira cidade destino: ")

print("Caminho encontrado: "+str(Mapa.instance().run_a_Estela(no_incial, no_objetivo))+"\n")