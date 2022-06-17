
euclidianas = {
    'Presidente_Prudente' : 0,
    'Assis': 118,
    'Marilia': 149,
    'Aracatuba': 143,
    'Fernandopolis': 237,
    'SJRP': 254,
    'Barretos': 340,
    'Franca': 451,
    'Ribeirao_Preto': 385,
    'Araraquara': 333,
    'Sao_Carlos': 361,
    'Bauru': 241,
    'Botucatu': 313,
    'SJBV': 474,
    'Mogi_Mirim': 457,
    'Limeira': 413,
    'Piracicaba': 390,
    'Itapeva': 327,
    'Sorocaba': 431,
    'Campinas': 453,
    'Jundiai': 478,
    'SP': 511,
    'Guarulhos': 521,
    'Registro': 448,
    'Itanhaem': 523,
    'Santos': 557,
    'SJC': 577,
    'Taubate': 608
}

def distancia_euclidiana(nome):
    try:
        return euclidianas[nome]
    except KeyError:
        return "Não existe nó com esse nome"

