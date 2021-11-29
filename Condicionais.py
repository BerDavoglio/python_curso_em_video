'''
temp = float(input('Quantos anos tem o seu carro? '))

if temp <=3:
    print('Seu carro esta novo =D')
else:
    print('Seu carro esta mais velhinho D=')
print('--FIM--')
#ou:
print('Carro Novo'if temp<=3 else'Carro Velho')

n = str(input('Qual é o seu nome? '))
nome = n.capitalize()
if nome == 'Bernardo':
    print('Prazer, meu nome também é Bernardo =D.')
else:
    print('Prazer, meu nome é Bernardo =D.')

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
nota = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(nota))
if nota >= 6:
    print('Você foi aprovad@! Parabéns!!!!')
else:
    print('Você ficou de recuperação. Estude mais!')
'''