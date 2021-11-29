import datetime

ano = int(input('Digite o ano que deseja saber se é Ano Bissexto: ; Se quiser saber esse ano, digite 0. '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 400 == 0:
    print('O ano {} É BISSEXTO!'.format(ano))
elif ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} É BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))
