dado = {}
gol = list()
jogadores = list()
s = cont = i = 0
d = 1
while True:
    dado['Nome'] = str(input('Digite o nome do jogador: '))
    part = int(input('Digite quantas partidas ele jogou: '))
    dado['Partidas'] = part
    for c in range(0, part):
        gols = int(input(f'Digite quantos gols ele fez no {c + 1}º jogo: '))
        gol.append(gols)
        s += gols
    jogadores.append(dado.copy())
    jogadores.append(gol[:])
    jogadores.append(s)
    dado.clear()
    gol.clear()
    s = 0
    cont += 1
    esc = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if esc in 'N':
        break
while True:
    print('-='*20)
    print(f'O jogardor {jogadores[i]["Nome"]}, camisa {d}, jogou {jogadores[i]["Partidas"]} partidas;\n'
            f'E fez {jogadores[i+2]} gols...')
    d += 1
    i += 3
    if i >= len(jogadores):
        break
print('-=' * 20)
d = 0
while True:
    d = int(input('Deseja escolher algum jogador em especifico? (0 para finalizar.) '))
    if d == 0:
        print('-=' * 20)
        print('Finalizando o programa... Aguarde')
        break
    else:
        print(f'O jogador selecionado fez {jogadores[1 + (3 * (d - 1))]} gols, respectivamente em cada jogo...')
print('Obrigado.')
