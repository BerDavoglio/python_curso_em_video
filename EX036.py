val = float(input('Digite o valor da Casa: '))
sal = float(input('Digite o valor do seu salário: '))
ano = float(input('Digite quantos anos você pretende pagar: '))

prest = val / (ano * 12)

print('Para pagar a casa de {:.2f} Reais em {} Anos, será necessário pagar {:.2f} Reais em prestações!'.format(val, ano, prest))
if prest <= (sal * 0.3):
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print('EMPRÉSTIMO NÃO CONCEDIDO!')
