from random import randint
p = '=-' * 40
s = 1
computador = randint(0, 10)
n = int(input('Digite um valor: '))
esc = str(input('Par ou Impar? ')).strip().upper()[0]
soma = (computador + n) % 2

while True:
    if esc == 'P':
        if soma == 0:
            print(f'\nO jogador ganhou!\n'
                  f'O computador jogou o valor {computador}.\n')
            s += 1
            computador = randint(0, 10)
            n = int(input('Digite um valor: '))
            esc = str(input('Par ou Impar? ')).strip().upper()[0]
            soma = (computador + n) % 2
        else:
            break
    elif esc == 'I':
        if soma == 1:
            print(f'\nO jogador ganhou!\n'
                  f'O computador jogou o valor {computador}.\n')
            s += 1
            computador = randint(0, 10)
            n = int(input('Digite um valor: '))
            esc = str(input('Par ou Impar? ')).strip().upper()[0]
            soma = (computador + n) % 2
        else:
            break
    else:
        print('\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\n')
print('')
print(p)
print(f'O jogador jogou {n} e o computador jogou {computador}, como a soma deu {computador + n}, o computador ganhou!\n'
      f'Foi na {s} rodada que isso aconteceu...\n'
      f'Obrigado por jogar!')
print(p)
