from utilidadesCeV import moeda

n = float(input('Digite o valor desejado: ').replace(',', '.'))
porau = float(input('Digite a porcentagem de aumento (em %): '))
pordi = float(input('Digite a porcentagem de redução (em %): '))
print(f'O aumento de {porau}% no valor é igual a {moeda.moeda(moeda.aumentar(n, porau))}.')
print(f'A redução de {pordi}% no valor é igual a {moeda.moeda(moeda.diminuir(n, pordi))}.')
print(f'O dobro do valor é igual a {moeda.moeda(moeda.dobro(n))}.')
print(f'A metade do valor é igual a {moeda.moeda(moeda.metade(n))}.')
