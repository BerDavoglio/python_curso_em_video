n = int(input('Digite um valor: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m{}'.format(c), end=' ')
        t += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
print('\033[m\n')
if t == 2:
    print('ESSE NÚMERO É PRIMO!')
else:
    print('ESSE NÚMERO NÃO É PRIMO')
print('\nObrigado.')
