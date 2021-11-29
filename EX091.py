from random import randint
from time import sleep
from operator import itemgetter
dado = {'Jogador 1': randint(0, 6), 'Jogador 2': randint(0, 6), 'Jogador 3': randint(0, 6), 'Jogador 4': randint(0, 6)}
ranking = dict()
for k, v in dado.items():
    print(f'O {k} tirou {v} no dado...')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
