from time import sleep

s = 0
i = 0
h = 0
for n in range(0, 4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = int(input('Digite o Sexo da pessoa [0 = Homem; 1 = Mulher]: '))
    s += idade
    if sexo == 1:
        if idade > 20:
            i += 1
    if sexo == 0:
        if idade > h:
            h = idade
            a = nome
media = s / 4

print('\nPROCESSANDO...\n')
sleep(1)
print('A MÉDIA das idades é igual a {} Anos;\n'
      'O NOME do HOMEM mais velho é {};\n'
      'O NÚMERO de MULHERES maiores de 20 anos é {}.'.format(media, a, i))
print('\nOBRIGADO!')
