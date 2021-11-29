from datetime import date
from time import sleep
dados = {}
nome = str(input('Digite seu nome: '))
dados['Nome'] = nome
anonasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year - anonasc
dados['Idade'] = ano
carteira = int(input('Digite a sua carteira de trabalho (0 caso não possua): '))
dados['CTPS'] = carteira
a = 0
if carteira == 0:
    print('Programa finalizando... Aguarde')
    sleep(1)
else:
    contr = int(input('Digite o ano de contratação: '))
    anocontr = 35 - (date.today().year - contr)
    dados['Contratação'] = contr
    sal = float(input('Digite seu salário: '))
    dados['Salario'] = sal
    a = f'Ainda faltam {anocontr} anos para você se aposentar, de acordo com a velha regra de aposentadoria...'
print('=-'*50)
print(f'O seu nome é {dados["Nome"]}')
print(f'A sua idade é {dados["Idade"]}')
print(f'A sua CTPS é {dados["CTPS"]}')
if a != 0:
    print(f'O ano de contratação é {dados["Contratação"]}')
    print(f'O seu salário é {dados["Salario"]}')
    print(a)
print('Obrigado.')
print('=-'*50)
