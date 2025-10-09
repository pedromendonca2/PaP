from estado import Estado

class Automato:
    def __init__(self, num_estados, estado_inicial, vocabulario, estados_aceitos, matriz_transicao):
        self.__estado_inicial = estado_inicial
        self.__vocabulario = vocabulario
        self.__matriz_transicao = matriz_transicao
                
        self.__estados = [0]*num_estados
        for i in range(num_estados):
            self.__estados[i] = Estado(vocabulario)
            for j in range(len(vocabulario)):
                a = self.__estados[matriz_transicao[i][j]]
                self.__estados[i].cadastrar_transicao(vocabulario[j], a)
                
        self.__estado = self.__estados[estado_inicial]
        self.__estados_aceitos = [0]*len(estados_aceitos)
        for i in range(len(estados_aceitos)):
            self.__estados_aceitos[i] = self.__estados[self.__estados_aceitos[i]]
                        
    def __aceito_ou_nao(self):
        return self.__estado in self.__estados_aceitos
    
    def processa_string(self, string):
        for letra in string:
            self.__estado = self._estado.proximo_estado(letra)
        return self.__aceito_ou_nao()