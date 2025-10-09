class Estado:
    def __init__(self, vocabulario: list):
        self.__transicoes = {}
        self.__vocabulario = vocabulario.copy()
        
    def proximo_estado(self, letra: str):
        if letra in self.__vocabulario:
            return self.__transicoes[letra]
        else:
            return ValueError()
        
    def cadastrar_transicao(self, letra: str, proximo_estado):
        self.__transicoes[letra] = proximo_estado