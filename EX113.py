def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[1;31mERRO! DIGITE UM VALOR VALIDO!!\033[m')
            continue
        else:
            return n
            break


def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[1;31mERRO! DIGITE UM VALOR VALIDO!!\033[m')
            continue
        else:
            return str(n).replace('.', ',')
            break


inteiro = LeiaInt('Digite um valor INTEIRO: ')
numfloat = LeiaFloat('Digite um valor FLOAT: ')
print(f'O número inteiro digitado foi {inteiro}; e o número float foi {numfloat}.')
