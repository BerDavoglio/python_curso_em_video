def voto(a):
    from datetime import date
    idade = date.today().year - a
    print(f'A sua idade é de {idade} anos.')
    if idade < 16:
        print('O voto é NEGADO!')
    elif 16 <= idade < 18 or idade > 65:
        print('O voto é OPCIONAL!')
    else:
        print('O voto é OBRIGATÓRIO!')


voto(int(input('Digite seu ano de nascimento: ')))
