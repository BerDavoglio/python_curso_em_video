def area(comp, larg):
    a = comp * larg
    print(f'A área calculada pelos parametros {comprimento}m X {largura}m é igual a {a}m2.')


comprimento = float(input('Digite o comprimento do terreno (m): '))
largura = float(input('Digite a largura do terreno (m): '))
area(comprimento, largura)
