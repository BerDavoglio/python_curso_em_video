n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('Você REPROVOU!')
elif m >= 5 and m < 7:
    print('Você esta de RECUPERAÇÃO!\n'
          'Você precisa tirar {} na recuperação para passar!'.format(14 - m))
else:
    print('Você foi APROVAD@!!\n'
          'PARABÉNS!')
