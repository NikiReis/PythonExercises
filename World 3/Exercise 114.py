import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.python.org/')
except urllib.error.URLError:
     print('O site não está disponível para ser acessado!')
else:
    print('O site está disponível para ser acessado!')