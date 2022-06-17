class Heuristica:

    def  __init__(self):
        self._preco_gasolina = 6

    def calculate(self, via, carro):
        #consideramos sempre que o carro está na velocidade máxima permitida na via
        return (((via.get_speed_limit() / carro.get_consumo) * self._preco_gasolina) + (via.get_kilometers() / via.get_speed_limit()))