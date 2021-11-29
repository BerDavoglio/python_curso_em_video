gol = list()
dado = {}
dado['Nome'] = str(input('Digite o nome do jogador: '))
part = int(input('Digite quantas partidas ele jogou: '))
dado['Partidas'] = part
s = 0
for c in range(0, part):
    gols = int(input(f'Digite quantos gols ele fez no {c + 1}º jogo: '))
    gol.append(gols)
    s += gols
print('=-'*30)
print(f'O jogador {dado["Nome"]} fez um total de {s} gols em {dado["Partidas"]} partidas.')
for i, v in enumerate(gol):
    print(f'Na {i + 1}º partida, ele fez {v} gols...')
print('=-'*30)
print('Fim de análise.')
