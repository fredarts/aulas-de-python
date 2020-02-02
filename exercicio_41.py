from datetime import date
ano = int(input('que ano vc nasceu seu cão?'))

idade = date.today().year - ano

if idade <= 9:
    print('Voce tem tem {} e sua classificação é mirim'.format(idade))
elif 9 < idade <= 14:
    print('Voce tem tem {} e sua classificação é Infantil'.format(idade))
elif 14 < idade <= 19:
    print('Voce tem tem {} e sua classificação é Junior'.format(idade))
elif 19 < idade <= 25:
    print('Voce tem tem {} e sua classificação é Senior'.format(idade))
else:
    print('Voce tem tem {} e sua classificação é Master'.format(idade))