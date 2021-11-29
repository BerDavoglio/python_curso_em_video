pre = float(input('Digite o valor do produto: '))
form = int(input('''ESCOLHA A FORMA DE PAGAMENTO: 
[1] - DINHEIRO/CHEQUE {10% de DESCONTO}.
[2] - CARTÃO (À VISTA) {5% de DESCONTO}.
[3] - CARTÃO (2x).
[4] - CARTÃO (3x OU MAIS) {20% de JUROS}. '''))

print()
if form == 1:
    nov = pre * 0.9
    print('O novo valor (com o desconto) fica igual a {:.2f} Reais.'.format(nov))
elif form == 2:
    nov = pre * 0.95
    print('O novo valor (com o desconto) fica igual a {:.2f} Reais.'.format(nov))
elif form == 3:
    print('Nesta forma de pagamento, não há descontos! O valor continua {:.2f} Reais.'.format(pre))
elif form == 4:
    nov = pre * 1.2
    print('O novo valor (com o ACRÉCIMO) fica igual a {:.2f} Reais.'.format(nov))
else:
    print('FORMA DE PAGAMENTO INVÁLIDA.')
print('\nObrigado por comprar em nossa loja!\n'
      'TENHA UM ÓTIMO DIA.')
