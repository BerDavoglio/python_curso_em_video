from time import sleep
nome = prod = ''
valor = s = t = c = 0

while True:
    nome = str(input('Digite o NOME do produto: ')).strip()
    valor = int(input('Digite o VALOR inteiro do produto: '))
    s += valor
    if valor > 1000:
        t += 1
    if valor < c:
        prod = nome
    c = valor
    cont = str(input('DESEJA CONTINUAR? ')).strip().upper()[0]
    if cont == 'N':
        break
print('')
print('CALCULANDO...')
sleep(1)
print('')
print(f'O VALOR TOTAL GASTO foi {s}\n'
      f'O número de produtos MAIS CAROS que 1000 reais foram {t};\n'
      f'O produto MAIS BARATO foi o/a {prod}.\n'
      f'OBRIGADO!')
