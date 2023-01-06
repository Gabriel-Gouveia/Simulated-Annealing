import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from problema import Problema
from fitness import FitnessFunction

fitness = mlrose.CustomFitness(FitnessFunction.fitness_function)

problem = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)

melhor_solucao, melhor_custo = mlrose.simulated_annealing(problem, 
mlrose.decay.GeomDecay(init_temp=10000), 
random_state=1)

print('Melhor solução: ' + str(melhor_solucao) + 
'  Melhor preço: ' + str(melhor_custo))

def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        nome = Problema.pessoas[i][0]
        origem = Problema.pessoas[i][1]
        voos = Problema.retorna_voos()
        id_voo += 1
        ida = voos[(origem, Problema.destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(Problema.destino, origem)][agenda[id_voo]] 
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                    volta[0], volta[1], volta[2]))
                
    print('Preço total: ', total_preco)
    

imprimir_voos(melhor_solucao)
