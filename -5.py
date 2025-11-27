num1 = int(input("Digite um número positivo: "))

while (num1 > 0):
    num1 += - 1
    if (num1 % 5 == 0):
        print("-------------------------------------\nAchei um múltiplo de 5: ",num1,"\n-------------------------------------")
    print(num1)