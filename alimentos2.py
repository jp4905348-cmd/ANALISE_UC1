numero = int(input('Informe o numero:'))
match numero:
    case 1:
        print('alimentos')
    case 2:
        print('bebidas')
    case 3 | 4:
        print('cosmeticos')
    case 5 | 6:
        print('produtos de limpeza')
    case _:
        print('Categoria não encontrada')