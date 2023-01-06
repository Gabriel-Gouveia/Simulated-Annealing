
class Problema:
    pessoas = [('Lisboa', 'LIS'),
            ('Madrid', 'MAD'),
            ('Paris', 'CDG'),
            ('Dublin', 'DUB'),
            ('Bruxelas', 'BRU'),
            ('Londres', 'LHR')
            ]
        
    destino = 'FCO'

    def retorna_voos():
        voos = {}

        for linha in open('flights.txt'):
            origem, destino, saida, chegada, preco = linha.split(',')
            voos.setdefault((origem, destino), [])
            voos[(origem, destino)].append((saida, chegada, int(preco)))

        return voos