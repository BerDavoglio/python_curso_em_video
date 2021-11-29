s = t = u = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    if idade < 18:
        s += 1
    if sexo == 'M':
        t += 1
    elif sexo == 'F':
        if idade > 20:
            u += 1
    adic = str(input('Deseja adicionar mais alguém? ')).strip().upper()[0]
    if adic == 'N':
        break
print('')
print(f'O número de pessoas MENORES DE 18 ANOS é igual a {s};\n'
      f'O número de HOMENS é igual a {t};\n'
      f'O número de MULHERES MAIORES DE 20 ANOS é igual a {u}.\n'
      f'Obrigado!')
