
soma = 0
while True:
    codigo = int(input('informe o codigo:'))
    quantidade = int(input('informe a quantidade:'))
    match (codigo):
        case 10:
            soma = soma + (40 * quantidade)
           
        case 11:
            soma = soma + (130 * quantidade)
        
        case 12:
            soma = soma + (80 * quantidade)
           
        case 13:
            soma = soma + (15 * quantidade)
           
        case 14:
            soma = soma + (20 * quantidade)
        
        case _:
            print('Categoria não existente')
    r = input('deseja continuar? (s/n)')
    if r == 'n' or r =='N':
            break
    
print(f'total:{soma:.2f}')
            
   

