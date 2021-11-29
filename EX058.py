from random import randint
from time import sleep

print('JOGO DO ADIVINHA!')
n1 = randint(1, 10)
n2 = int(input('Digite um valor entre 1 a 10: '))
s = 0

while n1 != n2:
    print('\033[31mVocê digitou errado, tente novamente\033[m')
    n2 = int(input('Digite novamente algum novo valor de 1 a 10: '))
    s += 1

print('\nVocê \033[30;44mACERTOU!\033[m o valor escolhido pelo computador foi mesmo {} !'
      '\nVocê levou {} tentativas para acertar!'.format(n1, s))
print('Obrigado por jogar!')
