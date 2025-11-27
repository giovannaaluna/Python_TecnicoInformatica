notas = []

for i in range(5):
    nota = float(input("Digite a sua nota: "))
    notas.append(nota)

soma_notas = sum(notas)

maior_nota = max(notas)

maior_nota_index = notas.index(max(notas))

print("\nNotas: ",notas)
print("A maior nota foi ",maior_nota," e ela está na posição ",maior_nota_index)
print("A sua média é: ",soma_notas/5)

if soma_notas/5 >= 7:
    print("Parabéns! Você foi aprovado.")
elif soma_notas/5 >= 5:
    print("Você está de recuperação.")
else:
    print("Você está reprovado.")