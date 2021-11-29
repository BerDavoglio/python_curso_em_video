from time import sleep


def ajuda(x):
    print('\033[35m=' * (44 + kk))
    print(f'\033[30m PROCESSANDO AS INFORMAÇÕES DO CÓDIGO "{x}" \033[m')
    print('\033[35m=' * (44 + kk))
    sleep(0.5)
    print('\033[36m')
    help(x)
    print('\033[m')
    sleep(0.5)


while True:
    y = str(input('Digite o comando [DIGITE FIM PARA FINALIZAR]: ')).lower()
    kk = len(y)
    if y == 'fim':
        break
    ajuda(y)
print('\033[1;34;40m FINALIZANDO PROGRAMA... \033[m')
sleep(0.5)
print('\033[35mObrigado!')
