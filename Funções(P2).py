'''
Interactive Help:
    help([comando])
    print([comando].__doc__)


DocStrings: #A docstring é feita a partir de 3 aspas duplas.
    def contador(i, f, p):
        """
        -> Faz uma contagem e mostra ela na tela.
        :param i: Inicio da contagem.
        :param f: Fim teórico da contagem.
        :param p: Passo da contagem.
        :return: Sem retorno
        """
        c = i
        while c <= f:
            print(f'{c}', end='..')
            c += p
        print('Fim!')


Parâmetros Opcionais:
    def somar(a, b, c=0): #Caso não seja digitado nada, o valor será o definido como padrão.
        s = a + b + c
        print(f'A soma vale {s}')
    somar(4, 5, 7)
    somar(2, 7)


Escopo de Variáveis:
    def teste(b):
        a = 8 #Escopo Local, só vale dentro da def. O A continua valendo 5 fora do def.
        b += 4  # Escopo Local
        c = 2  # Escolo Local
        print(f'A dentro recebe {a}')
        print(f'B dentro recebe {b}') #Escopo local
        print(f'C dentro recebe {c}') #Escopo local
    a = 5
    teste(a)  # Escopo global
    print(f'A fora recebe {a}')
    # print(f'B fora recebe {b}') # Não dariam certo, pq não foram declaradas em todo o programa,
    # print(f'C fora recebe {c}') # Apenas dentro da def teste().

    def teste(b):
        global a # A partir deste comando, o valor A global passa a ser 8.
        a = 8
        b += 4  # Escopo Local
        c = 2  # Escolo Local
        print(f'A dentro recebe {a}')
        print(f'B dentro recebe {b}') #Escopo local
        print(f'C dentro recebe {c}') #Escopo local
    a = 5
    teste(a)  # Escopo global
    print(f'A fora recebe {a}')


Retorno de Valores:
    def somar(a=0, b=0, c=0):
        s = a + b + c
        return s # Pode retornar valores, True or False, Tuplas, Listas, Dicionários, oque for...
    r1 = somar(4, 7, 1)
    r2 = somar(17, 42)
    r3 = somar(6)
    print(f'A soma dos meus cálculos é {r1}; {r2}; {r3}')

'''
