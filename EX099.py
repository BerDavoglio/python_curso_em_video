from random import randint
def maior(*lst):
    print('=-'*35)
    if len(lst) < 1:
        print('Foram informados 0 valores... Não foi possivel analizar esta lista!')
    else:
        print(f'O maior número da lista {lst}, de {len(lst)} digito(s), é {max(lst)}.')


maior(1, 2, 5, 4, 7, 3)
maior(10, 14, 42, 12, 7)
maior(101, 14, 117)
maior(1)
maior()
maior(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
