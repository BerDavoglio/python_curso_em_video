a = int(input('Digite o primeiro valor da P.A.: '))
r = int(input('Digite a Razão da P.A.: '))
p = 1

while p != 11:
    print('O termo {} é {}.'.format(p, a))
    p += 1
    a += r

pergunta = 'S'
while pergunta in ('Ss'):
    pergunta = str(input('Deseja continuar? [ S / N ] '))
    if pergunta in ('Ss'):
        quantos = int(input('Quantos termos você deseja acrescentar? '))
        n = (quantos + p)
        while p != n:
            print('O termo {} é {}.'.format(p, a))
            p += 1
            a += r
print('\nOBRIGADO!')
