d = float(input('Quantos Dias foram utilizados pelo carro? '))
k = float(input('Quantos Quilometros foram percorridos com o carro? '))

pd = d * 60
pk = k * 0.15
c = pd + pk

print('O valor total para {} dias e {}Km foi igual a {} Reais.'.format(d, k, c))
