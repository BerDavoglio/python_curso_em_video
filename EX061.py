a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão da P.A.: '))
p = 1

while p != 11:
    print('O termo {} é {}.'.format(p, a))
    a += r
    p += 1
print('Obrigado!')
