from utilidadesCeV import moeda

n = float(input('Digite o valor desejado: ').replace(',', '.'))
porau = float(input('Digite a porcentagem de aumento (em %): '))
pordi = float(input('Digite a porcentagem de redução (em %): '))
formatacao = str(input('Deseja que seja formatado os valores: [T/F] ')).strip().upper()[0]
print(f'O aumento de {porau}% no valor é igual a {moeda.aumentar(n, porau, formatacao)}')
print(f'A redução de {pordi}% no valor é igual a {moeda.diminuir(n, pordi, formatacao)}')
print(f'O dobro do valor é igual a {moeda.dobro(n, formatacao)}')
print(f'A metade do valor é igual a {moeda.metade(n, formatacao)}')
