cont = c = 0
valores = list()
while True:
    s = int(input('Digite um valor: '))
    valores.append(s)
    esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if s == 5:
        c += 1
    if esc in 'N':
        break
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)};\n'
      f'A ordem DECRESCENTE de valores é {valores};\n'
      f'O valor 5 foi digitados {c} vezes.')
print('Obrigado!')
