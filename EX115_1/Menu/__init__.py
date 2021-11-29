def linhas(esc):
    print(esc * 40)


def modulo(esc):
    linhas('=')
    print('{:^40}'.format(f' {esc} '))
    linhas('=')


def chose(msg):
    from time import sleep
    while True:
        try:
            linhas('-')
            print('{:^40}'.format(' MENU PRINCIPAL '))
            linhas('-')
            print('\033[33m[ 1 ]\033[m - \033[34mPessoas Cadastradas;\033[m\n'
                  '\033[33m[ 2 ]\033[m - \033[34mCadastrar uma nova pessoa;\033[m\n'
                  '\033[33m[ 3 ]\033[m - \033[34mSair do programa\033[m')
            linhas('-')
            esq = int(input(msg))
        except:
            print('\033[31mERRO, DIGITE UMA OPÇÃO VALIDA!\033[m')
            sleep(1)
        else:
            return esq
            break


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


