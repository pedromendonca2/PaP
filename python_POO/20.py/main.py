from automato import Automato

def main():

    vocabulario = ["a", "b"]
    num_estados = 4
    estado_inicial = 0
    matriz_transicoes = [
        [1,0],
        [1,2],
        [1,3],
        [1,0]
    ]
    estados_aceitos = [3]
    automato = Automato(num_estados, estado_inicial, vocabulario, estados_aceitos)
    
    print(automato.processa_string("abb"))
    
main()