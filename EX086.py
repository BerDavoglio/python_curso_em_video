linha1 = list()
linha2 = list()
linha3 = list()
num = 0
for c in range(0, 3):
    num = int(input(f'Digite o valor para a posição (0, {c}): '))
    linha1.append(num)
for d in range(0, 3):
    num = int(input(f'Digite o valor para a posição (1, {d}): '))
    linha2.append(num)
for e in range(0, 3):
    num = int(input(f'Digite o valor para a posição (2, {e}): '))
    linha3.append(num)
print('[{:^5}] [{:^5}] [{:^5}]\n'
      '[{:^5}] [{:^5}] [{:^5}]\n'
      '[{:^5}] [{:^5}] [{:^5}]'.format(linha1[0], linha1[1], linha1[2], linha2[0], linha2[1], linha2[2], linha3[0], linha3[1], linha3[2]))
