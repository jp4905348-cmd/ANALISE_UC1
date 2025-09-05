soma = 0
for i in range(5):
    preco = float(input('digite o preço:'))
if preco >= 200:
    soma = soma + preco
print(f'a soma dos produtos acima de 200 é {soma}')