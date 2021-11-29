dado = {'Nome': str(input('Digite seu nome: ')), 'Media': float(input('Digite sua média: '))}
for k, v in dado.items():
    print(f'{k}: {v}')
    if k == 'Media' and dado['Media'] >= 7:
        print('Sua média é maior que 7, você foi aprovad@!')
    elif k == 'Media' and dado['Media'] < 7:
        print('Sua média é menor que 7, você esta de recuperação...')
print('Obrigado!')
