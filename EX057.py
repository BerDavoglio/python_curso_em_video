s = str(input('Qual é o seu Sexo [M/F]: ')).strip()[0]
while s not in ('MmFf'):
    print('Você digitou errado! Digite novamente...')
    s = str(input('Qual é o seu Sexo: '))
print('Você digitou corretamente!')
