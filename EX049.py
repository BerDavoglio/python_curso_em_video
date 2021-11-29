n = int(input('Digite o valor que quer saber a tabuada: '))
s = 0
for c in range(0, 10):
    print('{} X {} = {}'.format(n, c+1, n * (c+1)))
