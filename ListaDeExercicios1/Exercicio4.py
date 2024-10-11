'''Dada uma lista de notas de alunos notas = [6.3, 7.5, 9.2, 5.1, 6.8],
calcule e exiba a média das notas. Além disso, exiba a quantidade de
notas acima da média (6).
'''

notas = [6.3, 7.5, 9.2, 5.1, 6.8] #Lista de Notas
media = 0
contador = 0

for nota in notas:
    media += nota
    if nota > 6:
        contador += 1

media /= len(notas)

print(f"A media das notas foi {media:.2f}")
print(f"A quantidade de notas a cima da media foi {contador}")