contatos = []
nome = 'luis'
nome = 'claudio'
print(nome)

contatos.append(nome)
contatos.append('feliciano')
#append sempre adiciona ao final
contatos.insert(0,'paula')
#insert adiciona na posição indicada e desloca os demais
print(contatos)
contatos.insert(99,'andre')
print(contatos)
print(contatos[1])
contatos[1] = 'fernanda'
for i in contatos:
    print(i)

contatos.append(20)
contatos.append(4.5)
print(contatos)

contatos.append(['renato', 20])
print(contatos)
