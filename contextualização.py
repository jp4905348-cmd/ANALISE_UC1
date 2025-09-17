nome = 'Joao'
print(nome)
print(nome.lower())#imprimir em minusculo sem alterar o conteudo

print(nome.upper())#imprimir em maiusculo sem alterar o conteudo
nome2 = 'renato'
print(nome2)
print(type(nome))
print(type(nome2))
#lista
contatos = []
#contatos[1] = 'Ricardo'
contatos.append('ricardo')
contatos.append('renato')
contatos.append('joao')
print(contatos)
print(type(contatos))
frutas = []
frutas = ['pera', 'uva' , 'morango']
frutas = frutas + ['abacaxi', 'ovo']
print(frutas) 
print(type(frutas))

frutas [4] = 'kiwi'
print(frutas)

print(f'numero de letras de {nome} é {len(nome)}')
print(f'tamanho "frutas" é {len(frutas)}')

print(frutas)
for f in frutas:
    print(f)
    #eliminando elementos
        
frutas.pop(2) #elimina pela posição do objeto

frutas.remove('uva') #elimina pelo nome do objeto
print(frutas)
#frutas.pop(20)
#frutas.remove('ovo')

#ordenar em ordem crescente
frutas.sort()
print(frutas)

#ordem decrescente
frutas.reverse()
print(frutas)
