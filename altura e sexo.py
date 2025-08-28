altura = float(input('informe a altura em metros:'))
sexo = (input('informe seu sexo:'))
peso = 0.0
if sexo == 'M'or sexo == 'm' :
    peso = (72.7 * altura) - 58
elif sexo == 'F' or sexo == 'f' :
    peso = (62.1 * altura) - 44.7
else: print ('informação inválida')
print(f'o peso ideal é: {peso:.3f}')