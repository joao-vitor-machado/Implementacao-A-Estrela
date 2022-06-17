class No:
    def __init__(self, nome, distancia_euclidiana):
        self._nome = nome
        self._distancia_euclidiana = distancia_euclidiana

    def get_nome(self):
        return self._nome

    def get_distancia_euclidiana(self):
        return self._distancia_euclidiana