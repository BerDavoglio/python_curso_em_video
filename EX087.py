linha1 = list()
linha2 = list()
linha3 = list()
num = soma = soma2 = 0
for c in range(0, 3):
    num = int(input(f'Digite o valor para a posição (0, {c}): '))
    linha1.append(num)
    if num % 2 == 0:
        soma += num
for d in range(0, 3):
    num = int(input(f'Digite o valor para a posição (1, {d}): '))
    linha2.append(num)
    if num % 2 == 0:
        soma += num
for e in range(0, 3):
    num = int(input(f'Digite o valor para a posição (2, {e}): '))
    linha3.append(num)
    if num % 2 == 0:
        soma += num
soma2 = linha1[2] + linha2[2] + linha3[2]
print('-='*15)
print('[{:^5}] [{:^5}] [{:^5}]\n'
      '[{:^5}] [{:^5}] [{:^5}]\n'
      '[{:^5}] [{:^5}] [{:^5}]'.format(linha1[0], linha1[1], linha1[2], linha2[0], linha2[1], linha2[2], linha3[0], linha3[1], linha3[2]))
print('-='*15)
print(f'A soma de todos os pares é igual a {soma};\n'
      f'A soma de todos os valores da 3 coluna é igual a {soma2};\n'
      f'O maior valor da linha 2 é igual a {max(linha2)}.')
print('Obrigado.')
