alt = float(input('Digite a sua ALTURA (m): '))
pes = float(input('Digite a sua MASSA (Kg): '))

imc = pes / (alt ** 2)
print()
if imc <= 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO!')
elif 18.5 < imc <= 25:
    print('Você está no PESO IDEAL.')
elif 25 < imc <= 30:
    print('Você está em SOBREPESO.\n'
          'CUIDADO!')
elif 30 < imc <= 40:
    print('VOCÊ ESTÁ EM OBESIDADE!')
else:
    print('VOCÊ ESTÁ EM OBESIDADE MORBIDA!\n'
          'VÁ EM UM MÉDICO!!')
print('\nObrigado.')