#calculo da media e a situação do aluno
nota1 = float(input('informe sua nota:'))
nota2 = float(input('informe sua nota:'))
nota3 = float(input('informe sua nota:'))
nota4 = float(input('informe sua nota:'))
media = (nota1 + nota2 + nota3 + nota4)/4
print(f'{nota1} + {nota2} + {nota3} + {nota4} = {media}')
if media >= 7:
    print('Aprovado')
else: 
    rec = float(input('Nota de recuperação:'))
    novamedia = (media + rec) / 2
    print('Reprovado')
recuperação = int(input('informe sua nota da recuperação:'))
recuperação = media / recuperação
print(f'{media} / {recuperação} = {media}')
if media >= 7:
    print('Aprovado')


