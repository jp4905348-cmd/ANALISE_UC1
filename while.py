#ler indeterminados numeros inteiros e informar a soma. A condição de parade é o usuario responder 'n' a pergunta deseja conteinuar
soma = 0
while True:
    n = int(input('informe o numero:'))
    soma = soma + n
    r = input('Deseja continuar? (s/n)')
    if r == 'n' or r == 'N':
        break

    print(f'a soma é {soma}')
   
