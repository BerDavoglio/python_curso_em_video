n = 0
z = 0

while n != 999:
    n = int(input('Digite algum valor: '))
    z += n
    if n == 999:
        z -= 999
print()
print('A soma dos valores digitados é igual a {}.'.format(z))
print('\nObrigado!')
