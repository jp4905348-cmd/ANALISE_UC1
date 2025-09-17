contatos = []
contatos.append(['renato', 20])
contatos.append(['paula', 15])
contatos.append(['adilson', 50, ['joca','mingau']])
print(contatos)

for i in contatos:
    #print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)
print(contatos[1][0])
print(contatos[2][2][0])
print(contatos[2][2][1])

