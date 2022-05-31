import aresta

class Rodovia(aresta.Aresta):
    def __init__(self, aresta_A, aresta_B, kilometers):
        super().__init__(aresta_A, aresta_B, kilometers)
        self._speed_limit = 110

    def get_speed_limit(self):
        return self._speed_limit