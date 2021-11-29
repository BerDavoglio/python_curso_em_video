from random import randint

print('{:=^23}'.format(' JOKENPÔ '))
esc = int(input('''Escolha uma das opções: 
[ 1 ] - Pedra;
[ 2 ] - Papel;
[ 3 ] - Tesoura;
ESCOLHA: '''))
if esc == 1:
    jan = 'Pedra'
elif esc == 2:
    jan = 'Papel'
elif esc == 3:
    jan = 'Tesoura'
com = randint(1, 3)
if com == 1:
    co = 'Pedra'
elif com == 2:
    co = 'Papel'
elif com == 3:
    co = 'Tesoura'
real = esc * 10
jogo = real + com

print()
if jogo == 11 or jogo == 22 or jogo == 33:
    print('O jogo deu VELHA!')
elif jogo == 13 or jogo == 21 or jogo == 32:
    print('O JOGADOR GANHOU!')
elif jogo == 12 or jogo == 23 or jogo == 31:
    print('O JOGADOR PERDEU!')
print('\nO Jogador jogou {};\n'
      'O computador jogou {}.\n'.format(jan, co))

print('Obrigado por jogar.')
