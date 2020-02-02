from datetime import date
ano = int(input('Qual ano você nasceu lazarento?'))

ano_atual = date.today().year

idade = ano_atual - ano

if idade < 18:
    print('Você precisa se alistar em {} anos, Voce devera se alistar em {}'.format(18 - idade, ano_atual + (18 - idade)))
elif idade > 18:
    print('Você deveria ter se alistado a {} anos, em {}'.format(idade - 18, ano_atual - (idade - 18)))
else:
    print('VOcê está em data de se alistar')