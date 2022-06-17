import networkx as nx
from elementos_do_mapa.mapa import Mapa

mapa = Mapa("Araraquara", "Presidente_Prudente")

print(mapa.run_A_estela())
