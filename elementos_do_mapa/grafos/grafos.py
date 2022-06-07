import networkx as nx

G = nx.read_weighted_edgelist('elementos_do_mapa\grafos\cidades.txt', delimiter =",")

fig = nx.draw_networkx(G)
