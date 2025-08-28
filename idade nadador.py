# programa principal
idade = int(input('informe sua idade:'))
if 5 >= idade <= 7:
    print('Sua categoria é: Infantil A')
elif 8 <= idade <= 10:
    print('Sua categoria é: Infantil B')
elif 11 <= idade <= 13:
    print('Sua categoria é: Juvenil A')
elif 14 <= idade <= 17:
    print('Sua categoria é: juvenil B')
elif idade >= 18:
    print('Sua categoria é: Adulto')
else: print('Sem classificação')