n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if n1 < n2 and n1 < n3:
    if n2 < n3:
        print('O maior valor é {} e o menor valor é {}!'.format(n3, n1))
    else:
        print('O maior valor é {} e o menor valor é {}!'.format(n2, n1))
elif n2 < n1 and n2 < n3:
    if n1 < n3:
        print('O maior valor é {} e o menor valor é {}!'.format(n3, n2))
    else:
        print('O maior valor é {} e o menor valor é {}!'.format(n1, n2))
else:
    if n1 < n2:
        print('O maior valor é {} e o menor valor é {}!'.format(n2, n3))
    else:
        print('O maior valor é {} e o menor valor é {}!'.format(n1, n3))
