vel = float(input('Qual a sua Velocidade? '))

if vel <= 80:
    print('Você está abaixo do limite de velocidade =D')
else:
    cus = (vel - 80) * 7
    print('Você esta acima do limite de velocidade!\n'
          'Sua multa será de {:.2f} Reais.\n'
          'Obrigado.'.format(cus))
