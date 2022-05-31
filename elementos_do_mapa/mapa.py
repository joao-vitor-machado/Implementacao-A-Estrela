from aresta import Aresta
from vias.estradas import Estrada
from vias.rodovias import Rodovia

class Mapa:

    def __init__(self):
        self.mapa = {
            "São Paulo" : {
                "São Paulo" : 0,
                "Piracicaba" : 0,
                "Jundiaí" : Rodovia("São Paulo", "Jundiaí", 27),
            },
            "Piracicaba" : {
                "São Paulo" : 0,
                "Piracicaba" : 0,
                "Jundiaí" : Estrada("Piracicaba", "Jundiaí", 34),
            },
            "Jundiai" : {
                "São Paulo" : Rodovia("Jundiai", "São Paulo", 27),
                "Piracicaba" : Estrada("Jundiai", "Piracicaba", 34),
                "Jundiaí" : 0,
            }
        }

#EQUIVALENTE À SEGUINTE MATRIZ
""""
        Sp Pi Jun
    Sp  [0  0  1]
    Pi  [0  0  1]
    Jun [1  1  0]

"""