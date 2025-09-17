#crie um programa que fara a leitura de indeterminados numeros que serao armazenados em uma lista, deve ser digitado o numero 0 para interromper a leitura
#no final o programa devera informar o numero total de elementos da lista, a soma dos numeros pares e a media dos numeros impares

#print(float(input ('informe os numeros:')))

#numero = []
#numero = []
#print(numero)
#print(type(numero))
#print(f'quantidade de elementos na lista  de {numero} é {len (numero)}')

#correção
numero = []
while True:
    n = int(input('informe o numero:'))
    numero.append(n)
    if n == 0:
        break
print(f'total de elementos é: {len(numero)}')
somapares = 0
somaimpares = 0
quantimpares = 0
for i in numero:
    if i % 2 == 1:
        print('impar')
        somaimpares = somaimpares + i
        quantimpares = quantimpares + 1
    if i % 2 == 0:
        print('par')
        somapares =somapares + i
print(f'a soma dos numeros é: {somapares}')
mediaimpares = somaimpares / quantimpares
print(f'a media dos impares é: {mediaimpares}')