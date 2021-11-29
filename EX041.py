from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Você irá participar da categoria MIRIM!')
elif 9 < idade <= 14:
    print('Você irá participar da categoria INFANTIL!')
elif 14 < idade <= 19:
    print('Você irá participar da categoria JUNIOR!')
elif 19 < idade <= 25:
    print('Você irá participar da categoria SÊNIOR!')
else:
    print('Você irá participar da categoria MASTER!')
print('OBRIGADO.')
