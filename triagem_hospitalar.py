print(
"""
----------------------------------------------
    Hospital Central de Emergências (HCE)
----------------------------------------------
"""
)

paciente_cadastro = []

especialidades = ["Cardiologia", "Dermatologista", "Pediatria", "Clínico Geral", "Traumatologia"]

sintomas_paciente = []

paciente_nome = str(input("Nome do Paciente: "))
paciente_cadastro.append(paciente_nome)

paciente_idade = int(input("idade: "))
paciente_cadastro.append(paciente_idade)

for espec in especialidades:
    print(espec)

opcao_sintomas = int(input("Selecione uma opção: "))

print("""
Sintomas Principais:
            
1 - Dor de Cabeça
2 - Dores no Peito
3 - Fratura/Lesão
4 - Sintomas de Gripe
5 - Coceira/Manchas na Pele
6 - Enjoo
7 - Dormência no Braço
""")

match opcao_sintomas:
    case 1:
       paciente_cadastro.append(1)
    case 2:
        paciente_cadastro.append(2)
    case 3:
        paciente_cadastro.append(3)
    case 4:
        paciente_cadastro.append(4)
    case 5:
        paciente_cadastro.append(5)
    case 6:
        paciente_cadastro.append(6)
    case 7:
        paciente_cadastro.append(7)

adicionar_sintomas = int()

print(paciente_cadastro)



#while triagem != 0:
 #print("""
    #Especialidades:
    
   #1 - Cardiologia
   # 2 - Dermatologista
   # 3 - Pediatria
   # 4 - Clínico Geral
   # 5 - Traumatologia""")
            
"""Sintomas Principais:
            
    1 - Dor de Cabeça
    2 - Dores no Peito
    3 - Fratura/Lesão
    4 - Sintomas de Gripe
    5 - Coceira/Manchas na Pele
    6 - Enjoo
    7 - Dormência no Braço
    ------------------------------------- """








