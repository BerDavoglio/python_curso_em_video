'''
if = Condicional Simples
elif = Condicional Multipla
else = Ultima Condicional

ex:
if :
    Bloco 1
elif :
    Bloco 2
elif :
    .
    .
    .
else :
    Bloco 3


nome = str(input('Digite seu nome: '))

if nome ==  'Bernardo':
    print('Seu nome é Lindo! Igual ao meu =D.')
elif nome == 'Eduarda' or nome == 'Luana' or nome == 'Luis Paulo':
    print('Você tem o nome de um dos meus melhores amigos!')
elif nome == 'Enzo' or nome == 'Valentina':
    print('Nome do século... aff')
elif nome in 'Vitor Guilherme Pedro Gustavo':
    print('Seu nome é dos meus amigos da escola.')

print('Tenha um bom dia, {} =D!'.format(nome))

'''
