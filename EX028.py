from random import randint
from time import sleep

n1 = int(input('Digite um valor inteiro entre 1 e 5: '))
n2 = randint(1, 5)

print('Você digitou {}; \n'
      'O computador irá pensar em um número, aguarde...'.format(n1))
sleep(1)
print('{:=^33}'.format(''))
print('O computador pensou no número {}'.format(n2))
if n1 == n2:
    print('Você e o computador pensaram no mesmo número!\n'
          'PARABÉNS, VOCÊ GANHOU!')
else:
    print('Você não conseguiu advinhar o número do computador.\n'
          'INFELIZMENTE, VOCÊ NÃO GANHOU!')
print('{:=^14} FIM {:=^14}'.format('', ''))
