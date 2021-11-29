from math import sqrt

s1 = float(input('Digite o valor do primeiro lado: '))
s2 = float(input('Digite o valor do segundo lado: '))
s3 = float(input('Digite o valor do terceiro lado: '))

tri = sqrt((s1 - s2) ** 2) < s3 < s1 + s2

if tri == True:
    if s1 == s2 == s3:
        print('Esse triângulo com os lados iguais a {} é um triângulo EQUILÁTERO!'.format(s1))
    elif s1 == s2 or s1 == s3 or s2 == s3:
            print('Esse triângulo com os lados {}; {}; {} é um triângulo ISÓSCILES!'.format(s1, s2, s3))
    else:
        print('Esse triângulo com os lados {}; {}; {} é um triângulo ESCALENO!'.format(s1, s2, s3))
else:
    print('OS LADOS DIGITADOS NÃO FORMAM UM TRIÂNGULO!!')
print('OBRIGADO.')
