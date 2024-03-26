"""
Crie um código em python que teste se o site pudim está acessível pelo
computador usado

Fonte: https://www.youtube.com/watch?v=8jAykqxIeqw
"""
import urllib
from urllib import request
# https://stackoverflow.com/questions/68275857/urllib-error-urlerror-urlopen-error-ssl-certificate-verify-failed-certifica
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print('Deu certo a conexão com o site www.pudim.com.br')
