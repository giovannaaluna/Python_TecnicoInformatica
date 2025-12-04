print(
"""
----------------------------------------------
    Hospital Central de Emergências (HCE)
----------------------------------------------
"""
)

paciente_cadastro = []

paciente_idade = []

especialidades = ["Cardiologista", "Dermatologista", "Pediatria", "Clínico Geral", "Ortopedia"]

espec_encaminhada = []

paciente_exames = []

paciente_nome = str(input("Nome do Paciente: "))
paciente_cadastro.append(paciente_nome)

paciente_nasc = int(input("idade: "))
paciente_idade.append(paciente_nasc)

if paciente_nasc <= 12:
    espec_encaminhada.append("Pediatra")

print("""
------------------------------
Sintomas Principais:
            
1 - Dor de Cabeça
2 - Dores no Peito
3 - Fratura/Lesão
4 - Sintomas de Gripe
5 - Coceira/Manchas na Pele
6 - Enjoo
7 - Dormência no Braço
8 - Outros
------------------------------
""")

opcao_sintomas = int(input("Sintoma Identificado: "))

match opcao_sintomas:
    case 1:
        espec_encaminhada.append(especialidades[3])
    case 2:
        espec_encaminhada.append(especialidades[0])
    case 3:
        espec_encaminhada.append(especialidades[4])
    case 4:
        espec_encaminhada.append(especialidades[3])
    case 5:
        espec_encaminhada.append(especialidades[1])
    case 6:
        espec_encaminhada.append(especialidades[3])
    case 7:
        espec_encaminhada.append(especialidades[0])  
    case 8:
        espec_encaminhada.append(especialidades[0])  

if opcao_sintomas == 2 or opcao_sintomas == 3 or opcao_sintomas == 7 or opcao_sintomas == 8:
    print("""
-------------------------------------------------------------------------------
  O paciente será encaminhado para exames de imagem/laboratório imediatamente.
-------------------------------------------------------------------------------""")
    paciente_exames.append("SIM")

else:
    print("""
-------------------------------------------------------------------------------
           O paciente será encaminhado diretamente ao consultório.
-------------------------------------------------------------------------------
          """)
    paciente_exames.append("NÃO")

adicionar_paciente = int(input("""
Adicionar outro paciente?

1 - Sim
0 - Não

Escolha uma opção: """))

while adicionar_paciente != 0:

    paciente_nome = str(input("Nome do Paciente: "))
    paciente_cadastro.append(paciente_nome)

    paciente_nasc = int(input("idade: "))
    paciente_idade.append(paciente_nasc)

    if paciente_nasc <= 12:
        espec_encaminhada.append(especialidades[2])
            
    print("""
------------------------------
Sintomas Principais:
                  
1 - Dor de Cabeça
2 - Dores no Peito
3 - Fratura/Lesão
4 - Sintomas de Gripe
5 - Coceira/Manchas na Pele
6 - Enjoo
7 - Dormência no Braço
8 - Outros
------------------------------
    """)

    opcao_sintomas = int(input("Sintoma Identificado: "))

    match opcao_sintomas:
        case 1:
            espec_encaminhada.append(especialidades[3])
        case 2:
            espec_encaminhada.append(especialidades[0])
        case 3:
            espec_encaminhada.append(especialidades[4])
        case 4:
            espec_encaminhada.append(especialidades[3])
        case 5:
            espec_encaminhada.append(especialidades[1])
        case 6:
            espec_encaminhada.append(especialidades[3])
        case 7:
            espec_encaminhada.append(especialidades[0])  
        case 8:
            espec_encaminhada.append(especialidades[0])  

    
    adicionar_paciente = int(input("""
Adicionar outro paciente?

1 - Sim
0 - Não

Escolha uma opção: """))


    if opcao_sintomas == 2 or opcao_sintomas == 3 or opcao_sintomas == 7 or opcao_sintomas == 8:
        print("""
-------------------------------------------------------------------------------
  O paciente será encaminhado para exames de imagem/laboratório imediatamente.
-------------------------------------------------------------------------------""" )
        paciente_exames.append("SIM")

    else:
        print("""
-------------------------------------------------------------------------------
           O paciente será encaminhado diretamente ao consultório.
-------------------------------------------------------------------------------""")
        paciente_exames.append("NÃO")

print("""
-------------------------------------------------------------------------------
                                FICHA DE ATENDIMENTO
-------------------------------------------------------------------------------""")

for paciente_cadastro, paciente_idade, espec_encaminhada, paciente_exames in zip(paciente_cadastro, paciente_idade, espec_encaminhada, paciente_exames):
    print(f"Nome: {paciente_cadastro}, Idade: {paciente_idade}, Especialidade: {espec_encaminhada}, Exames: {paciente_exames} " )
    



