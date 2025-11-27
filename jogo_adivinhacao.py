num1 = 1
num2 = 2
num3 = 3

print("\n======================= JOGO DE =======================\n==================== ADIVINHAÇÃO ======================")
print("\n--- Este algiritmo simula um jogo de adivinhação. ----")

print("\n======================= FASE 1 ========================")

adivinhar_num1 = int(input("\nAdivinhe o número: "))

while (adivinhar_num1 != num1):
    print("\nOPS, RESPOSTA INCORRETA. TENTE NOVAMENTE\n")

    adivinhar_num1 = int(input("Adivinhe o número: "))

print("\nRESPOSTA CORRETA\n")

print("======================= FASE 2 ========================\n")

adivinhar_num2 = int(input("Adivinhe o próximo número: "))
while (adivinhar_num2 != num2):
    print("\nOPS, RESPOSTA INCORRETA. TENTE NOVAMENTE\n")

    adivinhar_num2 = int(input("Adivinhe o próximo número: "))

print("\nRESPOSTA CORRETA\n")

print("======================= FASE 3 ========================\n")

adivinhar_num3 = int(input("Adivinhe o próximo número: "))
while (adivinhar_num3 != num3):
    print("\nOPS, RESPOSTA INCORRETA. TENTE NOVAMENTE\n")

    adivinhar_num3 = int(input("Adivinhe o próximo número: "))

print("\nRESPOSTA CORRETA")

print("\n==== VOCÊ GANHOU O JOGO! ====\n")

jogar_denovo = int(input("Você deseja jogar novamente?\n\n1 - Sim\n2 - Não\n\nEscolha uma opção: "))

match jogar_denovo:
    case 1:
       print("\nQue pena! Vai ficar querendo. :D\n") 
    case 2:
        print("\nQue pena! Foi muito bom ter você aqui.\n")






