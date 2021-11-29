from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = s = 0
print(f'A sequencia foi {num}')
print(f'O maior valor foi {max(num)}')
print(f'O menor valor foi {min(num)}')
print('Fim!')
