import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[1;31mO SITE ESTÁ FORA DO AR!\033[m')
else:
    print('\033[1;36mÉ POSSIVEL ACESSAR O SITE!\033[m')