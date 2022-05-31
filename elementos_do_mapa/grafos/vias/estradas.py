import imp


import aresta

class Estrada(aresta.Aresta):
    def __init__(self, aresta_A, aresta_B, kilometers):
        super().__init__(aresta_A, aresta_B, kilometers)
        self._speed_limit = 60

    def get_speed_limit(self):
        return self._speed_limit