import pdfkit
print('#' * 20)
print('''Olá, selecione a url da página da wiki que vocẽ deseja baixar e conbverter em pdf.
 Ex: https://pt.wikipedia.org/wiki/Google''')
print('#' * 20)
url = str(input('url: '))
nome_arquivo = str(input('Digite o nome do arquivo: '))
pdfkit.from_url(url, nome_arquivo)
print('Pronto o seu arquivo foi salvo!!')
