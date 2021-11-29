def ficha(nom, gol=0):
    if nom == '':
        nom = '<Desconhecido>'
    print(f'O jogador {nom} marcou {gol} gol(s) no ultimo jogo.')


nome = str(input('Digite o nome do jogador: '))
numero = str(input('Digite quandos gols ele fez no ultimo jogo: '))
if numero.isnumeric():
    numero = int(numero)
else:
    numero = 0
ficha(nome, numero)
