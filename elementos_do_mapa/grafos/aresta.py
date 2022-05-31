class Aresta:
    def __init__(self, aresta_A, aresta_B, kilometers):
        self._aresta_A =  aresta_A
        self._aresta_B = aresta_B
        self._kilometers = kilometers

    def get_aresta_A(self):
        return self._aresta_A

    def get_aresta_B(self):
        return self._aresta_B

    def get_kilometers(self):
        return self._kilometers


    def print_aresta(self):
        print(self.get_aresta_A() + "-->" + self.get_aresta_B())
    