n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print('O valor {} é maior do que {}!'.format(n1, n2))
elif n2 > n1:
    print('O valor {} é maior do que {}!'.format(n2, n1))
else:
    print('Os valores são iguais a {}!'.format(n1))
print('{}\n'
      '\033[1;30mOBRIGADO!\033[m\n'
      '{}'.format('=-'*5, '=-'*5))
