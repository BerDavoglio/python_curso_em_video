import datetime
import time

dia = int(input('Digite o DIA do seu nascimento: '))
mes = int(input('Digite o MÊS do seu nascimento (em número): '))
ano = int(input('Digite o ANO do seu nascimento: '))

print('\nAGUARDE, CALCULANDO OS DADOS!...\n')
time.sleep(1)

if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    d1 = dia / (31 * 12)
    da = datetime.date.today().day / (31 * 12)
elif mes == 2:
    d1 = dia / (28 * 12)
    da = datetime.date.today().day / (28 * 12)
else:
    d1 = dia / (30 * 12)
    da = datetime.date.today().day / (30 * 12)
m1 = mes / 12
ma = datetime.date.today().month / 12
aa = datetime.date.today().year

idade = (da + ma + aa) - (d1 + m1 + ano)

if idade < 18:
    print('Você ainda não precisa se preocupar com o alistamento;\n'
          'Ele só irá ocorrer em {:.0f} anos!'.format(18 - (aa - ano)))
elif idade == 18:
    print('Esse ano você é OBRIGADO a se alistar;\n'
          'NÃO PERCA AS DATAS!')
else:
    print('O SEU TEMPO JÁ ESPIROU;\n'
          'ESPERO QUE TENHA SE ALISTADO!')
print('\n'
      'Obrigado.')
