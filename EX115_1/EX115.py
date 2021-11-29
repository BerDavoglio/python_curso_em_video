from EX115_1.Menu import *
from EX115_1.Arquivos import *
from time import sleep

arq = 'Pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    escolha = chose('\033[30mQual é o seu destino? \033[m')
    if escolha == 1:
        modulo(' PESSOAS CADASTRADAS ')
        # Opção de listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif escolha == 2:
        modulo(' NOVO CADASTRO ')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif escolha == 3:
        sleep(1)
        break
    else:
        print('\033[1;31mDIGITE ALGUM VALOR VÁLIDO\033[m')
    sleep(1)

print('\nFinalizando, Obrigado!')
