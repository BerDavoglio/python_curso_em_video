'''
import ModuloPacotes_Uteis
from ModulosPacote_Pacote import Numeros # Não existe, meramente ilustrativo de como chamar um pacote.

num = int(input('Digite um valor: '))
fat = ModuloPacotes_Uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro é {ModuloPacotes_Uteis.dobro(num)}')
print(f'O triplo é {ModuloPacotes_Uteis.triplo(num)}')

num = int(input('Digite um valor: '))
fat = Numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro é {Numeros.dobro(num)}')
print(f'O triplo é {Numeros.triplo(num)}')

'''
