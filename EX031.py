dis = int(input('Distância que deseja percorrer em Km: '))

if dis < 200:
    val = dis * 0.5
    print('O valor da viagem de {}Km será de {:.2f} Reais.'.format(dis, val))
elif dis >= 200:
    val = dis * 0.45
    print('O valor da viagem de {}Km será de {:.2f} Reais.'.format(dis, val))
