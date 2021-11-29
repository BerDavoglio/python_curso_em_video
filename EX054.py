from datetime import datetime

s = 0
for n in range(0, 7):
    data = int(input('Digite os anos de nascimento: '))
    anos = datetime.today().year - data
    if anos >= 21:
        s += 1
print('Temos {} pessoas maiores de 21 anos!\n'
      'Óbviamente, temos {} menores de 21 anos...'.format(s, 7 - s))
