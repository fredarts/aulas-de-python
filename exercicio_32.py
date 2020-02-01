from datetime import date
ano = int(input('Qual ano você deseja saber se é bissexto?'))

if ano == 0:
    ano = date.today().year

bi = ano % 4 == 0

bu = ano % 400 == 0



if bu:
    print('O ano de {} é bissexto'.format(ano))
elif bi and ano % 100 != 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))

