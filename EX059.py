from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
e = 0
while e != 5:
    e = int(input('''ESCOLHA UMA DELAS: 
    [ 1 ] - SOMA DOS VALORES;
    [ 2 ] - MULTIPLICAR OS VALORES; 
    [ 3 ] - QUAL DELES É MAIOR; 
    [ 4 ] - ESCOLHA NOVOS NÚMEROS; 
    [ 5 ] - SAIR DO PROGRAMA:
    '''))
    if e == 1:
        s = n1 + n2
        print('\nA soma de {} + {} é igual a {}.\n'.format(n1, n2, s))
    elif e == 2:
        m = n1 * n2
        print('\nA multiplicação de {} X {} é igual a {}.\n'.format(n1, n2, m))
    elif e == 3:
        if n1 > n2:
            print('\nO {} é maior que {}.\n'.format(n1, n2))
        elif n2 > n1:
            print('\nO {} é maior que {}.\n'.format(n2, n1))
        else:
            print('\nOS VALORES SÃO IGUAIS A {}.\n'.format(n1))
    elif e == 4:
        n1 = int(input('\nDigite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif e == 5:
        print('Saindo do programa...\n'
              'AGUARDE!')
        sleep(1)
    else:
        print('\033[31mVALOR INVÁLIDO!\033[m')
print('\n=-= Obrigado =-=')
