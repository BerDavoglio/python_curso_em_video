n = int(input('Digite o valor que deseja se saber seu fatorial: '))
e = n
z = 1

while e != 0:
    z = e * z
    e -= 1

print('O fatorial do valor {} é igual a {}.'.format(n, z))
print('Obrigado!')
