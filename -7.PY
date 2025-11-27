numeros = [1, 2, 3, 4, 5]

print("\nLista atual:",numeros)

user_num = int(input("Digite um numero: "))

numeros[2] = user_num

numeros.remove(numeros[-1])

print("Com o número removido, o comprimento atual da lista é:",len(numeros))

print("A lista agora é:",numeros)

