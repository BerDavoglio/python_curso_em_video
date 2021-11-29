sal = float(input('Digite seu salário: '))

if sal > 1250:
    print('Seu novo salário é de {} Reais.'.format(sal * 1.1))
else:
    print('Seu novo salário é de {} Reais.'.format(sal * 1.15))