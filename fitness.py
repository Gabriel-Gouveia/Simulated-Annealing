from problema import Problema


class FitnessFunction:

    def fitness_function(agenda):
        pessoas = Problema.pessoas
        voos = Problema.retorna_voos()
        destino = Problema.destino
        id_voo = -1
        total_preco = 0
        for i in range(len(agenda) // 2):
            origem = pessoas[i][1]
            id_voo += 1
            ida = voos[(origem, destino)][agenda[id_voo]]
            total_preco += ida[2]
            id_voo += 1
            volta = voos[(destino, origem)][agenda[id_voo]]
            total_preco += volta[2]

        return total_preco
