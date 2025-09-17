dono1 = {'nome' : 'renato', 'idade' : 20}
print(dono1['nome'])
print(dono1['idade'])
dono1['nome'] = 'luis renato'
print(dono1['nome'])
dono1['celular'] = '3932-2020'
print(dono1['celular'])
dono1['animais'] = ['lucky']
print(dono1['animais'])
dono2 = {'nome' : 'paula', 'idade' : 15}
dono3 = {'nome' : 'adilson', 'idade' : 50, 'animais' : ['joca', 'mingau']}
contatos = []
contatos.append(dono1)
contatos.append(dono2)
contatos.append(dono3)
for i in contatos:
    print(f"{i['nome']} - {i['idade']}")
    try:   #ele vai tentar encontrar
        for j in i ['animais']:
            print(j)
    except:  #se não encontrar, vai cair aqui
        print('não possui animais')
