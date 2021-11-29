from EX115_1.Menu import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # 'rt' significa 'read text'. E o 't' é de arquivo de texto.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # 'wt+' irá criar o arquivo texto.
        a.close()
    except:
        print('Houve algum erro na criação de arquivos!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        modulo('FALHA AO LER O ARQUIVO')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<25}{dado[1]:>10} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at+') # 'a' significa 'append text'
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Não foi possivel introduzir novo cadastro.')
        else:
            print(f'Novo cadastro de {nome} realizado.')
            a.close()
