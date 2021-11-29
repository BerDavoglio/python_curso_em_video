from utilidadesCeV import moeda

n = float(input('Digite o valor desejado: '))
porau = float(input('Digite a porcentagem de aumento (em %): '))
pordi = float(input('Digite a porcentagem de redução (em %): '))
print(f'O aumento de {porau}% no valor é igual a {moeda.aumentar(n, porau)} .')
print(f'A redução de {pordi}% no valor é igual a {moeda.diminuir(n, pordi)} .')
print(f'O dobro do valor é igual a {moeda.dobro(n)} .')
print(f'A metade do valor é igual a {moeda.metade(n)} .')
