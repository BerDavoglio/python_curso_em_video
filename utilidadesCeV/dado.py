def LeiaDinheiro(num):
    num = str(num)
    while True:
        if num.isalpha():
            print('ERRO, DIGITE UM VALOR VÁLIDO.')
            num = str(input('Digite outro valor: '))
        else:
            num = float(num)
            print(f'O valor digitado foi R${num:.2f}'.replace('.', ','))
            break
