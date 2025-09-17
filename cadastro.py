clientes = []

while True:
    pessoa = {}
    nome = input('informe o nome:')
    idade = int(input('informe a idade:'))
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    animais = []
    while True:
        pet = input('informe o nom e do pet:')
        animais.append(pet)
        r1 = input('deseja cadastrar mais um pet? (s/n)')
        if r1.lower() == 'n':
            break
    pessoa['animais'] = animais
    clientes.append(pessoa)
    r1 = input('deseja cadastrar mais um cliente? (s/n)')
    if r1.lower() == 'n':
        break
print('fim')